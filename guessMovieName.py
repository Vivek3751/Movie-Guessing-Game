import random
import os
import time
import csv
from datetime import datetime

# ─────────────────────────────────────────
#  CSV DATA LOGGING SETUP (for QuickSight)
# ─────────────────────────────────────────
LOG_FILE = "game_log.csv"

def initialize_log():
    """Create CSV file with headers if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                "date", "time", "movie_name", "result",
                "total_guesses", "wrong_guesses", "correct_letters",
                "time_taken_seconds", "letters_wrong"
            ])

def log_game(movie, result, total_guesses, wrong_guesses_list, correct_letters_list, time_taken):
    """Save one game session's data to the CSV log."""
    now = datetime.now()
    with open(LOG_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            now.strftime("%Y-%m-%d"),           # date
            now.strftime("%H:%M:%S"),           # time
            movie,                              # movie_name
            result,                             # "WIN" or "LOSS"
            total_guesses,                      # total letter guesses made
            len(wrong_guesses_list),            # number of wrong guesses
            len(correct_letters_list),          # number of correct letters found
            round(time_taken, 2),               # seconds taken to finish
            ", ".join(wrong_guesses_list)       # which letters were wrong
        ])
    print(f"\n📊 Game data saved to '{LOG_FILE}' for QuickSight dashboard!")

# ─────────────────────────────────────────
#  GAME SETUP
# ─────────────────────────────────────────
movies = [
    "inception", "avatar", "gladiator", "interstellar", "titanic",
    "dangal", "bahubali", "shershaah", "pushpa"
]

guess_count = 0
guessed_letters = []
wrong_guesses = []
movie = random.choice(movies)

# Show user the list of movie names for 5 seconds
print("=" * 40)
print("       🎬 MOVIE GUESSING GAME 🎬")
print("=" * 40)
print("\n📋 Movies List (memorize in 5 seconds!):\n")
for each in movies:
    print("  -", each)

# Wait for 5 seconds
time.sleep(5)

# Clear console
os.system("cls" if os.name == "nt" else "clear")

# ─────────────────────────────────────────
#  DISPLAY FUNCTION
# ─────────────────────────────────────────
def display_movie_name(movie, guessed_letters):
    """Show guessed letters and blanks for unguessed ones."""
    display_name = ""
    for letter in movie:
        if letter == " ":
            display_name += "  "
        elif letter in guessed_letters:
            display_name += letter
        else:
            display_name += "_"
        display_name += " "
    return display_name.strip()

# ─────────────────────────────────────────
#  GAME START
# ─────────────────────────────────────────
initialize_log()
start_time = time.time()

print("=" * 40)
print("       🎬 MOVIE GUESSING GAME 🎬")
print("=" * 40)
print(f"\n🎯 The movie has {len(movie)} letters.")
displayed_name = display_movie_name(movie, guessed_letters)
print(f"\n --> {displayed_name}")
print(f"\n❌ Wrong guesses allowed: 7")
print("-" * 40)

# ─────────────────────────────────────────
#  GAME LOOP
# ─────────────────────────────────────────
while guess_count < 7 and "_" in displayed_name:
    guess = input("\n🔤 Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️  Invalid input. Please guess a single letter.")
        continue

    if guess in guessed_letters or guess in wrong_guesses:
        print(f"⚠️  You already guessed '{guess}'. Try another!")
        continue

    if guess in movie:
        guessed_letters.append(guess)
        print(f"✅ '{guess}' is correct!")
    else:
        wrong_guesses.append(guess)
        guess_count += 1
        print(f"❌ '{guess}' is wrong! --> Wrong: {', '.join(wrong_guesses)} ({guess_count}/7)")

    displayed_name = display_movie_name(movie, guessed_letters)
    print(f"\n --> {displayed_name}")

# ─────────────────────────────────────────
#  GAME RESULT + LOG DATA
# ─────────────────────────────────────────
time_taken = time.time() - start_time
total_guesses = len(guessed_letters) + len(wrong_guesses)

print("\n" + "=" * 40)
if "_" not in displayed_name:
    result = "WIN"
    print(f"🎉 Congratulations! You guessed the movie: {movie.upper()}")
else:
    result = "LOSS"
    print(f"💀 Game Over! The movie was: {movie.upper()}")

print(f"⏱️  Time taken: {round(time_taken, 2)} seconds")
print(f"📝 Total guesses: {total_guesses} | Wrong: {len(wrong_guesses)} | Correct letters: {len(guessed_letters)}")
print("=" * 40)

# Save game data to CSV
log_game(movie, result, total_guesses, wrong_guesses, guessed_letters, time_taken)