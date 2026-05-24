# CODSOFT - Artificial Intelligence Internship 🤖

Welcome to my repository for the **CodSoft Artificial Intelligence Internship**! This repository serves as a showcase of the practical AI applications and systems built during the internship program. It covers core concepts in Natural Language Processing (NLP), Game Theory, and Computer Vision.

---

## 📂 Repository Structure

The project code is organized by tasks as outlined in the internship requirements:

```text
CODSOFT/
├── Task_1_Rule_Based_Chatbot/
│   ├── chatbot.py
│   └── README.md (Optional task overview)
├── Task_2_Tic_Tac_Toe_AI/
│   ├── tictactoe_ai.py
│   └── README.md
└── Task_3_Image_Captioning/
    ├── image_captioning.py
    └── README.md

🚀 Completed Tasks Overview
🔹 Task 1: Chatbot with Rule-Based Responses
Description: A conversational assistant (RuleBot) that interacts with users based on predefined rules and pattern-matching techniques.

Core Technologies: Python, Regular Expressions (re), random, datetime.

Key Features:

Uses advanced regex word-boundary patterns to capture multiple conversational intents (Greetings, Name queries, Creator info, and Wellness questions).

Dynamic functionality including real-time system clock fetching (datetime) and contextual responses.

Robust input fallback handling when no rule conditions are triggered.

🔹 Task 2: Tic-Tac-Toe AI (Unbeatable)
Description: An AI game agent that plays a classic game of Tic-Tac-Toe against a human player using an adversarial search algorithm.

Core Technologies: Python, math, os.

Key Features:

Powered by the Minimax Algorithm paired with Alpha-Beta Pruning to drastically optimize the game tree search space.

Fully unbeatable logic; the AI plays perfectly, forcing either an AI win or a hard-fought draw.

Clear terminal-based UI with real-time rendering, an intuitive position coordinate guide, and dynamic board updates.

🔹 Task 3: Image Captioning AI
Description: A pipeline combining Computer Vision (CV) and simple Natural Language Generation (NLG) to automatically generate descriptive text captions for input images.

Core Technologies: Python, PyTorch/Torchvision (ResNet-50), urllib.

Key Features:

Leverages a pre-trained ResNet-50 deep learning network architecture to parse feature maps and extract top class-label predictions.

Zero heavy model download weights required at startup (~100 MB cached runtime asset footprint).

Passes computer vision class predictions into a custom template-driven Natural Language Generation (NLG) rule engine to construct fluent descriptive strings along with model prediction confidence parameters.

🛠️ Tech Stack & Requirements
To clone and run these projects locally, ensure you have Python 3.8+ installed.

Core Language: Python

Key Libraries Used:

torch & torchvision (For deep learning feature extraction in Task 3)

Standard library utilities: re, math, random, datetime, os, sys, argparse

📦 Getting Started
1. Clone the Repository
Bash
git clone [https://github.com/nishchalsoni27/CODSOFT](https://github.com/nishchalsoni27/CODSOFT)
cd CODSOFT
2. Install Dependencies
Bash
pip install torch torchvision
3. Run the Applications
To run the Rule-Based Chatbot:

Bash
python Task_1_Rule_Based_Chatbot/chatbot.py
To play against the Tic-Tac-Toe AI:

Bash
python Task_2_Tic_Tac_Toe_AI/tictactoe_ai.py
To run the Image Captioning AI:

Bash
python Task_3_Image_Captioning/image_captioning.py --image "path/to/your/image.jpg"
🎓 Acknowledgments
Special thanks to CodSoft for providing this structured learning framework and internship platform to explore practical implementations of artificial intelligence.

Developed with 💻 by Nishchal Soni
