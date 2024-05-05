import paho.mqtt.client as mqtt
import json
import threading
import asyncio

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    for action in actions:
        client.subscribe(action["topic"])
    print(userdata)
    if("connect_event" in userdata):
        print("triggering the event")
        event = userdata["connect_event"]
        loop = userdata["loop"]
        loop.call_soon_threadsafe(event.set)
        print("event safely triggered")

def on_message(client, userdata, msg):
    print(f"Message received on {msg.topic}")
    for action in actions:
        if msg.topic == action["topic"]:
            try:
                data = json.loads(msg.payload)
                action["function"](msg.topic,data)
            except json.decoder.JSONDecodeError as e:
                print(f"json.decoder.JSONDecodeError {e}")

def start_thread(connect_event):
    loop = asyncio.get_running_loop()
    client.user_data_set({
        "connect_event":connect_event,
        "loop":loop
        })
    thread = threading.Thread(target=start)
    thread.start()
    return

def start():
    print(f"connecting to {BROKER}:{PORT}")
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
BROKER = 'host.docker.internal'
PORT = 1883
CACHE_PATH = "/cache"

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

actions = []
