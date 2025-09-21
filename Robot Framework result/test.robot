*** Settings ***
Library    SeleniumLibrary
Library    helper.py

*** Variables ***
${REPORT_FILE}      ${EXECDIR}/report.html
${PARQUET_FOLDER}   C:/parquet_data/facility_type_avg_time_spent_per_visit_date
${FILTER_DATE}      2025-08-27    # Optional; comment/remove if no filtering needed

*** Test Cases ***
Compare HTML Table With Parquet Data
    [Documentation]    Open HTML file, read table, read parquet data, and compare.
    Open Browser    file://${REPORT_FILE}    Chrome
    ${table_element}=    Get WebElement    xpath=//*[@class="table"]
    ${df_html}=    Table Read Data    ${table_element}
    ${df_parquet}=    Read Parquet Data    ${PARQUET_FOLDER}    ${FILTER_DATE}

    ${match}    ${diff}=    Compare Dataframes    ${df_html}    ${df_parquet}
    Run Keyword If    not ${match}    Fail    Data mismatch:\n${diff}

    [Teardown]    Close Browser