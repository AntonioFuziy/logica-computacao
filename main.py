import sys

from Node import Assignment, BinOp, Block, Identifier, IntVal, NoOp, Printf, UnOp
from PrePro import PrePro
from SymbolTable import SymbolTable
from Tokenizer import Tokenizer

class Parser:
  tokens = None

  def parse_factor():
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

    elif Parser.tokens.actual_token.token_type == "IDENTIFIER":
      node = Identifier(Parser.tokens.actual_token.value, [])
      Parser.tokens.select_next()
    
    else:
      raise Exception("Parse factor error")
      
    return node

  def parse_term():
    node = Parser.parse_factor()
    
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
    node = Parser.parse_term()

    while (Parser.tokens.actual_token.token_type == "PLUS" or Parser.tokens.actual_token.token_type == "MINUS"):
      if Parser.tokens.actual_token.token_type == "PLUS":
        Parser.tokens.select_next()
        node = BinOp("+", [node, Parser.parse_term()])

      elif Parser.tokens.actual_token.token_type == "MINUS":
        Parser.tokens.select_next()
        node = BinOp("-", [node, Parser.parse_term()])

      else:
        raise Exception("Parse expression")

    return node

  def parse_statement():
    if Parser.tokens.actual_token.token_type == "IDENTIFIER":
      node = Identifier(Parser.tokens.actual_token.value, [])
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "EQUAL":
        Parser.tokens.select_next()
        node = Assignment("=", [node, Parser.parse_expression()])
        if Parser.tokens.actual_token.token_type == "SEMICOLON":
          Parser.tokens.select_next()
        else:
          raise Exception("Parse statement error")
      else:
        raise Exception("Parse statement error")

    elif Parser.tokens.actual_token.token_type == "PRINTF":
      Parser.tokens.select_next()
      if Parser.tokens.actual_token.token_type == "OPEN_PAR":
        Parser.tokens.select_next()
        node = Printf("printf", [Parser.parse_expression()])
        if Parser.tokens.actual_token.token_type != "CLOSE_PAR":
          raise Exception("Parse statement error")
        else:
          Parser.tokens.select_next()
          if Parser.tokens.actual_token.token_type == "SEMICOLON":
            Parser.tokens.select_next()
          else:
            raise Exception("Parse statement error")
      else:
        raise Exception("Parse statement error")

    elif Parser.tokens.actual_token.token_type == "SEMICOLON":
      node = NoOp(None, [])
      Parser.tokens.select_next()
      
    else:
      raise Exception("Parse statement error")
    
    return node

  def parse_block():
    children = []
    if Parser.tokens.actual_token.token_type == "OPEN_BRACKET":
      Parser.tokens.select_next()
      while Parser.tokens.actual_token.token_type != "CLOSE_BRACKET":
        node = Parser.parse_statement()
        children.append(node)
      node = Block(None, children)
      Parser.tokens.select_next()
    else:
      raise Exception("Parse block error")
    return node
  
  def run(code):
    code_filtered = PrePro(code).filter_expression()
    Parser.tokens = Tokenizer(code_filtered)
    Parser.tokens.select_next()
    node = Parser.parse_block()

    if Parser.tokens.actual_token.token_type != "EOF":
      raise Exception("EOF run error")
    
    return node

f = open(sys.argv[1],"r")
code = f.read()
f.close()
AST = Parser.run(code)
symbol_table = SymbolTable()
AST.Evaluate(symbol_table)