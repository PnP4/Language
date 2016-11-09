import overrides as overrides

from LanguageListener import *


class Check(LanguageListener):
    ##@overrides(LanguageListener)
    def enterMethod(self, ctx):
        value = ctx.METHOD().getText()
        result = False
        with open("DNS.txt") as f:
            content = f.readlines()
            for line in content:
                read = content.split(" ")
                if read[0] == value:
                    result = True
                    break

        if result == True:
            print "Method " + value

        else:
            print "No method found"
