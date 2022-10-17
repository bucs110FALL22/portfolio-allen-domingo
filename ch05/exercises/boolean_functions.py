def percentage_to_letter(score=0):
  if score >= 90:
    grade = "A"
    
    return("A")
  elif 80 <= score < 90:
    grade = "B"
    
    return("B")
  elif 70 <= score < 80:
    grade = "C"
    
    return("C")
  elif 60 <= score < 70:
    grade = "D"
    
    return("D")
  elif score < 60:
    grade = "F"
    
    return("F")
    
  print(grade)
def is_passing(letter=None):
  if letter == "A" or letter == "B" or letter == "C":
    return(True)
    
  else:
    return(False)
    

enter_score = float(input("Enter grade:"))
enter = percentage_to_letter(enter_score)
result = is_passing(enter)
print(enter)
if result == True:
  print("is passing")
else:
  print("not passing")