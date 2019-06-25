from typing import Set, Tuple
from runtime_monitor.subformula import SubformulaVisitor
import runtime_monitor.formula as F
import runtime_monitor.fbexp as FBExp
import runtime_monitor.bexp as BExp


class Monitor:
    def __init__(self, formula, topics):
        self.debug = False

        self.formula = formula
        self.topics = topics

        self.subformulas = list(reversed(self.formula.accept(SubformulaVisitor())))

        self.now = -1
        self.off = 0

        self.history = {}

        self.previous = [BExp.FalseConstant()] * len(self.subformulas)
        self.current = [FBExp.Now(BExp.FalseConstant())] * len(self.subformulas)

        self.boolean_verdicts = []
        self.equivalence_verdicts = []

    def print_debug(self, state, timestamp):
        print("Processing state %s @ %d" % (state, timestamp))
        if len(self.boolean_verdicts) != 0:
            print("Boolean verdicts for time-point %d:" % self.now)
            for boolean_verdict in sorted(self.boolean_verdicts):
                print("(%d,%d):%s" % (boolean_verdict[0][0], boolean_verdict[0][1], boolean_verdict[1]))
        if len(self.equivalence_verdicts) != 0:
            print("Equivalence verdicts for time-point %d:" % self.now)
            for equivalence_verdict in sorted(self.equivalence_verdicts):
                print("(%d,%d) = (%d,%d)" % (
                equivalence_verdict[0][0][0], equivalence_verdict[0][0][1], equivalence_verdict[1][0][0],
                equivalence_verdict[1][0][1]))
        print("Table for eval(curr[-]) or Previous:")
        for k in range(0, len(self.previous)):
            print("%d) %s: %s" % (k, self.subformulas[k], self.previous[k]))
        print("History:")
        for (time_point, boolean_expression) in sorted(self.history):
            print(time_point, boolean_expression)

    def step(self, timestamp: int, state: dict):
        delta = timestamp - self.now
        for k in range(0, len(self.previous)):
            self.previous[k] = self.evaluate(delta, self.current[k])
        self.history, self.boolean_verdicts, self.equivalence_verdicts = self.filter_verdicts()
        self.now = timestamp
        self.off = self.off + 1 if delta == 0 else 0
        for k in range(0, len(self.current)):
            self.current[k] = self.progress(k, delta, state)
        if self.debug:
            self.print_debug(state, timestamp)

    def evaluate(self, delta: int, fbexp: FBExp.FutureBooleanExpression) -> BExp.BooleanExpression:
        result = None
        if isinstance(fbexp, FBExp.Now):
            result = fbexp.bexp
        elif isinstance(fbexp, FBExp.Later):
            result = fbexp.f(delta)
            if isinstance(result, BExp.Disjunction) or isinstance(result, BExp.Conjunction):
                result = result.simplify()
        else:
            raise NotImplementedError("Evaluate not implemented for FBexp.FutureBooleanExpression.")
        return result

    def filter_verdicts(self):
        history = {((self.now, self.off), self.previous[-1])}
        for j, c in self.history:
            history.add((j, self.substitute_boolean_expression(c)))
        boolean_verdicts = self.filter_boolean_verdicts(history)
        equivalence_verdicts = self.filter_equivalent_verdicts(history)
        return history, boolean_verdicts, equivalence_verdicts

    def substitute_boolean_expression(self, bexp: BExp.BooleanExpression) -> BExp.BooleanExpression:
        result = None
        if isinstance(bexp, BExp.TrueConstant):
            result = bexp
        elif isinstance(bexp, BExp.FalseConstant):
            result = bexp
        elif isinstance(bexp, BExp.Variable):
            result = self.previous[bexp.k]
        elif isinstance(bexp, BExp.NegatedVariable):
            result = bexp.simplify(self.previous[bexp.k])
        elif isinstance(bexp, BExp.Conjunction):
            result = BExp.Conjunction(self.substitute_boolean_expression(bexp.left),
                                      self.substitute_boolean_expression(bexp.right)).simplify()
        elif isinstance(bexp, BExp.Disjunction):
            result = BExp.Disjunction(self.substitute_boolean_expression(bexp.left),
                                      self.substitute_boolean_expression(bexp.right)).simplify()
        return result

    def filter_boolean_verdicts(self, history: Set[Tuple[Tuple[int, int], BExp.BooleanExpression]]) \
            -> Set[Tuple[Tuple[int, int], BExp.BooleanExpression]]:
        boolean_verdicts = set()
        for (_, bexp) in history:
            if isinstance(bexp, BExp.TrueConstant):
                boolean_verdicts.add((_, bexp))
            elif isinstance(bexp, BExp.FalseConstant):
                boolean_verdicts.add((_, bexp))
        for boolean_verdict in boolean_verdicts:
            history.remove(boolean_verdict)
        return boolean_verdicts

    def filter_equivalent_verdicts(self, history: Set[Tuple[Tuple[int, int], BExp.BooleanExpression]]) \
            -> Set[Tuple[Tuple[Tuple[int, int], BExp.BooleanExpression], Tuple[Tuple[int, int], BExp.BooleanExpression]]]:
        equivalence_verdicts = set()
        for i in history:
            ((now_i, off_i), bexp_i) = i
            for j in history:
                ((now_j, off_j), bexp_j) = j
                if i == j or bexp_i != bexp_j:
                    continue
                if now_i < now_j or (now_i == now_j and off_i < off_j):
                    equivalence_verdicts.add((j, i))
        # filter all pairwise equivalent pairs
        remove_me_please = set()
        for e1 in equivalence_verdicts:
            (((now_i1, off_i1), _), ((now_i2, off_i2), _)) = e1
            for e2 in equivalence_verdicts:
                (((now_j1, off_j1), _), ((now_j2, off_j2), _)) = e2
                if e1 == e2:
                    continue
                if now_i2 == now_j1 and off_i2 == off_j1:
                    if (((now_i1, off_i1), _), ((now_j1, off_j1), _)) in equivalence_verdicts:
                      remove_me_please.add(e1)
        for remove_me in remove_me_please:
            equivalence_verdicts.remove(remove_me)

        for equivalence_verdict in sorted(equivalence_verdicts):
            if equivalence_verdict[0] in history:
                history.remove(equivalence_verdict[0])
        return equivalence_verdicts

    def progress(self, k: int, delta: int, state: dict) -> FBExp.FutureBooleanExpression:
        subformula = self.subformulas[k]
        if isinstance(subformula, F.Atomic):
            if subformula.identifier in state:
                if state[subformula.identifier]:
                    return FBExp.Now(BExp.TrueConstant())
                else:
                    return FBExp.Now(BExp.FalseConstant())
            else:
                # todo: is there a case where the formula is inconclusive?
                return FBExp.Now(BExp.FalseConstant())
        elif isinstance(subformula, F.Boolean):
            if subformula.constant:
                return FBExp.Now(BExp.TrueConstant())
            else:
                return FBExp.Now(BExp.FalseConstant())
        elif isinstance(subformula, F.Negation):
            return FBExp.Negation(self.current[self.subformulas.index(subformula.left)]).simplify()
        elif isinstance(subformula, F.Disjunction):
            return FBExp.Disjunction(self.current[self.subformulas.index(subformula.left)], self.current[self.subformulas.index(subformula.right)]).simplify()
        elif isinstance(subformula, F.Previous):
            raise NotImplementedError("Progress not implemented for F.Previous.")
        elif isinstance(subformula, F.Next):
            raise NotImplementedError("Progress not implemented for F.Next.")
        elif isinstance(subformula, F.Since):
            left, right = None, None
            if subformula.member(0):
                left = self.current[self.subformulas.index(subformula.right)]
            else:
                left = FBExp.Now(BExp.FalseConstant())
            if delta <= subformula.right_bound:
                right = FBExp.Conjunction(self.current[self.subformulas.index(subformula.left)],
                                          self.substitute_future_boolean_expression(self.previous[k - delta])).simplify()
            else:
                right = FBExp.Now(BExp.FalseConstant())
            return FBExp.Disjunction(left, right).simplify()
        elif isinstance(subformula, F.Until):
            left, right = None, None
            if subformula.member(0):
                left = self.current[self.subformulas.index(subformula.right)]
            else:
                left = FBExp.Now(BExp.FalseConstant())
            if subformula.is_unbounded():
                right = FBExp.Later(lambda t: BExp.FalseConstant() if t > subformula.right_bound else
                                    BExp.Conjunction(self.evaluate(t, self.current[self.subformulas.index(subformula.left)]),
                                    BExp.Variable(k)))
            else:
                right = FBExp.Later(lambda t: BExp.FalseConstant() if t > subformula.right_bound else
                                    BExp.Conjunction(self.evaluate(t, self.current[self.subformulas.index(subformula.left)]),
                                    BExp.Variable(k - t)))
            return FBExp.Disjunction(left, right).simplify()
        else:
            raise NotImplementedError("Progress not implemented for subformula.")

    def substitute_future_boolean_expression(self, bexp: BExp.BooleanExpression) -> FBExp.FutureBooleanExpression:
        result = None
        if isinstance(bexp, BExp.TrueConstant):
            result = FBExp.Now(bexp)
        elif isinstance(bexp, BExp.FalseConstant):
            result = FBExp.Now(bexp)
        elif isinstance(bexp, BExp.Variable):
            result = self.current[bexp.k]
        elif isinstance(bexp, BExp.NegatedVariable):
            result = self.current[bexp.k]
        elif isinstance(bexp, BExp.Conjunction):
            result = FBExp.Conjunction(self.substitute_future_boolean_expression(bexp.left),
                                       self.substitute_future_boolean_expression(bexp.right)).simplify()
        elif isinstance(bexp, BExp.Disjunction):
            result = FBExp.Disjunction(self.substitute_future_boolean_expression(bexp.left),
                                       self.substitute_future_boolean_expression(bexp.right)).simplify()
        return result
