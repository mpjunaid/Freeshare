import os
import random
import string
import sys
import time
import websockets
import asyncio
import json
import zipfile

random_string: str = "".join(random.choice(string.ascii_lowercase) for _ in range(8))

data = {"Code": "random_string", "Action": "Send", "Key": random_string}

json_data = json.dumps(data)
url = "ws://localhost:1234"


async def send_file(file_path, code):
    zip_file_path = "temp.zip"

    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)

    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        for f in file_path:
            zip_file.write(f, os.path.basename(f))
    with open(zip_file_path, "rb") as f:
        zip_data = f.read()
        data = {
            "Code": code,
            "Action": "Send",
            "ZipFile": zip_data.decode("latin-1"),
            "Key": "".join(random.choice(string.ascii_lowercase) for _ in range(8)),
        }
        json_data = json.dumps(data)

    async with websockets.connect(url) as ws:
        await ws.send(json_data)

        while True:
            msg = await ws.recv()
            val = json.loads(msg)
            print(val)
    asyncio.get_event_loop().run_until_complete(sendfile(files, code))


async def receive_file(code):
    async with websockets.connect(url) as ws:
        data = {"Code": code, "Action": "Receive"}
        json_data = json.dumps(data)
        print(data)
        await ws.send(json_data)
        try:
            while True:
                msg = await ws.recv()
                val = json.loads(msg)
                print(val)
                if val["Auth"]:
                    print("File found downliading begins:")
                    download_folder: str = "Freeshare_Downloads"
                    download_folder = download_folder + "_" + code
                    zip_data = val["Zip_file"]
                    # Create a unique filename with timestamp
                    filename = f"{code}_{int(time.time())}.zip"
                    filepath = os.path.join(download_folder, filename)

                    # Ensure the download folder exists
                    os.makedirs(
                        download_folder, exist_ok=True
                    )  # Create the folder if needed

                    # Save the zipped file
                    with open(filepath, "wb") as f:
                        f.write(
                            zip_data.encode("latin-1")
                        )  # Decode the data before writing

                    # Unzip the file
                    with zipfile.ZipFile(filepath, "r") as zip_ref:
                        zip_ref.extractall(
                            download_folder
                        )  # Extract to the download folder
                    os.remove(filepath)
                    print(f"File received and unzipped: {filepath}")
                    return
                else:
                    print("File not found with code :" + code)
                    return
        except websockets.exceptions.ConnectionClosed:
            print("Connection closed.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python script.py [-s|-r] [-f file1 file2 ...]")
        sys.exit(1)
    action = sys.argv[1]

    if action == "-s":
        if len(sys.argv) < 3 or sys.argv[2] != "-f":
            print("Usage: python script.py -s -f file1 file2 ...")
            sys.exit(1)
        files = sys.argv[3:]
        code = "".join(random.choice(string.ascii_lowercase) for _ in range(8))
        asyncio.run(send_file(files, code))
    elif action == "-r":
        if len(sys.argv) != 3:
            print("Usage: python script.py -r code")
            sys.exit(1)
        code = sys.argv[2]
        asyncio.run(receive_file(code))
    else:
        print("Usage: python script.py [-s|-r] [-f file1 file2 ...]")
        sys.exit(1)
