# 🤖 Rule-Based Chatbot
**Task 1 — Chatbot with Rule-Based Responses**
Built by **Nishchal Soni**

---

## 📖 Overview

This is a simple command-line chatbot written in **pure Python** (no external libraries needed). It responds to user messages using **predefined rules** — each rule is a regular expression pattern paired with one or more possible replies. When you type a message, the bot scans through its rules, finds the first match, and returns a randomly chosen response from that rule's response pool.

This project demonstrates:
- Pattern matching using Python's `re` module
- If-else style rule engines
- Basic conversation flow & NLP concepts
- Capture groups for personalised replies

---

## 📁 File Structure

```
📦 project/
 ┣ 📄 chatbot_nishchal.py   ← Main chatbot script
 ┗ 📄 README.md             ← This file
```

---

## ⚙️ Requirements

- **Python 3.6+**
- No third-party libraries — uses only the Python standard library (`re`, `random`, `datetime`)

Check your Python version:
```bash
python3 --version
```

---

## 🚀 How to Run

**Step 1 — Download the file**

Save `chatbot_nishchal.py` to any folder on your computer.

**Step 2 — Open a terminal**

Navigate to the folder where you saved the file:
```bash
cd path/to/your/folder
```

**Step 3 — Run the chatbot**
```bash
python3 chatbot_nishchal.py
```

On Windows you may use:
```bash
python chatbot_nishchal.py
```

**Step 4 — Start chatting!**

You'll see the welcome banner and a `You:` prompt. Just type naturally and press **Enter**.

---

## 💬 What You Can Say

| What you type                        | What the bot does                        |
|--------------------------------------|------------------------------------------|
| `hi` / `hello` / `hey`              | Greets you back                          |
| `what is your name`                  | Tells you its name (RuleBot)             |
| `who made you`                       | Credits Nishchal Soni                    |
| `how are you`                        | Responds with its status                 |
| `what is the time`                   | Prints the current system time           |
| `what is today's date`               | Prints today's date                      |
| `tell me a joke`                     | Cracks a programming joke 😄            |
| `what can you do` / `help`           | Lists all capabilities                   |
| `my name is <your name>`             | Greets you by name (capture group)       |
| `python` / `coding` / `programming`  | Talks about Python                       |
| `AI` / `chatbot` / `NLP`            | Discusses artificial intelligence        |
| `weather`                            | Directs you to a weather site            |
| `meaning of life`                    | Answers with 42 😄                      |
| `thanks` / `thank you`              | Acknowledges your thanks                 |
| `bye` / `quit` / `exit`             | Ends the conversation and exits          |
| *(anything else)*                    | Returns a friendly fallback message      |

---

## 🔍 How It Works — Step by Step

```
User types a message
        │
        ▼
Input is passed to get_response()
        │
        ▼
Loop through COMPILED_RULES list
        │
        ├─ re.search(pattern, input)  ← checks each rule
        │         │
        │    Match found?
        │    YES → pick a random reply from that rule's list
        │           └─ if reply has {match}, substitute capture group
        │    NO  → try next rule
        │
        ▼
No rules matched? → return a random fallback message
        │
        ▼
Print reply to terminal
```

---

## 🧠 Code Architecture

### 1. The Rules List — `RULES`
Each entry is a tuple:
```python
(r"regex pattern", ["response 1", "response 2", ...])
```
Rules are checked **in order** — the first match wins, so more specific rules should come before general ones.

### 2. Pre-compiled Patterns — `COMPILED_RULES`
```python
COMPILED_RULES = [(re.compile(pat, re.IGNORECASE), responses)
                  for pat, responses in RULES]
```
Patterns are compiled once at startup using `re.IGNORECASE` so matching is **case-insensitive** and fast.

### 3. The Response Function — `get_response()`
```python
def get_response(user_input: str) -> str:
    for pattern, responses in COMPILED_RULES:
        match = pattern.search(user_input)
        if match:
            reply = random.choice(responses)
            ...
            return reply
    return random.choice(fallbacks)
```

### 4. The Main Loop — `main()`
Keeps reading input from the user until a goodbye word is detected or `Ctrl+C` is pressed.

---

## ➕ How to Add Your Own Rules

Open `chatbot_nishchal.py` and add a new tuple inside the `RULES` list **before the last entry**:

```python
# Example: respond to questions about food
(r"\b(food|hungry|eat|pizza|burger)\b",
 ["I wish I could eat! 🍕 What's your favourite food?",
  "Food sounds great! I'm on a strict data diet though. 😄"]),
```

**Tips:**
- Use `\b` (word boundary) to avoid partial word matches.
- Add multiple strings in the response list for variety — one is chosen at random.
- Keep the more specific patterns near the **top** of the list.

---

## 🛑 How to Exit

Type any of the following and press Enter:
```
bye   |   goodbye   |   quit   |   exit   |   cya   |   later
```
Or press **Ctrl + C** at any time.

---

## 📌 Example Session

```
=======================================================
       RULE-BASED CHATBOT  🤖
       Built by  : Nishchal Soni
       Task      : Task 1 — Rule-Based Responses
=======================================================
Type 'bye' or 'quit' to exit.

You: hello
RuleBot: Hey there! What's on your mind?

You: what is your name
RuleBot: I'm RuleBot, built by Nishchal Soni! 🤖

You: my name is Alex
RuleBot: Nice to meet you, Alex! 😊

You: tell me a joke
RuleBot: Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂

You: what is the time
RuleBot: The current time is 10:30 PM. ⏰

You: bye
RuleBot: Goodbye! Have a great day! 👋
```

---

## 📚 Concepts Learned

| Concept | Where Used |
|---|---|
| Regular Expressions (`re`) | Pattern matching for every rule |
| `re.IGNORECASE` flag | Case-insensitive matching |
| Capture Groups `(\w+)` | Extracting the user's name |
| `random.choice()` | Picking varied responses |
| `datetime` module | Live time and date responses |
| While loop | Keeping the conversation running |
| Exception handling | Graceful exit on `Ctrl+C` |

---

## 👨‍💻 Author

**Nishchal Soni**
Task 1 — Chatbot with Rule-Based Responses
