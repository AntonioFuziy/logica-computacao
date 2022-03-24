import sys

from Node import BinOp, IntVal, UnOp
from PrePro import PrePro
from Tokenizer import Tokenizer

class Parser:
  tokens = None

  def parse_factor():
    node = 0

    if Parser.tokens.actual_token.token_type == "NUMBER":
      node = IntVal(Parser.tokens.actual_token.value, [])
      Parser.tokens.select_next()
    
    elif Parser.tokens.actual_token.token_type == "OPEN_PAR":
      node = Parser.parse_expression()
      if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
        raise Exception("Parenthesis error")
      Parser.tokens.select_next()
    
    elif Parser.tokens.actual_token.token_type == "PLUS":
      Parser.tokens.select_next()
      node = UnOp("+", [Parser.parse_factor()])
      
    elif Parser.tokens.actual_token.token_type == "MINUS":
      Parser.tokens.select_next()
      node = UnOp("-", [Parser.parse_factor()])
    
    else:
      raise Exception("Parse factor error")
      
    return node

  def parse_term():
    node = Parser.parse_factor()
  
    #enquanto nao terminar e for * ou /
    while (Parser.tokens.actual_token.token_type == "MULT" or Parser.tokens.actual_token.token_type == "DIV"):      
      if Parser.tokens.actual_token.token_type == "MULT":
        Parser.tokens.select_next()
        node = BinOp("*", [node, Parser.parse_factor()])

      elif Parser.tokens.actual_token.token_type == "DIV":
        Parser.tokens.select_next()
        node = BinOp("/", [node, Parser.parse_factor()])
      
      else:
        raise Exception("Parse term error")

    return node
  
  def parse_expression():
    Parser.tokens.select_next()
    node = Parser.parse_term()

    #enquanto nao terminar e for + ou -
    while (Parser.tokens.actual_token.token_type == "PLUS" or Parser.tokens.actual_token.token_type == "MINUS") and Parser.tokens.actual_token.token_type != "EOF":      
      #se for +
      if Parser.tokens.actual_token.token_type == "PLUS":
        Parser.tokens.select_next()

        #Se for numero soma
        node = BinOp("+", [node, Parser.parse_term()])
        
      #se for -
      elif Parser.tokens.actual_token.token_type == "MINUS":
        Parser.tokens.select_next()

        #Se for numero subtrai
        node = BinOp("-", [node, Parser.parse_term()])

      #se não for numero retorna erro
      else:
        raise Exception("Parse expression")

    return node
  
  def run(code):
    f = open(code,"r")
    code = f.read()
    f.close()
    code_filtered = PrePro(code).filter_expression()
    Parser.tokens = Tokenizer(code_filtered)
    node = Parser.parse_expression()
    if Parser.tokens.actual_token.token_type != "EOF":
      raise Exception("EOF run error")
    print(node.Evaluate())

Parser.run(sys.argv[1])