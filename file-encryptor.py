import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import shutil
import ast
import zipfile


class encryption(object):
    def __init__(self):
        self.user_function()

    def encrypt(self, file, password):

        if os.path.isdir(file):
            folder = file
            shutil.make_archive(file, "zip", file)
            file = file + ".zip"
            shutil.rmtree(folder)

        try:
            dir, filename = os.path.split(file)
        except:
            filename = file
            dir = os.getcwd()
            file = os.path.join(dir, filename)

        chunksize = 64 * 1024
        key = self.keygen(password)
        outfilename = "encrypted_" + filename
        outputfile = os.path.join(dir, outfilename)
        if os.path.exists(outputfile):
            print("File already exists")
            return
        filesize = str(os.path.getsize(file)).zfill(
            16
        )  ## adds 0 to make it a 16 digit number
        nonce = Random.new().read(16)

        encryptor = AES.new(key, AES.MODE_CBC, nonce)

        with open(file, "rb") as infile:
            with open(outputfile, "wb") as outfile:
                outfile.write(filesize.encode("utf-8"))
                outfile.write(nonce)

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b" " * (16 - (len(chunk) % 16))
                    outfile.write(encryptor.encrypt(chunk))
            outfile.close()
        infile.close()
        os.remove(file)
        return

    def decrypt(self, file, password):
        file = file.strip(" ")  ## remove quotations
        try:
            dir, filename = os.path.split(file)
        except:
            filename = file
            dir = os.getcwd()
            file = os.path.join(dir, filename)

        chunksize = 64 * 1024
        key = self.keygen(password)
        outfile = filename[10:]  ## after "encrypted_"
        outputfile = os.path.join(dir, outfile)
        if os.path.exists(outputfile):
            print("File already exists")
            return

        with open(file, "rb") as infile:
            filesize = int(infile.read(16))
            nonce = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, nonce)
            with open(outputfile, "wb") as of:
                while True:
                    chunk = infile.read(chunksize)

                    if len(chunk) == 0:
                        break

                    of.write(decryptor.decrypt(chunk))
                    of.truncate(filesize)
            of.close()
        infile.close()
        os.remove(file)

        try:
            shutil.unpack_archive(outputfile, os.path.join(dir, outfile[:-3]), "zip")
            os.remove(outputfile)
        except:
            pass
        return

    def keygen(self, password):
        hasher = SHA256.new(password.encode("utf-8"))
        return hasher.digest()

    def create_password_vault(self, masterkey):

        filename = "password_vault.txt"
        cwd = os.getcwd()
        pass_file = os.path.join(cwd, filename)
        with open(pass_file, "w") as pf:
            pf.write(str(("Filename", "password")))
            pf.write("\n")
        pf.close()

        self.encrypt(pass_file, masterkey)
        return

    def update_password_vault(self, filename, password, masterkey):

        enc_pass_file = "encrypted_password_vault.txt"
        pass_file = enc_pass_file[10:]
        password_file = self.decrypt(enc_pass_file, masterkey)
        tup = (filename, password)
        with open(pass_file, "a") as pfile:
            pfile.write(str(tup))
            pfile.write("\n")
        pfile.close()

        self.encrypt(pass_file, masterkey)
        return

    def check_password_vault(self, masterkey):
        enc_pass_file = "encrypted_password_vault.txt"
        self.decrypt(enc_pass_file, masterkey)
        pass_file = os.path.join(os.getcwd(), enc_pass_file[10:])
        with open(pass_file, "r") as pfile:
            for line in pfile.readlines():
                print(line)
        pfile.close()
        self.encrypt(pass_file, masterkey)

    def cmd_user_function(self, *args):

        if args[0] == "enc":
            for i in range(1, len(args) - 1):
                filename = args[i]
                password = args[len(args) - 1]
                key = self.keygen(password)
                if os.path.exists(os.path.join(os.getcwd(), filename)):
                    encrypted_file = self.encrypt(filename, key)
                else:
                    print("File does not exist\n")

        elif args[0] == "dec":
            for i in range(1, len(args) - 1):
                filename = args[i]
                password = args[len(args) - 1]
                key = self.keygen(password)
                if os.path.exists(os.path.join(os.getcwd(), filename)):
                    decrypted_file = self.decrypt(filename, key)
                else:
                    print("File does not exist\n")
        else:
            print("Incorrect operation")
        return

    def user_function(self):
        cwd = os.getcwd()
        masterkey = input("Enter masterkey or press Enter to skip: ")
        if masterkey:
            self.create_password_vault(masterkey)
        else:
            pass
        prompt = int(
            input(
                "Press 1 to encrypt file or directory\nPress 2 to decrypt file or directory\nPress 3 to view password vault: "
            )
        )
        if prompt == 1:
            filename = input("Enter file or directory: ")
            filename = filename.replace('"', "")
            file = os.path.join(cwd, filename)
            if os.path.exists(file):
                password = input("Enter password: ")
                encrypted_file = self.encrypt(filename, password)
                print("Encryption successful")
                if masterkey:
                    print("Saving password into password vault\n")
                    self.update_password_vault(filename, password, masterkey)
                else:
                    pass
            else:
                print("File does not exist\n")
                print("Encryption unsuccessful")

        elif prompt == 2:
            filename = input("Enter file: ")
            filename = filename.replace('"', "")
            file = os.path.join(cwd, filename)
            if os.path.exists(file):
                password = input("Enter password: ")
                decrypted_file = self.decrypt(filename, password)
                print("Decryption successful")
            else:
                print("File does not exist")
                print("Decryption unsuccessful")

        elif prompt == 3:
            if masterkey:
                self.check_password_vault(masterkey)
        else:
            print("Wrong Prompt")


def main():

    enc = encryption()


main()
