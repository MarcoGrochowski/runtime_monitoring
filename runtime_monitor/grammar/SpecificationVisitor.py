# Generated from grammar/Specification.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SpecificationParser import SpecificationParser
else:
    from SpecificationParser import SpecificationParser

# This class defines a complete generic visitor for a parse tree produced by SpecificationParser.

class SpecificationVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SpecificationParser#specification.
    def visitSpecification(self, ctx:SpecificationParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecificationParser#Parenthesis.
    def visitParenthesis(self, ctx:SpecificationParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecificationParser#UnboundedBinaryOperator.
    def visitUnboundedBinaryOperator(self, ctx:SpecificationParser.UnboundedBinaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecificationParser#BooleanConstant.
    def visitBooleanConstant(self, ctx:SpecificationParser.BooleanConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecificationParser#AtomicProposition.
    def visitAtomicProposition(self, ctx:SpecificationParser.AtomicPropositionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecificationParser#UnaryOperator.
    def visitUnaryOperator(self, ctx:SpecificationParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecificationParser#BinaryOperator.
    def visitBinaryOperator(self, ctx:SpecificationParser.BinaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SpecificationParser#BoundedBinaryOperator.
    def visitBoundedBinaryOperator(self, ctx:SpecificationParser.BoundedBinaryOperatorContext):
        return self.visitChildren(ctx)



del SpecificationParser