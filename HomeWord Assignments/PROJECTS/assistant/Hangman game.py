
import random

word_list = ["python", "javascript", "java", "ruby", "html", "css", "swift", "kotlin"]

# Function to display the word with guessed letters
def display_word(word, guessed_letters):
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "-"
        display_word += " "  # Adds a space between the characters for better readability
    return display_word.strip()

# Randomly select a word from the list
word = random.choice(word_list)
word_letters = set(word)
guessed_letters = set()
attempts = 6

# Game loop
print("Welcome to the Hangman game!")

while attempts > 0:
    print(f"\nWord: {display_word(word, guessed_letters)}")
    print(f"You have {attempts} attempts left.")
    print(f"Guessed letters: {' '.join(guessed_letters)}")

    guess = input("Guess a letter: ").lower()
    
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue  # Skip the rest of the loop and ask for a new guess

    guessed_letters.add(guess)
    
    if guess in word_letters:
        print("Good job!")
    else:
        print("Wrong guess!")
        attempts -= 1
    
    # Check if the player has guessed all the letters
    if "_" not in display_word(word, guessed_letters):
        print(f"\nCongratulations! You guessed the word: {word}")
        break  # Exit the loop if the word is guessed correctly

if attempts == 0:
    print(f"\nYou lose! The word was: {word}")







# import random
# word_list = ["python", "javescript", "java", "ruby", "html", "css", "swift", "kotlin"]
# def display_word(word,guessed_letters):
#    display_word=""
#    for letter in word:
#      if letter in guessed_letters:
#        display_word += letter
#      else:
#        display_word += "-"
#        display_word += " "
#        return display_word
# word =random.choice(word_list)
# word_letters = set(word)
# attempts = 6
# while  attempts >0:
#   guessed_letters = set() 
# print("welcome to the hangman game!")
# print (f"word:{display_word(word,guessed_letters)}")
# print(f"you have six change to guess the world!")
# print (f"guessed letters:{" ".join(guessed_letters)}")
# print (f"Attempts left:{attempts}")
# guess = input("guess a letter:") .lower()
# guessed_letters.add (guess)
# if guess in word_letters:
#   print(f"good job!")
# else:
#   print("wrong Guess!" )
#   attempts -= 1
#   if attempts == 0:
#    if "_" not in display_word(word_letters,guessed_letters):
#      print (f"congratulations! you guessed the word {word}")
#      print (f" you lose! the word was {word}")
#     break