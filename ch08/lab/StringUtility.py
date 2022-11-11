class StringUtility:
  def __init__(self,string=""):
    self.stri = string
    
  def vowels(self):
    vowel = 0
    self.low_string = self.stri.lower()
    
    for l in f"{self.low_string}":
      if l == "a":
        vowel +=1 
      elif l == "e" :
        vowel +=1 
      elif l == "i":
        vowel +=1 
      elif l == "o":
        vowel +=1 
      elif l == "u":
        vowel +=1  
      else:
        vowel += 0
      print(l,vowel)

    if vowel >= 5:
      vowel = "many"
    print(self.low_string,vowel)
    return str(vowel)
  def bothEnds(self):
    return f"{self.stri[0:2]}"+f"{self.stri[-2:]}"
  def fixStart(self):
    self.fix_string = list(self.stri)

    v = 1
    for l in self.fix_string[1:]:
      if str(l) is str(self.fix_string[0]):
        self.fix_string[v]= "*"
        str(self.fix_string[v])
      v+=1
    
    return "".join(self.fix_string)
    

      
    
        

        
      
      
  def __str__(self):
    return self.stri

