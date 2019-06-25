# Generated from grammar/Specification.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("\66\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3\36\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\61\n\3\f\3\16\3")
        buf.write("\64\13\3\3\3\2\3\4\4\2\4\2\7\3\2\22\23\4\2\b\b\13\13\4")
        buf.write("\2\t\n\f\f\3\2\20\21\3\2\r\16\2<\2\7\3\2\2\2\4\35\3\2")
        buf.write("\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\t\3\2\2\2\t\7\3\2\2\2\t")
        buf.write("\n\3\2\2\2\n\13\3\2\2\2\13\f\7\2\2\3\f\3\3\2\2\2\r\16")
        buf.write("\b\3\1\2\16\17\7\3\2\2\17\20\5\4\3\2\20\21\7\4\2\2\21")
        buf.write("\36\3\2\2\2\22\36\t\2\2\2\23\36\7\25\2\2\24\25\t\3\2\2")
        buf.write("\25\36\5\4\3\b\26\27\t\4\2\2\27\30\7\5\2\2\30\31\7\24")
        buf.write("\2\2\31\32\7\6\2\2\32\33\7\24\2\2\33\34\7\7\2\2\34\36")
        buf.write("\5\4\3\7\35\r\3\2\2\2\35\22\3\2\2\2\35\23\3\2\2\2\35\24")
        buf.write("\3\2\2\2\35\26\3\2\2\2\36\62\3\2\2\2\37 \f\6\2\2 !\t\5")
        buf.write("\2\2!\"\7\5\2\2\"#\7\24\2\2#$\7\6\2\2$%\7\24\2\2%&\7\7")
        buf.write("\2\2&\61\5\4\3\6\'(\f\5\2\2()\t\5\2\2)\61\5\4\3\5*+\f")
        buf.write("\4\2\2+,\t\6\2\2,\61\5\4\3\5-.\f\3\2\2./\7\17\2\2/\61")
        buf.write("\5\4\3\3\60\37\3\2\2\2\60\'\3\2\2\2\60*\3\2\2\2\60-\3")
        buf.write("\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63\5")
        buf.write("\3\2\2\2\64\62\3\2\2\2\6\t\35\60\62")
        return buf.getvalue()


