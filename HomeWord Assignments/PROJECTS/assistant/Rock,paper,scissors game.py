
import random

choices = ['rock', 'paper', 'scissors']

def play_rps(input_choice):
    # Adjust input case for consistency and ensure it matches valid choices
    input_choice = input_choice.lower()  # Ensure lowercase comparison
    if input_choice == "rock":
        return "rock"
    elif input_choice == 'paper':
        return "paper"
    elif input_choice == 'scissors':
        return "scissors"
    else:
        return "Invalid choice. Please choose rock, paper, or scissors."

print("Welcome to Rock, Paper, Scissors - shoot!")
print("Choose your weapon:")

counter = 0

while True:
    print('Game ' + str(counter) + ":")
    print('Please choose: Rock, Paper, or Scissors (or type Quit to exit)')

    user_choice = input()

    if user_choice.lower() == "quit":
        print("Thanks for playing!")
        break
    
    # Check if the user's choice is valid
    if user_choice.lower() not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue
    
    # Randomly choose for the computer
    computer_choice = random.choice(choices)
    
    print(f'Your choice: {user_choice.capitalize()}')
    print(f'Computer choice: {computer_choice.capitalize()}')

    # Determine the winner
    if user_choice.lower() == computer_choice:
        print("It's a tie!")
    elif (user_choice.lower() == "rock" and computer_choice == "scissors") or \
         (user_choice.lower() == "paper" and computer_choice == "rock") or \
         (user_choice.lower() == "scissors" and computer_choice == "paper"):
        print(f"You win! {user_choice.capitalize()} beats {computer_choice.capitalize()}")
    else:
        print(f"Computer wins! {computer_choice.capitalize()} beats {user_choice.capitalize()}")
    
    counter += 1
    print("\n THANKS FOR PLAYING! \n")  # Add space between rounds





# import random
# choices =['rock','paper','scissors']
# def play_rps(input_choice):
#     if input_choice == "Rock":
#      return "Rock"
#     elif input_choice == 'paper':
#     return "paper"
#     elif input_choice == 'Scissors':
#     return "scissors"
# else:
# return:"Invalid choice. Please choose rock,paer or scissors."
# print("Welcome to Pock,Paper,Scissorss - shoot!")
# print("choose your weapon:")
# counter = 0

# while True:
#    print('Game'+str(counter)+":")
#    print ('Please choose a letter:')
#    user_choice = input()

#    if user_choice == "Quit":
#       print("Thanks for Playing!")
#       break
#     random_choice = random.choice(choices ,0,2)
#    computer_choice = play_rps(random_choice)
#    print ('computer choice:', your_choice(user_choice)+'the computer chose'+get_choice(computer_choice)):
#    if user_choice == 'R' and computer_choice == "S":
#    print("you win!,rock beats scissors")
# elif user_choice == "P" and computer_choice == "R":
# print ("you win!, papaer beats rock")
# elif user_choice == "S" and computer_choice == "P":
# print ("you win!, scissors beats paper")
# elif user_choice == "R" and computer_choice == "P":
# print ("Computer win!, Paper beats Rock")
# elif user_choice == "P" and computer_choice == "S":
# print ("Computer win!, scissors beats Paper")
# elif user_choice == "S" and computer_choice == "R":
# print ("Computer win!, Rock beats Scissors")
# elif user_choice == computer_choice:
# print ("It's a tie!")
# else:
# print(Please choices rock,paper or scissors or quit to exit the game)
# counter = counter + 1
# print('\n THANKS FOR PLAYING! \n')