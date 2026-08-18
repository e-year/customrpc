from pypresence import Presence
import time
import os

CLIENT_ID = "" # discord bot/developers client ID 

RPC = Presence(CLIENT_ID)
RPC.connect()

now = int(time.time())
duration_seconds = 400_000 # set as what u want it to be

payload = {
    "cmd": "SET_ACTIVITY",
    "args": {
        "pid": os.getpid(),
        "activity": {
            "type": 2,
            "details": "add something",
            "assets": {
                "large_image": "" # from ur https://discord.com/developers/applications
            },
            "timestamps": {
                "start": now,
                "end": now + duration_seconds
            },
            "buttons": [
                {"label": "button", "url": "url.com"}
            ]
        }
    },
    "nonce": "deftones"
}

RPC.send_data(1, payload)
print("Sent activity update.")

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    RPC.close()
    print("\nRich Presence stopped.")
