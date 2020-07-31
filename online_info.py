
import socket
import speedtest

class Internet_Info(object):
    def __init__(self):
        self.parser = speedtest.Speedtest()
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)

    def download_speed(self):
        speed = round(self.parser.download() / 1_000_000, 2)
        return str(speed) + " Mbps"

    def upload_speed(self):
        speed = round(self.parser.upload() / 1_000_000, 2)
        return str(speed) + " Mbps"
    
    def __repr__(self):
        return str(f"""\t[Internet Information]
        Host-Name: \t{self.host}
        IP-Address: \t{self.ip}
        Download Speed: {self.download_speed()}
        Upload Speed: \t{self.upload_speed()}
        """)

if __name__ == "__main__":
    print(Internet_Info())

