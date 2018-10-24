import sys
from antlr4 import *
from cocoapodsLexer import cocoapodsLexer
from cocoapodsParser import cocoapodsParser
from cocoapodsListener import cocoapodsListener

def main(argv):
    input = FileStream(argv[1])
    lexer = cocoapodsLexer(input)
    stream = CommonTokenStream(lexer)
    parser = cocoapodsParser(stream)
    tree = parser.prog()
    print(tree.__dir__())
    printer = cocoapodsListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)


