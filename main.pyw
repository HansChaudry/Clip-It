import sys
import os
from dotenv import load_dotenv
import paho.mqtt.client as paho
import OBS
import traceback

load_dotenv()

def message_handling(client, userdata, msg):
    print(f"{msg.topic}: {msg.payload.decode()}")
    OBS.recordClip(int(msg.payload.decode()))


client = paho.Client()
client.on_message = message_handling

if client.connect(os.getenv("HOSTNAME"), int(os.getenv("PORT")), 60) != 0:
    print("Couldn't connect to the mqtt broker")
    sys.exit(1)

client.subscribe(os.getenv("inTopic"))

if __name__ == "__main__":
    try:
        print("Press CTRL+C to exit...")
        OBS.StartReplayBuffer()
        client.loop_forever()
    except Exception:
        print("Caught an Exception, something went wrong...")
        print(traceback.print_exc())
    finally:
        OBS.StopReplayBuffer()
        
        print("Disconnecting from the MQTT broker")
        client.disconnect()
else:
    print("my_module is being imported")