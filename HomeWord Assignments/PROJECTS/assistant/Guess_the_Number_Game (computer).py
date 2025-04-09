import random

def guess_the_number():
    """Project 2: Guess the Number Game computer."""
    number = random.randint(1, 100)
    guesses_left = 7
    print("Welcome to the GUESS THE NUMBER GAME!")
    print("I have selected a number between 1 and 100.")
    
    while guesses_left > 0:
        print(f"\nYou have {guesses_left} guesses left.")
        
        try:
            guess = int(input("Take a guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {number} correctly!")
            return
        
        guesses_left -= 1
    
    print("Sorry, you have no guesses left.")
    print(f"The number was {number}.")

# Start the game
guess_the_number()
























# import random
# def guess_the_number():
#     """Project 2: Guess the Number Game computer."""
#     number = random.randint(1, 100)
#     guess_left =7
#     print("Welcome to the GUESS THE NUMBER GAME!")
#     print ("I have selected a number between 1 and 100.")
#     while guesses_left > 0:
#         print(f"\n You have (guesses_left) guesses left.")
#     try:
#            guess = int(input("Take a guess of another number."))
#     except ValueError:
#          print ("Invalid input. Please entre a number.")
#        continue
#            if guess  < number:
#             print("Too low number  . Tell another!")
#           elif guess > number:
#            print("Too high number  . Tell another!")
#           else:
#         print(f" Congratulations! You guessed the number {number} correctly!")
#     return 
# guesses_left -= 1
#     print("Sorry, you have no guesses left.")
#     print(f" the number was {number}")
     