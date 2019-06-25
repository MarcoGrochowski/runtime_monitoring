class Visitor:
    def visit_atomic_formula(self, formula):
        raise NotImplementedError("Visitor for atomic formula not implemented.")

    def visit_boolean_formula(self, formula):
        raise NotImplementedError("Visitor for boolean formula not implemented.")

    def visit_negation_formula(self, formula):
        raise NotImplementedError("Visitor for negation formula not implemented.")

    def visit_always_formula(self, formula):
        raise NotImplementedError("Visitor for always formula not implemented")

    def visit_eventually_formula(self, formula):
        raise NotImplementedError("Visitor for eventually formula not implemented")

    def visit_until_formula(self, formula):
        raise NotImplementedError("Visitor for until formula not implemented")

    def visit_since_formula(self, formula):
        raise NotImplementedError("Visitor for since formula not implemented")

    def visit_conjunction_formula(self, formula):
        raise NotImplementedError("Visitor for disjunction formula not implemented")

    def visit_disjunction_formula(self, formula):
        raise NotImplementedError("Visitor for disjunction formula not implemented")

    def visit_implication_formula(self, formula):
        raise NotImplementedError("Visitor for implication formula not implemented")
