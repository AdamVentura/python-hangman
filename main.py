# Adam Ventura 3/30/2022
# The overall purpose of the program is to mimic the typical hand drawn game of hangman. 
# The program does this by first drawing underscores that represent letters in the word and then drawing a “hanger” which will hang the hangman. 
# The program then allows users to guess the word letter by letter by pressing letter keys. 
# If the letter guessed is in the word, the letter will display over the underscore in green to indicate which letter in the word it is. 
# If the guess is incorrect, the guessed letter will display to the left of the hanger in red and will draw the body part that corresponds with the amount of incorrect guesses they have had. 
# The user may have up to 5 incorrect guesses. 
# If they reach 6 incorrect guesses, the last body part of the hangman will be drawn and a message saying the game is over as well as the correct word will be displayed to the user. 
# The program works as expected and does not produce bugs unless they are intentionally triggered through pressing multiple keys at once or not waiting for the turtle to finish drawing before pressing a key again.
# These bugs are due to the nature of how the event listener and key handler works and would require an alternate method of getting letter guesses to be debugged.
# I cannot find the original source to the words file I am using. I have used it for other projects and have despite great effort have not been able to find where I originally got it from.


from words import word_list
import random as rand
import turtle as trtl
import time

# Initialize Turtle Screen
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
# Initialize turtle objects
letter_drawer = trtl.Turtle()
hangman_drawer = trtl.Turtle()
# Initialize attributes of turtles
# Initialize pen sizes
hangman_drawer.pensize(3)
letter_drawer.pensize(3)
# Slow down the turtles to show drawing effect
hangman_drawer.speed(4)
letter_drawer.speed(3)
# Randomly select a word from the word list
word = rand.choice(word_list)
word_length = len(word)
# Split word into list of letters
global letters 
letters = list(word)
# Intialize a list of all the letters in the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# Initialize global variable for the amount of incorrect guesses
incorrect_guesses = 0




#---------------Define Functions--------------

def draw_underscores(letters, word_length, letter_drawer):
    # Start with penup
    letter_drawer.penup()
    # Dependent on the number of letters in the word determine where 
    # the letter drawer needs to start drawing underscores to center it under the hanger
    if word_length <= 3:
        letter_drawer.goto(-40, -50)
    elif word_length <= 5: 
        letter_drawer.goto(-60, -50)
    elif word_length <= 7: 
        letter_drawer.goto(-90, -50)
    elif word_length <= 9: 
        letter_drawer.goto(-120, -50)
    elif word_length <= 11: 
        letter_drawer.goto(-150, -50)
    elif word_length <= 13: 
        letter_drawer.goto(-180, -50)
    elif word_length <= 15: 
        letter_drawer.goto(-210, -50)
    elif word_length > 15: 
        letter_drawer.goto(-240, -50)
    # For each letter in the word draw an underscore 
    for letter in letters:
        #Draw underscore
        letter_drawer.pendown()
        letter_drawer.forward(20)
        # Draw space
        letter_drawer.penup()
        letter_drawer.forward(10)



# Define function for drawing the hanger that will hang the hangman
def draw_hanger():
    hangman_drawer.penup()
    # Go to center of screen
    hangman_drawer.goto(0,0)
    # Draw hanger base
    hangman_drawer.pendown()
    hangman_drawer.forward(40)
    hangman_drawer.backward(80)
    hangman_drawer.forward(40)
    # Draw vertical part of hanger
    hangman_drawer.left(90)
    hangman_drawer.forward(150)
    # Draw hanger
    hangman_drawer.right(90)
    hangman_drawer.forward(40)
    hangman_drawer.right(90)
    hangman_drawer.forward(50)
    

def handle_guess(key):
    global incorrect_guesses
    letter_order = 1
    # If the key is in list of letters of the randomly generated word, the guess is correct
    for letter in letters:
        if letter == key:
            # Capitalize letter
            letter_capitalized = key.upper()
            # Determine the coordinates of the underscore in which the letter should appear above
            if word_length <= 3:
                first_underscore_x = -40
            elif word_length <= 5: 
                first_underscore_x = -60
            elif word_length <= 7: 
                first_underscore_x = -90
            elif word_length <= 9: 
                first_underscore_x  = -120
            elif word_length <= 11: 
                first_underscore_x = -150
            elif word_length <= 13: 
                first_underscore_x = -180
            elif word_length <= 15: 
                first_underscore_x = -210
            elif word_length > 15: 
                first_underscore_x = -240
            # Based on which letter in the word the guess is, add a certain amount of x-coordinates to the first underscore
            if letter_order == 1:
                x_coordinate = first_underscore_x + 10
            else:
                # Use this formula to determine the coordinates of the underscore the guessed letter should appear above
                x_coordinate = (((letter_order - 1) * 30) + 10) + first_underscore_x
            letter_drawer.penup()
            letter_drawer.goto(x_coordinate, -50)
            # Change color of pen so correct colors are green
            letter_drawer.pencolor('green')
            # Write letter to screen
            letter_drawer.write(letter_capitalized, font = ("Arial", 16, "bold"), align = 'center')
        # Increment the letter order by 1 before looping again
        letter_order += 1
    # If the key pressed is not a letter in the word, display letter in red and draw part of hangman
    if key not in letters:
        # Increment the amount of incorrect guesses
        incorrect_guesses += 1
        # Display the incorrect letter in red on the screen
        display_incorrect_letter(key, incorrect_guesses)
        # Draw body part based on amount of incorrect guesses
        draw_body_part()
        # If the amount of incorrect guesses is equal to 6, then the game is over
        if incorrect_guesses == 6:
            game_over()
            display_correct_word()
        

