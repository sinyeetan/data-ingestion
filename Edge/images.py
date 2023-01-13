import tensorflow as tf
import base64
from io import BytesIO
from PIL import Image


image_feature = {
        "image": tf.io.FixedLenFeature([], tf.string), # tf.string means bytestring
        "class": tf.io.FixedLenFeature([], tf.int64),  # shape [] means single element
    }


def _parse_image_function(example_proto):
  # Parse the input tf.train.Example proto using the dictionary above.
  return tf.io.parse_single_example(example_proto, image_feature)


def convert(filename):
    # parsing tfrecords path to the TFrecordDataset function from tensorflow
    raw_image_dataset = tf.data.TFRecordDataset(filenames=filename)
    # Basically our tfrecorf file is in the shape, where it contains
    parsed_image_dataset = raw_image_dataset.map(_parse_image_function)
    dataset = []

    for image_features in parsed_image_dataset:
        image_raw = image_features['image'].numpy()
        np_array = tf.io.decode_jpeg(image_raw).numpy()
        im = Image.fromarray(np_array)

        buffered = BytesIO()
        im.save(buffered, format='jpeg')
        img_byte_arr = buffered.getvalue()

        base64_str = str(base64.b64encode(img_byte_arr), 'utf-8')
        data = {"meta":{"label":str(image_features['class'].numpy())},"type":"jpeg","data":base64_str}

        dataset.append(data)

    return dataset
