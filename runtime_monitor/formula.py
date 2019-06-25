import math


class Formula:
    def __init__(self):
        pass

    def accept(self, visitor):
        raise NotImplementedError("Accept method not implemented for formula.")


class Atomic(Formula):
    def __init__(self, identifier):
        super().__init__()
        self.identifier = identifier

    def __str__(self):
        return self.identifier

    def __eq__(self, other):
        if isinstance(other, Atomic):
            return self.identifier == other.identifier
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def accept(self, visitor):
        return visitor.visit_atomic_formula(self)


class Boolean(Formula):
    def __init__(self, constant):
        super().__init__()
        self.constant = constant

    def __str__(self):
        if self.constant:
            return "⊤"
        else:
            return "⊥"

    def __eq__(self, other):
        if isinstance(other, Boolean):
            return self.constant == other.constant
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def accept(self, visitor):
        return visitor.visit_boolean_formula(self)


class Negation(Formula):
    def __init__(self, left: Formula):
        super().__init__()
        self.left = left

    def __str__(self):
        return "¬" + self.left.__str__()

    def __eq__(self, other):
        if isinstance(other, Negation):
            return self.left.__eq__(other.left)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def accept(self, visitor):
        return visitor.visit_negation_formula(self)


class Always(Formula):
    def __init__(self, left: Formula):
        super().__init__()
        self.left = left

    def __str__(self):
        return "□" + self.left.__str__()

    def __eq__(self, other):
        if isinstance(other, Always):
            return self.left.__eq__(other.left)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def accept(self, visitor):
        return visitor.visit_always_formula(self)


class Eventually(Formula):
    def __init__(self, left: Formula, left_bound, right_bound):
        super().__init__()
        self.left = left
        self.left_bound = left_bound
        self.right_bound = right_bound

    def __str__(self):
        return "◊" + "[" + str(self.left_bound) + "," + str(self.right_bound) + "]" + " " + self.left.__str__()

    def __eq__(self, other):
        if isinstance(other, Eventually):
            return self.left.__eq__(other.left) \
                   and self.left_bound == other.left_bound \
                   and self.right_bound == other.right_bound
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def accept(self, visitor):
        return visitor.visit_eventually_formula(self)


class Previous(Formula):
    def accept(self, visitor):
        raise NotImplementedError("Accept method not implemented for Previous.")


class Next(Formula):
    def accept(self, visitor):
        raise NotImplementedError("Accept method not implemented for Next.")


class Until(Formula):
    def __init__(self, left: Formula, right: Formula, left_bound, right_bound):
        super().__init__()
        self.left = left
        self.right = right
        self.left_bound = left_bound
        self.right_bound = right_bound

    def __str__(self):
        interval = ""
        if self.is_unbounded():
            interval = "[" + str(self.left_bound) + "," + str(self.right_bound) + ")"
        else:
            interval = "[" + str(self.left_bound) + "," + str(self.right_bound) + "]"
        return "(" + self.left.__str__() \
               + " " + "U" + interval + " " \
               + self.right.__str__() + ")"

    def __eq__(self, other):
        if isinstance(other, Until):
            return self.left.__eq__(other.left) \
                   and self.right.__eq__(other.right) \
                   and self.left_bound == other.left_bound \
                   and self.right_bound == other.right_bound
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_unbounded(self):
        return True if self.right_bound == math.inf else False

    def member(self, n):
        return self.left_bound <= n <= self.right_bound

    def accept(self, visitor):
        return visitor.visit_until_formula(self)


class Since(Formula):
    def __init__(self, left: Formula, right: Formula, left_bound, right_bound):
        super().__init__()
        self.left = left
        self.right = right
        self.left_bound = left_bound
        self.right_bound = right_bound

    def __str__(self):
        return self.left.__str__() \
               + " " + "S" + "[" + str(self.left_bound) + "," + str(self.right_bound) + "]" + " " \
               + self.right.__str__()

    def __eq__(self, other):
        if isinstance(other, Since):
            return self.left.__eq__(other.left) \
                   and self.right.__eq__(other.right) \
                   and self.left_bound == other.left_bound \
                   and self.right_bound == other.right_bound
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def is_unbounded(self):
        return True if self.right_bound == math.inf else False

    def member(self, n):
        return self.left_bound <= n <= self.right_bound

    def accept(self, visitor):
        return visitor.visit_since_formula(self)


class Conjunction(Formula):
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + self.left.__str__() + " " + "∧" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        if isinstance(other, Conjunction):
            return self.left.__eq__(other.left) and self.right.__eq__(other.right)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def accept(self, visitor):
        return visitor.visit_disjunction_formula(self)


class Disjunction(Formula):
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return "(" + self.left.__str__() + " " + "∨" + " " + self.right.__str__() + ")"

    def __eq__(self, other):
        if isinstance(other, Disjunction):
            return self.left.__eq__(other.left) and self.right.__eq__(other.right)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def accept(self, visitor):
        return visitor.visit_disjunction_formula(self)


class Implication(Formula):
    def __init__(self, left: Formula, right: Formula):
        super().__init__()
        self.left = left
        self.right = right

    def __str__(self):
        return self.left.__str__() + " " + "→" + " " + self.right.__str__()

    def __eq__(self, other):
        if isinstance(other, Implication):
            return self.left.__eq__(other.left) and self.right.__eq__(other.right)
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def accept(self, visitor):
        return visitor.visit_implication_formula(self)
