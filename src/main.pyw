import sys
import os
import traceback
from dotenv import load_dotenv
import paho.mqtt.client as paho
import OBS  # Custom module to control OBS Studio

# Load environment variables from .env file
load_dotenv()

def message_handling(client, userdata, msg):
    """Callback function for when a message is received."""
    print("Message received on topic:", msg.topic)
    OBS.record_clip()  # Triggers OBS to save a replay clip

def get_mqtt_client():
    """Creates and configures the MQTT client."""
    client = paho.Client()
    client.on_message = message_handling
    return client

def connect_mqtt(client):
    """Connects the MQTT client to the broker."""
    hostname = os.getenv("HOSTNAME")
    port = int(os.getenv("PORT"))
    result = client.connect(hostname, port, 60)
    if result != 0:
        raise ConnectionError("Couldn't connect to the MQTT broker")
    print(f"Connected to MQTT broker at {hostname}:{port}")

def subscribe_to_topic(client):
    """Subscribes to the configured MQTT topic."""
    topic = os.getenv("inTopic")
    if topic:
        client.subscribe(topic)
        print(f"Subscribed to topic: {topic}")
    else:
        raise ValueError("No MQTT topic specified in environment variables")

def main():
    try:
        # Ensure OBS is running and connected
        obs_client = OBS.get_obs_client(timeout=3)
        if obs_client is None:
            print("OBS is not running or connection failed. Exiting.")
            return

        # Setup MQTT
        client = get_mqtt_client()
        connect_mqtt(client)
        subscribe_to_topic(client)

        print("Press CTRL+C to exit...")
        OBS.start_replay_buffer()
        client.loop_forever()

    except Exception:
        print("Caught an exception, something went wrong:")
        traceback.print_exc()
    finally:
        try:
            OBS.stop_replay_buffer()
        except Exception as e:
            print("Failed to stop OBS replay buffer:", e)

        try:
            client.disconnect()
            print("Disconnected from MQTT broker")
        except Exception as e:
            print("Failed to disconnect from MQTT broker:", e)


if __name__ == "__main__":
    main()
else:
    print("my_module is being imported")
