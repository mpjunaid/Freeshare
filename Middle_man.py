import websockets
import asyncio
import json

send_connected_dict = {}
PORT = 1234
print("Middle Man : Ready at: " + str(PORT))


class Connection:
    def __init__(self, code, websocket, action):
        self.code = code
        self.websocket = websocket
        self.action = action
        self.key = None


async def listener(websocket):
    print("New connection")
    try:
        async for message in websocket:
            data = json.loads(message)
            connection = Connection(data["Code"], websocket, data["Action"])
            print(
                "Recived message:" + data["Code"] + "Action:" + data["Action"],
                "Secret:" + data["Key"],
            )
            if data["Action"] == "Send":
                response = {"Code": data["Code"], "Status": "Waiting"}
                await websocket.send(json.dumps(response))
                send_connected_dict[data["Code"]] = connection
                connection.key = data["Key"]
                print(data["ZipFile"])
            else:
                status = data["Code"] in send_connected_dict.keys()
                web = send_connected_dict[data["Code"]]
                print(web.key)
                response = {"Code": data["Code"], "Auth": status, "Key": web.key}
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
