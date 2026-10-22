import random

def scramble_word(word):
    return "".join(random.sample(word, len(word)))

words = ['python', 'scramble', 'programming', 'challenge', 'function']
secret_word = random.choice(words)
scrambled = scramble_word(secret_word)

print("--- WORD SCRAMBLE GAME ---")
print(f"Scrambled word: {scrambled}")

attempts = 5
while attempts > 0:
    guess = (input(f"Guess the word: ({attempts} attempts left):")).lower().strip()
    
    if guess == secret_word:
        print("Congratulations! You guessed the word correctly! 🎉")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Incorrect guess. Try again!")
        else:
            print(f"Sorry, you've run out of attempts. The correct word was: {secret_word} 😢")
        