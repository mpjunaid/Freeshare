import websockets
import asyncio
import json

send_connected_dict: set = {}
PORT = 80
print("Middle Man : Ready at: " + str(PORT))
status: bool = None


class Connection:
    def __init__(self, code, websocket, action):
        self.code = code
        self.websocket = websocket
        self.action = action
        self.file = None


async def listener(websocket):
    print("New connection")
    try:
        async for message in websocket:
            data = json.loads(message)
            connection = Connection(data["Code"], websocket, data["Action"])

            if data["Action"] == "Send":
                print(
                    "Recived message:" + data["Code"] + "Action:" + data["Action"],
                    "Secret:" + data["Key"],
                )
                response = {"Code": data["Code"], "Status": "Waiting"}
                await websocket.send(json.dumps(response))
                send_connected_dict[data["Code"]] = connection
                connection.file = data["ZipFile"]
                print(data["ZipFile"])
            else:
                print(
                    "Recived message:" + data["Code"] + " " + "Action:" + data["Action"]
                )
                status = data["Code"] in send_connected_dict.keys()
                print("Status :" + str(status))
                web = send_connected_dict[data["Code"]]

                response = {"Code": data["Code"], "Auth": status, "Zip_file": web.file}
                print(response)
                await websocket.send(json.dumps(response))

                response = {
                    "Code": data["Code"],
                    "Auth": status,
                    "Status": "Send",
                }
                # print(response)
                await web.websocket.send(json.dumps(response))

    except:
        print("Disconnected")


start_server = websockets.serve(listener, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
