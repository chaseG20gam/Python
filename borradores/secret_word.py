def set_secret():
    secret_word = str(input("Enter the secret word: "))
    while secret_word == "":
        print("Secret word cannot be empty. Please try again.")
        secret_word = str(input("Enter the secret word: "))
    print(f"Secret word set successfully. {secret_word}")
    return secret_word

def guess_letter(secret_word, test_letter):
    letter_in_word = test_letter in secret_word
    while not letter_in_word:
        print(f"The letter '{test_letter}' is not in the secret word.")
        test_letter = input("Try again. Enter a letter: ")
        letter_in_word = test_letter in secret_word
        
    print(f"Congratulations! The letter '{test_letter}' is in the secret word.")

def guess_word(secret_word, test_word):
    word_correct = test_word == secret_word
    while not word_correct:
        print(f"The word '{test_word}' is not the secret word.")
        test_word = input("Try again. Enter a word: ")
        word_correct = test_word == secret_word
        
    print(f"Congratulations! The word '{test_word}' is the secret word.")
    
def main():
    print("Letter and Word Guessing Game")
    secret_word = set_secret()
    
    test_letter = input("Enter a letter to test: ")
    guess_letter(secret_word, test_letter)

    test_word = input("Enter a word to test: ")
    guess_word(secret_word, test_word)

if __name__ == "__main__":
    main()