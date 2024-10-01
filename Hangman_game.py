import random
import Stages 

def hangman():
    word_list = ['python', 'hangman', 'programming', 'challenge', 'developer','Codealpha']
    chosen_word = random.choice(word_list)
    guessed_letters = []
    attempts = 6
    word_completion = "_" * len(chosen_word)

    print("Welcome to Hangman!")
    print(Stages.stages[attempts])
    print("_ " * len(chosen_word))
    
    while attempts > 0 and "_" in word_completion:
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        elif guess not in chosen_word:
            pass
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
            guessed_letters.append(guess)
        else:
            guessed_letters.append(guess)
            word_completion = ''.join([letter if letter in guessed_letters else '_' for letter in chosen_word])
            print(f"Good guess! Current word: {' '.join(word_completion)}")

        print(Stages.stages[attempts])
        print("\nCurrent word: " + ' '.join(word_completion))
    
    if "_" not in word_completion:
        print("Congratulations! You've guessed the word:", chosen_word)
    else:
        print(Stages.stages[attempts])
        print("Game over! The word was:", chosen_word)
    print(Stages.stages[attempts])
if __name__ == "__main__":
    hangman()
