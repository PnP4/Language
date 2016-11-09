import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("localhost", 3443))
val = raw_input("sdfsfsd")
s.send(val)
while True :
    print s.recv(1024)