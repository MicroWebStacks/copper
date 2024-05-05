import asyncio
from aiomqtt import Client
from utils import utils as utl
import json


async def handle_messages(messages):
    async for message in messages:
        print(f"Received message: {message.payload.decode()}")
        # Break after receiving the first response
        break

async def run():
    print("async run()")
    workflow = utl.load_yaml("/app/workflow.yaml")    
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
