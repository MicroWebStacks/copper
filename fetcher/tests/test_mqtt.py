import json
import paho.mqtt.client as mqtt
import utils as utl  # Ensure you have this utility module for saving the JSON

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
        client.loop_stop()  # Stop the network loop
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
    client.loop_start()  # Start the network loop in the background
    input("Press Enter to stop...\n")  # Keep the script running until you press Enter
    client.loop_stop()  # Stop the network loop
    client.disconnect()  # Cleanly disconnect the client
    return

BROKER = 'mosquitto'
PORT = 1883

test_fetch_list([
            {
                "type": "github",
                "repository": "HomeSmartMesh/website",
                "ref": "main",
                "path": "repos",
                "filter": "content/3dprinting/**/*"
            }
        ])
