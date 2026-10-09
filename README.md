# CodeOrbit_tasks
# Code Orbit Internship Tasks

This repository contains my work for the one-month internship at **Code Orbit**.

## Task List

| Task | Title | Status |
|------|-------|--------|
| 1 | Rule-Based Chatbot | ✅ Completed |
| 2 | Coming soon | ⏳ Pending |
| 3 | Coming soon | ⏳ Pending |
| 4 | Coming soon | ⏳ Pending |

---

## Task 1: Rule-Based Chatbot

A simple chatbot built in Python that responds to user input using predefined rules and regex pattern matching.

### Features
- Handles greetings (hi, hello, good morning)
- Answers common questions (name, how are you, what can you do)
- Tells the current time and date
- Tells jokes and replies to thanks and feelings
- Gives a fallback response for unknown input
- Ends the chat on `bye`, `exit` or `quit`

### How It Works
1. The user's input is cleaned (lowercased, punctuation removed).
2. It is checked against a list of rules, top to bottom, using regular expressions.
3. The first matching rule is used, and one of its replies is picked at random.
4. If no rule matches, a fallback response is returned.

### Requirements
- Python 3.x
- No external libraries (uses only `re`, `random` and `datetime`)

### How to Run
```bash
python chatbot.py
```

### Sample Output
```
OrbitBot: Hi! I'm OrbitBot. Type 'bye' to exit.
You: hello
OrbitBot: Hey! What's up?
You: what is your name?
OrbitBot: I'm OrbitBot, a simple rule-based chatbot.
You: asdfgh
OrbitBot: Hmm, I'm not sure how to answer that. Try asking something else!
You: bye
OrbitBot: Bye! Talk to you soon!
```

### Project Structure
```
├── chatbot.py
└── README.md
```

---

## What I Learned
- Pattern matching with Python's `re` module
- Structuring decision logic with rules and conditions
- Writing clean, well-commented code
- Handling user input and edge cases


---
*Made as part of the Code Orbit Internship.*
