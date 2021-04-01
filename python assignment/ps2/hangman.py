# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
secret_word="abcd"
WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if i not in letters_guessed:
            return False
    return True
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    compressed_guess_string=""
    for i in secret_word:
        if i in letters_guessed:
            compressed_guess_string+=i
        else:
            compressed_guess_string+="_ "
    return compressed_guess_string
            

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_not_in_guess=""
    all_lowcase_letters=string.ascii_lowercase
    for i in all_lowcase_letters:
        if i not in letters_guessed:
            letters_not_in_guess+=i
    return letters_not_in_guess
   

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    number_of_warnings=3
    number_of_guesses=6
    letters_guessed=""
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is",len(secret_word),"letters long.")
    print("You have",number_of_warnings,"warnings left.")
    print("-----------------------------")   
    while number_of_guesses!=0 and not is_word_guessed(secret_word, letters_guessed):
    
     if number_of_warnings==0:
        number_of_warnings=3
     if number_of_guesses!=0:
        print("You have",number_of_guesses,"guesses left.")
        print("Available letters: "+get_available_letters(letters_guessed))
        guess_letter=(input("Please guess a letter: "))
        if not guess_letter.isalpha():
          print("Your in put is not a LETTER so you lose a warning")
          number_of_warnings+=-1
          guess_letter=(input("Please guess a letter: "))
        else:
         guess_letter=guess_letter.lower()
        
        if guess_letter in letters_guessed:
            number_of_warnings+=-1
            print("Oops! You've already guessed that letter. You have",number_of_warnings,"left:")
            
            if number_of_warnings==0:
               print("You have 0 warnings remaining so you lose one guess chance")
               number_of_guesses+=-1 
            get_guessed_word(secret_word, letters_guessed)
            print("-----------------------------")
        else:
            if guess_letter in secret_word:
                letters_guessed+=guess_letter
                print("Good guess: "+get_guessed_word(secret_word, letters_guessed))
                print("-----------------------------")
            else:
                letters_guessed+=guess_letter
                print("Oops! That letter is not in my word."+get_guessed_word(secret_word, letters_guessed))
                print("-----------------------------")
                number_of_guesses+=-1
     else:
         break
    if number_of_guesses==0:
      print("You lose")  
    else:             
      print("You win")        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    my_word_with_no_spaces = ''
    letters_guessed = []
    for char in my_word:
        if char != ' ':
            my_word_with_no_spaces += char
            
        if char.isalpha():
            letters_guessed.append(char)
        
    if len(my_word_with_no_spaces.strip()) != len(other_word.strip()):
        return False
    
    for i in range(len(my_word_with_no_spaces)):
        current_letter =  my_word_with_no_spaces[i]
        other_letter = other_word[i]
        if current_letter.isalpha():
            has_same_letter = current_letter == other_letter
            if not has_same_letter:
                return False
        else:
            if current_letter == '_' and other_letter in letters_guessed:
                return False
            
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matched_words = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            matched_words.append(word)
    
    if len(matched_words) > 0:
        for word in matched_words:
            print(word, end=' ')
        print()
    else:
        print('No matches found')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is {} letters long'.format(len(secret_word)))
    
    num_of_guesses_left = 6
    num_of_warnings_left = 3
    letters_guessed = []
    
    print('You have {} warnings left'.format(num_of_warnings_left))
    print('-------------')
    
    while True:
        print('You have {} guesses left'.format(num_of_guesses_left))
        print('Available letters: {}'.format(get_available_letters(letters_guessed)))
    
        letter_guessed = input('Please enter a letter: ').lower()
        guessed_word = get_guessed_word(secret_word, letters_guessed)
        
        if letter_guessed.isalpha():
            if letter_guessed not in letters_guessed:   
                letters_guessed.append(letter_guessed)
                guessed_word = get_guessed_word(secret_word, letters_guessed)
                
                if letter_guessed in secret_word:
                    print('Good guess: {}'.format(guessed_word))
                else:
                    if letter_guessed in 'aeiou':
                        num_of_guesses_left -= 2
                    else:
                        num_of_guesses_left -= 1  
                    print('Oops! That letter is not in my word: {}'.format(guessed_word))
            else:
                if num_of_warnings_left > 0:
                    num_of_warnings_left -= 1
                    print('Oops! You\'ve already guessed that letter. You now have {} warnings: {}'.format(num_of_warnings_left, guessed_word))
                else:
                    num_of_guesses_left -= 1
                    print('Oops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess: {}'.format(guessed_word))
        elif letter_guessed == '*':
            print('Possible word matches are: ')
            show_possible_matches(guessed_word)
        else:
            if num_of_warnings_left > 0:
                num_of_warnings_left -= 1
                print('Oops! That is not a valid letter. You have {} warnings left: {}'.format(num_of_warnings_left, guessed_word))
            else:
                num_of_guesses_left -= 1
                print('Oops! You\'ve already guessed that letter. You now have no warnings left so you lose one guess: {}'.format(guessed_word))
    
        print('-------------')
    
        if is_word_guessed(secret_word, letters_guessed):
            unique_letters_in_secret_word = []
            for char in secret_word:
                if char not in unique_letters_in_secret_word:
                    unique_letters_in_secret_word.append(char)
            
            print('Congratulations, you won!')
            print('Your total score for this game is {}'.format(num_of_guesses_left * len(unique_letters_in_secret_word)))
            break
    
        if num_of_guesses_left <= 0:
            print('Sorry, you ran out of guesses. The word was {}'.format(secret_word))
            break





# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
   

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
