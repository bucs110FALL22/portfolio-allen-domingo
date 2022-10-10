def star_pyramid():
  rows = int(input("How many rows would you like?"))
  s = 1
  star_list = []
  while s != rows+1:
   star_list.append(s)
   s +=1
  for stars1 in star_list:
    print("*"*stars1)

def rstar_pyramid():
 stars = int(input("How many rows would you like?"))
 while stars != 0:
   print(stars*"*")
   stars -=1
   

star_pyramid()
rstar_pyramid()