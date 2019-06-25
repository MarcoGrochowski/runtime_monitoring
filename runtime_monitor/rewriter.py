from runtime_monitor.visitor import Visitor
from runtime_monitor.formula import *


class Rewriter(Visitor):
    def visit_atomic_formula(self, formula):
        return formula

    def visit_boolean_formula(self, formula):
        return formula

    def visit_negation_formula(self, formula):
        left = formula.left
        if isinstance(left, Atomic):
            return Negation(left.accept(self))
        elif isinstance(left, Boolean):
            return Boolean(not left.constant)
        elif isinstance(left, Negation):
            return left.accept(self)
        elif isinstance(left, Always):
            return Negation(left.accept(self))
        elif isinstance(left, Eventually):
            return Negation(left.accept(self))
        elif isinstance(left, Until):
            return Negation(left.accept(self))
        elif isinstance(left, Conjunction):
            raise NotImplementedError("Visitor for conjunction not implemented.")
        elif isinstance(left, Disjunction):
            return Negation(left.accept(self))
        elif isinstance(left, Implication):
            return Negation(Disjunction(Negation(left.left).accept(self), left.right.accept(self)))
        else:
            raise NotImplementedError("Visitor for negation formula not implemented.")

    def visit_always_formula(self, formula):
        return Negation(Eventually(Negation(formula.left), 0, math.inf)).accept(self)

    def visit_eventually_formula(self, formula):
        return Until(Boolean(True), formula.left.accept(self), formula.left_bound, formula.right_bound)

    def visit_until_formula(self, formula):
        left = formula.left.accept(self)
        right = formula.right.accept(self)
        return Until(left, right, formula.left_bound, formula.right_bound)

    def visit_since_formula(self, formula):
        left = formula.left.accept(self)
        right = formula.right.accept(self)
        return Since(left, right, formula.left_bound, formula.right_bound)

    def visit_conjunction_formula(self, formula):
        raise NotImplementedError("Visitor for conjunction formula not implemented.")

    def visit_disjunction_formula(self, formula):
        left = formula.left.accept(self)
        right = formula.right.accept(self)
        return Disjunction(left, right)

    def visit_implication_formula(self, formula):
        raise NotImplementedError("Visitor for implication formula not implemented")
