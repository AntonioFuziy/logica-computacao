class Node():
  _id = 0
  def __init__(self, value, children):
    self.value = value
    self.children = children
  
  @staticmethod
  def new_id():
    Node._id += 1
    return Node._id
  
  def Evaluate(self, symbol_table, asm_code):
    pass

class Identifier(Node):
  def Evaluate(self, symbol_table, asm_code):
    asm_code.write(f"MOV EBX, [EBP-{symbol_table.getter(self.value)[2]}]")
    return symbol_table.getter(self.value)

class Assignment(Node):
  def Evaluate(self, symbol_table, asm_code):
    tmp = self.children[1].Evaluate(symbol_table, asm_code)[0]
    asm_code.write(f"MOV[EBP-{symbol_table.getter(self.children[0].value)[2]}], EBX")
    symbol_table.setter(self.children[0].value, tmp)

class Printf(Node):
  def Evaluate(self, symbol_table, asm_code):
    self.children[0].Evaluate(symbol_table, asm_code)[0]
    asm_code.write("PUSH EBX")
    asm_code.write("CALL print")
    asm_code.write("POP EBX")
    # print(self.children[0].Evaluate(symbol_table, asm_code)[0])

class Block(Node):
  def Evaluate(self, symbol_table, asm_code):
    for child in self.children:
      child.Evaluate(symbol_table, asm_code)
    
class VarDec(Node):
  def Evaluate(self, symbol_table, asm_code):
    for child in self.children:
      asm_code.write("PUSH DWORD 0")
      symbol_table.create(child.value, self.value)

class BinOp(Node):
  def Evaluate(self, symbol_table, asm_code):
    first_children = self.children[0].Evaluate(symbol_table, asm_code)
    asm_code.write(f"PUSH EBX")
    second_children = self.children[1].Evaluate(symbol_table, asm_code)
    asm_code.write(f"POP EAX")

    if self.value == ".":
      return (str(first_children[0]) + str(second_children[0]), "STRING", "")

    if first_children[1] != second_children[1]:
      raise Exception("Type doesnt match")

    if first_children[1] == "STRING" and second_children[1] == "STRING":
      if self.value == ">":
        asm_code.write("CMP EAX, EBX")
        asm_code.write(f"CALL binop_jg")
        if first_children[0] > second_children[0]:
          return (1, "INT", "")
        else:
          return (0, "INT", "")

      elif self.value == "<":
        asm_code.write("CMP EAX, EBX")
        asm_code.write(f"CALL binop_jl")
        if first_children[0] < second_children[0]:
          return (1, "INT", "")
        else:
          return (0, "INT", "")

      elif self.value == "==":
        asm_code.write("CMP EAX, EBX")
        asm_code.write(f"CALL binop_je")
        if first_children[0] == second_children[0]:
          return (1, "INT", "")
        else:
          return (0, "INT", "")

    elif first_children[1] == "INT" and second_children[1] == "INT":
      if self.value == "*":
        asm_code.write(f"IMUL EAX, EBX")
        asm_code.write(f"MOV EBX, EAX")
        return (first_children[0] * second_children[0], "INT", "")

      elif self.value == "/":
        asm_code.write(f"IDIV EAX, EBX")
        asm_code.write(f"MOV EBX, EAX")
        return (first_children[0] // second_children[0], "INT", "")
        
      elif self.value == "+":
        asm_code.write(f"ADD EAX, EBX")
        asm_code.write(f"MOV EBX, EAX")
        return (first_children[0] + second_children[0], "INT", "")

      elif self.value == "-":
        asm_code.write(f"SUB EAX, EBX")
        asm_code.write(f"MOV EBX, EAX")
        return (first_children[0] - second_children[0], "INT", "")

      elif self.value == "==":
        asm_code.write("CMP EAX, EBX")
        asm_code.write(f"CALL binop_je")
        if first_children[0] == second_children[0]:
          return (1, "INT", "")
        else:
          return (0, "INT", "")

      elif self.value == "&&":
        asm_code.write(f"AND EAX, EBX")
        asm_code.write(f"MOV EBX, EAX")
        if first_children[0] and second_children[0]:
          return (1, "INT", "")
        else:
          return (0, "INT", "")

      elif self.value == "||":
        asm_code.write(f"OR EAX, EBX")
        asm_code.write(f"MOV EBX, EAX")
        if first_children[0] or second_children[0]:
          return (1, "INT", "")
        else:
          return (0, "INT", "")

      elif self.value == ">":
        asm_code.write("CMP EAX, EBX")
        asm_code.write(f"CALL binop_jg")
        if first_children[0] > second_children[0]:
          return (1, "INT", "")
        else:
          return (0, "INT", "")

      elif self.value == "<":
        asm_code.write("CMP EAX, EBX")
        asm_code.write(f"CALL binop_jl")
        if first_children[0] < second_children[0]:
          return (1, "INT", "")
        else:
          return (0, "INT", "")

    else:
      raise Exception("BinOp error")

class UnOp(Node):
  def Evaluate(self, symbol_table, asm_code):
    unique_children = self.children[0].Evaluate(symbol_table, asm_code)
    
    if unique_children[1] == "STRING":
      raise Exception("STRING cannot be used for this operation")

    if self.value == "+":
      return (unique_children[0], "INT", "")
    elif self.value == "-":
      return (-unique_children[0], "INT", "")
    elif self.value == "!":
      return (not unique_children[0], "INT", "")
    else:
      raise Exception("UnOp error")

class IntVal(Node):
  def Evaluate(self, symbol_table, asm_code):
    asm_code.write(f"MOV EBX, {self.value}")
    return (self.value, "INT", "")
  
class StrVal(Node):
  def Evaluate(self, symbol_table, asm_code):
    return (self.value, "STRING", "")

class NoOp(Node):
  def Evaluate(self, symbol_table, asm_code):
    pass

class While(Node):
  def Evaluate(self, symbol_table, asm_code):
    current_label_id = Node.new_id()
    asm_code.write(f"LOOP_{current_label_id}:")
    self.children[0].Evaluate(symbol_table, asm_code)
    asm_code.write("CMP EBX, False")
    asm_code.write(f"JE EXIT_{current_label_id}")
    self.children[1].Evaluate(symbol_table, asm_code)
    asm_code.write(f"JMP LOOP_{current_label_id}")
    asm_code.write(f"EXIT_{current_label_id}:")
    
    # while self.children[0].Evaluate(symbol_table, asm_code)[0]:
    #   self.children[1].Evaluate(symbol_table, asm_code)

class If(Node):
  def Evaluate(self, symbol_table, asm_code):
    current_label_id = Node.new_id()
    asm_code.write(f"IF_{current_label_id}:")
    self.children[0].Evaluate(symbol_table, asm_code)
    asm_code.write("CMP EBX, False")
    asm_code.write(f"JE ELSE_{current_label_id}")
    self.children[1].Evaluate(symbol_table, asm_code)
    asm_code.write(f"JMP END_IF_{current_label_id}:")
    asm_code.write(f"ELSE_{current_label_id}:")
    
    if len(self.children) > 2:
      self.children[2].Evaluate(symbol_table, asm_code)
    asm_code.write(f"END_IF_{current_label_id}:")


    if self.children[0].Evaluate(symbol_table, asm_code)[0]:
      self.children[1].Evaluate(symbol_table, asm_code)
    elif len(self.children) > 2:
      self.children[2].Evaluate(symbol_table, asm_code)

class Scanf(Node):
  def Evaluate(self, symbol_table, asm_code):
    return (int(input()), "INT", "")