# Freeshare

Freeshare is a Python script for secure file transfer. It uses encryption and temporary codes for privacy.

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
