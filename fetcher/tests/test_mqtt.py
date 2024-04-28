import json
import paho.mqtt.client as mqtt
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils import utils as utl

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the completion topic
    client.subscribe("fetcher/completion")

def on_message(client, userdata, msg):
    if msg.topic == "fetcher/completion":
        print("Completion message received:")
        response = json.loads(msg.payload.decode())
        print(response)
        utl.save_json(response, "response.json")
        client.disconnect()  # Cleanly disconnect the client
        exit(0)
    if msg.topic == "fetcher/confirmation":
        print("Confirmation message received:")
        response = json.loads(msg.payload.decode())
        print(response)
    return

def test_fetch_list(fetch_list):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)

    # Prepare the payload
    payload = {
        "fetch_list": fetch_list
    }

    print("Publishing request to job/request")
    client.publish("fetcher/request", json.dumps(payload))
    try:
        client.loop_forever()  # Start the blocking network loop
    except KeyboardInterrupt:
        pass
    finally:
        client.disconnect()  # Ensure disconnection on exit
    return

BROKER = 'localhost'
PORT = 1883

test_fetch_list([
            {
                "type": "github",
                "repository": "HomeSmartMesh/raspi",
                "ref": "master",
                "path": "repos",
                "filter": "design/*"
            }
        ])
