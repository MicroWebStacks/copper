import json
import paho.mqtt.client as mqtt
from os.path import join, dirname

import github as gutl  # Ensure you have this module available

# Constants
BROKER = 'localhost'  # Change to your MQTT broker's IP address
PORT = 1883
cache_path = "/cache"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("fetcher/request")

def on_message(client, userdata, msg):
    print(f"Message received on {msg.topic}")
    if msg.topic == "fetcher/request":
        data = json.loads(msg.payload.decode())
        client.publish("fetcher/confirmation", json.dumps(data))
        fetch_list = data.get('fetch_list')
        results = process_fetch_list(fetch_list)
        client.publish("fetcher/completion", json.dumps(results))

def process_fetch_list(fetch_list):
    if fetch_list:
        results = []
        for entry in fetch_list:
            if entry["type"] == "github":
                print("Fetching files for repository:", entry['repository'])
                result = gutl.get_repo(entry, cache_path)
                entry.update(result)
                results.append(entry)
        return results
    else:
        return {"error": "Invalid or missing 'fetch_list'"}

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnecting.
client.loop_forever()
