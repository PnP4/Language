import socket
import threading


# Server for each client
from Controller import addingMethods


def clientCommunicator(conn):
    #first take the id
    id = int(conn.recv(4))
    print id
    conn.send("hello")
    #ip = conn.recv(15)
    #print ip
    #port = int(conn.recv(4))
    #print port
    #name = conn.recv(10)
    #print name
    #addingMethods(id, ip, port, name)
    #print id
    # Binding to a port according to clients id
    # Keep lisning until the json file is transfered
    # Then send it to the IoT device
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', id+3002))
    print "succsesful"
    server.listen(1)
    print "in"
    conn1, address1 = server.accept()
    print "good"
    file = conn1.recv(1024) ## recive the file
    print file
    conn.send(file) ## send the file to the IoT device
    conn1.close()
    conn.close()
    thread.exit()


## This is the main server this should be turned on first
def server():
    global dic
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 8080))
    server.listen(1)
    ## This will creat separate thread for each client application
    while True:
        conn, address = server.accept()
        thread = threading.Thread(target=clientCommunicator, args=[conn])
        thread.daemon = True
        thread.start()

## This will run the main server on a another thread (joliyata)
thread = threading.Thread(target=server)
thread.start()


