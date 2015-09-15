import socket
import time

host = socket.gethostbyname('localhost')
port = 12001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print 'waiting for connection...'

(client_sock, client_addr) = sock.accept()

while True:
  while True:
    time.sleep(1)
    client_sock.send("It started cloudy, but it got sunny later. \n")
    time.sleep(1)
    client_sock.send("There's nothing better than a cold beer after exercise. \n")
    time.sleep(1)
    client_sock.send("I'd like to buy some of these, but how do I buy these? \n")
    time.sleep(1)
    client_sock.send("It doesn't really matter when your birthday is. \n")
client_sock.close()

sock.close()
