import random

lowest_num = 2
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True
print("Python Number Guessing Game")
print(f"Welcome to the Guess the Number Game! \n I have selected a number between {lowest_num} and {highest_num}. \n Try to guess it in 10 attempts or less.")
while is_running:
     guess = input("Entre your guess:")
     if guess.isdigit():
      guess = int(guess)
      guesses += 1

      if guess < lowest_num or guess > highest_num:
         print ("Please entre  a number between 2 and 100.")
         print("Try again.")
    
      elif guess < answer:
         print("Too low! Try again.")
      elif guess > answer:
           print("Too high! Try again.")
      else:
          print(f"Correct! the answer was {answer}")
          print(f"Number of guesses: {guesses}")
          is_running = False
     else:
         print("Invalid input. Please entre a number.")
         print("Try again.")
    