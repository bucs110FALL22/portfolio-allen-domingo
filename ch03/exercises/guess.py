import random
answer = random.randint(1,11)
#print(answer)
num_guesses = 0
for c in range(5):
  guess = int(input("Guess a number between 1 and 10: "))
  num_guesses += 1
  if guess > answer:
   print("Too High")
  elif guess < answer: 
    print("Too low")
  else:
    print("Correct!")
    print("It took you", num_guesses, "guesses to get it right")
    break