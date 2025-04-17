import obsws_python as obs
import os
from dotenv import load_dotenv

load_dotenv()

def recordClip(duration):
    print("Clipping for " + str(duration) + " seconds")
    client = obs.ReqClient(host="localhost", port=os.getenv("OBSPORT"), password=os.getenv("OBSPASSWORD"), timeout=3) # Replace with your OBS WebSocket server details

    client.save_replay_buffer()

def StartReplayBuffer():
    print("starting replay buffer")
    client = obs.ReqClient(host="localhost", port=os.getenv("OBSPORT"), password=os.getenv("OBSPASSWORD"), timeout=3) # Replace with your OBS WebSocket server details

    client.start_replay_buffer()

def StopReplayBuffer():
    print("stoping replay buffer")
    client = obs.ReqClient(host="localhost", port=os.getenv("OBSPORT"), password=os.getenv("OBSPASSWORD"), timeout=3) # Replace with your OBS WebSocket server details

    client.stop_replay_buffer()


if __name__ == "__main__":
    print("This is the main program")
else:
    print("my_module is being imported")