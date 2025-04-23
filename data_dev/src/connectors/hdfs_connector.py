# hdfs_handler.py
from hdfs import InsecureClient
from data_dev.config import hdfs_config

class HDFSHandler:
    def __init__(self):
        self.client = InsecureClient(hdfs_config.user, user=hdfs_config.host)

    def upload_file(self, local_path, hdfs_path):
        self.client.upload(hdfs_path, local_path, overwrite=True)