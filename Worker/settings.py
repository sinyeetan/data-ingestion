import os

HUB_HOST = "localhost"
HUB_PORT = 1883
HUB_TOPIC = "mlops/#"

LAKE_HOST = os.getenv('LAKE_HOST',"192.168.122.75")
MINIO_PORT = os.getenv('MINIO_PORT',"9000")
MINIO_BUCKET = os.getenv('MINIO_BUCKET',"ml-ops")
MINIO_ACCESS = os.getenv('MINIO_ACCESS',"QmBvktoBhb5hxfqj")
MINIO_SECRET = os.getenv('MINIO_SECRET',"F1wG5vpmczDeTVjbz5LGnMA0b8D782Et")

DB_USER = os.getenv('DB_USER',"data_uploader")
DB_PW = os.getenv('DB_PW',"pa33w0rd")
DB_PORT = os.getenv('DB_PORT',"5432")
DB_NAME = os.getenv('DB_NAME',"mlops")