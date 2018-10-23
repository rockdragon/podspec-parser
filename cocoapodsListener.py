# Generated from cocoapods.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cocoapodsParser import cocoapodsParser
else:
    from cocoapodsParser import cocoapodsParser

# This class defines a complete listener for a parse tree produced by cocoapodsParser.
class cocoapodsListener(ParseTreeListener):

    # Enter a parse tree produced by cocoapodsParser#requirement.
    def enterRequirement(self, ctx:cocoapodsParser.RequirementContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#requirement.
    def exitRequirement(self, ctx:cocoapodsParser.RequirementContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#version.
    def enterVersion(self, ctx:cocoapodsParser.VersionContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#version.
    def exitVersion(self, ctx:cocoapodsParser.VersionContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#major.
    def enterMajor(self, ctx:cocoapodsParser.MajorContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#major.
    def exitMajor(self, ctx:cocoapodsParser.MajorContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#minor.
    def enterMinor(self, ctx:cocoapodsParser.MinorContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#minor.
    def exitMinor(self, ctx:cocoapodsParser.MinorContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#patch.
    def enterPatch(self, ctx:cocoapodsParser.PatchContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#patch.
    def exitPatch(self, ctx:cocoapodsParser.PatchContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#operator.
    def enterOperator(self, ctx:cocoapodsParser.OperatorContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#operator.
    def exitOperator(self, ctx:cocoapodsParser.OperatorContext):
        pass


