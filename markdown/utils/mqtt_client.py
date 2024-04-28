import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    for action in actions:
        client.subscribe(action["topic"])

def on_message(client, userdata, msg):
    print(f"Message received on {msg.topic}")
    for action in actions:
        if msg.topic == action["topic"]:
            action["function"]()

def start():
    client.connect(BROKER, PORT, 60)
    # Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
    client.loop_forever()
    return

def add_action(topic,function):
    actions.append({
        "topic":topic,
        "function":function
    })
    return

def publish(topic, data):
    client.publish(topic, json.dumps(data))
    return

# Constants
BROKER = 'mosquitto'
PORT = 1883
CACHE_PATH = "/cache"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

actions = []
