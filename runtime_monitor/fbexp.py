from typing import Callable
import runtime_monitor.bexp as BExp


class FutureBooleanExpression:
    pass


class Now(FutureBooleanExpression):
    def __init__(self, bexp: BExp.BooleanExpression):
        self.bexp = bexp

    def __str__(self):
        return "Now " + self.bexp.__str__()


class Later(FutureBooleanExpression):
    def __init__(self, f: Callable[[int], BExp.BooleanExpression]):
        self.f = f

    def __str__(self):
        return "Later " + self.f(0).__str__()


class Negation(FutureBooleanExpression):
    def __init__(self, left: FutureBooleanExpression):
        self.left = left

    def __str__(self):
        return "¬_fbexp " + self.left.__str__()

    def simplify(self):
        if isinstance(self.left, Now):
            return Now(self.simplify_bexp(self.left.bexp))
        elif isinstance(self.left, Later):
            return Later(lambda t: self.simplify_bexp(self.left.f(t)))
        else:
            raise NotImplementedError("Simplify negation for FBExp.FutureBooleanExpression not implemented.")

    def simplify_bexp(self, bexp: BExp.BooleanExpression) -> BExp.BooleanExpression:
        result = None
        if isinstance(bexp, BExp.TrueConstant):
            result = BExp.FalseConstant()
        elif isinstance(bexp, BExp.FalseConstant):
            result = BExp.TrueConstant()
        elif isinstance(bexp, BExp.Variable):
            result = BExp.NegatedVariable(bexp.k)
        elif isinstance(bexp, BExp.NegatedVariable):
            result = BExp.Variable(bexp.k)
        elif isinstance(bexp, BExp.Conjunction):
            result = BExp.Disjunction(self.simplify_bexp(bexp.left),
                                      self.simplify_bexp(bexp.right)).simplify()
        elif isinstance(bexp, BExp.Disjunction):
            result = BExp.Conjunction(self.simplify_bexp(bexp.left),
                                      self.simplify_bexp(bexp.right)).simplify()
        else:
            raise NotImplementedError("Simplify negation for BExp.BooleanExpression not implemented.")
        return result


class Conjunction(FutureBooleanExpression):
    def __init__(self, left: FutureBooleanExpression, right: FutureBooleanExpression):
        self.left = left
        self.right = right

    def __str__(self):
        return self.left.__str__() + " ∧_fbexp " + self.right.__str__()

    def simplify(self):
        if isinstance(self.left, Now) and isinstance(self.right, Now):
            return Now(BExp.Conjunction(self.left.bexp, self.right.bexp).simplify())
        elif isinstance(self.left, Now) and isinstance(self.right, Later):
            if isinstance(self.left.bexp, BExp.TrueConstant):
                return self.right
            elif isinstance(self.left.bexp, BExp.FalseConstant):
                return Now(BExp.FalseConstant())
            else:
                return Later(lambda t: BExp.Conjunction(self.left.bexp, self.right.f(t)).simplify())
        elif isinstance(self.left, Later) and isinstance(self.right, Now):
            if isinstance(self.right.bexp, BExp.TrueConstant):
                return self.left
            elif isinstance(self.right.bexp, BExp.FalseConstant):
                return Now(BExp.FalseConstant())
            else:
                return Later(lambda t: BExp.Conjunction(self.left.f(t), self.right.bexp).simplify())
        elif isinstance(self.left, Later) and isinstance(self.right, Later):
            return Later(lambda t: BExp.Conjunction(self.left.f(t), self.right.f(t)).simplify())
        else:
            raise NotImplementedError("Simplify not implemented for FBExp.Conjunction.")


class Disjunction(FutureBooleanExpression):
    def __init__(self, left: FutureBooleanExpression, right: FutureBooleanExpression):
        self.left = left
        self.right = right

    def __str__(self):
        return self.left.__str__() + " ∨_fbexp " + self.right.__str__()

    def simplify(self):
        if isinstance(self.left, Now) and isinstance(self.right, Now):
            return Now(BExp.Disjunction(self.left.bexp, self.right.bexp).simplify())
        elif isinstance(self.left, Now) and isinstance(self.right, Later):
            if isinstance(self.left.bexp, BExp.TrueConstant):
                return self.left
            elif isinstance(self.left.bexp, BExp.FalseConstant):
                return self.right
            else:
                return Later(lambda t: BExp.Disjunction(self.left.bexp, self.right.f(t)).simplify())
        elif isinstance(self.left, Later) and isinstance(self.right, Now):
            if isinstance(self.right.bexp, BExp.TrueConstant):
                return self.right
            elif isinstance(self.right.bexp, BExp.FalseConstant):
                return self.left
            else:
                return Later(lambda t: BExp.Disjunction(self.left.f(t), self.right.bexp).simplify())
        elif isinstance(self.left, Later) and isinstance(self.right, Later):
            return Later(lambda t: BExp.Disjunction(self.left.f(t), self.right.f(t)).simplify())
        else:
            raise NotImplementedError("Simplify for FBExp.Disjunction not implemented.")
