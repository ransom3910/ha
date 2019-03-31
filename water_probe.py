#!/usr/bin/python3

import socket
import os

host = "192.168.20.155"
port = 80
threshold = "2"


def main():
    try:
        s = socket.socket()
        s.settimeout(5)
        s.connect((host, port))
        s.send("water\r".encode())
        data = s.recv(1024)
        if "Full" in data.decode():
            print("Ok")
        else:
            print(data.decode())
        s.close()
        with open(f"{os.getcwd()}/water_probe_state.state", "w") as f:
            f.writelines("0")
            f.close()
    except Exception as error:
        with open(f"{os.getcwd()}/water_probe_state.state", "r") as f:
            data = f.readline()
            if data == threshold:
                print("Probe Offline")
                f.close()
            else:
                tracker = int(data)
                tracker += 1
                f.close()
                with open(f"{os.getcwd()}/water_probe_state.state", "w") as f:
                    f.writelines(str(tracker))
                    f.close()
                    print("Ok")


main()
