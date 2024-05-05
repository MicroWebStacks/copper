from utils import mqtt_client as mc
from utils import utils as utl
import asyncio
from time import sleep

async def run_action(action):
    print("------------- will run ----------------")
    print(action)
    sleep(3)
    return

async def run():
    print("run()")
    connect_event = asyncio.Event()
    mc.start_thread(connect_event)
    workflow = utl.load_yaml("/app/workflow.yaml")    
    print("workflow loaded - waiting for event")
    await connect_event.wait()
    print("connected")
    mc.publish("runner/workflow/start",workflow)
    for action in workflow:
        await run_action(action)
    mc.publish("runner/workflow/complete",workflow)
    return

asyncio.run(run())
