from playerClass import *
from Constants import *
import pickle
from playerClass import *
from pygame import *

with open("Player1_Info.data", "rb") as file:
    player1 = pickle.load(file)

s.connect((socket.gethostname(), 1234)) #Client connecting to server

while True:
    P1coordinates = s.recv(8)
    formatedP1 = (P1coordinates.decode("utf-8")) #Received Coordinates
    player1.draw(formatedP1)





