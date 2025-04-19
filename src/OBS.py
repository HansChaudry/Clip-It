import obsws_python as obs
import os
from dotenv import load_dotenv

load_dotenv()

# Global variable to hold the shared OBS client instance
_obs_client = None

def get_obs_client(timeout=5):
    global _obs_client

    if _obs_client is not None:
        return _obs_client

    try:
        _obs_client = obs.ReqClient(
            host="localhost",
            port=os.getenv("OBSPORT"),
            password=os.getenv("OBSPASSWORD"),
            timeout=timeout
        )
        print("Connected to OBS WebSocket server")
    except Exception as e:
        print("Failed to connect to OBS WebSocket server:", e)
        _obs_client = None

    return _obs_client

def record_clip(duration=60):
    print(f"Clipping for {duration} seconds")
    client = get_obs_client(timeout=3)
    if client:
        try:
            client.save_replay_buffer()
        except Exception as e:
            print("Error saving replay buffer:", e)

def start_replay_buffer():
    print("Starting replay buffer")
    client = get_obs_client(timeout=3)
    if client:
        try:
            client.start_replay_buffer()
        except Exception as e:
            print("Error starting replay buffer:", e)

def stop_replay_buffer():
    print("Stopping replay buffer")
    client = get_obs_client(timeout=3)
    if client:
        try:
            client.stop_replay_buffer()
        except Exception as e:
            print("Error stopping replay buffer:", e)

if __name__ == "__main__":
    print("This is the main program")
else:
    print("my_module is being imported")
