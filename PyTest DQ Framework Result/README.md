## Failures
1) facility_name_min_time_spent_per_visit_date: completness, count, uniqueness

Reason: duplicates for facility_type = 'Clinic', facility_name can be different due to generation specifics

Used sql for parquet files creation with comments:
```
SELECT
    f.facility_name,
    v.visit_timestamp::date AS visit_date,
    MIN(v.duration_minutes) AS min_time_spent
FROM
    visits v
JOIN facilities f
    ON f.id = v.facility_id
GROUP BY
    f.facility_name,
    visit_date
UNION ALL  -- misstake
SELECT
    f.facility_name,
    v.visit_timestamp::date AS visit_date,
    MIN(v.duration_minutes) AS min_time_spent
FROM
    visits v
JOIN facilities f
    ON f.id = v.facility_id
WHERE
    f.facility_type = 'Clinic' -- reason of duplicates
GROUP BY
    f.facility_name,
    visit_date;
```

2) facility_type_avg_time_spent_per_visit_date: completness, count

Reason: Incorrect filtering of source data

Used sql for parquet files creation with comments:
```
SELECT
    f.facility_type,
    v.visit_timestamp::date AS visit_date,
    ROUND(AVG(v.duration_minutes), 2) AS avg_time_spent
FROM
    visits v
JOIN
    facilities f
    ON f.id = v.facility_id
WHERE
    v.visit_timestamp > '2000-11-01' -- misstake, should be '2000-01-01'
    AND f.facility_type IN ('Hospital', 'Clinic', 'Specialty Center') -- misstake
GROUP BY
    f.facility_type,
    visit_date;
```

3) patient_sum_treatment_cost_per_facility_type: completness, count, null values

Reason: nulls in full_name, negative values in sum_treatment_cost

Used sql for parquet files creation with comments:
```
SELECT
    f.facility_type,
    CASE
        WHEN p.id <= 15 THEN
            NULL  -- misstake
        ELSE
            CONCAT(p.first_name, ' ', p.last_name)
    END AS full_name,
    CASE
        WHEN f.facility_type = 'Clinic' THEN
            -SUM(v.treatment_cost) -- misstake
        ELSE
            SUM(v.treatment_cost)
    END AS sum_treatment_cost
FROM
    visits v
JOIN facilities f
    ON f.id = v.facility_id
JOIN patients p
    ON p.id = v.patient_id
GROUP BY
    f.facility_type,
    full_name;
```

## Credentials Example

![Credentials Example](jenkins_credentials.png)