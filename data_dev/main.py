from src.connectors.postgre_connector import PostgresConnectorContextManager
from src.data.inject_generated_data_to_src import GeneratedDataInject


def main():
    """
    from src.data.data_generator import DataGenerator
    dg = DataGenerator()
    dg.generate_data()
    dim_patient = dg.get_patients()
    dim_facility = dg.get_facilities()
    fact_visits = dg.get_visits()
    print(dim_patient)
    print(dim_facility)
    print(fact_visits)
    """
    with PostgresConnectorContextManager() as conn:
        # generate and load generated data into postgres
        gdi = GeneratedDataInject(conn)
        gdi.inject_data()
        # load generated data - increment\batch

        # load parquet file into hdfs


if __name__ == '__main__':
    main()
