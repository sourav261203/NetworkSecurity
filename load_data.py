import os
import sys
import json
import certifi
import pandas as pd
import pymongo
from dotenv import load_dotenv

from NetworkSecurity.exception.exception import NetworkSecurityException
from NetworkSecurity.logging.logger import logging

# Load environment variables
load_dotenv()

MONGO_DB_URL = os.getenv("MONGODB_URL")
if not MONGO_DB_URL:
    raise RuntimeError("Environment variable MONGO_DB_URL is not set.")

CA_CERT_PATH = certifi.where()


class NetworkDataExtract:
    """Handles CSV-to-JSON conversion and insertion into MongoDB."""

    def __init__(self):
        pass  # Reserved for future configurations

    def csv_to_json_converter(self, file_path: str):
        """
        Converts a CSV file to a list of JSON-like dictionaries.

        Args:
            file_path (str): Path to the CSV file.

        Returns:
            list: List of dictionaries representing CSV rows.
        """
        try:
            logging.info(f"Reading CSV file from {file_path}")
            data = pd.read_csv(file_path)
            records = json.loads(data.to_json(orient="records"))
            logging.info(f"CSV converted to JSON with {len(records)} records.")
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def insert_data_to_mongodb(self, records, database: str, collection: str):
        """
        Inserts a list of records into a MongoDB collection.

        Args:
            records (list): Data to be inserted.
            database (str): MongoDB database name.
            collection (str): MongoDB collection name.

        Returns:
            int: Number of records inserted.
        """
        try:
            logging.info(f"Connecting to MongoDB: {database}.{collection}")
            with pymongo.MongoClient(MONGO_DB_URL, tlsCAFile=CA_CERT_PATH) as client:
                db = client[database]
                result = db[collection].insert_many(records)
            logging.info(f"Inserted {len(result.inserted_ids)} records into MongoDB.")
            return len(result.inserted_ids)
        except Exception as e:
            raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    FILE_PATH = "Network_Data\phisingData.csv"
    DATABASE = "MLOps"
    COLLECTION = "NetworkData"

    try:
        network_obj = NetworkDataExtract()
        records = network_obj.csv_to_json_converter(FILE_PATH)
        inserted_count = network_obj.insert_data_to_mongodb(records, DATABASE, COLLECTION)
        logging.info(f"Successfully inserted {inserted_count} records.")
    except NetworkSecurityException as e:
        logging.error(f"Network security exception occurred: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
