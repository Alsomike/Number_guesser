import random
print("Hello, what is your name?")
name = input()
randomNum = random.randint(1, 20)
print("Hey " + name + ", I am thinking a number between 1 and 20. Take a guess!")


for guessesTaken in range(1, 6):
  guess = int(input())
  if guess > randomNum:
    print("Too high, try again")
  elif guess < randomNum:
    print("Too low, try again")
  else:
    break

if randomNum == guess and guessesTaken == 1:
  print("you gussed it correctly in " + str(guessesTaken) + " guess!")
elif randomNum == guess and guessesTaken > 1:
  print("you gussed it correctly in " + str(guessesTaken) + " guesses!")
else:
  print("sorry, the number I was thinking about was " + str(randomNum))