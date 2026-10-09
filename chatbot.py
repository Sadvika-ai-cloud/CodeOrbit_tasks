"""
Rule-Based Chatbot
Task 1 - Code Orbit Internship

How it works (big picture):
1. The bot reads what the user types.
2. It cleans the text (lowercase, remove extra spaces/punctuation).
3. It checks the text against a list of RULES, from top to bottom.
   Each rule has keywords/patterns and a list of possible replies.
4. The FIRST rule whose pattern matches is used, and the bot picks one
   of its replies at random.
5. If no rule matches, the bot gives a FALLBACK response.
"""

import random
import re
from datetime import datetime

BOT_NAME = "OrbitBot"

# ---------------------------------------------------------------------------
# RULES: each rule is (list_of_regex_patterns, list_of_possible_replies)
#
# - Patterns use regular expressions (re module).
# - \b means "word boundary", so "hi" matches "hi there" but NOT "this".
# - Order matters: the bot checks rules from top to bottom and stops at the
#   first match. More specific rules go first, general ones later.
# ---------------------------------------------------------------------------
RULES = [
    # Goodbye rule (checked first so "bye" always ends the chat properly)
    (
        [r"\bbye\b", r"\bgoodbye\b", r"\bsee you\b", r"\bexit\b", r"\bquit\b"],
        ["Goodbye! Have a great day!", "Bye! Talk to you soon!"],
    ),
    # Greetings
    (
        [r"\bhi\b", r"\bhello\b", r"\bhey\b", r"\bgood (morning|afternoon|evening)\b"],
        ["Hello! How can I help you today?", "Hi there! Nice to see you.", "Hey! What's up?"],
    ),
    # Asking about the bot's well-being
    (
        [r"\bhow are you\b", r"\bhow('s| is) it going\b", r"\bwhat'?s up\b"],
        ["I'm doing great, thanks for asking! How about you?",
         "All good here! How are you?"],
    ),
    # Asking the bot's name
    (
        [r"\byour name\b", r"\bwho are you\b"],
        [f"I'm {BOT_NAME}, a simple rule-based chatbot."],
    ),
    # Asking what the bot can do
    (
        [r"\bwhat can you do\b", r"\bhelp\b", r"\bfeatures\b"],
        ["I can greet you, tell you the time or date, tell a joke, "
         "and chat about simple things. Try asking me something!"],
    ),
    # Time
    (
        [r"\btime\b"],
        ["TIME"],  # special marker, replaced with the real time below
    ),
    # Date
    (
        [r"\bdate\b", r"\btoday\b", r"\bday is it\b"],
        ["DATE"],  # special marker, replaced with the real date below
    ),
    # Joke
    (
        [r"\bjoke\b", r"\bfunny\b"],
        ["Why do programmers prefer dark mode? Because light attracts bugs!",
         "Why did the Python programmer wear glasses? Because he couldn't C!"],
    ),
    # Thanks
    (
        [r"\bthank(s| you)\b"],
        ["You're welcome!", "No problem, happy to help!"],
    ),
    # Feelings (positive / negative)
    (
        [r"\b(i am|i'm|im) (good|fine|great|happy|okay|ok)\b"],
        ["That's wonderful to hear!", "Glad you're doing well!"],
    ),
    (
        [r"\b(i am|i'm|im) (sad|bad|tired|upset|not good)\b"],
        ["I'm sorry to hear that. I hope things get better soon!"],
    ),
]

# Used when NO rule matches the user's input
FALLBACK_REPLIES = [
    "Sorry, I didn't understand that. Can you rephrase?",
    "Hmm, I'm not sure how to answer that. Try asking something else!",
    "I'm still learning. Could you say that in a different way?",
]


def clean_text(text):
    """Lowercase the text and strip extra spaces so matching is easier."""
    text = text.lower().strip()
    # Remove punctuation except apostrophes (so "what's" still works)
    text = re.sub(r"[^\w\s']", "", text)
    return text


def get_response(user_input):
    """Decide the bot's reply by checking the rules one by one."""
    text = clean_text(user_input)

    # Empty input -> ask the user to type something
    if not text:
        return "Please type something so I can respond."

    # Go through each rule in order
    for patterns, replies in RULES:
        for pattern in patterns:
            if re.search(pattern, text):
                reply = random.choice(replies)
                # Handle special dynamic replies
                if reply == "TIME":
                    return "The current time is " + datetime.now().strftime("%I:%M %p")
                if reply == "DATE":
                    return "Today's date is " + datetime.now().strftime("%d %B %Y")
                return reply

    # No rule matched -> fallback response
    return random.choice(FALLBACK_REPLIES)


def is_goodbye(user_input):
    """Check if the user wants to end the conversation."""
    return bool(re.search(r"\b(bye|goodbye|exit|quit|see you)\b", clean_text(user_input)))


def main():
    print(f"{BOT_NAME}: Hi! I'm {BOT_NAME}. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        print(f"{BOT_NAME}: {get_response(user_input)}")
        if is_goodbye(user_input):
            break


if __name__ == "__main__":
    main()