# Define function to display incorrect letters in rows
def display_incorrect_letter(key, incorrect_guesses):
    # Start with penup before moving to correct location
    letter_drawer.penup()
    # Based on how many letters they already have guessed incorrectly, go to that location
    if incorrect_guesses == 1:
        letter_drawer.goto(200, 100)
    elif incorrect_guesses == 2:
        letter_drawer.goto(225, 100)
    elif incorrect_guesses == 3:
        letter_drawer.goto(250, 100)
    elif incorrect_guesses == 4:
        letter_drawer.goto(200, 50)
    elif incorrect_guesses == 5:
        letter_drawer.goto(225, 50)
    elif incorrect_guesses == 6:
        letter_drawer.goto(250, 50)
    # Write the incorrect guess to the screen in red
    letter_drawer.pendown()
    letter_drawer.color("red")
    letter_drawer.write(key.upper(), font = ("Arial", 16, "bold"), align = 'center')




# Define function for drawing the body part
def draw_body_part():
    # Make speed of ha
    # Draw the head after one incorrect guess
    if incorrect_guesses == 1:
        hangman_drawer.penup()
        hangman_drawer.goto(20, 80)
        hangman_drawer.pendown()
        hangman_drawer.circle(20)
    # Draw the body of the hangman after two incorrect guesses
    if incorrect_guesses == 2:
        hangman_drawer.penup()
        hangman_drawer.goto(40, 60)
        hangman_drawer.setheading(-90)
        hangman_drawer.pendown()
        hangman_drawer.forward(30)
    # Draw the left arm
    if incorrect_guesses == 3:
        hangman_drawer.penup()
        hangman_drawer.goto(40, 55)
        hangman_drawer.pendown()
        hangman_drawer.setheading(240)
        hangman_drawer.forward(20)

    # Draw the right arm
    if incorrect_guesses == 4:
        hangman_drawer.penup()
        hangman_drawer.goto(40, 55)
        hangman_drawer.pendown()
        hangman_drawer.setheading(-60)
        hangman_drawer.forward(20)

    # Draw the left leg
    if incorrect_guesses == 5:
        hangman_drawer.penup()
        hangman_drawer.goto(40, 30)
        hangman_drawer.pendown()
        hangman_drawer.setheading(240)
        hangman_drawer.forward(20)

    # Draw the right leg
    if incorrect_guesses == 6:
        hangman_drawer.penup()
        hangman_drawer.goto(40, 30)
        hangman_drawer.pendown()
        hangman_drawer.setheading(-60)
        hangman_drawer.forward(20)



# Define function to display the correct word
def display_correct_word():
    # Display the correct word under the game
    letter_drawer.penup()
    letter_drawer.goto(0, -200)
    letter_drawer.color("black")
    # Use f-string and write function to display correct word
    letter_drawer.write(f"The correct word is {word}", font = ("Arial", 32, "bold"), align = 'center')
        
# Define function to display that the game is over and ask user if they would like to play again
def game_over():
    # Display Game Over above game
    letter_drawer.penup()
    letter_drawer.goto(0, 200)
    letter_drawer.color("black")
    letter_drawer.write("GAME OVER!", font = ("Arial", 64, "bold"), align = 'center')




    
    


#----------Call functions----------
# Hide turtles
letter_drawer.hideturtle()
hangman_drawer.hideturtle()
draw_underscores(letters, word_length, letter_drawer)
draw_hanger()

wn.listen()

# Listen for keypresses by making instances of an onkeypress handler for each letter in the alphabet through using a for loop that iterates through a list of the letters in the alphabet
for letter in alphabet:
    # Use a lambda so that we can pass the key to the function the handler is calling
    wn.onkeypress(lambda key = letter: handle_guess(key), letter)

# Allows screen to persist
wn.mainloop()