# Freeshare: Secure File Sharing Over WebSockets

This Python script, Middle.py, facilitates secure file sharing between two parties using WebSockets. It operates on a client-server model, where the script can function in either sending or receiving mode.

Features:
Secure Communication: Leverages WebSockets for real-time, bidirectional communication, potentially offering enhanced security compared to traditional HTTP requests.
File Zipping: Packs multiple files into a single ZIP archive for efficient transmission.
Random Key Generation: Employs random codes for added security in data exchange.
Command-Line Interface: Provides a user-friendly interface for sending and receiving files.
Installation:

Prerequisites: Ensure you have Python (version 3.6 or later) and the websockets library installed. You can install websockets using pip install websockets.

Starting the middle man
python Middle.py -r /<code/>

Example:
Sender:
python Middle.py -s -f document.txt image.jpg secret_code

Receiver:
python Middle.py -r secret_code
