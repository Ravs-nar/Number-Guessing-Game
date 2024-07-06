"""
Data Analysis Techdegree
Project 1 - A Number Guessing Game
--------------------------------
"""
# Import the random and statistics modules.
import random
import statistics



# Create the start_game function.
# Write your code inside this function.

def start_game():
    print("Welcome to the Number Guessing Game")  #1. Display an intro/welcome message to the player.
    winning_number = random.randint(1,10)          #2. Store a random number as the answer/solution.
    guess = None
    guess_count = 0
    attempts_list = [] #Initialize an empty list to store attempts
    

    def record_attempts(attempt_trys, attempt_number):
        attempts_list.append(guess_count) #Function to record attempts

      

    while guess != winning_number:
        try:
            guess = int(input("Enter your guess: "))            #3. Continuously prompt the player for a guess.
            guess_count += 1 #initialize a counter variable 
            if guess > winning_number:                          #a. If the guess is greater than the solution, display to the player "It's lower".
                print("Its lower")
            elif guess < winning_number:                        #b. If the guess is less than the solution, display to the player "It's higher".
                print("It's higher")
                record_attempts(guess_count,attempts_list)
            else:                                               #4. Once the guess is correct, stop looping, inform the user they "Got it" and store the number of guesses it took in a list.
                average = statistics.mean(attempts_list)
                median_attempts = statistics.median(attempts_list)
                mode_attempts = statistics.mode(attempts_list)
                print("Congrations! You guessed the correct number. ")                          #   5. Display the following data to the player
                print("It took you {} attempts to get the correct answer".format(guess_count)) #a. How many attempts it took them to get the correct number in this game
                print(attempts_list)
                print("The mean of your attempts list is: {}".format(average))           #b. The mean of the saved attempts list
                print("The median of your attempts list is:{}".format(median_attempts))  #c. The median of the saved attempts list
                print("The mode of your attempts list is:{}".format(mode_attempts))      #d. The mode of the saved attempts list
                play_again = input("Would you like to play again?")
                while True:
                    start_game()  
                    if play_again == "yes":          #6. Prompt the player to play again
                        continue                    #a. If they decide to play again, start the game loop over.
                    elif play_again == "no":
                        print("Thank you for playing")
                        break                       #b. If they decide to quit, show them a goodbye message.
                    else:
                        print("Invalid entry. Exiting the game.")
                        break
               

        except ValueError:
            print("Please enter a valid integer.")

            
start_game()    # Kick off the program by calling the start_game function.
    