class SpecificationParser ( Parser ):

    grammarFileName = "Specification.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'['", "','", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NEGATION", "PREVIOUS", 
                      "NEXT", "ALWAYS", "EVENTUALLY", "CONJUNCTION", "DISJUNCTION", 
                      "IMPLICATION", "SINCE", "UNTIL", "TRUE", "FALSE", 
                      "NUMBER", "ATOMIC_PROPOSITION", "WS" ]

    RULE_specification = 0
    RULE_formula = 1

    ruleNames =  [ "specification", "formula" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    NEGATION=6
    PREVIOUS=7
    NEXT=8
    ALWAYS=9
    EVENTUALLY=10
    CONJUNCTION=11
    DISJUNCTION=12
    IMPLICATION=13
    SINCE=14
    UNTIL=15
    TRUE=16
    FALSE=17
    NUMBER=18
    ATOMIC_PROPOSITION=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SpecificationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.phi = None # FormulaContext

        def EOF(self):
            return self.getToken(SpecificationParser.EOF, 0)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationParser.FormulaContext)
            else:
                return self.getTypedRuleContext(SpecificationParser.FormulaContext,i)


        def getRuleIndex(self):
            return SpecificationParser.RULE_specification

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecification" ):
                return visitor.visitSpecification(self)
            else:
                return visitor.visitChildren(self)




    def specification(self):

        localctx = SpecificationParser.SpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                localctx.phi = self.formula(0)
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SpecificationParser.T__0) | (1 << SpecificationParser.NEGATION) | (1 << SpecificationParser.PREVIOUS) | (1 << SpecificationParser.NEXT) | (1 << SpecificationParser.ALWAYS) | (1 << SpecificationParser.EVENTUALLY) | (1 << SpecificationParser.TRUE) | (1 << SpecificationParser.FALSE) | (1 << SpecificationParser.ATOMIC_PROPOSITION))) != 0)):
                    break

            self.state = 9
            self.match(SpecificationParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FormulaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return SpecificationParser.RULE_formula

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ParenthesisContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecificationParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(SpecificationParser.FormulaContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesis" ):
                return visitor.visitParenthesis(self)
            else:
                return visitor.visitChildren(self)


    class UnboundedBinaryOperatorContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecificationParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.op = None # Token
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationParser.FormulaContext)
            else:
                return self.getTypedRuleContext(SpecificationParser.FormulaContext,i)

        def UNTIL(self):
            return self.getToken(SpecificationParser.UNTIL, 0)
        def SINCE(self):
            return self.getToken(SpecificationParser.SINCE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnboundedBinaryOperator" ):
                return visitor.visitUnboundedBinaryOperator(self)
            else:
                return visitor.visitChildren(self)


    class BooleanConstantContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecificationParser.FormulaContext
            super().__init__(parser)
            self.val = None # Token
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(SpecificationParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(SpecificationParser.FALSE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanConstant" ):
                return visitor.visitBooleanConstant(self)
            else:
                return visitor.visitChildren(self)


    class AtomicPropositionContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecificationParser.FormulaContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def ATOMIC_PROPOSITION(self):
            return self.getToken(SpecificationParser.ATOMIC_PROPOSITION, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtomicProposition" ):
                return visitor.visitAtomicProposition(self)
            else:
                return visitor.visitChildren(self)


    class UnaryOperatorContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecificationParser.FormulaContext
            super().__init__(parser)
            self.op = None # Token
            self.left = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self):
            return self.getTypedRuleContext(SpecificationParser.FormulaContext,0)

        def NEGATION(self):
            return self.getToken(SpecificationParser.NEGATION, 0)
        def ALWAYS(self):
            return self.getToken(SpecificationParser.ALWAYS, 0)
        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SpecificationParser.NUMBER)
            else:
                return self.getToken(SpecificationParser.NUMBER, i)
        def PREVIOUS(self):
            return self.getToken(SpecificationParser.PREVIOUS, 0)
        def NEXT(self):
            return self.getToken(SpecificationParser.NEXT, 0)
        def EVENTUALLY(self):
            return self.getToken(SpecificationParser.EVENTUALLY, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOperator" ):
                return visitor.visitUnaryOperator(self)
            else:
                return visitor.visitChildren(self)


    class BinaryOperatorContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecificationParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.op = None # Token
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationParser.FormulaContext)
            else:
                return self.getTypedRuleContext(SpecificationParser.FormulaContext,i)

        def CONJUNCTION(self):
            return self.getToken(SpecificationParser.CONJUNCTION, 0)
        def DISJUNCTION(self):
            return self.getToken(SpecificationParser.DISJUNCTION, 0)
        def IMPLICATION(self):
            return self.getToken(SpecificationParser.IMPLICATION, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOperator" ):
                return visitor.visitBinaryOperator(self)
            else:
                return visitor.visitChildren(self)


    class BoundedBinaryOperatorContext(FormulaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a SpecificationParser.FormulaContext
            super().__init__(parser)
            self.left = None # FormulaContext
            self.op = None # Token
            self.right = None # FormulaContext
            self.copyFrom(ctx)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SpecificationParser.NUMBER)
            else:
                return self.getToken(SpecificationParser.NUMBER, i)
        def formula(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SpecificationParser.FormulaContext)
            else:
                return self.getTypedRuleContext(SpecificationParser.FormulaContext,i)

        def UNTIL(self):
            return self.getToken(SpecificationParser.UNTIL, 0)
        def SINCE(self):
            return self.getToken(SpecificationParser.SINCE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoundedBinaryOperator" ):
                return visitor.visitBoundedBinaryOperator(self)
            else:
                return visitor.visitChildren(self)



    def formula(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = SpecificationParser.FormulaContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_formula, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SpecificationParser.T__0]:
                localctx = SpecificationParser.ParenthesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 12
                self.match(SpecificationParser.T__0)
                self.state = 13
                localctx.left = self.formula(0)
                self.state = 14
                self.match(SpecificationParser.T__1)
                pass
            elif token in [SpecificationParser.TRUE, SpecificationParser.FALSE]:
                localctx = SpecificationParser.BooleanConstantContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 16
                localctx.val = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==SpecificationParser.TRUE or _la==SpecificationParser.FALSE):
                    localctx.val = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [SpecificationParser.ATOMIC_PROPOSITION]:
                localctx = SpecificationParser.AtomicPropositionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                localctx.atom = self.match(SpecificationParser.ATOMIC_PROPOSITION)
                pass
            elif token in [SpecificationParser.NEGATION, SpecificationParser.ALWAYS]:
                localctx = SpecificationParser.UnaryOperatorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 18
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not(_la==SpecificationParser.NEGATION or _la==SpecificationParser.ALWAYS):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 19
                localctx.left = self.formula(6)
                pass
            elif token in [SpecificationParser.PREVIOUS, SpecificationParser.NEXT, SpecificationParser.EVENTUALLY]:
                localctx = SpecificationParser.UnaryOperatorContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 20
                localctx.op = self._input.LT(1)
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SpecificationParser.PREVIOUS) | (1 << SpecificationParser.NEXT) | (1 << SpecificationParser.EVENTUALLY))) != 0)):
                    localctx.op = self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
                self.match(SpecificationParser.T__2)
                self.state = 22
                self.match(SpecificationParser.NUMBER)
                self.state = 23
                self.match(SpecificationParser.T__3)
                self.state = 24
                self.match(SpecificationParser.NUMBER)
                self.state = 25
                self.match(SpecificationParser.T__4)
                self.state = 26
                localctx.left = self.formula(5)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 48
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 46
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = SpecificationParser.BoundedBinaryOperatorContext(self, SpecificationParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 29
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 30
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SpecificationParser.SINCE or _la==SpecificationParser.UNTIL):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 31
                        self.match(SpecificationParser.T__2)
                        self.state = 32
                        self.match(SpecificationParser.NUMBER)
                        self.state = 33
                        self.match(SpecificationParser.T__3)
                        self.state = 34
                        self.match(SpecificationParser.NUMBER)
                        self.state = 35
                        self.match(SpecificationParser.T__4)
                        self.state = 36
                        localctx.right = self.formula(4)
                        pass

                    elif la_ == 2:
                        localctx = SpecificationParser.UnboundedBinaryOperatorContext(self, SpecificationParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 37
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 38
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SpecificationParser.SINCE or _la==SpecificationParser.UNTIL):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        localctx.right = self.formula(3)
                        pass

                    elif la_ == 3:
                        localctx = SpecificationParser.BinaryOperatorContext(self, SpecificationParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 40
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 41
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==SpecificationParser.CONJUNCTION or _la==SpecificationParser.DISJUNCTION):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        localctx.right = self.formula(3)
                        pass

                    elif la_ == 4:
                        localctx = SpecificationParser.BinaryOperatorContext(self, SpecificationParser.FormulaContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_formula)
                        self.state = 43
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 44
                        localctx.op = self.match(SpecificationParser.IMPLICATION)
                        self.state = 45
                        localctx.right = self.formula(1)
                        pass

             
                self.state = 50
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.formula_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def formula_sempred(self, localctx:FormulaContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




