# Guess-the-number-game
This code is a simple number guessing game. 
The game generates a random number between 1 and 100 and prompts the user to guess the number. 
If the user's guess is incorrect, the game provides feedback about whether the guess was too high or too low and prompts the user to enter a new guess. 
If the user's guess is correct, the game congratulates the user and ends.
The code begins by generating a random number using the random.randrange function from the random module. 
It then enters a loop that continues until the user guesses the correct number. 
Inside the loop, the code prompts the user to enter a guess and uses a try-except block to catch any ValueError exceptions that may be raised if the user does not enter a whole number. 
If a ValueError is caught, the code prints an error message and prompts the user to enter a new guess.
If the user enters a valid number, the code checks whether the guess is correct. 
If the guess is too low or too high, the code provides feedback and prompts the user to enter a new guess. 
If the guess is correct, the code congratulates the user and breaks out of the loop. 
The game then ends.