# Generated from cocoapods.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("n\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\3\2\3\2\5\2\60\n\2\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\7\48\n\4\f\4\16\4;\13\4\5\4=\n\4")
        buf.write("\3\5\3\5\3\6\3\6\3\7\3\7\5\7E\n\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\5\bL\n\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3")
        buf.write("\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3")
        buf.write("\22\3\23\3\23\3\24\3\24\3\25\3\25\3\26\6\26k\n\26\r\26")
        buf.write("\16\26l\2\2\27\3\3\5\2\7\4\t\5\13\6\r\7\17\2\21\2\23\2")
        buf.write("\25\2\27\2\31\2\33\2\35\2\37\b!\t#\n%\13\'\f)\r+\16\3")
        buf.write("\2\3\4\2\13\13\"\"\2m\2\3\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2")
        buf.write("\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2")
        buf.write("\2\3/\3\2\2\2\5\61\3\2\2\2\7<\3\2\2\2\t>\3\2\2\2\13@\3")
        buf.write("\2\2\2\rD\3\2\2\2\17K\3\2\2\2\21M\3\2\2\2\23P\3\2\2\2")
        buf.write("\25S\3\2\2\2\27U\3\2\2\2\31W\3\2\2\2\33Y\3\2\2\2\35[\3")
        buf.write("\2\2\2\37]\3\2\2\2!_\3\2\2\2#a\3\2\2\2%c\3\2\2\2\'e\3")
        buf.write("\2\2\2)g\3\2\2\2+j\3\2\2\2-\60\5\17\b\2.\60\5\5\3\2/-")
        buf.write("\3\2\2\2/.\3\2\2\2\60\4\3\2\2\2\61\62\5\33\16\2\62\63")
        buf.write("\5\27\f\2\63\6\3\2\2\2\64=\5\13\6\2\659\5\t\5\2\668\5")
        buf.write("\r\7\2\67\66\3\2\2\28;\3\2\2\29\67\3\2\2\29:\3\2\2\2:")
        buf.write("=\3\2\2\2;9\3\2\2\2<\64\3\2\2\2<\65\3\2\2\2=\b\3\2\2\2")
        buf.write(">?\4\63;\2?\n\3\2\2\2@A\7\62\2\2A\f\3\2\2\2BE\5\13\6\2")
        buf.write("CE\5\t\5\2DB\3\2\2\2DC\3\2\2\2E\16\3\2\2\2FL\5\23\n\2")
        buf.write("GL\5\21\t\2HL\5\25\13\2IL\5\27\f\2JL\5\31\r\2KF\3\2\2")
        buf.write("\2KG\3\2\2\2KH\3\2\2\2KI\3\2\2\2KJ\3\2\2\2L\20\3\2\2\2")
        buf.write("MN\5\25\13\2NO\5\31\r\2O\22\3\2\2\2PQ\5\27\f\2QR\5\31")
        buf.write("\r\2R\24\3\2\2\2ST\7>\2\2T\26\3\2\2\2UV\7@\2\2V\30\3\2")
        buf.write("\2\2WX\7?\2\2X\32\3\2\2\2YZ\7\u0080\2\2Z\34\3\2\2\2[\\")
        buf.write("\7`\2\2\\\36\3\2\2\2]^\7]\2\2^ \3\2\2\2_`\7_\2\2`\"\3")
        buf.write("\2\2\2ab\7*\2\2b$\3\2\2\2cd\7+\2\2d&\3\2\2\2ef\7\60\2")
        buf.write("\2f(\3\2\2\2gh\7.\2\2h*\3\2\2\2ik\t\2\2\2ji\3\2\2\2kl")
        buf.write("\3\2\2\2lj\3\2\2\2lm\3\2\2\2m,\3\2\2\2\t\2/9<DKl\2")
        return buf.getvalue()


class cocoapodsLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    OPERATOR = 1
    VERSION_ELEMENT = 2
    NON_ZERO = 3
    ZERO = 4
    NUMBER = 5
    LEFT_BRACKET = 6
    RIGHT_BRACKET = 7
    LEFT_PARENS = 8
    RIGHT_PARENS = 9
    DOT = 10
    COMMA = 11
    WS = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'0'", "'['", "']'", "'('", "')'", "'.'", "','" ]

    symbolicNames = [ "<INVALID>",
            "OPERATOR", "VERSION_ELEMENT", "NON_ZERO", "ZERO", "NUMBER", 
            "LEFT_BRACKET", "RIGHT_BRACKET", "LEFT_PARENS", "RIGHT_PARENS", 
            "DOT", "COMMA", "WS" ]

    ruleNames = [ "OPERATOR", "COCOA_VERSION", "VERSION_ELEMENT", "NON_ZERO", 
                  "ZERO", "NUMBER", "SIMPLE_OPERATOR", "LTEQ", "GTEQ", "LT", 
                  "GT", "EQ", "TILDE", "CARET", "LEFT_BRACKET", "RIGHT_BRACKET", 
                  "LEFT_PARENS", "RIGHT_PARENS", "DOT", "COMMA", "WS" ]

    grammarFileName = "cocoapods.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


