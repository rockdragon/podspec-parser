grammar cocoapods;

requirement: WS* operator? WS* version WS* EOF;

version: major (DOT minor (DOT patch)?)?  ;
major: VERSION_ELEMENT ;
minor: VERSION_ELEMENT ;
patch: VERSION_ELEMENT ;
operator: OPERATOR ;

OPERATOR: SIMPLE_OPERATOR | COCOA_VERSION ;
fragment COCOA_VERSION: TILDE GT ;

VERSION_ELEMENT: ZERO | NON_ZERO (NUMBER)*  ;
NON_ZERO: '1'..'9' ;
ZERO: '0' ;
NUMBER: ZERO | NON_ZERO ;

fragment SIMPLE_OPERATOR: GTEQ | LTEQ | LT | GT | EQ ;
fragment LTEQ: LT EQ ;
fragment GTEQ: GT EQ ;
fragment LT: '<' ;
fragment GT: '>' ;
fragment EQ: '=' ;
fragment TILDE: '~' ;
fragment CARET: '^' ;

LEFT_BRACKET: '[' ;
RIGHT_BRACKET: ']' ;
LEFT_PARENS: '(' ;
RIGHT_PARENS: ')' ;

DOT: '.' ;
COMMA: ',' ;

WS                 : [\t ]+;