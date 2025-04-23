from data_dev.src.data.data_generator import DataGenerator
from data_dev.queries import (CREATE_SRC_GENERATED_FACILITIES_TABLE_QUERY,
                              CREATE_SRC_GENERATED_PATIENTS_TABLE_QUERY,
                              CREATE_SRC_GENERATED_VISITS_TABLE_QUERY)
from data_dev.queries import (INSERT_SRC_GENERATED_FACILITIES_QUERY,
                              INSERT_SRC_GENERATED_PATIENTS_QUERY,
                              INSERT_SRC_GENERATED_VISITS_QUERY)


class GeneratedDataInject:
    def __init__(self, conn):
        self.conn = conn
        self.dg = DataGenerator()

    @staticmethod
    def is_table_empty(cursor, table_name):
        query = f"SELECT COUNT(*) FROM {table_name}"
        cursor.execute(query)
        return cursor.fetchone()[0] == 0

    @staticmethod
    def create_table(cursor, query):
        cursor.execute(query)

    @staticmethod
    def inject_data_into_table(cursor, data, query):
        for params in data:
            cursor.execute(query, params)

    def inject_data(self):
        cursor = self.conn.cursor()
        try:
            self.create_table(cursor, CREATE_SRC_GENERATED_FACILITIES_TABLE_QUERY)
            self.create_table(cursor, CREATE_SRC_GENERATED_PATIENTS_TABLE_QUERY)
            self.create_table(cursor, CREATE_SRC_GENERATED_VISITS_TABLE_QUERY)
            if self.is_table_empty(cursor=cursor, table_name='src_generated_visits'):
                self.dg.generate_data()
                self.inject_data_into_table(cursor=cursor, data=self.dg.get_facilities(),
                                            query=INSERT_SRC_GENERATED_FACILITIES_QUERY)
                self.inject_data_into_table(cursor=cursor, data=self.dg.get_patients(),
                                            query=INSERT_SRC_GENERATED_PATIENTS_QUERY)
                self.inject_data_into_table(cursor=cursor, data=self.dg.get_visits(),
                                            query=INSERT_SRC_GENERATED_VISITS_QUERY)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
        finally:
            cursor.close()
