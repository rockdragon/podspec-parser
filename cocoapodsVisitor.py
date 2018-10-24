# Generated from cocoapods.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cocoapodsParser import cocoapodsParser
else:
    from cocoapodsParser import cocoapodsParser

# This class defines a complete generic visitor for a parse tree produced by cocoapodsParser.

class cocoapodsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cocoapodsParser#prog.
    def visitProg(self, ctx:cocoapodsParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#expression_list.
    def visitExpression_list(self, ctx:cocoapodsParser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#expression.
    def visitExpression(self, ctx:cocoapodsParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#global_get.
    def visitGlobal_get(self, ctx:cocoapodsParser.Global_getContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#global_set.
    def visitGlobal_set(self, ctx:cocoapodsParser.Global_setContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#global_result.
    def visitGlobal_result(self, ctx:cocoapodsParser.Global_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_inline_call.
    def visitFunction_inline_call(self, ctx:cocoapodsParser.Function_inline_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#require_block.
    def visitRequire_block(self, ctx:cocoapodsParser.Require_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#pir_inline.
    def visitPir_inline(self, ctx:cocoapodsParser.Pir_inlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#pir_expression_list.
    def visitPir_expression_list(self, ctx:cocoapodsParser.Pir_expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_definition.
    def visitFunction_definition(self, ctx:cocoapodsParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_definition_body.
    def visitFunction_definition_body(self, ctx:cocoapodsParser.Function_definition_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_definition_header.
    def visitFunction_definition_header(self, ctx:cocoapodsParser.Function_definition_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_name.
    def visitFunction_name(self, ctx:cocoapodsParser.Function_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_definition_params.
    def visitFunction_definition_params(self, ctx:cocoapodsParser.Function_definition_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_definition_params_list.
    def visitFunction_definition_params_list(self, ctx:cocoapodsParser.Function_definition_params_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_definition_param_id.
    def visitFunction_definition_param_id(self, ctx:cocoapodsParser.Function_definition_param_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#return_statement.
    def visitReturn_statement(self, ctx:cocoapodsParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_call.
    def visitFunction_call(self, ctx:cocoapodsParser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_call_param_list.
    def visitFunction_call_param_list(self, ctx:cocoapodsParser.Function_call_param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_call_params.
    def visitFunction_call_params(self, ctx:cocoapodsParser.Function_call_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_param.
    def visitFunction_param(self, ctx:cocoapodsParser.Function_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_unnamed_param.
    def visitFunction_unnamed_param(self, ctx:cocoapodsParser.Function_unnamed_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_named_param.
    def visitFunction_named_param(self, ctx:cocoapodsParser.Function_named_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#function_call_assignment.
    def visitFunction_call_assignment(self, ctx:cocoapodsParser.Function_call_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#all_result.
    def visitAll_result(self, ctx:cocoapodsParser.All_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#elsif_statement.
    def visitElsif_statement(self, ctx:cocoapodsParser.Elsif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#if_elsif_statement.
    def visitIf_elsif_statement(self, ctx:cocoapodsParser.If_elsif_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#if_statement.
    def visitIf_statement(self, ctx:cocoapodsParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#unless_statement.
    def visitUnless_statement(self, ctx:cocoapodsParser.Unless_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#while_statement.
    def visitWhile_statement(self, ctx:cocoapodsParser.While_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#for_statement.
    def visitFor_statement(self, ctx:cocoapodsParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#init_expression.
    def visitInit_expression(self, ctx:cocoapodsParser.Init_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#all_assignment.
    def visitAll_assignment(self, ctx:cocoapodsParser.All_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#for_init_list.
    def visitFor_init_list(self, ctx:cocoapodsParser.For_init_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#cond_expression.
    def visitCond_expression(self, ctx:cocoapodsParser.Cond_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#loop_expression.
    def visitLoop_expression(self, ctx:cocoapodsParser.Loop_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#for_loop_list.
    def visitFor_loop_list(self, ctx:cocoapodsParser.For_loop_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#statement_body.
    def visitStatement_body(self, ctx:cocoapodsParser.Statement_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#statement_expression_list.
    def visitStatement_expression_list(self, ctx:cocoapodsParser.Statement_expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#assignment.
    def visitAssignment(self, ctx:cocoapodsParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#dynamic_assignment.
    def visitDynamic_assignment(self, ctx:cocoapodsParser.Dynamic_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#int_assignment.
    def visitInt_assignment(self, ctx:cocoapodsParser.Int_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#float_assignment.
    def visitFloat_assignment(self, ctx:cocoapodsParser.Float_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#string_assignment.
    def visitString_assignment(self, ctx:cocoapodsParser.String_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#initial_array_assignment.
    def visitInitial_array_assignment(self, ctx:cocoapodsParser.Initial_array_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#array_assignment.
    def visitArray_assignment(self, ctx:cocoapodsParser.Array_assignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#array_definition.
    def visitArray_definition(self, ctx:cocoapodsParser.Array_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#array_definition_elements.
    def visitArray_definition_elements(self, ctx:cocoapodsParser.Array_definition_elementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#array_selector.
    def visitArray_selector(self, ctx:cocoapodsParser.Array_selectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#dynamic_result.
    def visitDynamic_result(self, ctx:cocoapodsParser.Dynamic_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#dynamic.
    def visitDynamic(self, ctx:cocoapodsParser.DynamicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#int_result.
    def visitInt_result(self, ctx:cocoapodsParser.Int_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#float_result.
    def visitFloat_result(self, ctx:cocoapodsParser.Float_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#string_result.
    def visitString_result(self, ctx:cocoapodsParser.String_resultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#comparison_list.
    def visitComparison_list(self, ctx:cocoapodsParser.Comparison_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#comparison.
    def visitComparison(self, ctx:cocoapodsParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#comp_var.
    def visitComp_var(self, ctx:cocoapodsParser.Comp_varContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#lvalue.
    def visitLvalue(self, ctx:cocoapodsParser.LvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#rvalue.
    def visitRvalue(self, ctx:cocoapodsParser.RvalueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#break_expression.
    def visitBreak_expression(self, ctx:cocoapodsParser.Break_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#literal_t.
    def visitLiteral_t(self, ctx:cocoapodsParser.Literal_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#float_t.
    def visitFloat_t(self, ctx:cocoapodsParser.Float_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#int_t.
    def visitInt_t(self, ctx:cocoapodsParser.Int_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#bool_t.
    def visitBool_t(self, ctx:cocoapodsParser.Bool_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#nil_t.
    def visitNil_t(self, ctx:cocoapodsParser.Nil_tContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#id.
    def visitId(self, ctx:cocoapodsParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#id_global.
    def visitId_global(self, ctx:cocoapodsParser.Id_globalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#id_function.
    def visitId_function(self, ctx:cocoapodsParser.Id_functionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#terminator.
    def visitTerminator(self, ctx:cocoapodsParser.TerminatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#else_token.
    def visitElse_token(self, ctx:cocoapodsParser.Else_tokenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cocoapodsParser#crlf.
    def visitCrlf(self, ctx:cocoapodsParser.CrlfContext):
        return self.visitChildren(ctx)



del cocoapodsParser