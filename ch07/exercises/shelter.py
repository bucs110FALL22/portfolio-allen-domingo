import time
class Shelter:
  def __init__(self,name,type):
    self.name = name
    self.type = type
    self.num = name,type
    self.arrived = time.strftime("%d/%m/%y")
    self.adopted = None
    self.id = id(self.num)
  def adoption(self):
    self.adopted = True
    self.time_adopted = time.strftime("%d/%m/%y")
    if self.adopted == True:
      print(self.name,"arrived:",self.arrived,"adopted:",self.time_adopted)
  def __str__(self):
    result_str = f"{self.name}{self.type}"
    result_str += f"\narrived:{self.arrived}"
    result_str += f"\nadopted:{self.time_adopted}"
    return result_str
def main():
  Fido = Shelter("fido","Shelter")
  Fido.adoption()
  print(Fido)


main() 