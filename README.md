# Status do teste

![git status](http://3.129.230.99/svg/AntonioFuziy/logica-computacao/)

___


## EBNF

```
BLOCK = "{", STATEMENT, "}";

STATEMENT =  (λ | ASSIGNMENT | BLOCK | PRINT | IF | WHILE), ";";

RELATIONAL_EXPRESSION = EXPRESSION, { ("==" | "<" | ">"), EXPRESSION };

EXPRESSION = TERM, { ("+" | "-" | "||"), TERM };

TERM = FACTOR, { ("*" | "/" | "&&") };

FACTOR = INT | IDENTIFIER | (("+" | "-" | "!"), FACTOR) | "(", RELATIONAL_EXPRESSION, ")" | SCANF;

ASSIGNMENT = IDENTIFIER, "=", EXPRESSION;

PRINT = "printf", "(", EXPRESSION, ")";

IF = "if", "(", RELATIONAL_EXPRESSION, ")", STATEMENT, { ("else", STATEMENT) | λ };

WHILE = "while", "(", RELATIONAL_EXPRESSION, ")", STATEMENT;

SCANF = "scanf", "(", ")";

INT = DIGIT, { DIGIT };

DIGIT = ( 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 );

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = (a | b | c | d | ... x | y | z | A | B | ... | Y | Z );
```