# ============================================================
#
#   Built by: Nishchal Soni
#   Task 1 -CHATBOT WITH RULE-BASED RESPONSE
#
# ============================================================

import re
import random
from datetime import datetime


# ──────────────────────────────────────────────
#  RULE ENGINE  (pattern → responses)
# ──────────────────────────────────────────────
RULES = [
    # Greetings
    (r"\b(hi|hello|hey|howdy|sup|what'?s up)\b",
     ["Hello! 😊 How can I help you today?",
      "Hey there! What's on your mind?",
      "Hi! Nice to meet you. How can I assist?"]),

    # Name queries
    (r"\bwhat(('?s| is) your name| are you called)\b",
     ["I'm RuleBot, built by Nishchal Soni! 🤖",
      "My name is RuleBot — Nishchal Soni's creation!"]),

    # Creator / author
    (r"\b(who (made|built|created|coded|programmed) you|who('?s| is) your (creator|developer|author))\b",
     ["I was built by Nishchal Soni as part of Task 1. 👨‍💻",
      "Nishchal Soni created me! Pretty cool, right?"]),

    # How are you
    (r"\bhow (are you|r u|are u|do you do)\b",
     ["I'm doing great, thanks for asking! 😄",
      "Running perfectly — all rules firing as expected!",
      "I'm wonderful! Ready to chat."]),

    # Age
    (r"\bhow old are you\b",
     ["I was just born today — fresh out of Nishchal's editor! 🎉"]),

    # Time
    (r"\b(what(('?s| is) the time| time is it)|current time)\b",
     [f"The current time is {datetime.now().strftime('%I:%M %p')}. ⏰"]),

    # Date
    (r"\b(what(('?s| is) (today'?s? date|the date)|day is it)|current date)\b",
     [f"Today is {datetime.now().strftime('%A, %d %B %Y')}. 📅"]),

    # Weather (rule-based stub)
    (r"\b(weather|temperature|forecast)\b",
     ["I don't have live weather data, but you can check weather.com! ☀️🌧️"]),

    # Jokes
    (r"\b(tell me a joke|joke|make me laugh|funny)\b",
     ["Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
      "Why did the chatbot break up? It had too many unresolved issues! 😄",
      "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads. 🍫"]),

    # Help
    (r"\b(help|what can you do|capabilities|features)\b",
     ["I can:\n  • Answer greetings\n  • Tell you the time & date\n  • Crack jokes\n  • Answer FAQs\n  • Chat about Python!\nJust type naturally. 😊"]),

    # Python / programming
    (r"\b(python|programming|code|coding|developer)\b",
     ["Python is awesome! 🐍 It's one of the best languages for AI & chatbots.",
      "Nishchal Soni built me in Python — it's elegant and powerful!"]),

    # AI / chatbot topic
    (r"\b(artificial intelligence|ai|machine learning|nlp|chatbot)\b",
     ["AI is transforming the world! 🤖 This rule-based chatbot is a simple first step into NLP.",
      "Rule-based systems are the foundation of conversational AI. Glad you're learning!"]),

    # Goodbye
    (r"\b(bye|goodbye|see you|later|quit|exit|cya)\b",
     ["Goodbye! Have a great day! 👋",
      "See you later! It was nice chatting. 😊",
      "Bye! Come back anytime. 🤖"]),

    # Thanks
    (r"\b(thanks|thank you|thx|ty|cheers)\b",
     ["You're welcome! 😊",
      "Happy to help!",
      "Anytime! That's what I'm here for. 🤖"]),

    # Affirmations
    (r"\b(yes|yeah|yep|sure|absolutely|correct|right)\b",
     ["Great! 😊", "Awesome, let's continue!", "Perfect!"]),

    # Negations
    (r"\b(no|nope|nah|not really)\b",
     ["Alright, no worries!", "Okay, let me know if I can help with something else."]),

    # Name of user
    (r"\bmy name is (\w+)\b",
     ["Nice to meet you, {match}! 😊"]),   # uses capture group

    # Favourite colour
    (r"\b(fav(ou?rite)? colou?r|what colou?r)\b",
     ["I'm a fan of blue — it's the colour of logic! 💙"]),

    # Meaning of life
    (r"\bmeaning of life\b",
     ["42. Obviously. 😄 (And also: keep learning!)"]),

    # Default / fallback  — kept last
]

# Pre-compile patterns for efficiency
COMPILED_RULES = [(re.compile(pat, re.IGNORECASE), responses)
                  for pat, responses in RULES]


# ──────────────────────────────────────────────
#  CORE RESPONSE FUNCTION
# ──────────────────────────────────────────────
def get_response(user_input: str) -> str:
    """Match user input against rules and return an appropriate response."""
    user_input = user_input.strip()

    for pattern, responses in COMPILED_RULES:
        match = pattern.search(user_input)
        if match:
            reply = random.choice(responses)
            # Handle capture-group substitutions (e.g. user's name)
            if "{match}" in reply and match.lastindex:
                reply = reply.replace("{match}", match.group(1).capitalize())
            return reply

    # Fallback response
    fallbacks = [
        "Hmm, I'm not sure about that. Could you rephrase? 🤔",
        "I don't have a rule for that yet! Try asking something else.",
        "Interesting! But I'm just a rule-based bot — I might not know everything. 😅",
    ]
    return random.choice(fallbacks)


# ──────────────────────────────────────────────
#  MAIN LOOP
# ──────────────────────────────────────────────
def main():
    print("=" * 55)
    print("       RULE-BASED CHATBOT  🤖")
    print("       Built by  : Nishchal Soni")
    print("       Task      : Task 1 — Rule-Based Responses")
    print("=" * 55)
    print("Type 'bye' or 'quit' to exit.\n")

    exit_pattern = re.compile(r"\b(bye|goodbye|quit|exit|cya|later)\b", re.IGNORECASE)

    while True:
        try:
            user_input = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nRuleBot: Goodbye! 👋")
            break

        if not user_input:
            print("RuleBot: Please type something! 😊\n")
            continue

        response = get_response(user_input)
        print(f"RuleBot: {response}\n")

        if exit_pattern.search(user_input):
            break


if __name__ == "__main__":
    main()
