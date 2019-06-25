import unittest

from antlr4 import CommonTokenStream, InputStream
from runtime_monitor.grammar.SpecificationLexer import SpecificationLexer
from runtime_monitor.grammar.SpecificationParser import SpecificationParser

from runtime_monitor.formula import *
from runtime_monitor.ast import AST

from runtime_monitor.rewriter import Rewriter


class TestRewriter(unittest.TestCase):

    def test_always(self):
        lexer = SpecificationLexer(InputStream("always a"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        specification = ast.accept(Rewriter())
        self.assertEqual(specification, Negation(Until(Boolean(True), Negation(Atomic("a")), 0, math.inf)))

    def test_eventually_bounded(self):
        lexer = SpecificationLexer(InputStream("eventually[0,1] a"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        specification = ast.accept(Rewriter())
        self.assertEqual(specification, Until(Boolean(True), Atomic("a"), 0, 1))

    def test_combination(self):
        lexer = SpecificationLexer(InputStream("always(E implies eventually[0, 10] R)"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        specification = ast.accept(Rewriter())
        self.assertEqual(specification, Negation(Until(Boolean(True),
                                                       Negation(Disjunction(Negation(Atomic("E")),
                                                                            Until(Boolean(True),
                                                                                  Atomic("R"), 0, 10))), 0, math.inf)))


if __name__ == '__main__':
    unittest.main()
