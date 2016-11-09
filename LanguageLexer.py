# Generated from Language.g4 by ANTLR 4.5.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\b+\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\3\2\6\2\21\n\2\r\2\16\2\22\3\3\3\3\6\3\27\n\3\r\3")
        buf.write(u"\16\3\30\3\4\3\4\6\4\35\n\4\r\4\16\4\36\3\5\3\5\3\6\3")
        buf.write(u"\6\3\7\6\7&\n\7\r\7\16\7\'\3\7\3\7\2\2\b\3\3\5\4\7\5")
        buf.write(u"\t\6\13\7\r\b\3\2\7\3\2c|\3\2\62;\3\2//\3\2~~\5\2\13")
        buf.write(u"\f\17\17\"\".\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t")
        buf.write(u"\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\20\3\2\2\2\5\24\3")
        buf.write(u"\2\2\2\7\32\3\2\2\2\t \3\2\2\2\13\"\3\2\2\2\r%\3\2\2")
        buf.write(u"\2\17\21\t\2\2\2\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3")
        buf.write(u"\2\2\2\22\23\3\2\2\2\23\4\3\2\2\2\24\26\5\t\5\2\25\27")
        buf.write(u"\t\2\2\2\26\25\3\2\2\2\27\30\3\2\2\2\30\26\3\2\2\2\30")
        buf.write(u"\31\3\2\2\2\31\6\3\2\2\2\32\34\5\t\5\2\33\35\t\3\2\2")
        buf.write(u"\34\33\3\2\2\2\35\36\3\2\2\2\36\34\3\2\2\2\36\37\3\2")
        buf.write(u"\2\2\37\b\3\2\2\2 !\t\4\2\2!\n\3\2\2\2\"#\t\5\2\2#\f")
        buf.write(u"\3\2\2\2$&\t\6\2\2%$\3\2\2\2&\'\3\2\2\2\'%\3\2\2\2\'")
        buf.write(u"(\3\2\2\2()\3\2\2\2)*\b\7\2\2*\16\3\2\2\2\7\2\22\30\36")
        buf.write(u"\'\3\b\2\2")
        return buf.getvalue()


class LanguageLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    METHOD = 1
    PARAMETER = 2
    IP = 3
    PARAMETERSIGN = 4
    SINPIP = 5
    WS = 6

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
 ]

    symbolicNames = [ u"<INVALID>",
            u"METHOD", u"PARAMETER", u"IP", u"PARAMETERSIGN", u"SINPIP", 
            u"WS" ]

    ruleNames = [ u"METHOD", u"PARAMETER", u"IP", u"PARAMETERSIGN", u"SINPIP", 
                  u"WS" ]

    grammarFileName = u"Language.g4"

    def __init__(self, input=None):
        super(LanguageLexer, self).__init__(input)
        self.checkVersion("4.5.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


