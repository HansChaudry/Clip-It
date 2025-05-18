# 🎬 Clip-It

**Clip-It** is a lightweight automation tool that enables a computer running OBS Studio to save a replay buffer clip upon receiving a specific MQTT message. This facilitates seamless integration between OBS and external systems, such as game servers, smart home devices, or custom hardware, allowing for automated clip recording without manual intervention.

## ⚙️ How It Works

- **OBS Studio**: Ensure OBS is running with the replay buffer enabled.
- **MQTT Broker**: Clip-It connects to a specified MQTT broker and listens for a predefined topic.
- **Triggering a Clip**: When a message is published to the designated topic, Clip-It sends a command to OBS to save the current replay buffer, capturing recent content.

This setup is ideal for scenarios like:

- Automatically recording gameplay highlights triggered by in-game events.
- Integrating with IoT devices to capture moments based on physical actions.
- Coordinating with other software systems to record specific events.

## 📂 Project Structure

```
Clip-It/
├── src/
│   ├── OBS.py             # Handles communication with OBS via WebSocket
│   ├── mqtt_handler.py    # Manages MQTT connections and message handling
│   ├── config.py          # Configuration settings for MQTT and OBS
│   └── main.py            # Entry point to start the Clip-It service
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/HansChaudry/Clip-It.git
   cd Clip-It
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. **Configure OBS**:
   - Enable the **Replay Buffer** in OBS settings.
   - Start the **Replay Buffer**.

2. **Set Up OBS WebSocket**:
   - Install the [obs-websocket](https://github.com/obsproject/obs-websocket) plugin if not already included.
   - Note the WebSocket server port and authentication settings.

3. **Configure MQTT Settings**:
   - Update `config.py` with your MQTT broker details and the topic to subscribe to.

4. **Run Clip-It**:

   ```bash
   python src/main.py
   ```

   Clip-It will now listen for MQTT messages on the specified topic and trigger OBS to save the replay buffer when a message is received.

## 🧪 Testing

To test the setup, publish a message to the configured MQTT topic using a tool like `mosquitto_pub`:

```bash
mosquitto_pub -h your_broker_address -t your/topic -m "trigger"
```

Upon receiving this message, OBS should save the current replay buffer as configured.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
