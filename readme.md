# Overview and Installation

The purpose of the program is to encrypt any file or directory anywhere on the system

The program uses AES algorithm with 256 bit key generated from hashing the user-defined password

The hashing algorithm using SHA256. Both the encryption and hashing algorithm are considered very secure till date.

To run the code, directly download the entire folder which contains three files
1. Source script - file-encryptor.py
2. Requirements.txt
3. Readme.md

First, open cmd and install all the dependencies which are present in the requirements.txt using
pip install -r requirements.txt

Then on cmd give the path of the directory where the files are download and run py ./file-encryptor.py

# Usage

You can encrypt or decrypt any file or directory by just pasting the path of the file/directory when prompted

You can also setup a master key which is the master password of the password vault
The password vault is a text file which is created on the first run of the code and it stores encryption-decryption passwords corresponding to the file
The password vault is itself encrypted with a master key and you can only view the stored passwords on the command line interface when given appropriate prompt

The encrypted file replaces the original file on the system. When decrypted, the encrypted file gets replaced by the decrypted file.

The user can also directly enter the filename without entering the full-path if the directory of the intended file and the code are the same


## Support

Please support the author to improve the code, finding bugs, use a better algorithm and so on.
The author thanks all the users and viewers alike.