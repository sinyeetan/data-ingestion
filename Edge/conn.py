import paho.mqtt.client as mqtt
from settings import HUB_PORT,HUB_HOST,HUB_RPC


def connect_handler(client,userdata,flags,rc):
    print("mqtt connected")
    client.subscribe(HUB_RPC)


def subscribe_handler(client,userdata,mid,rc):
    print("subscribed to topic")


def disconnect_handler(client,userdata,rc):
    print(rc)
    print("MQTT disconnected")


def rpc_handler(client,userdata,message):
    print("Incoming msg : ",str(message.payload.decode("utf-8")))


def publish_handler(client,userdata,mid):
    client.count_flag += 1


def conn():
    client = mqtt.Client(client_id="edge01",clean_session=False)

    client.count_flag = 0
    client.on_connect = connect_handler
    client.on_subscribe = subscribe_handler
    client.on_disconnect = disconnect_handler
    client.on_message = rpc_handler
    client.on_publish = publish_handler
    client.username_pw_set("admin","p@33w0rd")

    client.connect(HUB_HOST,HUB_PORT)
    client.loop_start()

    return client


connector = conn()
