# Generated from Language.g4 by ANTLR 4.5.3
from antlr4 import *
import sqlite3 as lite
namr = "good"
# This class defines a complete listener for a parse tree produced by LanguageParser.
class LanguageListener(ParseTreeListener):


    # Enter a parse tree produced by LanguageParser#init.
    def enterInit(self, ctx):
        pass

    # Exit a parse tree produced by LanguageParser#init.
    def exitInit(self, ctx):
        pass


    # Enter a parse tree produced by LanguageParser#com.
    def enterCom(self, ctx):
        pass

    # Exit a parse tree produced by LanguageParser#com.
    def exitCom(self, ctx):
        pass


    # Enter a parse tree produced by LanguageParser#method.
    def enterMethod(self, ctx):
        value = ctx.METHOD()[0].getText()
        if (value == "man"):
            self.man()

        elif(value == "addmethod"):
            value = ctx.METHOD().PARAMETER()[0].getText
            print value
            #self.enterIp()
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

    # Exit a parse tree produced by LanguageParser#method.
    def exitMethod(self, ctx):
        pass


    # Enter a parse tree produced by LanguageParser#pipe.
    def enterPipe(self, ctx):
        pass

    # Exit a parse tree produced by LanguageParser#pipe.
    def exitPipe(self, ctx):
        pass


    # Enter a parse tree produced by LanguageParser#parameter.
    def enterParameter(self, ctx):
        print "param"
        va = ctx.PARAMETER()[0]
        #print namr
        #print va
        pass

    # Exit a parse tree produced by LanguageParser#parameter.
    def exitParameter(self, ctx):
        pass


    # Enter a parse tree produced by LanguageParser#ip.
    def enterIp(self, ctx):
        print "IP"
        print namr
        pass

    # Exit a parse tree produced by LanguageParser#ip.
    def exitIp(self, ctx):
        pass


    # Enter a parse tree produced by LanguageParser#parametersign.
    def enterParametersign(self, ctx):
        pass

    # Exit a parse tree produced by LanguageParser#parametersign.
    def exitParametersign(self, ctx):
        pass


