import os

HUB_HOST = "localhost"
HUB_PORT = 1883
HUB_TOPIC = "mlops/#"

LAKE_HOST = os.getenv('LAKE_HOST')
MINIO_PORT = os.getenv('MINIO_PORT',"9000")
MINIO_BUCKET = os.getenv('MINIO_BUCKET',"ml-ops")
MINIO_ACCESS = os.getenv('MINIO_ACCESS')
MINIO_SECRET = os.getenv('MINIO_SECRET')

DB_USER = os.getenv('DB_USER')
DB_PW = os.getenv('DB_PW')
DB_PORT = os.getenv('DB_PORT',"5432")
DB_NAME = os.getenv('DB_NAME',"mlops")
