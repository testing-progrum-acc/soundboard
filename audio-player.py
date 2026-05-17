import os
import random
import sys
import socket
import threading

linux = False
if sys.platform.startswith("linux"):
    print("Running on Linux")
    from pydub import AudioSegment
    from pydub.playback import play

    linux = True
    AUDIO_DIR = "/home/person/Documents/p/logger/audio/"
else:
    print("Not Linux")
    AUDIO_DIR = "D:\\person\\audio\\"


UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 6789

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
serverSock.settimeout(1.0)

print("UDP server up and listening")


def playinback():
    r = os.listdir(AUDIO_DIR)
    c = random.choice(r)
    audfile = AUDIO_DIR + c
    if linux:
        song = AudioSegment.from_mp3(audfile)
        play(song)
    else:
        os.system(f"playaudio {audfile}")


while True:
    try:
        a, b = serverSock.recvfrom(1024)
        print(f"Received message: {a} from {b}")
        t = threading.Thread(target=playinback)
        t.start()
    except Exception as e:
        print(f"Error occurred: {e}")
