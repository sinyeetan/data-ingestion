import io,base64, uuid,json
import settings
import logging
from db import imagebase,minioClient


def get_file_extension(extension):
    #extension = imghdr.what(file_name, decoded_file)
    extension = "jpg" if extension == "jpeg" else extension
    return extension


def decode_base64_file(data):
    # Check if the base64 string is in the "data:" format
    if 'data:' in data and ';base64,' in data:
        # Break out the header from the base64 content
        header, data = data.split(';base64,')

    try:
        decoded = base64.b64decode(data)
        return io.BytesIO(decoded)

    except TypeError:
        TypeError('invalid_image')


def process_data(data):
    try:
        data = json.loads(data)
        img_str = data['data']

        img = decode_base64_file(img_str)

        ext = get_file_extension(data['type'])
        filename = str(uuid.uuid4()) + "." + ext

        minioClient.put_object(bucket_name=settings.MINIO_BUCKET,
                               object_name=filename,
                               data=img,
                               length=-1,
                               part_size=10*1024*1024,
                               )

        imagebase.insert(filename,data['meta'])

    except Exception as err:
        logging.error(err.__str__())
