from src.connectors.postgre_connector import PostgresConnectorContextManager
from src.data.inject_generated_data_to_src import GeneratedDataLoader
from src.data.nf3_loader import NF3Loader
from src.data.parquet_loader import LoadParquet
from src.reporting.report_generator import ReportGenerator

import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    with PostgresConnectorContextManager() as connection_object:
        # generate and load generated data into src layer
        try:
            logging.info(f"Starting data generation and injection into Postgres...")
            gdi = GeneratedDataLoader(connection_object.get_connection())
            gdi.inject_data()
        except Exception as e:
            logging.exception(f"Data generation and injection into Postgres FAILED: {e}")
        # load to nf3 layer
        try:
            logging.info(f"Starting transformation of injected data...")
            l3nf = NF3Loader(connection_object.get_connection())
            l3nf.load_data()
        except Exception as e:
            logging.exception(f"Transformation of injected data FAILED: {e}")
        # load parquet files
        try:
            logging.info(f"Starting transformation of parquet files...")
            ld = LoadParquet(connection_object)
            ld.load_parquet()
        except Exception as e:
            logging.exception(f"Transformation of parquet files FAILED: {e}")
        try:
            logging.info(f"Starting report generation...")
            import os
            directory_contents = os.listdir(".")
            print(directory_contents)
            current_dir = os.getcwd()
            parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
            # List files in the parent directory
            print(f"Current Directory: {current_dir}")
            print(f"Parent Directory: {parent_dir}")

            print("Files in Parent Directory:")
            for file_name in os.listdir(parent_dir):
                file_path = os.path.join(parent_dir, file_name)
                if os.path.isfile(file_path):
                    print(f" - {file_name}")
            rp = ReportGenerator()
            rp.generate_report()
        except Exception as e:
            logging.exception(f"Report generation FAILED: {e}")


if __name__ == '__main__':
    main()
