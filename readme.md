# Freeshare

Freeshare is a Python script for secure file transfer. It uses encryption and temporary codes for privacy.

### Prerequisites:

- Python 3

# Setup:

1. Clone the repository:

   **Bash**

   git clone https://github.com/mpjunaid/Freeshare.git

Install dependencies:

Bash
pip install -r requirements.txt
Use code with caution.

Sending Files:

Use the following command to send files:

Bash
python freeshare.py -s -f file1 file2 ...
Use code with caution.

Replace file1, file2, etc. with your file names. This generates a unique code for the recipient.

Receiving Files:

Use the following command to receive files:

Bash
python freeshare.py -r code
Use code with caution.

Replace code with the received code. Freeshare downloads and extracts files to Freeshare_Downloads/<code/>.

Important Notes:

The generated code is temporary (expiry not specified).
Stable internet connection is required for both parties.
Troubleshooting:

If you encounter issues, check the config.ini file (if it exists)
