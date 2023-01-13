from settings import HUB_PORT,HUB_HOST
from data import process_data
import logging,pika, sys


worker = sys.argv[1]
logging.basicConfig(filename=f"/tmp/{worker}.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def msg_handler(ch,method,properties,message):
    process_data(message.decode("utf-8"))


def main():
    cred = pika.PlainCredentials("admin","p@33w0rd")
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HUB_HOST,
                                                                   port=HUB_PORT,
                                                                   credentials=cred))
    channel = connection.channel()
    #channel.queue_declare(queue='mqtt-message')
    # channel.queue_bind(queue='ml.classification.dv001',exchange='amq.topic',routing_key='ml.classification')

    channel.basic_consume(queue="ml.classification", on_message_callback=msg_handler, auto_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
