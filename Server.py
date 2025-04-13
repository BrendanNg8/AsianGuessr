from playerClass import player1
import socket
from Constants import *

s.bind((socket.gethostname()), 1234) #bind socket to ip, port
s.listen(5)

while True:
    clientsocket, address = s.accept() #Kinda like storing connector info
    print(f"[CONNECTION FROM]: {address}")
    clientsocket.send(bytes(player1.get_coordinates(), "utf-8"))

