class StringUtility:
  def __init__(self,string=""):
    self.stri = string
    
  def vowels(self):
    '''
    
    counts the number of vowels in a string (many if it is >= 5)
    args: self - instance of StringUtility
    returns: number of vowels in a string
    '''
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


    if vowel >= 5:
      vowel = "many"

    return str(vowel)
  def bothEnds(self):
    '''
    Brings only the first and last two characters in a string in python, or nothing if there are two or less characters
    args: self - instance of StringUtility
    returns first and last two characters or nothing if characters <=2 
    '''
    return f"{self.stri[0:2]}"+f"{self.stri[-2:]}"
  def fixStart(self):
    '''
    replaces the instances of the first character (other than the first character) with "*"
    args: self - instance of StringUtility
    returns modified string with instances of first character changed to "*"
    '''
    self.fix_string = list(self.stri)

    v = 1
    for l in self.fix_string[1:]:
      if str(l) is str(self.fix_string[0]):
        self.fix_string[v]= "*"
        str(self.fix_string[v])
      v+=1
    
    return "".join(self.fix_string)
    

      
  def asciiSum(self):
    '''
    sums up the ascii calues of each character in the string
    args: self - instance of StringUtility 
    returns sum of ascii values of each character
    '''
    return sum([ord(letter) for letter in self.stri])
  def cipher(self):
    '''
    takes each letter in the string and moves it up by the length of the string
    args: self - instance of StringUtility
    returns string with letters shifted by string length
    '''

    
    ciph = ""
    for letter in range(len(self.stri)):
      if self.stri[letter].isupper() == True:
        ciph += chr((ord(self.stri[letter].lower())+len(self.stri)-97)%26+97).upper()
        
      if self.stri[letter].islower()==True:
        ciph += chr((ord(self.stri[letter])+len(self.stri)-97)%26+97)
        
      if self.stri[letter] == " ":
        ciph += " "
    return ciph

        
      
      
  def __str__(self):
    return self.stri

