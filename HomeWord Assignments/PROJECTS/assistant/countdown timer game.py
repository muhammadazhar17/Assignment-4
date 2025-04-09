import time
import random
import os

# Input for the countdown time in seconds
my_time = int(input("Enter the time in seconds: "))

# Countdown loop
for x in range(my_time, 0, -1):
    second = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 24
    # Print the time in HH:MM:SS format
    print(f"{hours:02}:{minutes:02}:{second:02} seconds left")
    
    # Clear the screen (works on most systems)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Wait for 1 second
    time.sleep(1)

# When the countdown reaches 0
print("Time's up!")
print(f"The countdown timer was set to {my_time} seconds.")
breakdown ={
    "second" : second,
    "minutes" : minutes,
    "hours" : hours
}


 