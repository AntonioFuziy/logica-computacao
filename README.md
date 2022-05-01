# Status do teste

![git status](http://3.129.230.99/svg/AntonioFuziy/logica-computacao/)

___

## Diagrama Sintático do Compilador

![Diagrama Sintatico](https://github.com/AntonioFuziy/logica-computacao/blob/main/images/diagrama_sintatico_roteiro6.png?raw=true)

## EBNF

```
BLOCK = "{", STATEMENT, "}";

STATEMENT = ";" | (identifier, "=", RELATIONAL_EXPRESSION, ";") | (printf, "(", RELATIONAL_EXPRESSION, ")", ";") | (BLOCK) | (while, "(", RELATIONAL_EXPRESSION, ")", STATEMENT) | (if, "(", RELATIONAL_EXPRESSION, ")", STATEMENT, { else, STATEMENT });

RELATIONAL_EXPRESSION = EXPRESSION, { ("==" | "<" | ">"), EXPRESSION };

EXPRESSION = TERM, { ("+" | "-" | "||"), TERM };

TERM = FACTOR, { ("*" | "/" | "&&") };

FACTOR = number | identifier | ("+" | "-" | "!"), FACTOR | "(", RELATIONAL_EXPRESSION, ")" | scanf, "(", ")";
```