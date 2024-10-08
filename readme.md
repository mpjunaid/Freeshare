# Freeshare: A Secure, Hassle-Free File Transfer Tool

Tired of the complexities of SSH or other file transfer methods? Freeshare offers a simple yet secure solution.

This Python-based tool allows you to effortlessly transfer files between any two computers connected to the internet. By utilizing encryption and temporary codes, Freeshare ensures your data remains private and protected


## How it works:

1. Send File: Select and send the file which will generate a Unique Code.
2. Share the Code: Safely transmit the code to the receiving device (e.g., via email, messaging app).
3. Receive files: Enter the code on the receiver's side to receive the files.
   
## Key Features:

- Secure Encryption: Protects your data from unauthorized access.
- Unique Codes: Ensures privacy and prevents unauthorized transfers.
- Easy to Use: Intuitive interface for hassle-free file sharing.
- Cross-Platform Compatibility: Works on various operating systems
### Prerequisites:

- Python 3

## Setup:

1. Clone the repository:

```
Bash
git clone https://github.com/mpjunaid/Freeshare.git
```

2. Install dependencies:

```
Bash
pip install -r requirements.txt
```

## Sending Files:

Use the following command to send files:

```
Bash
python freeshare.py -s -f file1 file2 ...
```

Replace file1, file2, etc. with your file names. This generates a unique code for the recipient.

## Receiving Files:

Use the following command to receive files:

```
Bash
python freeshare.py -r code
```

Replace code with the received code. Freeshare downloads and extracts files to _Freeshare_Downloads_code_.

#### Important Notes:

1. The generated code is temporary (expiry not specified).
2. Stable internet connection is required for both parties.

#### Troubleshooting:

Check if the turn server is wokring or the IP address is the same in github repository and your _freeshare.py_ file
