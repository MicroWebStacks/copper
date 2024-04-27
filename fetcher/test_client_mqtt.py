import json
import paho.mqtt.client as mqtt
import utils as utl  # Ensure you have this utility module for saving the JSON

# Constants
BROKER = 'localhost'  # Change to your MQTT broker's IP address
PORT = 1883
REQUEST_TOPIC = "job/request"
COMPLETION_TOPIC = "job/completion"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribe to the completion topic
    client.subscribe(COMPLETION_TOPIC)

def on_message(client, userdata, msg):
    if msg.topic == COMPLETION_TOPIC:
        print("Completion message received:")
        response = json.loads(msg.payload.decode())
        print(response)
        utl.save_json(response, "response.json")

def publish_request():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER, PORT, 60)

    # Prepare the payload
    payload = {
        "fetch_list": [
            {
                "type": "github",
                "repository": "HomeSmartMesh/website",
                "ref": "main",
                "path": "repos",
                "filter": "content/3dprinting/**/*"
            }
        ]
    }

    print("Publishing request to job/request")
    client.publish(REQUEST_TOPIC, json.dumps(payload))
    client.loop_start()  # Start the network loop in the background
    input("Press Enter to stop...\n")  # Keep the script running until you press Enter
    client.loop_stop()  # Stop the network loop
    client.disconnect()  # Cleanly disconnect the client

# Call the function to publish the request
publish_request()
