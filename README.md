# Quiz Game — Python Project
# Overview

The Quiz Game is a simple Python console-based project designed to test the user’s general knowledge with multiple-choice questions.

It demonstrates basic Python programming concepts such as:

Conditional statements (if/else)

Loops (for, while)

User input handling

Functions and scoring systems

This project is ideal for beginners who are learning Python and want to build their first interactive program.

# Features
# 1. Multiple-Choice Questions
Each question has four options (A, B, C, D) and one correct answer.

# 2. Scoring System
The program tracks the user’s score throughout the quiz and displays the final result at the end.

# 3. Replay Option
After finishing the quiz, users can choose to play again or exit.

# 4. Input Validation
Handles invalid inputs gracefully and prompts the user to enter a valid option.

# 5. Beginner-Friendly Code
Written in a simple, readable format suitable for learning Python basics.

# Project Structure

##  Project Structure

The project is organized for readability, scalability, and maintainability.  
Below is the clean directory layout for the **Quiz Game** project:

```
quiz_game/
│
├──  src/                         # Source code directory
│   ├── quiz.py                    # Main Python script (handles game logic & user interaction)
│   ├── questions.py               # Question bank (stores quiz questions & answers)
│   └── students.json              # Player data file (stores student names, scores, or attempts)
│
├── docs/                        # Documentation folder
│   └── README.md                  # Project documentation and usage guide
│
├── assets/                      # (Optional) Folder for screenshots, sample outputs, or media
│   └── sample_output.txt          # Example of program output (optional file)
│
└──  requirements.txt             # (Optional) Python dependencies file (for future use)
```

###  Folder & File Description

| Folder/File | Description |
|--------------|-------------|
| **src/** | Contains all source code and data files for the quiz game. |
| ├── `quiz.py` | Main executable script that runs the quiz and handles user interaction. |
| ├── `questions.py` | Stores the quiz questions, options, and correct answers. |
| └── `students.json` | JSON file for storing user names and scores for persistence. |
| **docs/** | Contains documentation and guides for using or contributing to the project. |
| **assets/** | Holds screenshots, example outputs, or any other static media (optional). |
| **requirements.txt** | Used for listing external Python libraries (if needed later). |

---

###  Example Command Flow

To run the project:
```bash
cd quiz_game/src
python quiz.py
```

To view player data:
```bash
cat students.json
```

To modify questions:
```bash
nano questions.py
```

---

###  Notes
- The `students.json` file will automatically update after each quiz session.  
- `requirements.txt` can remain empty unless you add extra Python modules (e.g., `json`, `colorama`, etc.).  
- The `assets/` folder is optional — you can use it for screenshots, sample output logs, or GIF demos.  

---

# Benefits of This Structure

Clean organization — separates code, docs, and data

Reusable — easy to expand with new features

Collaborative — clear structure for multiple contributors

GitHub-friendly — looks professional and readable

# Requirements

Python 3.6 or above
(You can check using python --version or python3 --version)

# Works on:

Windows (PowerShell / CMD)

Linux / macOS terminal

VS Code or any Python IDE

# 1.Clone or Create the Project Folder

mkdir quiz_game

cd quiz_game

# 2️.Create the Script

Create a file named quiz_game.py

# 3.Run the Program

Open terminal or PowerShell in your project folder and run:

python quiz_game.py

# Sample Output
===================================

 Welcome to the Python Quiz Game!

===================================

1️.What is the capital of France?

A. Berlin

B. Paris

C. Rome

D. Madrid

Enter your answer (A/B/C/D): B

 Correct!

2️.Which programming language is known as the backbone of web development?

A. Python

B. C++

C. JavaScript

D. Java

Enter your answer (A/B/C/D): C

 Correct!

3️.Who developed Python Programming Language?

A. Dennis Ritchie

B. Guido van Rossum

C. James Gosling

D. Elon Musk

Enter your answer (A/B/C/D): A

Wrong! The correct answer was: B

 Quiz Completed! Your final score: 2/3
 
 Good job! You passed the quiz.

Do you want to play again? (yes/no): no

 Thanks for playing the Quiz Game!

# Future Enhancements

 Add question randomization

 Store user scores in a text file or database

 Add categories (Science, Geography, Tech)

 Add a timer for each question

 Create a GUI version using tkinter

# Learning Outcomes

By completing this project, you’ll understand:

How to structure Python programs

Handling user input

Using functions for modular code

Building simple games in the terminal

# Author

Author: Bunny Kukkunoori

Email: bunnykukkunoori@gmail.com

GitHub: github.com/bunnykukkunoori-wq

Project: Python Quiz Game

Version: 1.0





