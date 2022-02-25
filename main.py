import sys
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

    #checar se o proximo caracter é um espaço
    if self.origin[self.position] == " ":
      self.position += 1
      self.select_next()
    
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
  def parse_expression():
    result = 0
    
    if (("-" not in Parser.tokens.origin) and ("+" not in Parser.tokens.origin)) and len(Parser.tokens.origin) > 1:
      raise ValueError

    #seleciona o proximo token para evitar bug com None
    Parser.tokens.select_next()
    
    # enquanto o token nao terminar
    while Parser.tokens.actual_token != "EOF":
      if Parser.tokens.actual_token.token_type == "NUMBER":
        result = Parser.tokens.actual_token.value
        Parser.tokens.select_next()
      
        #enquanto for + ou -
        while Parser.tokens.actual_token.token_type == "PLUS" or Parser.tokens.actual_token.token_type == "MINUS":
          #se for +
          if Parser.tokens.actual_token.token_type == "PLUS":
            Parser.tokens.select_next()

            #Se for numero soma
            if Parser.tokens.actual_token.token_type == "NUMBER":
              result += Parser.tokens.actual_token.value
            
            #se não for numero retorna erro
            else:
              raise ValueError
            
          #se for -
          elif Parser.tokens.actual_token.token_type == "MINUS":
            Parser.tokens.select_next()

            #Se for numero subtrai
            if Parser.tokens.actual_token.token_type == "NUMBER":
              result -= Parser.tokens.actual_token.value

            #se não for numero retorna erro
            else:
              raise ValueError
          
          Parser.tokens.select_next()
        print(result)
        return result

      else:
        raise ValueError
  
  def run(code):
    Parser.tokens = Tokenizer(code)
    Parser.parse_expression()

Parser.run(sys.argv[1])