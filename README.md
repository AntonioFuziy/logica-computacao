# Status do teste

![git status](http://3.129.230.99/svg/AntonioFuziy/logica-computacao/)

___

## Diagrama Sintático do Compilador

![Diagrama Sintatico](https://github.com/AntonioFuziy/logica-computacao/blob/main/images/diagrama_sintatico_roteiro6.png?raw=true)

## EBNF

```
BLOCK = "{", STATEMENT, "}";

STATEMENT =  (λ | ASSIGNMENT | BLOCK | PRINT | IF | WHILE), ";";

RELATIONAL_EXPRESSION = EXPRESSION, { ("==" | "<" | ">"), EXPRESSION };

EXPRESSION = TERM, { ("+" | "-" | "||"), TERM };

TERM = FACTOR, { ("*" | "/" | "&&") };

FACTOR = NUMBER | IDENTIFIER | (("+" | "-" | "!"), FACTOR) | "(", RELATIONAL_EXPRESSION, ")" | SCANF;

ASSIGNMENT = IDENTIFIER, "=", EXPRESSION;

PRINT = "printf", "(", EXPRESSION, ")";

IF = "if", "(", RELATIONAL_EXPRESSION, ")", STATEMENT, { ("else", STATEMENT) | λ };

WHILE = "while", "(", RELATIONAL_EXPRESSION, ")", STATEMENT;

SCANF = "scanf", "(", ")";

NUMBER = DIGIT, { DIGIT };

DIGIT = ( 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 );

IDENTIFIER = LETTER, { LETTER | DIGIT | "_" };

LETTER = (a | b | c | d | ... x | y | z | A | B | ... | Y | Z );
```