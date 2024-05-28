import random

def choose_word():
    words = ['python', 'hangman', 'challenge', 'programming', 'task', 'artificial','laptop','codealpha','internship','apple','banana', 'dog','cat','notebook','lemon','pizza']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    
    print("Welcome to Hangman!")
    print("You have", max_incorrect_guesses, "incorrect guesses allowed.")
    print(display_word(word, guessed_letters))
    
    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess! You have", max_incorrect_guesses - incorrect_guesses, "guesses left.")
        
        current_display = display_word(word, guessed_letters)
        print(current_display)
        
        if '_' not in current_display:
            print("Congratulations, you've won!")
            break
    else:
        print("Sorry, you've run out of guesses. The word was:", word)
    
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thank you for playing!")

hangman()




