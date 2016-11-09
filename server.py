import socket
import threading


# Server for each client
def clientCommunicator(conn):
    #first take the id
    id = int(conn.recv(4))
    #print id
    # Binding to a port according to clients id
    # Keep lisning until the json file is transfered
    # Then send it to the IoT device
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', id+3000))
    server.listen(1)
    while True:
        conn1, address1 = server.accept()
        file = conn1.recv(1024) ## recive the file
        # print file
        conn.send(file) ## send the file to the IoT device

## This is the main server this should be turned on first
def server():
    global dic
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', 3441))
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


