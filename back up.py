import sqlite3 as lite
import sys


# Enter a parse tree produced by LanguageParser#method.
def enterMethod(self, ctx):
    value = ctx.METHOD().getText()
    if (value == "man"):
        self.man()
    else:
        con = lite.connect('main.db')

        cur = con.cursor()
        cur.execute(
            'SELECT methodname, ip FROM methoddetails JOIN ips ON ips.method_id = methoddetails.id where ips.status = "AVAILABLE" AND methodname = "' + value + '";')

        data = cur.fetchone()

        if data != None:
            self.appendToXml(data)
            print data;
            print "Method " + value

        else:
            print "No method found"
        pass



    def man(self):
        try:
            con = lite.connect('main.db')

            cur = con.cursor()
            cur.execute('SELECT methodname, ip FROM methoddetails JOIN ips ON ips.method_id = methoddetails.id;')

            ##data = cur.fetchone()
            for row in cur:
                print "Method_name:   %s" %row[0]
                print "ip:    %s"%row[1]

        except lite.Error, e:

            print "Error %s:" % e.args[0]
            sys.exit(1)

        finally:

            if con:
                con.close()

    def appendToXml(self, methodDetails):
        import sys
        import xml.etree.ElementTree as ET
        doc = ET.parse("server.xml")
        root = doc.getroot()
        ##root_new = ET.Element("servers")
        method = ET.SubElement(root, "methods")
        ET.SubElement(method,"method").text = methodDetails[0]
        ET.SubElement(method, "Ip").text = methodDetails[1]
        tree = ET.ElementTree(root)
        tree.write("server.xml")

