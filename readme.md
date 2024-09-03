Freeshare: Secure File Sharing Over WebSockets

This Python script, Middle.py, facilitates secure file sharing between two parties using WebSockets. It operates on a client-server model, where the script can function in either sending or receiving mode.

Features:

Secure Communication: Leverages WebSockets for real-time, bidirectional communication, potentially offering enhanced security compared to traditional HTTP requests.
File Zipping: Packs multiple files into a single ZIP archive for efficient transmission.
Random Key Generation: Employs random codes for added security in data exchange.
Command-Line Interface: Provides a user-friendly interface for sending and receiving files.
Installation:

Prerequisites: Ensure you have Python (version 3.6 or later) and the websockets library installed. You can install websockets using pip install websockets.
Usage:

The script offers two modes: sending and receiving files.

Sending Files (Sender):

Navigate to the directory containing Middle.py and your files.

Open a terminal window.

Execute the following command, replacing <files> with the space-separated names of your files and <code> with a desired random code (8 lowercase letters):

Bash
python Middle.py -s -f <files> <code>

Receiving Files (Receiver):

Navigate to the directory where you want to receive the files.

Open a terminal window.

Execute the following command, replacing <code> with the code provided by the sender:

Bash
python Middle.py -r <code>

Example:

Sender:

    python Middle.py -s -f document.txt image.jpg secret_code

Receiver:
python Middle.py -r secret_code
