import asyncio
from aiomqtt import Client
import json
import yaml

def load_yaml(fileName):
    with open(fileName, "r") as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as e:
            print(e)
    return

async def run():
    print("async run()")
    workflow = load_yaml("/app/workflow.yaml")
    print("workflow loaded - waiting for event")
    async with Client(BROKER) as client:
        await client.publish("runner/status","up")
        for action in workflow:
            finish_topic = action["action"] + "/finish"
            await client.publish(f"runner/start", payload=json.dumps(action))
            await client.subscribe(finish_topic)
            await client.publish(action["action"], payload=json.dumps(action))
            async for message in client.messages:
                print(f"received message on {message.topic}")
                print(message.payload)
                break
            await client.publish(f"runner/finish", payload=json.dumps(action))
    return

BROKER = 'host.docker.internal'
PORT = 1883
CACHE_PATH = "/cache"

asyncio.run(run())
