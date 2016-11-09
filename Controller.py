import json
import socket
import threading

dictionary ={}
def creatfile(ip, port):
    with open("text.json", "w") as outfile:
        json.dump({'ip': ip, 'port': port}, outfile, indent=4)


def appendToJson(data):
    with open("server.json", mode='r') as feedsjson:
        feeds = json.load(feedsjson)
    with open("server.json", mode='w') as feedsjson:
        entry = {'id': data[0], 'ip': data[1], 'port' : data[2]}
        feeds["server"].append(entry)
        json.dump(feeds, feedsjson)

def run():
   with open('server.json') as data_file:
       data = json.load(data_file)
       for i in range(len(data["server"])):
           if(i != len(data["server"])-1 ):
               creatfile(data["server"][i+1]["ip"], data["server"][i+1]["port"])
               fileSender(data["server"][i]["id"])


def fileSender(id) :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ## connecting to the accroding clientCommunicator
    s.connect(("localhost", id+3000))
    f = open("text.json", "rb")
    ## this will send the file to the clientCommunicator
    l = f.read(1024)
    s.send(l)



