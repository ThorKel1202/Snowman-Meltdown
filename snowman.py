import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___
     /___\\
     (o o)
     ( : )
     ( : )
     """,
     # Stage 1: Bottom part starts melting
     """
      ___
     /___\\
     (o o)
     ( : )
     """,
     # Stage 2: Only the head remains
     """
      ___
     /___\\
     (o o)
     """,
     # Stage 3: Snowman completely melted
     """
      ___
     /___\\
     """
 ]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def play_game():
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print("Secret word selected: " + secret_word)  # for testing, later remove this line
    number_of_wrong = 0
    number_of_correct = 0
    
    while True:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        if guess in secret_word:
            print("Correct!")
            secret_word = secret_word.replace(guess, "", 1)
            if len(secret_word) == 0:
                print("Congratulations, you saved the snowman!")
                break
            else:
                continue
            
        else:
            print("Wrong!")
            number_of_wrong += 1
            if number_of_wrong >= 4:
                print(f"Game Over! The word was: {secret_word}")
                break
            else:
                continue
                




if __name__ == "__main__":
    play_game()
    