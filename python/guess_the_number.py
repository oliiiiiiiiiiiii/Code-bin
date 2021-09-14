from random import randint

max_number = input("Enter the max number you want:")

ans = True

while ans:
  number = randint(1,max_number)
  guess = input("Guess the number: ")
  ans = number == guess
  if ans:
    print("Wow you guessed it right")
  else:
    print("You tried unfortunately it was not right better luck next time.")
    break
