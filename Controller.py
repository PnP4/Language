import json
import socket
import sqlite3 as lite

def creatfile():
    with open("text.json", "w") as outfile:
        data={}
        data['inpdeamon']={"ip":"127.0.0.1","port":8120,"name":'inpdeamon',"type":"server","protocol":"tcp"}
        data["oupdeamon"]={"ip":"127.0.0.1","port":8100,"name":'oudeamon',"type":"server","protocol":"udp"}
        data["cntrldeamon"]={"ip":"192.168.1.2","port":8080,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
        data["timestamp"] = "2016-10-07"
        data["fromip"] = "127.0.0.1"
        data["sysid"] = 1500
        data["sysname"] = "control1"
        data["programproperties"] = "-p 100 -q 1000"
        data["deviceproperties"] = "-p 1500 -q 150"
        #json.dump({'ip': ip, 'port': port}, outfile, indent=4)
        json.dump(data, outfile,indent=4)


def creatfile2(ip,port):
    with open("text.json", "w") as outfile:
        data={}
        data['inpdeamon']={"ip":ip,"port":8100,"name":'inpdeamon',"type":"client","protocol":"udp"}
        data["oupdeamon"]={"ip":"127.0.0.1","port":8100,"name":'oudeamon',"type":"server","protocol":"udp"}
        data["cntrldeamon"]={"ip":"192.168.1.2","port":8080,"name":'cntrldeamon',"type":"client","protocol":"tcp"}
        data["timestamp"] = "2016-10-07"
        data["fromip"] = "127.0.0.1"
        data["sysid"] = 1500
        data["sysname"] = "control1"
        data["sysname"] = "control1"
        data["programproperties"] = "-p 100 -q 1000"
        data["deviceproperties"] = "-p 1500 -q 150"
        json.dump(data, outfile, indent=4)


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
           if (i==0):
               creatfile()
               print "first file created"
               fileSender(data["server"][i]["id"])
               print "1st send"
           else :
               creatfile2(data["server"][i-1]["ip"],data["server"][i-1]["port"])
               fileSender(data["server"][i]["id"])
               print "2nd send"


def fileSender(id) :
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ## connecting to the accroding clientCommunicator
    s.connect(("localhost", id+3002))
    f = open("text.json", "rb")
    ## this will send the file to the clientCommunicator
    l = f.read(1024)
    s.send(l)
    s.close()


def addingMethods (id, ip, port, name) :
    print "1"
    con = lite.connect('main.db')
    cur = con.cursor()
    print "2"
    if (isnotexist(cur, id)) :
        print "3"
        cur.execute('INSERT INTO methoddetails VALUES(?,?)', (id, name,))
        cur.execute('INSERT INTO ips(method_id, ip, port) VALUES(?,?,?)', (id, ip, port,))
        con.commit()








def isnotexist(cur, id):
    print "1.2"
    cur.execute(
        'SELECT id FROM methoddetails  where id = ?', (id,))
    data = cur.fetchall()
    print "1.3"
    if len(data)==0:
        print "1.4"
        return True
    else:
        print "1.5"
        return False


