import random

# List of words for the game
word_list = ['python', 'hangman', 'challenge', 'developer', 'openai', 'function', 'variable', 'matrix', 'algotithm', 'programming', 'keyboard', 'mouse', 'monitor', 'computer', 'internet', 'software', 'hardware', 'database', 'quadratic', 'equation', 'solution', 'derivative', 'integral', 'calculud', 'geometry', 'algebra', 'trigonometry', 'statistics', 'provbability', 'analysis', 'engineering', 'mathematics', 'science', 'technology', 'engineer', 'scientist', 'physicist', 'chemist', 'biologist', 'astronomer', 'geologist', 'biochemist', 'biophysicist', 'robotics', 'differential', 'probability', 'statistics', 'geometry', 'inverse', 'vector', 'tensor', 'determinant', 'relation', 'function']

# Choose a random word
chosen_word = random.choice(word_list).lower()
word_display = ['_'] * len(chosen_word)
guessed_letters = set()
max_tries = 9
tries = 0
stages_threats = ['The Base has been Set Up','The Wooden Beam has been Set Up','The Cross-Piece has been Set Up',"""

The Rope has been Set Up

    😈 The Gallow has been constructed"""]

# Hangman stages for visual representation
hangman_stages = [
    """
    """,
    """
       =========
    """,
    """
            |
            |
            |
            |
            |
       =========
    """,
    """
        -----
            |
            |
            |
            |
            |
       =========
    """,
    """
        -----
        |   |
            |
            |
            |
            |
       =========
    """,
    """
        -----
        |   |
        O   |
            |
            |
            |
       =========
    """,
    """
        -----
        |   |
        O   |
        |   |
            |
            |
       =========
    """,
    """
        -----
        |   |
        O   |
       /|   |
            |
            |
       =========
    """,
    """
        -----
        |   |
        O   |
       /|\\  |
            |
            |
       =========
    """,
    """
        -----
        |   |
        O   |
       /|\\  |
       /    |
            |
       =========
    """,
    """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
       =========
       😈You're Dead
    """
]

print("\n\n     🎮 Welcome to Hangman!")
print("\n############################################################################################################\n")
print(hangman_stages[0])
print('😈 Ready to Die')

# Game loop
while tries < max_tries and '_' in word_display:
    print("\n   Current word: ", ' '.join(word_display))
    guess = input("     Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("   ❗ Please enter a single valid letter.")
        continue

    if guess in guessed_letters:
        print("   ⚠️ You already guessed that letter.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess
        print("\n   ✅ Correct!\n")
        print("\n############################################################################################################\n")
        print(hangman_stages[tries])
    else:
        tries += 1
        print("\n   ❌ Wrong! Tries left:", max_tries - tries, '\n')
        print("\n############################################################################################################\n")
        print(hangman_stages[tries])
        try:
            print(stages_threats[tries-1])
        except:
            pass

# Final result
if '_' not in word_display:
    print("   🎉 You won! The word was:", chosen_word)
else:
    print("   💀 Game over! The word was:", chosen_word)

print("\n\n")