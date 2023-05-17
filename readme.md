# Overview and Installation

The purpose of the project is to make a user-friendly file encryption and decryption program
The purpose of the program is to encrypt any file or directory anywhere on the system
The current program works only on desktop operating system

The program uses AES algorithm with 256 bit key generated from hashing the user-defined password

The hashing algorithm using SHA256. Both the encryption and hashing algorithm are considered very secure till date.

To run the code, directly download the entire folder which contains three files
1. Source script - file-encryptor.py
2. Requirements.txt
3. Readme.md

The program runs on Python 3 and above.

First, open cmd and install all the dependencies which are present in the requirements.txt using

pip install -r requirements.txt

Then run the terminal at the path of the directory where the source files are downloaded.

To run the script, type 

py ./file-encryptor.py

# Usage

You can encrypt or decrypt any file or directory by just pasting the path of the file/directory when prompted
You can also drag and drop multiple files / directories on the terminal to encrypt and decrypt them


You can also setup a master key which is the master password of the password vault

The password vault is a text file which is created on the first run of the code and it stores encryption-decryption passwords corresponding to the file

The password vault is itself encrypted with a master key and you can only view the stored passwords on the command line interface when given appropriate prompt

The default masterkey is the string '1' which should be entered as 1 in cmd terminal when prompted
The custom masterkey entered by user should be stored securely because if the masterkey is lost, you cannot recover the passwords of the encrypted files if forgotten


The encrypted file replaces the original file on the system. When decrypted, the encrypted file gets replaced by the decrypted file.

The user can also directly enter the filename without entering the full-path if the directory of the intended file and the code are the same


## Support

Please support the author to improve the code, finding bugs, use a better algorithm and so on.
Currently the code uses pycryptodomex library. If the implementation is insecure or the library is outdated, please notify to the authors.
The author thanks all the users and viewers alike.

In future, I would like to create an android and ios app for the same. The viewers and users are free to fork it and use this project as a seed to create the app

# License

The program is absolutely free to be used for both commercial and non-commercial purposes

# Citation

Please use the following citation if you want to use anywhere-encrypt for publication

```html
@software{nakul:anywhere-encrypt,
      title={anywhere-encrypt},
      version={1.0},
      author={Nakul Ghate},
      year={2023},
      url={https://github.com/Nakul4/anywhere-encrypt}
}
```