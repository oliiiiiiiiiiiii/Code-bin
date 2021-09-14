from random import randint #importing randint function from random library

max_number = int(input("Enter the max number you want:")) #enter the max limit of the randomly generated number and make it an integer

ans = True 

while ans: #since we defined ans as True so it will keep iterating unless ans becomes False
  number = randint(1,max_number) #the randint function generates a random number such that : if randint(a,b) , a <= number <= b
  guess = int(input("Guess the number: ")) #to take input from user about thier guess and converting it into an integer
  if number==guess: #checking equality of the guess and the randomly genrated number
    print("Wow you guessed it right") 
  else:
    print("You tried unfortunately it was incorrect better luck next time.")
    break #exiting from the loop if the guess is incorrect
