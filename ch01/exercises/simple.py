#print(10*5)
#print(10**2)
#print(15/10)
#print(15//10)
#print(-15//10)
#print(15%10)
#print(10%15)
#print(10%10)
#print(0%10)
#print(10/15)
#the result is technically an decimal that repeats forever but it ends after a few sixes.
rate = float(input("What is the exchange rate from a Euro to a Dollar? "))

amount = float(input("What is the amount of currency that will be exchanged? "))

total = rate*amount
result = total-3.00
print(result)