from src.connectors.postgre_connector import PostgresConnectorContextManager
from src.data.inject_generated_data_to_src import GeneratedDataLoader
from src.data.nf3_loader import NF3Loader
from src.data.parquet_loader import LoadParquet

import logging
import warnings

warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def main():
    with PostgresConnectorContextManager() as connection_object:
        # generate and load generated data into src layer
        logging.info(f"Data generation and injection into Postgres")
        gdi = GeneratedDataLoader(connection_object.get_connection())
        gdi.inject_data()
        # load to nf3 layer
        logging.info(f"Transformation of injected data")
        l3nf = NF3Loader(connection_object.get_connection())
        l3nf.load_data()
        # load parquet files
        logging.info(f"Transformation of parquet files")
        ld = LoadParquet(connection_object)
        ld.to_parquet()


if __name__ == '__main__':
    main()
