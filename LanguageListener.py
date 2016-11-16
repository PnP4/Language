# Generated from Language.g4 by ANTLR 4.5.3
from pandas import json

from antlr4 import *
import sqlite3 as lite
import Controller
# This class defines a complete listener for a parse tree produced by LanguageParser.
class LanguageListener(ParseTreeListener):


    # Enter a parse tree produced by LanguageParser#init.
    def enterInit(self, ctx):
        pass

    # Exit a parse tree produced by LanguageParser#init.
    def exitInit(self, ctx):
        Controller.run()
        pass


    # Enter a parse tree produced by LanguageParser#com.
    def enterCom(self, ctx):
        pass

    # Exit a parse tree produced by LanguageParser#com.
    def exitCom(self, ctx):
        pass

    # Enter a parse tree produced by LanguageParser#method.
    def enterMethod(self, ctx):
        value = ctx.METHOD().getText()
        if (value == "man"):
            self.man()
        else:
            con = lite.connect('main.db')

            cur = con.cursor()
            cur.execute(
                'SELECT id, ip, port FROM methoddetails JOIN ips ON ips.method_id = methoddetails.id where ips.status = "AVAILABLE" AND methodname = "' + value + '";')

            data = cur.fetchone()

            if data != None:
                Controller.appendToJson(data)
                #cur.execute('UPDATE ips status= "BUSY" where method_id = ?',(data[0],))
                #con.commit()
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
        pass

    # Exit a parse tree produced by LanguageParser#parameter.
    def exitParameter(self, ctx):
        pass


    # Enter a parse tree produced by LanguageParser#ip.
    def enterIp(self, ctx):
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


