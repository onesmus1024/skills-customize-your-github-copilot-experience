
# 📘 Assignment: Games in Python - Hangman

## 🎯 Objective

Build a classic Hangman game in Python. Practice string manipulation, loops, conditionals, and random selection by creating a word-guessing game.

## 📝 Tasks

### 🛠️ Task 1: Set Up the Word List and Game Loop

#### Description
Create a list of words and set up the main game loop that randomly selects a word for the player to guess.

#### Requirements
Completed program should:

- Contain a predefined list of at least 5 words
- Randomly select one word for each game session
- Start the game loop and display the initial blank word (e.g., _ _ _ _)

Example:
```python
words = ["python", "hangman", "challenge", "program", "string"]
# ...game logic...
```

### 🛠️ Task 2: Implement Guessing and Game End Logic

#### Description
Allow the player to guess letters, track their progress, and end the game with win/lose messages.

#### Requirements
Completed program should:

- Accept letter guesses from the user
- Show current progress after each guess (e.g., p _ t h o n)
- Track and display the number of incorrect guesses remaining
- End the game when the word is guessed or attempts run out
- Display a win message if the word is guessed, or a lose message if attempts are exhausted

Example output:
```
Word: _ _ _ _ _ _
Guess a letter: a
Word: _ a _ _ _ a _
Incorrect guesses left: 5
```
