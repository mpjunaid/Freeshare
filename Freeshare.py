import os
import random
import string
import sys
import time
import websockets
import asyncio
import json
import zipfile
from Hashing_lib import create_hash
from Encryption import encrypt_data, decrypt_data
import base64

# random_string: str = "".join(random.choice(string.ascii_lowercase) for _ in range(8))
Key = base64.urlsafe_b64encode(os.urandom(32))


# data = {"Code": "random_string", "Action": "Send", "Key": random_string}

# json_data = json.dumps(data)
url = "ws://34.44.108.217:1234"
# url = "ws://127.0.0.1:1234"


async def send_file(file_path, code):
    zip_file_path = "temp.zip"
    count = 0
    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)

    with zipfile.ZipFile(zip_file_path, "w") as zip_file:
        for f in file_path:
            zip_file.write(f, os.path.basename(f))
    with open(zip_file_path, "rb") as f:
        zip_data = f.read()
        print("Here")
        enc_zip_data = encrypt_data(zip_data.decode("latin-1"), Key)
        print(type(enc_zip_data))
        data = {
            "Code": str(code),
            "Action": "Send",
            # "ZipFile": enc_zip_data
            "ZipFile": enc_zip_data,
        }
        json_data = json.dumps(data)
    os.remove(zip_file_path)
    async with websockets.connect(url, timeout=10) as ws:
        await ws.send(json_data)
        try:
            while True:
                msg = await ws.recv()
                val = json.loads(msg)
                if val["Status"] == "Check":
                    count = count + 1
                    # print("Waiting : " + str(count))
                    response = {"Code": data["Code"], "Status": "Check"}
                    await ws.send(json.dumps(response))
                else:
                    print(val)
        except:
            print("Server Disconnected")
    # asyncio.get_event_loop().run_until_complete(send_file(files, code))


async def receive_file(l_key, code):
    async with websockets.connect(url) as ws:
        data = {"Code": code, "Action": "Receive"}
        json_data = json.dumps(data)

        await ws.send(json_data)
        try:
            while True:
                msg = await ws.recv()
                val = json.loads(msg)
                # print(val)
                if val["Auth"]:
                    print("File recieve code : " + val["Code"])
                    print("File found downliading begins...")
                    download_folder: str = "Freeshare_Downloads"
                    download_folder = download_folder + "_" + code
                    zip_data = decrypt_data(val["Zip_file"], l_key)
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
                    print(f"File received and unzipped: {download_folder}")
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
        # code = "".join(random.choice(string.ascii_lowercase) for _ in range(16))
        print("Use the following code to recieve data:" + str(Key.decode()))
        asyncio.run(send_file(files, create_hash(Key)))
    elif action == "-r":
        if len(sys.argv) != 3:
            print("Usage: python script.py -r code")
            sys.exit(1)
        code = sys.argv[2]
        asyncio.run(receive_file(code, create_hash(code)))
    else:
        print("Usage: python script.py [-s|-r] [-f file1 file2 ...]")
        sys.exit(1)
