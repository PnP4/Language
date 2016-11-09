from pandas import json

from antlr4 import *
from LanguageLexer import LanguageLexer
from LanguageListener import LanguageListener
from LanguageParser import LanguageParser
import sys
import xml.etree.cElementTree as ET

class LanguagePrintListener(LanguageListener):
    def enterHi(self, ctx):
        print("Hello: %s" % ctx.ID())

def createJson():
    with open("server.json", mode='w') as f:
        json.dump({'server' : []} , f)

def main():
    createJson()
    lexer = LanguageLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = LanguageParser(stream)
    tree = parser.init()
    printer = LanguagePrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
if __name__ == '__main__':
    main()




