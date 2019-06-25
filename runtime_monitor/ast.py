from runtime_monitor.grammar.SpecificationParser import SpecificationParser
from runtime_monitor.grammar.SpecificationVisitor import SpecificationVisitor
from runtime_monitor.formula import *


class AST(SpecificationVisitor):

    def visitSpecification(self, ctx: SpecificationParser.SpecificationContext):
        return self.visit(ctx.phi)

    def visitParenthesis(self, ctx: SpecificationParser.ParenthesisContext):
        return self.visit(ctx.left)

    def visitAtomicProposition(self, ctx: SpecificationParser.AtomicPropositionContext):
        return Atomic(ctx.getText())

    def visitBooleanConstant(self, ctx: SpecificationParser.BooleanConstantContext):
        return Boolean(ctx.getText())

    def visitUnaryOperator(self, ctx: SpecificationParser.UnaryOperatorContext):
        left = self.visit(ctx.left)
        if ctx.op.type == SpecificationParser.NEGATION:
            return Negation(left)
        elif ctx.op.type == SpecificationParser.ALWAYS:
            return Always(left)
        elif ctx.op.type == SpecificationParser.EVENTUALLY:
            return Eventually(left, int(ctx.NUMBER(0).getText()), int(ctx.NUMBER(1).getText()))
        elif ctx.op.type == SpecificationParser.NEXT:
            raise NotImplementedError("Unary operator next is not implemented.")
        elif ctx.op.type == SpecificationParser.PREVIOUS:
            raise NotImplementedError("Unary operator previous is not implemented.")
        else:
            raise NotImplementedError("Unary operator is not implemented.")

    def visitBinaryOperator(self, ctx: SpecificationParser.BinaryOperatorContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if ctx.op.type == SpecificationParser.CONJUNCTION:
            return Conjunction(left, right)
        elif ctx.op.type == SpecificationParser.DISJUNCTION:
            return Disjunction(left, right)
        elif ctx.op.type == SpecificationParser.IMPLICATION:
            return Implication(left, right)
        else:
            raise NotImplementedError("Binary operator is not implemented.")

    def visitBoundedBinaryOperator(self, ctx: SpecificationParser.BoundedBinaryOperatorContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if ctx.op.type == SpecificationParser.UNTIL:
            return Until(left, right, int(ctx.NUMBER(0).getText()), int(ctx.NUMBER(1).getText()))
        elif ctx.op.type == SpecificationParser.SINCE:
            return Since(left, right, int(ctx.NUMBER(0).getText()), int(ctx.NUMBER(1).getText()))
        else:
            raise NotImplementedError("Bounded binary operator is not implemented.")

    def visitUnboundedBinaryOperator(self, ctx: SpecificationParser.UnboundedBinaryOperatorContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if ctx.op.type == SpecificationParser.UNTIL:
            return Until(left, right, 0, math.inf)
        elif ctx.op.type == SpecificationParser.SINCE:
            return Since(left, right, 0, math.inf)
        else:
            raise NotImplementedError("Unbounded binary operator is not implemented.")
