import time
class Shelter:
  def __init__(self,name,type,birth):
    self.title = name
    self.animal = type
    self.born = birth
    self.time_adopted = time.strftime("%d/%m/%y")
    self.adopted = False
def main():
  fido = Shelter("cat","dog","4/5/2016")
  print(fido.title,fido.time_adopted,fido.born)


main() 