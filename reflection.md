# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
#1. Corrected guess assumptions to reflect too high and too low guesses while keeping secret the same. 
#2. Added tests to check said logic. 
Corrected app.py and logic_utils to reflect corrections to lines 21-26 in app.py.
#3. Corrected scoring to reflect 100% as a final score if guessed on first attempt. 
| | | | |
| | | | |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
#I used Codepilot to help me figure out where the primary issued lied with the hint system. It worked well by identifying the error but made a suggestion that the deployment passed the pytests. However, when I ran it myself, all 11 tests passed. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

#I checkeddthe lines of code edited by commiting them, running pytests after each manual test. To start, I tested the code manually first to figure out where the bugs were. I identified the hint bug, the scoring bug, and the lack of reset once an individual won. With AI assistance I was able to correct the errors. 

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would explain that Streamlit reruns the entire apps script after a user uses a component of said code like Blockbusters asks people to rewind their VHS tapes. Only the rewind isn't after the game finishes, it's after you finish, say, a chapter. Session state allows the system to remember values between those reruns. This allows the user to maintain their place and game-based selections. 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  #Moving forward I plan to continue to create a separate log to track changes, comments, and key insights/points from projects for better reflections and review later. 
- What is one thing you would do differently next time you work with AI on a coding task?
#I would run the code separately through a IDE that I'm familiar with and outline the bugs I've personally noticed and then ask the AI to run the code and check for bugs. This allows me to test my own knowledge but use AI to finetune my knowledge. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
#This assignment solidified the importance of always checking AI generated code and responses for hallucinations. 
