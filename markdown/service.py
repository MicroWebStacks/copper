from utils import mqtt_client as mc

def test_received():
    print("test received")
    mc.publish("markdown/confirmation",{"status":"received"})
    return

mc.add_action("markdown/request",test_received)
mc.start()
