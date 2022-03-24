from Token import Token

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

    elif self.origin[self.position] == "(":
      self.position += 1
      self.actual_token = Token("OPEN_PAR", " ")
      return self.actual_token

    elif self.origin[self.position] == ")":
      self.position += 1
      self.actual_token = Token("CLOSE_PAR", " ")
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
      raise Exception("select next error")