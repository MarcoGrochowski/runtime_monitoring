class BooleanExpression(object):
    pass


class TrueConstant(BooleanExpression):
    def __str__(self):
        return "⊤"

    def __eq__(self, other):
        if isinstance(other, TrueConstant):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__str__())


class FalseConstant(BooleanExpression):
    def __str__(self):
        return "⊥"

    def __eq__(self, other):
        if isinstance(other, FalseConstant):
            return True
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__str__())


class Variable(BooleanExpression):
    def __init__(self, k: int):
        self.k = k

    def __str__(self):
        return "Var " + str(self.k)

    def __eq__(self, other):
        if isinstance(other, Variable):
            return self.k == other.k
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.k)


class NegatedVariable(BooleanExpression):
    def __init__(self, k: int):
        self.k = k

    def __str__(self):
        return "¬Var " + str(self.k)

    def __eq__(self, other):
        if isinstance(other, NegatedVariable):
            return self.k == other.k
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.k) * hash(self.__str__())

    def simplify(self, bexp: BooleanExpression) -> BooleanExpression:
        result = None
        if isinstance(bexp, TrueConstant):
            result = FalseConstant()
        elif isinstance(bexp, FalseConstant):
            result = TrueConstant()
        elif isinstance(bexp, Variable):
            result = NegatedVariable(bexp.k)
        elif isinstance(bexp, NegatedVariable):
            result = Variable(bexp.k)
        elif isinstance(bexp, Conjunction):
            result = Disjunction(self.simplify(bexp.left),
                                 self.simplify(bexp.right)).simplify()
        elif isinstance(bexp, Disjunction):
            result = Conjunction(self.simplify(bexp.left),
                                 self.simplify(bexp.right)).simplify()
        else:
            raise NotImplementedError("Simplify negation for BExp.BooleanExpression not implemented.")
        return result


class Conjunction(BooleanExpression):
    def __init__(self, left: BooleanExpression, right: BooleanExpression):
        self.left = left
        self.right = right

    def __str__(self):
        return self.left.__str__() + " ∧ " + self.right.__str__()

    def __eq__(self, other):
        if isinstance(other, Conjunction):
            return self.left.__eq__(other.left) and self.right.__eq__(other.right)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.left) ^ hash(self.right)

    def simplify(self):
        if isinstance(self.left, TrueConstant):
            if isinstance(self.right, Conjunction) or isinstance(self.right, Disjunction):
                return self.right.simplify()
            else:
                return self.right
        elif isinstance(self.right, TrueConstant):
            if isinstance(self.left, Conjunction) or isinstance(self.left, Disjunction):
                return self.left.simplify()
            else:
                return self.left
        elif isinstance(self.left, FalseConstant) or isinstance(self.right, FalseConstant):
            return FalseConstant()
        elif isinstance(self.left, Disjunction) or isinstance(self.left, Conjunction):
            return Conjunction(self.left.simplify(), self.right)
        elif isinstance(self.right, Disjunction) or isinstance(self.right, Conjunction):
            return Conjunction(self.left, self.right.simplify())
        elif (isinstance(self.left, Disjunction) or isinstance(self.left, Conjunction)) \
                and (isinstance(self.right, Disjunction) or isinstance(self.right, Conjunction)):
            return Conjunction(self.left.simplify(), self.right.simplify())
        else:
            return self


class Disjunction(BooleanExpression):
    def __init__(self, left: BooleanExpression, right: BooleanExpression):
        self.left = left
        self.right = right

    def __str__(self):
        return self.left.__str__() + " ∨ " + self.right.__str__()

    def __eq__(self, other):
        if isinstance(other, Disjunction):
            return self.left.__eq__(other.left) and self.right.__eq__(other.right)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.left) ^ hash(self.right)

    def simplify(self):
        if isinstance(self.left, FalseConstant):
            if isinstance(self.right, Conjunction) or isinstance(self.right, Disjunction):
                return self.right.simplify()
            else:
                return self.right
        elif isinstance(self.right, FalseConstant):
            if isinstance(self.left, Conjunction) or isinstance(self.left, Disjunction):
                return self.left.simplify()
            else:
                return self.left
        elif isinstance(self.left, TrueConstant) or isinstance(self.right, TrueConstant):
            return TrueConstant()
        elif isinstance(self.left, Disjunction) or isinstance(self.left, Conjunction):
            return Disjunction(self.left.simplify(), self.right)
        elif isinstance(self.right, Disjunction) or isinstance(self.right, Conjunction):
            return Disjunction(self.left, self.right.simplify())
        elif (isinstance(self.left, Disjunction) or isinstance(self.left, Conjunction)) \
                and (isinstance(self.right, Disjunction) or isinstance(self.right, Conjunction)):
            return Disjunction(self.left.simplify(), self.right.simplify())
        else:
            return self
