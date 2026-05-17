import keyboard
import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 6789
MESSAGE = b"Hello, World!"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    event = keyboard.read_event()
    if "down" in str(event.event_type):
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
