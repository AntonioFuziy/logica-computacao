import re
import sys

class PrePro:
  def __init__(self, entire_string):
    self.entire_string = entire_string
  
  def filter_expression(self):
    self.entire_string = re.sub("/\*.*?\*/", "", self.entire_string)
    return self.entire_string

class Token:
  def __init__(self, token_type, value):
    self.token_type = token_type
    self.value = value

class Tokenizer:
  def __init__(self, origin):
    self.origin = origin
    self.position = 0
    self.actual_token = None

  def select_next(self):
    #checar se o proximo caracter é um EOF
    if self.position >= len(self.origin):
      self.actual_token = Token("EOF", " ")
      return self.actual_token
    
    if self.origin[0] == " ":
      pass
    else:
      if (("-" not in self.origin) and ("+" not in self.origin) and ("*" not in self.origin) and ("/" not in self.origin)) and len(self.origin) > 1:
        raise ValueError
    

    #checar se o proximo caracter é um espaço
    if self.origin[self.position] == " ":
      self.position += 1
      self.select_next()

    #checar se o proximo caracter é um *
    elif self.origin[self.position] == "*":
      self.position += 1
      self.actual_token = Token("MULT", "*")
      return self.actual_token
      
    #checar se o proximo caracter é um /
    elif self.origin[self.position] == "/":
      self.position += 1
      self.actual_token = Token("DIV", "/")
      return self.actual_token
    
    #checar se o proximo caracter é um +
    elif self.origin[self.position] == "+":
      self.position += 1
      self.actual_token = Token("PLUS", " ")
      return self.actual_token
    
    #checar se o proximo caracter é um -
    elif self.origin[self.position] == "-":
      self.position += 1
      self.actual_token = Token("MINUS", " ")
      return self.actual_token
    
    #checar se o proximo caracter é um digito
    elif self.origin[self.position].isnumeric():
      candidato = self.origin[self.position]
      self.position += 1

      #enquanto o caractere não estiver no fim
      while self.position < len(self.origin):
        
        #se o caractere for um digito
        if self.origin[self.position].isnumeric():
          #concatena o caractere ao candidato
          candidato += self.origin[self.position]
          self.position += 1
        
        #se não for um digito
        else:
          self.actual_token = Token("NUMBER", int(candidato))
          return self.actual_token

      #atualiza o token
      self.actual_token = Token("NUMBER", int(candidato))
      return self.actual_token
    
    else:
      raise ValueError

class Parser:
  tokens = None

  def parse_term():
    result = 0

    if Parser.tokens.actual_token.token_type != "NUMBER":
      raise ValueError

    result = Parser.tokens.actual_token.value
    Parser.tokens.select_next()
  
    # print(Parser.tokens.actual_token.token_type)
    # print(Parser.tokens.actual_token.value)
    #enquanto nao terminar e for * ou /
    while (Parser.tokens.actual_token.token_type == "MULT" or Parser.tokens.actual_token.token_type == "DIV") and Parser.tokens.actual_token.token_type != "EOF":
      # print(Parser.tokens.actual_token.token_type)
      # print(Parser.tokens.actual_token.value)
      
      if Parser.tokens.actual_token.token_type == "MULT":
        Parser.tokens.select_next()

        #Se for numero MULT
        if Parser.tokens.actual_token.token_type == "NUMBER":
          result *= Parser.tokens.actual_token.value
        
        #se não for numero retorna erro
        else:
          raise ValueError

      elif Parser.tokens.actual_token.token_type == "DIV":
        Parser.tokens.select_next()

        #Se for numero DIV
        if Parser.tokens.actual_token.token_type == "NUMBER":
          result //= Parser.tokens.actual_token.value
        
        #se não for numero retorna erro
        else:
          raise ValueError
          
      Parser.tokens.select_next()
    return result
  
  def parse_expression():
    
    Parser.tokens.select_next()
    result = Parser.parse_term()

    # print(Parser.tokens.actual_token.token_type)
    # print(Parser.tokens.actual_token.value)
    #enquanto nao terminar e for + ou -
    while (Parser.tokens.actual_token.token_type == "PLUS" or Parser.tokens.actual_token.token_type == "MINUS") and Parser.tokens.actual_token.token_type != "EOF":      
      # print(Parser.tokens.actual_token.token_type)
      # print(Parser.tokens.actual_token.value)
      #se for +
      if Parser.tokens.actual_token.token_type == "PLUS":
        Parser.tokens.select_next()

        #Se for numero soma
        result += Parser.parse_term()
        
      #se for -
      elif Parser.tokens.actual_token.token_type == "MINUS":
        Parser.tokens.select_next()

        #Se for numero subtrai
        result -= Parser.parse_term()

      #se não for numero retorna erro
      else:
        raise ValueError
    return result
  
  def run(code):
    code_filtered = PrePro(code).filter_expression()
    # print(code_filtered)
    Parser.tokens = Tokenizer(code_filtered)
    result = Parser.parse_expression()
    print(result)

Parser.run(sys.argv[1])