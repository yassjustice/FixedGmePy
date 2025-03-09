Here are the errors I fixed:

Fixed the indentation throughout the code (although the indentation was mostly correct in the original)
Added a blank line after the import statement for better readability
Fixed the if __name__ == "__main__": line at the end:

Changed *name* to __name__
Changed "_main_" to "__main__"
Corrected the double underscores in both cases



The game logic itself was already functioning correctly. The code now properly:

Selects a random 6-letter word from the list
Handles user input validation
Tracks previously guessed letters
Updates the display based on correct guesses
Counts failed attempts
Shows win/loss messages appropriately
