import json,sys
from settings import HUB_DATA


def start(tfset):
    from conn import connector
    import images

    goal_count = 0

    if connector.is_connected():
        dataset = images.convert(tfset)
        goal_count = len(dataset)

        for data in dataset:
            connector.publish(HUB_DATA,json.dumps(data),qos=1)

    while True:
        if connector.count_flag == goal_count:
            connector.disconnect()
            break


if __name__ == "__main__":
    tfset = sys.argv[1]
    start(tfset)


