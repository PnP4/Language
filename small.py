
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(("localhost", 3002))
s.send("hello")
val = raw_input("sdfsfsd")
s.send(val)
s.close()
#val = raw_input("sdfsfsd")
#s.send(val)
#val = raw_input("sdfsfsd")
#s.send(val)