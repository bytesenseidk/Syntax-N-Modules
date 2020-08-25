import os
import hashlib
from tabulate import tabulate

class Hash_Generator(object):
    def __init__(self, check_file):
        self.file_name = check_file.split("\\")[-1]
        self.file_path = check_file.strip(self.file_name)
        self.BUF_SIZE  = 65536  # Reads in 64kb chunks.
        self.md5  = hashlib.md5()
        self.sha1 = hashlib.sha1()
        self.data = [["MD5", str(self.md5.hexdigest())],
                    ["SHA1", str(self.sha1.hexdigest())]]

    def hash_generator(self):
        os.chdir(self.file_path)
        with open(self.file_name, 'rb') as file:
            while True:
                data = file.read(self.BUF_SIZE)
                if not data:
                    break
                self.md5.update(data)
                self.sha1.update(data)

    def __repr__(self):
        table = str(tabulate(self.data, headers="firstrow", tablefmt="grid"))
        return table

if __name__ == "__main__":
    """ Be Aware of tailing whitespace"""
    check_file = str(input(r"Drag n' Drop File: ")).replace('"', "")
    print(Hash_Generator(check_file))
