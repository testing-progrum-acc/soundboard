import os
import random
from pydub import AudioSegment
from pydub.playback import play
import socket
import threading

AUDIO_DIR="/home/person/Documents/p/logger/audio/"


UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

print("UDP server up and listening")


def playinback():
    r = os.listdir(AUDIO_DIR)
    c = random.choice(r)
    audfile = AUDIO_DIR+c
    song = AudioSegment.from_mp3(audfile)
    play(song)


while True:
    a,b = serverSock.recvfrom(1024)
    t = threading.Thread(target=playinback)
    t.start()
