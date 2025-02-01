import random  # Import the 'random' module for selecting a random word
from collections import Counter  # Import 'Counter' for efficient letter counting
from tkinter import *  # Import the tkinter library for GUI elements

class HangmanGUI:
    """
    Class to represent the Hangman game with a graphical user interface.
    """
    def __init__(self, master):
        """
        Constructor for the HangmanGUI class.

        Args:
            master: The root window of the Tkinter application.
        """
        self.master = master  # Store the root window for later use
        master.title("Hangman")  # Set the title of the main window

        # Initialize game variables
        self.word = random.choice(['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape'])  # Select a random word
        self.word_display = StringVar()  # Create a StringVar to hold the displayed word
        self.word_display.set("_ " * len(self.word))  # Initialize the displayed word with underscores
        self.guessed_letters = []  # List to store guessed letters
        self.chances = len(self.word) + 2  # Number of attempts
        self.flag = 0  # Flag to indicate if the game is won

        # Create the GUI elements
        self.create_widgets()

    def create_widgets(self):
        """
        Creates and positions the GUI elements (labels, entry, button).
        """
        Label(self.master, text="Guess the word!").grid(row=0, column=0, columnspan=2)  # Create a label for the game title
        Label(self.master, textvariable=self.word_display).grid(row=1, column=0, columnspan=2)  # Display the word
        Label(self.master, text="Enter a letter:").grid(row=2, column=0)  # Label for the letter input
        self.guess_entry = Entry(self.master)  # Create an entry field for user input
        self.guess_entry.grid(row=2, column=1)  # Position the entry field

        self.guess_button = Button(self.master, text="Guess", command=self.guess_letter)  # Create the guess button
        self.guess_button.grid(row=3, column=0, columnspan=2)  # Position the button

        self.result_label = Label(self.master, text="")  # Create a label to display game messages
        self.result_label.grid(row=4, column=0, columnspan=2)  # Position the message label

    def guess_letter(self):
        """
        Handles the player's guess.
        """
        guess = self.guess_entry.get().lower()  # Get the player's guess (lowercase)
        self.guess_entry.delete(0, END)  # Clear the entry field

        # Validate the input
        if not guess.isalpha() or len(guess) != 1:
            self.result_label.config(text="Enter only a single letter.")
            return

        if guess in self.guessed_letters:
            self.result_label.config(text="You have already guessed that letter.")
            return

        self.guessed_letters.append(guess)  # Add the guessed letter to the list
        self.chances -= 1  # Decrement the number of chances

        if guess in self.word:
            self.update_word_display()  # Update the displayed word
            if self.check_win():
                self.result_label.config(text="Congratulations, You won!")
                self.guess_button.config(state=DISABLED)  # Disable the button after winning
        else:
            if self.chances == 0:
                self.result_label.config(text=f"You lost! The word was: {self.word}")
                self.guess_button.config(state=DISABLED)  # Disable the button after losing
            else:
                self.result_label.config(text=f"Incorrect guess. Chances left: {self.chances}")

    def update_word_display(self):
        """
        Updates the displayed word with correctly guessed letters.
        """
        word_display = ""
        for char in self.word:
            if char in self.guessed_letters:
                word_display += char + " "
            else:
                word_display += "_ "
        self.word_display.set(word_display)  # Update the StringVar

    def check_win(self):
        """
        Checks if all letters in the word have been guessed.
        """
        return all(char in self.guessed_letters for char in self.word)

root = Tk()  # Create the main window
game = HangmanGUI(root)  # Create an instance of the HangmanGUI class
root.mainloop()  # Start the GUI event loop