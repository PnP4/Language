import json




def creatfile(id, ip):
    with open("text.json", "w") as outfile:
        dataelement = {}
        data = dataelement[str(id)] = {}
        data['inpdeamon'] = {"ip": "127.0.0.1" , "port": 8100, "name": 'inpdeamon', "type": "client", "protocol": "udp"}
        data["oupdeamon"] = {"ip": ip, "port": 8100, "name": 'oudeamon', "type": "server", "protocol": "udp"}
        data["cntrldeamon"] = {"ip": "192.168.1.2", "port": 8080, "name": 'cntrldeamon', "type": "client",
                               "protocol": "tcp"}
        data["next"] = {"ip": ip, "type": "client", "port": 8888, "protocol": "tcp", "name": "cntrldeamon"}
        data["timestamp"] = "2016-10-07"
        data["fromip"] = "127.0.0.1"
        data["sysid"] = 1500
        data["sysname"] = "control1"
        data["sysname"] = "control1"
        data["programproperties"] = "-p 100 -q 1000"
        data["deviceproperties"] = "-p 1500 -q 150"
        json.dump(dataelement, outfile, indent=4)

def updatefile(ip,port,id):
    with open('text.json') as f:
        dic = json.load(f)

    dataelement = {}
    data = dataelement[str(3)] = {}
    data['inpdeamon'] = {"ip": "127.0.0.1", "port": 8100, "name": 'inpdeamon', "type": "client", "protocol": "udp"}
    data["oupdeamon"] = {"ip": ip, "port": 8100, "name": 'oudeamon', "type": "server", "protocol": "udp"}
    data["cntrldeamon"] = {"ip": "192.168.1.2", "port": 8080, "name": 'cntrldeamon', "type": "client",
                           "protocol": "tcp"}
    data["next"] = {"ip": ip, "type": "client", "port": 8888, "protocol": "tcp", "name": "cntrldeamon"}

    data["timestamp"] = "2016-10-07"
    data["fromip"] = "127.0.0.1"
    data["sysid"] = 1500
    data["sysname"] = "control1"
    data["sysname"] = "control1"
    data["programproperties"] = "-p 100 -q 1000"
    data["deviceproperties"] = "-p 1500 -q 150"

    dic.update(dataelement)

    with open('text.json', 'w') as f:
        json.dump(dic, f, indent=4)

def updatefile2(ip,port,id):
    with open('text.json') as f:
        dic = json.load(f)

    dataelement = {}
    data = dataelement[str(3)] = {}
    data['inpdeamon'] = {"ip": "127.0.0.1", "port": 8100, "name": 'inpdeamon', "type": "client", "protocol": "udp"}
    data["oupdeamon"] = {"ip": ip, "port": 8100, "name": 'oudeamon', "type": "server", "protocol": "udp"}
    data["cntrldeamon"] = {"ip": "192.168.1.2", "port": 8080, "name": 'cntrldeamon', "type": "client",
                           "protocol": "tcp"}
    data["next"] = {"ip": "0.0.0.0" , "type": "client", "port": 8888, "protocol": "tcp", "name": "cntrldeamon"}

    data["timestamp"] = "2016-10-07"
    data["fromip"] = "127.0.0.1"
    data["sysid"] = 1500
    data["sysname"] = "control1"
    data["sysname"] = "control1"
    data["programproperties"] = "-p 100 -q 1000"
    data["deviceproperties"] = "-p 1500 -q 150"

    dic.update(dataelement)

    with open('text.json', 'w') as f:
        json.dump(dic, f, indent=4)

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
               creatfile(data["server"][i]["id"])
               print "first file created"

           elif (i==len(data["server"])-1):
               updatefile2(data["server"][0]["ip"],data["server"][0]["port"],data["server"][i]["id"])
               print "first file created"
               print "1st send"
           else :
               updatefile(data["server"][i+1]["ip"],data["server"][i+1]["port"],data["server"][i]["id"])
               print "2nd send"