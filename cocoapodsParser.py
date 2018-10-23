# Generated from cocoapods.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("8\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\7\2\20\n\2\f\2\16\2\23\13\2\3\2\5\2\26\n\2\3\2\7\2\31")
        buf.write("\n\2\f\2\16\2\34\13\2\3\2\3\2\7\2 \n\2\f\2\16\2#\13\2")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\5\3,\n\3\5\3.\n\3\3\4\3\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\3\7\2\2\b\2\4\6\b\n\f\2\2\2\67")
        buf.write("\2\21\3\2\2\2\4&\3\2\2\2\6/\3\2\2\2\b\61\3\2\2\2\n\63")
        buf.write("\3\2\2\2\f\65\3\2\2\2\16\20\7\16\2\2\17\16\3\2\2\2\20")
        buf.write("\23\3\2\2\2\21\17\3\2\2\2\21\22\3\2\2\2\22\25\3\2\2\2")
        buf.write("\23\21\3\2\2\2\24\26\5\f\7\2\25\24\3\2\2\2\25\26\3\2\2")
        buf.write("\2\26\32\3\2\2\2\27\31\7\16\2\2\30\27\3\2\2\2\31\34\3")
        buf.write("\2\2\2\32\30\3\2\2\2\32\33\3\2\2\2\33\35\3\2\2\2\34\32")
        buf.write("\3\2\2\2\35!\5\4\3\2\36 \7\16\2\2\37\36\3\2\2\2 #\3\2")
        buf.write("\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#!\3\2\2\2$%\7\2")
        buf.write("\2\3%\3\3\2\2\2&-\5\6\4\2\'(\7\f\2\2(+\5\b\5\2)*\7\f\2")
        buf.write("\2*,\5\n\6\2+)\3\2\2\2+,\3\2\2\2,.\3\2\2\2-\'\3\2\2\2")
        buf.write("-.\3\2\2\2.\5\3\2\2\2/\60\7\4\2\2\60\7\3\2\2\2\61\62\7")
        buf.write("\4\2\2\62\t\3\2\2\2\63\64\7\4\2\2\64\13\3\2\2\2\65\66")
        buf.write("\7\3\2\2\66\r\3\2\2\2\b\21\25\32!+-")
        return buf.getvalue()


class cocoapodsParser ( Parser ):

    grammarFileName = "cocoapods.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'0'", "<INVALID>", "'['", "']'", "'('", "')'", "'.'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "OPERATOR", "VERSION_ELEMENT", "NON_ZERO", 
                      "ZERO", "NUMBER", "LEFT_BRACKET", "RIGHT_BRACKET", 
                      "LEFT_PARENS", "RIGHT_PARENS", "DOT", "COMMA", "WS" ]

    RULE_requirement = 0
    RULE_version = 1
    RULE_major = 2
    RULE_minor = 3
    RULE_patch = 4
    RULE_operator = 5

    ruleNames =  [ "requirement", "version", "major", "minor", "patch", 
                   "operator" ]

    EOF = Token.EOF
    OPERATOR=1
    VERSION_ELEMENT=2
    NON_ZERO=3
    ZERO=4
    NUMBER=5
    LEFT_BRACKET=6
    RIGHT_BRACKET=7
    LEFT_PARENS=8
    RIGHT_PARENS=9
    DOT=10
    COMMA=11
    WS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class RequirementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def version(self):
            return self.getTypedRuleContext(cocoapodsParser.VersionContext,0)


        def EOF(self):
            return self.getToken(cocoapodsParser.EOF, 0)

        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(cocoapodsParser.WS)
            else:
                return self.getToken(cocoapodsParser.WS, i)

        def operator(self):
            return self.getTypedRuleContext(cocoapodsParser.OperatorContext,0)


        def getRuleIndex(self):
            return cocoapodsParser.RULE_requirement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRequirement" ):
                listener.enterRequirement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRequirement" ):
                listener.exitRequirement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRequirement" ):
                return visitor.visitRequirement(self)
            else:
                return visitor.visitChildren(self)




    def requirement(self):

        localctx = cocoapodsParser.RequirementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_requirement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 12
                    self.match(cocoapodsParser.WS) 
                self.state = 17
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 19
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cocoapodsParser.OPERATOR:
                self.state = 18
                self.operator()


            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoapodsParser.WS:
                self.state = 21
                self.match(cocoapodsParser.WS)
                self.state = 26
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 27
            self.version()
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==cocoapodsParser.WS:
                self.state = 28
                self.match(cocoapodsParser.WS)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(cocoapodsParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VersionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def major(self):
            return self.getTypedRuleContext(cocoapodsParser.MajorContext,0)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(cocoapodsParser.DOT)
            else:
                return self.getToken(cocoapodsParser.DOT, i)

        def minor(self):
            return self.getTypedRuleContext(cocoapodsParser.MinorContext,0)


        def patch(self):
            return self.getTypedRuleContext(cocoapodsParser.PatchContext,0)


        def getRuleIndex(self):
            return cocoapodsParser.RULE_version

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVersion" ):
                listener.enterVersion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVersion" ):
                listener.exitVersion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVersion" ):
                return visitor.visitVersion(self)
            else:
                return visitor.visitChildren(self)




    def version(self):

        localctx = cocoapodsParser.VersionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_version)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.major()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==cocoapodsParser.DOT:
                self.state = 37
                self.match(cocoapodsParser.DOT)
                self.state = 38
                self.minor()
                self.state = 41
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==cocoapodsParser.DOT:
                    self.state = 39
                    self.match(cocoapodsParser.DOT)
                    self.state = 40
                    self.patch()




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MajorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION_ELEMENT(self):
            return self.getToken(cocoapodsParser.VERSION_ELEMENT, 0)

        def getRuleIndex(self):
            return cocoapodsParser.RULE_major

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMajor" ):
                listener.enterMajor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMajor" ):
                listener.exitMajor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMajor" ):
                return visitor.visitMajor(self)
            else:
                return visitor.visitChildren(self)




    def major(self):

        localctx = cocoapodsParser.MajorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_major)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(cocoapodsParser.VERSION_ELEMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MinorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION_ELEMENT(self):
            return self.getToken(cocoapodsParser.VERSION_ELEMENT, 0)

        def getRuleIndex(self):
            return cocoapodsParser.RULE_minor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMinor" ):
                listener.enterMinor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMinor" ):
                listener.exitMinor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinor" ):
                return visitor.visitMinor(self)
            else:
                return visitor.visitChildren(self)




    def minor(self):

        localctx = cocoapodsParser.MinorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_minor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(cocoapodsParser.VERSION_ELEMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PatchContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VERSION_ELEMENT(self):
            return self.getToken(cocoapodsParser.VERSION_ELEMENT, 0)

        def getRuleIndex(self):
            return cocoapodsParser.RULE_patch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPatch" ):
                listener.enterPatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPatch" ):
                listener.exitPatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPatch" ):
                return visitor.visitPatch(self)
            else:
                return visitor.visitChildren(self)




    def patch(self):

        localctx = cocoapodsParser.PatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_patch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(cocoapodsParser.VERSION_ELEMENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class OperatorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(cocoapodsParser.OPERATOR, 0)

        def getRuleIndex(self):
            return cocoapodsParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperator" ):
                return visitor.visitOperator(self)
            else:
                return visitor.visitChildren(self)




    def operator(self):

        localctx = cocoapodsParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_operator)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(cocoapodsParser.OPERATOR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





