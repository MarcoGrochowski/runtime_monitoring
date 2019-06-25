from runtime_monitor.visitor import Visitor
from runtime_monitor.formula import Until, Since


class SubformulaVisitor(Visitor):

    def visit_atomic_formula(self, formula):
        return [formula]

    def visit_boolean_formula(self, formula):
        return [formula]

    def visit_negation_formula(self, formula):
        return [formula] + formula.left.accept(self)

    def visit_always_formula(self, formula):
        raise NotImplementedError("Visitor for always formula not implemented")

    def visit_eventually_formula(self, formula):
        raise NotImplementedError("Visitor for eventually formula not implemented")

    def visit_until_formula(self, formula):
        interval_skewed_subformulas = []
        if formula.is_unbounded():
            for i in range(1, formula.left_bound + 1):
                interval_skewed_subformula = Until(formula.left,
                                                   formula.right,
                                                   max(0, formula.left_bound - i),
                                                   formula.right_bound)
                interval_skewed_subformulas.append(interval_skewed_subformula)
        else:
            for i in range(1, formula.right_bound + 1):
                interval_skewed_subformula = Until(formula.left,
                                                   formula.right,
                                                   max(0, formula.left_bound - i),
                                                   max(0, formula.right_bound - i))
                interval_skewed_subformulas.append(interval_skewed_subformula)
        return [formula] + interval_skewed_subformulas + formula.right.accept(self) + formula.left.accept(self)

    def visit_since_formula(self, formula):
        interval_skewed_subformulas = []
        if formula.is_unbounded():
            for i in range(1, formula.left_bound + 1):
                interval_skewed_subformula = Since(formula.left,
                                                   formula.right,
                                                   max(0, formula.left_bound - i),
                                                   formula.right_bound)
                interval_skewed_subformulas.append(interval_skewed_subformula)
        else:
            for i in range(1, formula.right_bound + 1):
                interval_skewed_subformula = Since(formula.left,
                                                   formula.right,
                                                   max(0, formula.left_bound - i),
                                                   max(0, formula.right_bound - i))
                interval_skewed_subformulas.append(interval_skewed_subformula)
        return [formula] + interval_skewed_subformulas + formula.right.accept(self) + formula.left.accept(self)

    def visit_conjunction_formula(self, formula):
        raise NotImplementedError("Visitor for disjunction formula not implemented")

    def visit_disjunction_formula(self, formula):
        return [formula] + formula.right.accept(self) + formula.left.accept(self)

    def visit_implication_formula(self, formula):
        raise NotImplementedError("Visitor for implication formula not implemented")
