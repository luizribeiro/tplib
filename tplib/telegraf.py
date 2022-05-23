import json

from paho.mqtt import publish


# TODO: move this to etcd
HOSTNAME = "sodium.i.thepromisedlan.club"


def log(topic: str, **kwargs) -> None:
    publish.single(f"telegraf/{topic}", json.dumps(kwargs), hostname=HOSTNAME)
