# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ x] Describe the game's purpose. This Game is an AI guessing game that requests the player guess a number between 1 and 100 against the 'mind' of the game. Each time a player loses, points are deducted. Each player receives 7 tries. After 7 failed attempts, the player loses. 
- [x ] Detail which bugs you found.
- [ x] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Scroll to the bottom of the screen and select a number between 1 and 100.
2. Click the "Submit Guess" button. 
3. A green message will appear at the bottom of the screen telling you if your guess was correct or not. 
4. <!-- Describe this step --> If you've tried 7 times, please select "New Game" to play again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
#======================================================== test session starts =========================================================
platform linux -- Python 3.14.7, pytest-9.1.1, pluggy-1.6.0
rootdir: /workspaces/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.15.1
collected 11 items                                                                                                                   

tests/test_game_logic.py ...........                                                                                           [100%]

========================================================= 11 passed in 0.16s =========================================================

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
