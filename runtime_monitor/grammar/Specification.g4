grammar Specification;

/*
 * Parser Rules
 */

specification: phi = formula+ EOF;

formula : '(' left = formula ')'                                                                        # Parenthesis
        | val = (TRUE | FALSE)	                                                                        # BooleanConstant
        | atom = ATOMIC_PROPOSITION                                                                     # AtomicProposition
        | op = (NEGATION | ALWAYS) left = formula                                                       # UnaryOperator
        | op = (PREVIOUS | NEXT | EVENTUALLY) '[' NUMBER ',' NUMBER ']' left = formula                  # UnaryOperator
        | <assoc=right> left = formula op = (UNTIL | SINCE) '[' NUMBER ',' NUMBER ']' right = formula	# BoundedBinaryOperator
        | <assoc=right> left = formula op = (UNTIL | SINCE) right = formula	                            # UnboundedBinaryOperator
        | left = formula op = (CONJUNCTION | DISJUNCTION) right = formula                               # BinaryOperator
        | <assoc=right> left = formula op = IMPLICATION right = formula                                 # BinaryOperator
        ;

/*
 * Lexer Rules
 */

NEGATION : ([nN]'ot' | '!');
PREVIOUS: ([pP]'revious' | 'P');
NEXT: ([nN]'ext' | 'X');
ALWAYS : [aA]'lways';
EVENTUALLY : [eE]'ventually';

CONJUNCTION: ([aA]'nd' | '&&');
DISJUNCTION : ([oO]'r' | '||');
IMPLICATION: ([iI]'mplies' | '->');
SINCE: ([sS]'ince' | 'S');
UNTIL : ([uU]'ntil' | 'U');

TRUE : ([tT]'rue' | 'tt');
FALSE : ([fF]'alse' | 'ff');
NUMBER : [0-9]+;
ATOMIC_PROPOSITION : [_a-zA-Z]+[_a-zA-Z0-9]*;

WS : [ \t]+ -> channel(HIDDEN) ;