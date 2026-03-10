# 🎬 Movie Guessing Game

A terminal-based Hangman-style game where you guess Bollywood & Hollywood movie names letter by letter — with built-in CSV logging for AWS QuickSight analytics.

---

## 🎮 How to Play

1. Run the script — a list of movies flashes for **5 seconds**
2. Guess one letter at a time to reveal the hidden movie title
3. You get a max of **7 wrong guesses** — good luck!

```bash
python movie_guessing_game.py
```

---

## 📊 Data Logging

Every game is saved to `game_log.csv` with: date, time, movie name, result (WIN/LOSS), total guesses, wrong guesses, correct letters, time taken, and wrong letters used.

---

## 🗂️ Movie List

`Inception`, `Avatar`, `Gladiator`, `Interstellar`, `Titanic`, `Dangal`, `Bahubali`, `Shershaah`, `Pushpa`

> Add more by editing the `movies` list in the script.

---

## 🛠️ Requirements

- Python 3.x (no external libraries needed)