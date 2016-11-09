# Generated from Language.g4 by ANTLR 4.5.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\b,\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write(u"\b\t\b\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4\3\4")
        buf.write(u"\3\4\5\4\35\n\4\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6&\n\6")
        buf.write(u"\3\7\3\7\3\b\3\b\3\b\2\2\t\2\4\6\b\n\f\16\2\2(\2\20\3")
        buf.write(u"\2\2\2\4\27\3\2\2\2\6\34\3\2\2\2\b\36\3\2\2\2\n%\3\2")
        buf.write(u"\2\2\f\'\3\2\2\2\16)\3\2\2\2\20\21\5\4\3\2\21\3\3\2\2")
        buf.write(u"\2\22\23\5\6\4\2\23\24\5\b\5\2\24\25\5\4\3\2\25\30\3")
        buf.write(u"\2\2\2\26\30\5\6\4\2\27\22\3\2\2\2\27\26\3\2\2\2\30\5")
        buf.write(u"\3\2\2\2\31\35\7\3\2\2\32\33\7\3\2\2\33\35\5\n\6\2\34")
        buf.write(u"\31\3\2\2\2\34\32\3\2\2\2\35\7\3\2\2\2\36\37\7\7\2\2")
        buf.write(u"\37\t\3\2\2\2 &\7\4\2\2!\"\7\4\2\2\"&\7\4\2\2#$\7\4\2")
        buf.write(u"\2$&\7\5\2\2% \3\2\2\2%!\3\2\2\2%#\3\2\2\2&\13\3\2\2")
        buf.write(u"\2\'(\7\5\2\2(\r\3\2\2\2)*\7\6\2\2*\17\3\2\2\2\5\27\34")
        buf.write(u"%")
        return buf.getvalue()


class LanguageParser ( Parser ):

    grammarFileName = "Language.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ u"<INVALID>", u"METHOD", u"PARAMETER", u"IP", u"PARAMETERSIGN", 
                      u"SINPIP", u"WS" ]

    RULE_init = 0
    RULE_com = 1
    RULE_method = 2
    RULE_pipe = 3
    RULE_parameter = 4
    RULE_ip = 5
    RULE_parametersign = 6

    ruleNames =  [ u"init", u"com", u"method", u"pipe", u"parameter", u"ip", 
                   u"parametersign" ]

    EOF = Token.EOF
    METHOD=1
    PARAMETER=2
    IP=3
    PARAMETERSIGN=4
    SINPIP=5
    WS=6

    def __init__(self, input):
        super(LanguageParser, self).__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class InitContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LanguageParser.InitContext, self).__init__(parent, invokingState)
            self.parser = parser

        def com(self):
            return self.getTypedRuleContext(LanguageParser.ComContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_init

        def enterRule(self, listener):
            if hasattr(listener, "enterInit"):
                listener.enterInit(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitInit"):
                listener.exitInit(self)




    def init(self):

        localctx = LanguageParser.InitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.com()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ComContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LanguageParser.ComContext, self).__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(LanguageParser.MethodContext,0)


        def pipe(self):
            return self.getTypedRuleContext(LanguageParser.PipeContext,0)


        def com(self):
            return self.getTypedRuleContext(LanguageParser.ComContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_com

        def enterRule(self, listener):
            if hasattr(listener, "enterCom"):
                listener.enterCom(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitCom"):
                listener.exitCom(self)




    def com(self):

        localctx = LanguageParser.ComContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_com)
        try:
            self.state = 21
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.method()
                self.state = 17
                self.pipe()
                self.state = 18
                self.com()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MethodContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LanguageParser.MethodContext, self).__init__(parent, invokingState)
            self.parser = parser

        def METHOD(self):
            return self.getToken(LanguageParser.METHOD, 0)

        def parameter(self):
            return self.getTypedRuleContext(LanguageParser.ParameterContext,0)


        def getRuleIndex(self):
            return LanguageParser.RULE_method

        def enterRule(self, listener):
            if hasattr(listener, "enterMethod"):
                listener.enterMethod(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMethod"):
                listener.exitMethod(self)




    def method(self):

        localctx = LanguageParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_method)
        try:
            self.state = 26
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(LanguageParser.METHOD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(LanguageParser.METHOD)
                self.state = 25
                self.parameter()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PipeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LanguageParser.PipeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def SINPIP(self):
            return self.getToken(LanguageParser.SINPIP, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_pipe

        def enterRule(self, listener):
            if hasattr(listener, "enterPipe"):
                listener.enterPipe(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitPipe"):
                listener.exitPipe(self)




    def pipe(self):

        localctx = LanguageParser.PipeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_pipe)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(LanguageParser.SINPIP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LanguageParser.ParameterContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PARAMETER(self, i=None):
            if i is None:
                return self.getTokens(LanguageParser.PARAMETER)
            else:
                return self.getToken(LanguageParser.PARAMETER, i)

        def IP(self):
            return self.getToken(LanguageParser.IP, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_parameter

        def enterRule(self, listener):
            if hasattr(listener, "enterParameter"):
                listener.enterParameter(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParameter"):
                listener.exitParameter(self)




    def parameter(self):

        localctx = LanguageParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameter)
        try:
            self.state = 35
            self._errHandler.sync(self);
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.match(LanguageParser.PARAMETER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.match(LanguageParser.PARAMETER)
                self.state = 32
                self.match(LanguageParser.PARAMETER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 33
                self.match(LanguageParser.PARAMETER)
                self.state = 34
                self.match(LanguageParser.IP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IpContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LanguageParser.IpContext, self).__init__(parent, invokingState)
            self.parser = parser

        def IP(self):
            return self.getToken(LanguageParser.IP, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_ip

        def enterRule(self, listener):
            if hasattr(listener, "enterIp"):
                listener.enterIp(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitIp"):
                listener.exitIp(self)




    def ip(self):

        localctx = LanguageParser.IpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_ip)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(LanguageParser.IP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParametersignContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(LanguageParser.ParametersignContext, self).__init__(parent, invokingState)
            self.parser = parser

        def PARAMETERSIGN(self):
            return self.getToken(LanguageParser.PARAMETERSIGN, 0)

        def getRuleIndex(self):
            return LanguageParser.RULE_parametersign

        def enterRule(self, listener):
            if hasattr(listener, "enterParametersign"):
                listener.enterParametersign(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitParametersign"):
                listener.exitParametersign(self)




    def parametersign(self):

        localctx = LanguageParser.ParametersignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_parametersign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(LanguageParser.PARAMETERSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





