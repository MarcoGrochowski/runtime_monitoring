import unittest

from antlr4 import CommonTokenStream, InputStream
from runtime_monitor.grammar.SpecificationLexer import SpecificationLexer
from runtime_monitor.grammar.SpecificationParser import SpecificationParser

from runtime_monitor.formula import *
from runtime_monitor.ast import AST


class TestParser(unittest.TestCase):

    def test_disjunction(self):
        lexer = SpecificationLexer(InputStream("a or b"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        self.assertEqual(ast, Disjunction(Atomic("a"), Atomic("b")))

    def test_conjunction(self):
        lexer = SpecificationLexer(InputStream("a and b"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        self.assertEqual(ast, Conjunction(Atomic("a"), Atomic("b")))

    def test_implication(self):
        lexer = SpecificationLexer(InputStream("a implies b"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        self.assertEqual(ast, Implication(Atomic("a"), Atomic("b")))

    def test_until_unbounded(self):
        lexer = SpecificationLexer(InputStream("a until b"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        self.assertEqual(ast, Until(Atomic("a"), Atomic("b"), 0, math.inf))

    def test_until_bounded(self):
        lexer = SpecificationLexer(InputStream("a until[0,4] b"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        self.assertEqual(ast, Until(Atomic("a"), Atomic("b"), 0, 4))

    def test_since_unbounded(self):
        lexer = SpecificationLexer(InputStream("a since b"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        self.assertEqual(ast, Since(Atomic("a"), Atomic("b"), 0, math.inf))

    def test_since_bounded(self):
        lexer = SpecificationLexer(InputStream("a since[0,1] b"))
        stream = CommonTokenStream(lexer)
        parser = SpecificationParser(stream)
        ast = AST().visit(parser.specification())
        self.assertEqual(ast, Since(Atomic("a"), Atomic("b"), 0, 1))


if __name__ == '__main__':
    unittest.main()
