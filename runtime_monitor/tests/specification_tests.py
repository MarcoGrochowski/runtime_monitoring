import unittest
import json

from antlr4 import CommonTokenStream, InputStream, FileStream
from runtime_monitor.grammar.SpecificationLexer import SpecificationLexer
from runtime_monitor.grammar.SpecificationParser import SpecificationParser

from runtime_monitor.ast import AST
from runtime_monitor.rewriter import Rewriter
from runtime_monitor.monitor import Monitor
import runtime_monitor.bexp as BExp


class TestSpecification(unittest.TestCase):

    def test_specification_ex0(self):
        with open('./../examples/ex0.monitor', 'r') as m:
            for line in m:
                data = json.loads(line)
                print("Topics: %s" % data['topics'])
                self.topics = data['topics']
                print("Specification: %s" % data['specification'])
                lexer = SpecificationLexer(InputStream(data['specification']))
                parser = SpecificationParser(CommonTokenStream(lexer))
                ast = AST().visit(parser.specification())
                self.formula = ast.accept(Rewriter())
                print("Formula: %s" % self.formula)
        monitor = Monitor(formula=self.formula, topics=self.topics)
        with open('./../examples/ex0.trace', 'r') as trace:
            for event in trace:
                event = json.loads(event)
                monitor.step(timestamp=event.pop('timestamp', None), state=event)
                if len(monitor.boolean_verdicts) != 0:
                    print("Boolean verdicts for time-point %d:" % monitor.now)
                    for boolean_verdict in sorted(monitor.boolean_verdicts):
                        print("(%d,%d):%s" % (boolean_verdict[0][0], boolean_verdict[0][1], boolean_verdict[1]))
                if len(monitor.equivalence_verdicts) != 0:
                    print("Equivalence verdicts for time-point %d:" % monitor.now)
                    for equivalence_verdict in sorted(monitor.equivalence_verdicts):
                        print("(%d,%d) = (%d,%d)" % (
                        equivalence_verdict[0][0][0], equivalence_verdict[0][0][1], equivalence_verdict[1][0][0],
                        equivalence_verdict[1][0][1]))
        self.assertEqual(BExp.FalseConstant(), monitor.previous[-1])

    def test_specification_ex1(self):
        with open('./../examples/ex1.monitor', 'r') as m:
            for line in m:
                data = json.loads(line)
                print("Topics: %s" % data['topics'])
                self.topics = data['topics']
                print("Specification: %s" % data['specification'])
                lexer = SpecificationLexer(InputStream(data['specification']))
                parser = SpecificationParser(CommonTokenStream(lexer))
                ast = AST().visit(parser.specification())
                self.formula = ast.accept(Rewriter())
                print("Formula: %s" % self.formula)
        monitor = Monitor(formula=self.formula, topics=self.topics)
        with open('./../examples/ex1.trace', 'r') as trace:
            for event in trace:
                event = json.loads(event)
                monitor.step(timestamp=event.pop('timestamp', None), state=event)
                if len(monitor.boolean_verdicts) != 0:
                    print("Boolean verdicts for time-point %d:" % monitor.now)
                    for boolean_verdict in sorted(monitor.boolean_verdicts):
                        print("(%d,%d):%s" % (boolean_verdict[0][0], boolean_verdict[0][1], boolean_verdict[1]))
                if len(monitor.equivalence_verdicts) != 0:
                    print("Equivalence verdicts for time-point %d:" % monitor.now)
                    for equivalence_verdict in sorted(monitor.equivalence_verdicts):
                        print("(%d,%d) = (%d,%d)" % (
                        equivalence_verdict[0][0][0], equivalence_verdict[0][0][1], equivalence_verdict[1][0][0],
                        equivalence_verdict[1][0][1]))
        self.assertEqual(BExp.TrueConstant(), monitor.previous[-1])

    def test_specification_ex2(self):
        with open('./../examples/ex2.monitor', 'r') as m:
            for line in m:
                data = json.loads(line)
                print("Topics: %s" % data['topics'])
                self.topics = data['topics']
                print("Specification: %s" % data['specification'])
                lexer = SpecificationLexer(InputStream(data['specification']))
                parser = SpecificationParser(CommonTokenStream(lexer))
                ast = AST().visit(parser.specification())
                self.formula = ast.accept(Rewriter())
                print("Formula: %s" % self.formula)
        monitor = Monitor(formula=self.formula, topics=self.topics)
        with open('./../examples/ex2.trace', 'r') as trace:
            for event in trace:
                event = json.loads(event)
                monitor.step(timestamp=event.pop('timestamp', None), state=event)
                if len(monitor.boolean_verdicts) != 0:
                    print("Boolean verdicts for time-point %d:" % monitor.now)
                    for boolean_verdict in sorted(monitor.boolean_verdicts):
                        print("(%d,%d):%s" % (boolean_verdict[0][0], boolean_verdict[0][1], boolean_verdict[1]))
                if len(monitor.equivalence_verdicts) != 0:
                    print("Equivalence verdicts for time-point %d:" % monitor.now)
                    for equivalence_verdict in sorted(monitor.equivalence_verdicts):
                        print("(%d,%d) = (%d,%d)" % (
                        equivalence_verdict[0][0][0], equivalence_verdict[0][0][1], equivalence_verdict[1][0][0],
                        equivalence_verdict[1][0][1]))
        self.assertEqual(BExp.FalseConstant(), monitor.previous[-1])

    def test_specification_ex3(self):
        with open('./../examples/ex3.monitor', 'r') as m:
            for line in m:
                data = json.loads(line)
                print("Topics: %s" % data['topics'])
                self.topics = data['topics']
                print("Specification: %s" % data['specification'])
                lexer = SpecificationLexer(InputStream(data['specification']))
                parser = SpecificationParser(CommonTokenStream(lexer))
                ast = AST().visit(parser.specification())
                self.formula = ast.accept(Rewriter())
                print("Formula: %s" % self.formula)
        monitor = Monitor(formula=self.formula, topics=self.topics)
        with open('./../examples/ex3.trace', 'r') as trace:
            for event in trace:
                event = json.loads(event)
                monitor.step(timestamp=event.pop('timestamp', None), state=event)
                if len(monitor.boolean_verdicts) != 0:
                    print("Boolean verdicts for time-point %d:" % monitor.now)
                    for boolean_verdict in sorted(monitor.boolean_verdicts):
                        print("(%d,%d):%s" % (boolean_verdict[0][0], boolean_verdict[0][1], boolean_verdict[1]))
                if len(monitor.equivalence_verdicts) != 0:
                    print("Equivalence verdicts for time-point %d:" % monitor.now)
                    for equivalence_verdict in sorted(monitor.equivalence_verdicts):
                        print("(%d,%d) = (%d,%d)" % (
                        equivalence_verdict[0][0][0], equivalence_verdict[0][0][1], equivalence_verdict[1][0][0],
                        equivalence_verdict[1][0][1]))
        self.assertEqual(BExp.FalseConstant(), monitor.previous[-1])

    def test_specification_ex4(self):
        with open('./../examples/ex4.monitor', 'r') as m:
            for line in m:
                data = json.loads(line)
                print("Topics: %s" % data['topics'])
                self.topics = data['topics']
                print("Specification: %s" % data['specification'])
                lexer = SpecificationLexer(InputStream(data['specification']))
                parser = SpecificationParser(CommonTokenStream(lexer))
                ast = AST().visit(parser.specification())
                self.formula = ast.accept(Rewriter())
                print("Formula: %s" % self.formula)
        monitor = Monitor(formula=self.formula, topics=self.topics)
        with open('./../examples/ex4.trace', 'r') as trace:
            for event in trace:
                event = json.loads(event)
                monitor.step(timestamp=event.pop('timestamp', None), state=event)
                if len(monitor.boolean_verdicts) != 0:
                    print("Boolean verdicts for time-point %d:" % monitor.now)
                    for boolean_verdict in sorted(monitor.boolean_verdicts):
                        print("(%d,%d):%s" % (boolean_verdict[0][0], boolean_verdict[0][1], boolean_verdict[1]))
                if len(monitor.equivalence_verdicts) != 0:
                    print("Equivalence verdicts for time-point %d:" % monitor.now)
                    for equivalence_verdict in sorted(monitor.equivalence_verdicts):
                        print("(%d,%d) = (%d,%d)" % (
                        equivalence_verdict[0][0][0], equivalence_verdict[0][0][1], equivalence_verdict[1][0][0],
                        equivalence_verdict[1][0][1]))
        self.assertEqual(BExp.Conjunction(BExp.Variable(7), BExp.NegatedVariable(11)), monitor.previous[-1])


if __name__ == '__main__':
    unittest.main()
