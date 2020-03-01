class NoteTemplate():
  def __init__(self, left, right, eqType):
    self.left = left
    self.right = right

    if (self.left < self.right):
      self.left, self.right = self.right, self.left

    self.eqType = eqType
    self.equation = str(self.left) + " " + self.getEquationType() + " " + str(self.right);
    self.result = self.calculate()

  def getEquationType(self):
    if (self.eqType == "add"):
      return "+"
    elif (self.eqType == "subtract"):
      return "-"

  def calculate(self):
    if (self.eqType == "add"):
      return self.addition()
    elif (self.eqType == "subtract"):
      return self.subtraction()
    else:
      return 0

  def addition(self):
    return self.left + self.right

  def subtraction(self):
    return self.left - self.right


