import random
import os, time

#sample input movies
movies=["inception", "avatar", "gladiator", "interstellar", "titanic", "dangal", "bahubali",
"shershaah", "pushpa"]
guess_count=0
guessed_letters = []
wrong_guesses = []
movie = random.choice(movies)

#Show user the user List of Movie Names for 5 seconds then ask him to guess
print("Movies List:")
for each in movies:
   print("-",each)
   
#wait for 5 sec
time.sleep(5)

#clear Console
os.system("cls")

#function to display the guessed letters in the movie name
def display_movie_name(movie, guessed_letters):
  display_name = ""
  for letter in movie:
    if letter in guessed_letters:
      display_name += letter
    else:
      display_name += "_"
    display_name += " "
  return display_name.strip() # Return the string without extra 

print(f"The movie has {len(movie)} letters.")
displayed_name = display_movie_name(movie, guessed_letters)
print(f"--> Display: {displayed_name}")
#while loop to handle the user input letters and 
while guess_count < 7 and "_" in displayed_name:
    guess = input("Guess a letter!: ").lower()
  
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please guess a single letter.")
        continue

    if guess in guessed_letters or guess in wrong_guesses:
        print(f"You already guessed '{guess}'.")
        continue

    if guess in movie:
        guessed_letters.append(guess)
        print(f"'{guess}' is correct!")
    else:
        wrong_guesses.append(guess)
        guess_count += 1
        print(f"'{guess}' is incorrect --> Wrong guesses: {', '.join(wrong_guesses)} ({guess_count}/7)")

    displayed_name = display_movie_name(movie, guessed_letters)
    print(f"--> Display: {displayed_name}")


if "_" not in displayed_name:
    print(f"Congratulations! You guessed the movie: {movie}")
else:
    print(f"Game Over! The movie was: {movie}")

