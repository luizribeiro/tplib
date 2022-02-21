from paho.mqtt import publish


HOSTNAME = "sodium.thepromisedlan.club"


def log(topic: str, **kwargs) -> None:
    publish.single(f"telegraf/{topic}", json.dumps(kwargs), hostname=HOSTNAME)
