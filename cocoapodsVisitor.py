# Generated from cocoapods.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cocoapodsParser import cocoapodsParser
else:
    from cocoapodsParser import cocoapodsParser

# This class defines a complete generic visitor for a parse tree produced by cocoapodsParser.

class cocoapodsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cocoapodsParser#requirement.
    def visitRequirement(self, ctx:cocoapodsParser.RequirementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#version.
    def visitVersion(self, ctx:cocoapodsParser.VersionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#major.
    def visitMajor(self, ctx:cocoapodsParser.MajorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#minor.
    def visitMinor(self, ctx:cocoapodsParser.MinorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#patch.
    def visitPatch(self, ctx:cocoapodsParser.PatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#operator.
    def visitOperator(self, ctx:cocoapodsParser.OperatorContext):
        return self.visitChildren(ctx)



del cocoapodsParser