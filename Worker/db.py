import sqlalchemy as db
import settings
from settings import DB_USER,DB_PW,LAKE_HOST, DB_PORT,DB_NAME
from minio import Minio


class ImageBase:
    def __init__(self):
        engine = db.create_engine(f"postgresql://{DB_USER}:{DB_PW}@{LAKE_HOST}:{DB_PORT}/{DB_NAME}")
        self.conn = engine.connect()
        meta = db.MetaData()

        self.images = db.Table('image_base', meta,
                               db.Column('id', db.BIGINT, primary_key=True),
                               db.Column('image', db.String(120)),
                               db.Column('meta', db.JSON),
                               db.Column('inserted', db.DATE)
                               )

        meta.create_all(engine)

    def insert(self,image_path,metadata):
        query = db.insert(self.images).values(image=image_path,meta=metadata)
        self.conn.execute(query)


imagebase = ImageBase()

minioClient = Minio(f"{settings.LAKE_HOST}:{settings.MINIO_PORT}", settings.MINIO_ACCESS, settings.MINIO_SECRET,
                    secure=False)