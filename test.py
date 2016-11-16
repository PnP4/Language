import json
with open("texsdf.json", "w") as outfile:
    dataelement = {}
    data = dataelement[str(2)] = {}
    #data = dataelement[str(2)];
    data['inpdeamon'] = {"ip": 23424, "port": 8100, "name": 'inpdeamon', "type": "client", "protocol": "udp"}
    data["oupdeamon"] = {"ip": "127.0.0.1", "port": 8100, "name": 'oudeamon', "type": "server", "protocol": "udp"}
    data["cntrldeamon"] = {"ip": "192.168.1.2", "port": 8080, "name": 'cntrldeamon', "type": "client",
                           "protocol": "tcp"}
    data["timestamp"] = "2016-10-07"
    data["fromip"] = "127.0.0.1"
    data["sysid"] = 1500
    data["sysname"] = "control1"
    data["sysname"] = "control1"
    data["programproperties"] = "-p 100 -q 1000"
    data["deviceproperties"] = "-p 1500 -q 150"
    json.dump(dataelement, outfile, indent=4)

with open('texsdf.json') as f:
    dic = json.load(f)

dataelement = {}
data = dataelement[str(3)] = {}
#data = dataelement[str(2)];
data['inpdeamon'] = {"ip": 23424, "port": 8100, "name": 'inpdeamon', "type": "client", "protocol": "udp"}
data["oupdeamon"] = {"ip": "127.0.0.1", "port": 8100, "name": 'oudeamon', "type": "server", "protocol": "udp"}
data["cntrldeamon"] = {"ip": "192.168.1.2", "port": 8080, "name": 'cntrldeamon', "type": "client",
                       "protocol": "tcp"}
data["timestamp"] = "2016-10-07"
data["fromip"] = "127.0.0.1"
data["sysid"] = 1500
data["sysname"] = "control1"
data["sysname"] = "control1"
data["programproperties"] = "-p 100 -q 1000"
data["deviceproperties"] = "-p 1500 -q 150"

dic.update(dataelement)

with open('texsdf.json', 'w') as f:
    json.dump(dic, f, indent=4)