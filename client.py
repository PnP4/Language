import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("localhost", 8080))
val = raw_input("Id")
s.send(val)
# s.send(raw_input("Ip"))
# s.send(raw_input("Port"))
# s.send(raw_input("Name"))
#while True :
print s.recv(6)
print s.recv(1024)
print s.recv(1024)