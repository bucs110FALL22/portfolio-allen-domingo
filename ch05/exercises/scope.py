def multi(a=0,b=0):
  num = 0
  for z in range (b):
    num +=a
  return num

def exponent(c=0,d=0):
  num2 = 1
  for x in range (d):
    num2 *= c
  return num2
def square(e):
  r = multi(e,e)
  return r

def main():
  numA = 3
  numB = 4
  numC = 6
  numD = 10
  function1 = multi(numA,numB)
  print(function1)

  function2 = exponent(numB,numC)
 
  print(function2)

  function3 = square(numD)
  
  print(function3)
main()