# Generated from cocoapods.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cocoapodsParser import cocoapodsParser
else:
    from cocoapodsParser import cocoapodsParser

# This class defines a complete listener for a parse tree produced by cocoapodsParser.
class cocoapodsListener(ParseTreeListener):

    # Enter a parse tree produced by cocoapodsParser#prog.
    def enterProg(self, ctx:cocoapodsParser.ProgContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#prog.
    def exitProg(self, ctx:cocoapodsParser.ProgContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#expression_list.
    def enterExpression_list(self, ctx:cocoapodsParser.Expression_listContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#expression_list.
    def exitExpression_list(self, ctx:cocoapodsParser.Expression_listContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#expression.
    def enterExpression(self, ctx:cocoapodsParser.ExpressionContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#expression.
    def exitExpression(self, ctx:cocoapodsParser.ExpressionContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#global_get.
    def enterGlobal_get(self, ctx:cocoapodsParser.Global_getContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#global_get.
    def exitGlobal_get(self, ctx:cocoapodsParser.Global_getContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#global_set.
    def enterGlobal_set(self, ctx:cocoapodsParser.Global_setContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#global_set.
    def exitGlobal_set(self, ctx:cocoapodsParser.Global_setContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#global_result.
    def enterGlobal_result(self, ctx:cocoapodsParser.Global_resultContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#global_result.
    def exitGlobal_result(self, ctx:cocoapodsParser.Global_resultContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_inline_call.
    def enterFunction_inline_call(self, ctx:cocoapodsParser.Function_inline_callContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_inline_call.
    def exitFunction_inline_call(self, ctx:cocoapodsParser.Function_inline_callContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#require_block.
    def enterRequire_block(self, ctx:cocoapodsParser.Require_blockContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#require_block.
    def exitRequire_block(self, ctx:cocoapodsParser.Require_blockContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#pir_inline.
    def enterPir_inline(self, ctx:cocoapodsParser.Pir_inlineContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#pir_inline.
    def exitPir_inline(self, ctx:cocoapodsParser.Pir_inlineContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#pir_expression_list.
    def enterPir_expression_list(self, ctx:cocoapodsParser.Pir_expression_listContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#pir_expression_list.
    def exitPir_expression_list(self, ctx:cocoapodsParser.Pir_expression_listContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_definition.
    def enterFunction_definition(self, ctx:cocoapodsParser.Function_definitionContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_definition.
    def exitFunction_definition(self, ctx:cocoapodsParser.Function_definitionContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_definition_body.
    def enterFunction_definition_body(self, ctx:cocoapodsParser.Function_definition_bodyContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_definition_body.
    def exitFunction_definition_body(self, ctx:cocoapodsParser.Function_definition_bodyContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_definition_header.
    def enterFunction_definition_header(self, ctx:cocoapodsParser.Function_definition_headerContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_definition_header.
    def exitFunction_definition_header(self, ctx:cocoapodsParser.Function_definition_headerContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_name.
    def enterFunction_name(self, ctx:cocoapodsParser.Function_nameContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_name.
    def exitFunction_name(self, ctx:cocoapodsParser.Function_nameContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_definition_params.
    def enterFunction_definition_params(self, ctx:cocoapodsParser.Function_definition_paramsContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_definition_params.
    def exitFunction_definition_params(self, ctx:cocoapodsParser.Function_definition_paramsContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_definition_params_list.
    def enterFunction_definition_params_list(self, ctx:cocoapodsParser.Function_definition_params_listContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_definition_params_list.
    def exitFunction_definition_params_list(self, ctx:cocoapodsParser.Function_definition_params_listContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_definition_param_id.
    def enterFunction_definition_param_id(self, ctx:cocoapodsParser.Function_definition_param_idContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_definition_param_id.
    def exitFunction_definition_param_id(self, ctx:cocoapodsParser.Function_definition_param_idContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#return_statement.
    def enterReturn_statement(self, ctx:cocoapodsParser.Return_statementContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#return_statement.
    def exitReturn_statement(self, ctx:cocoapodsParser.Return_statementContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_call.
    def enterFunction_call(self, ctx:cocoapodsParser.Function_callContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_call.
    def exitFunction_call(self, ctx:cocoapodsParser.Function_callContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_call_param_list.
    def enterFunction_call_param_list(self, ctx:cocoapodsParser.Function_call_param_listContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_call_param_list.
    def exitFunction_call_param_list(self, ctx:cocoapodsParser.Function_call_param_listContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_call_params.
    def enterFunction_call_params(self, ctx:cocoapodsParser.Function_call_paramsContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_call_params.
    def exitFunction_call_params(self, ctx:cocoapodsParser.Function_call_paramsContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_param.
    def enterFunction_param(self, ctx:cocoapodsParser.Function_paramContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_param.
    def exitFunction_param(self, ctx:cocoapodsParser.Function_paramContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_unnamed_param.
    def enterFunction_unnamed_param(self, ctx:cocoapodsParser.Function_unnamed_paramContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_unnamed_param.
    def exitFunction_unnamed_param(self, ctx:cocoapodsParser.Function_unnamed_paramContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_named_param.
    def enterFunction_named_param(self, ctx:cocoapodsParser.Function_named_paramContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_named_param.
    def exitFunction_named_param(self, ctx:cocoapodsParser.Function_named_paramContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#function_call_assignment.
    def enterFunction_call_assignment(self, ctx:cocoapodsParser.Function_call_assignmentContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#function_call_assignment.
    def exitFunction_call_assignment(self, ctx:cocoapodsParser.Function_call_assignmentContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#all_result.
    def enterAll_result(self, ctx:cocoapodsParser.All_resultContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#all_result.
    def exitAll_result(self, ctx:cocoapodsParser.All_resultContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#elsif_statement.
    def enterElsif_statement(self, ctx:cocoapodsParser.Elsif_statementContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#elsif_statement.
    def exitElsif_statement(self, ctx:cocoapodsParser.Elsif_statementContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#if_elsif_statement.
    def enterIf_elsif_statement(self, ctx:cocoapodsParser.If_elsif_statementContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#if_elsif_statement.
    def exitIf_elsif_statement(self, ctx:cocoapodsParser.If_elsif_statementContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#if_statement.
    def enterIf_statement(self, ctx:cocoapodsParser.If_statementContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#if_statement.
    def exitIf_statement(self, ctx:cocoapodsParser.If_statementContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#unless_statement.
    def enterUnless_statement(self, ctx:cocoapodsParser.Unless_statementContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#unless_statement.
    def exitUnless_statement(self, ctx:cocoapodsParser.Unless_statementContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#while_statement.
    def enterWhile_statement(self, ctx:cocoapodsParser.While_statementContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#while_statement.
    def exitWhile_statement(self, ctx:cocoapodsParser.While_statementContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#for_statement.
    def enterFor_statement(self, ctx:cocoapodsParser.For_statementContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#for_statement.
    def exitFor_statement(self, ctx:cocoapodsParser.For_statementContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#init_expression.
    def enterInit_expression(self, ctx:cocoapodsParser.Init_expressionContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#init_expression.
    def exitInit_expression(self, ctx:cocoapodsParser.Init_expressionContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#all_assignment.
    def enterAll_assignment(self, ctx:cocoapodsParser.All_assignmentContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#all_assignment.
    def exitAll_assignment(self, ctx:cocoapodsParser.All_assignmentContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#for_init_list.
    def enterFor_init_list(self, ctx:cocoapodsParser.For_init_listContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#for_init_list.
    def exitFor_init_list(self, ctx:cocoapodsParser.For_init_listContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#cond_expression.
    def enterCond_expression(self, ctx:cocoapodsParser.Cond_expressionContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#cond_expression.
    def exitCond_expression(self, ctx:cocoapodsParser.Cond_expressionContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#loop_expression.
    def enterLoop_expression(self, ctx:cocoapodsParser.Loop_expressionContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#loop_expression.
    def exitLoop_expression(self, ctx:cocoapodsParser.Loop_expressionContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#for_loop_list.
    def enterFor_loop_list(self, ctx:cocoapodsParser.For_loop_listContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#for_loop_list.
    def exitFor_loop_list(self, ctx:cocoapodsParser.For_loop_listContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#statement_body.
    def enterStatement_body(self, ctx:cocoapodsParser.Statement_bodyContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#statement_body.
    def exitStatement_body(self, ctx:cocoapodsParser.Statement_bodyContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#statement_expression_list.
    def enterStatement_expression_list(self, ctx:cocoapodsParser.Statement_expression_listContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#statement_expression_list.
    def exitStatement_expression_list(self, ctx:cocoapodsParser.Statement_expression_listContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#assignment.
    def enterAssignment(self, ctx:cocoapodsParser.AssignmentContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#assignment.
    def exitAssignment(self, ctx:cocoapodsParser.AssignmentContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#dynamic_assignment.
    def enterDynamic_assignment(self, ctx:cocoapodsParser.Dynamic_assignmentContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#dynamic_assignment.
    def exitDynamic_assignment(self, ctx:cocoapodsParser.Dynamic_assignmentContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#int_assignment.
    def enterInt_assignment(self, ctx:cocoapodsParser.Int_assignmentContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#int_assignment.
    def exitInt_assignment(self, ctx:cocoapodsParser.Int_assignmentContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#float_assignment.
    def enterFloat_assignment(self, ctx:cocoapodsParser.Float_assignmentContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#float_assignment.
    def exitFloat_assignment(self, ctx:cocoapodsParser.Float_assignmentContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#string_assignment.
    def enterString_assignment(self, ctx:cocoapodsParser.String_assignmentContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#string_assignment.
    def exitString_assignment(self, ctx:cocoapodsParser.String_assignmentContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#initial_array_assignment.
    def enterInitial_array_assignment(self, ctx:cocoapodsParser.Initial_array_assignmentContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#initial_array_assignment.
    def exitInitial_array_assignment(self, ctx:cocoapodsParser.Initial_array_assignmentContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#array_assignment.
    def enterArray_assignment(self, ctx:cocoapodsParser.Array_assignmentContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#array_assignment.
    def exitArray_assignment(self, ctx:cocoapodsParser.Array_assignmentContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#array_definition.
    def enterArray_definition(self, ctx:cocoapodsParser.Array_definitionContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#array_definition.
    def exitArray_definition(self, ctx:cocoapodsParser.Array_definitionContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#array_definition_elements.
    def enterArray_definition_elements(self, ctx:cocoapodsParser.Array_definition_elementsContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#array_definition_elements.
    def exitArray_definition_elements(self, ctx:cocoapodsParser.Array_definition_elementsContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#array_selector.
    def enterArray_selector(self, ctx:cocoapodsParser.Array_selectorContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#array_selector.
    def exitArray_selector(self, ctx:cocoapodsParser.Array_selectorContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#dynamic_result.
    def enterDynamic_result(self, ctx:cocoapodsParser.Dynamic_resultContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#dynamic_result.
    def exitDynamic_result(self, ctx:cocoapodsParser.Dynamic_resultContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#dynamic.
    def enterDynamic(self, ctx:cocoapodsParser.DynamicContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#dynamic.
    def exitDynamic(self, ctx:cocoapodsParser.DynamicContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#int_result.
    def enterInt_result(self, ctx:cocoapodsParser.Int_resultContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#int_result.
    def exitInt_result(self, ctx:cocoapodsParser.Int_resultContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#float_result.
    def enterFloat_result(self, ctx:cocoapodsParser.Float_resultContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#float_result.
    def exitFloat_result(self, ctx:cocoapodsParser.Float_resultContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#string_result.
    def enterString_result(self, ctx:cocoapodsParser.String_resultContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#string_result.
    def exitString_result(self, ctx:cocoapodsParser.String_resultContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#comparison_list.
    def enterComparison_list(self, ctx:cocoapodsParser.Comparison_listContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#comparison_list.
    def exitComparison_list(self, ctx:cocoapodsParser.Comparison_listContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#comparison.
    def enterComparison(self, ctx:cocoapodsParser.ComparisonContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#comparison.
    def exitComparison(self, ctx:cocoapodsParser.ComparisonContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#comp_var.
    def enterComp_var(self, ctx:cocoapodsParser.Comp_varContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#comp_var.
    def exitComp_var(self, ctx:cocoapodsParser.Comp_varContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#lvalue.
    def enterLvalue(self, ctx:cocoapodsParser.LvalueContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#lvalue.
    def exitLvalue(self, ctx:cocoapodsParser.LvalueContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#rvalue.
    def enterRvalue(self, ctx:cocoapodsParser.RvalueContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#rvalue.
    def exitRvalue(self, ctx:cocoapodsParser.RvalueContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#break_expression.
    def enterBreak_expression(self, ctx:cocoapodsParser.Break_expressionContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#break_expression.
    def exitBreak_expression(self, ctx:cocoapodsParser.Break_expressionContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#literal_t.
    def enterLiteral_t(self, ctx:cocoapodsParser.Literal_tContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#literal_t.
    def exitLiteral_t(self, ctx:cocoapodsParser.Literal_tContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#float_t.
    def enterFloat_t(self, ctx:cocoapodsParser.Float_tContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#float_t.
    def exitFloat_t(self, ctx:cocoapodsParser.Float_tContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#int_t.
    def enterInt_t(self, ctx:cocoapodsParser.Int_tContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#int_t.
    def exitInt_t(self, ctx:cocoapodsParser.Int_tContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#bool_t.
    def enterBool_t(self, ctx:cocoapodsParser.Bool_tContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#bool_t.
    def exitBool_t(self, ctx:cocoapodsParser.Bool_tContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#nil_t.
    def enterNil_t(self, ctx:cocoapodsParser.Nil_tContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#nil_t.
    def exitNil_t(self, ctx:cocoapodsParser.Nil_tContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#id.
    def enterId(self, ctx:cocoapodsParser.IdContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#id.
    def exitId(self, ctx:cocoapodsParser.IdContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#id_global.
    def enterId_global(self, ctx:cocoapodsParser.Id_globalContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#id_global.
    def exitId_global(self, ctx:cocoapodsParser.Id_globalContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#id_function.
    def enterId_function(self, ctx:cocoapodsParser.Id_functionContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#id_function.
    def exitId_function(self, ctx:cocoapodsParser.Id_functionContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#terminator.
    def enterTerminator(self, ctx:cocoapodsParser.TerminatorContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#terminator.
    def exitTerminator(self, ctx:cocoapodsParser.TerminatorContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#else_token.
    def enterElse_token(self, ctx:cocoapodsParser.Else_tokenContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#else_token.
    def exitElse_token(self, ctx:cocoapodsParser.Else_tokenContext):
        pass


    # Enter a parse tree produced by cocoapodsParser#crlf.
    def enterCrlf(self, ctx:cocoapodsParser.CrlfContext):
        pass

    # Exit a parse tree produced by cocoapodsParser#crlf.
    def exitCrlf(self, ctx:cocoapodsParser.CrlfContext):
        pass


