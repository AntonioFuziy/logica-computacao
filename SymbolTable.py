class SymbolTable():
  def __init__(self):
    self.table = {}
    self.address = 0
    
  def setter(self, name, value):
    if name not in self.table.keys():
      raise Exception(f"{name} is not defined")
    if self.table[name][1] == "INT":
      if type(value) == int:
        self.table[name] = (value, "INT", self.table[name][2])
    elif self.table[name][1] == "STRING":
      if type(value) == str:
        self.table[name] = (value, "STRING", self.table[name][2])
    else:
      raise Exception(f"{name} type doesnt match")

  def getter(self, name):
    if name not in self.table.keys():
      raise Exception(f"{name} is not defined")
    return self.table[name]

  def create(self, name, var_type):
    if name in self.table.keys():
      raise Exception(f"{name} is already defined")
    if var_type == "INT":
      self.address += 4
      self.table[name] = (None, var_type, self.address)
    elif var_type == "STRING":
      self.address += 4
      self.table[name] = (None, var_type, self.address)
    else:
      raise Exception(f"{var_type} doesnt exist")