# 🧠 Quiz Game (Python)

A simple **command-line Quiz Game** built in Python .  
This project asks multiple-choice questions, checks your answers, tracks your score, and automatically saves results to a JSON file for future reference.

---

## ✨ Features

- ✅ Multiple-choice questions  
- 🧾 Score tracking system  
- 💾 Auto-save player results to `students.json`  
- 📁 Loads questions from `questions.json`  
- 🧑‍💻 Beginner-friendly Python project  
- ⚙️ Easy to expand with new questions  

---

## 📂 Project Structure
quiz_game/
├── quiz_game.py # Main game logic
├── questions.json # Question bank file
├── students.json # Stores scores automatically
└── README.md # Project documentation

2️⃣ (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate   

3️⃣ Run the game
python quiz_game.py

🧩 How the Game Works
1️⃣ The game loads questions from questions.json.
2️⃣ Each question has multiple-choice answers (a, b, c, etc.).
3️⃣ You select the answer by typing the correct letter.
4️⃣ The program checks your answer and updates your score.
5️⃣ After finishing, your name and score are saved in students.json.

Future Enhancements
⏰ Add timer per question
🏆 Add leaderboard display from students.json
📊 Export results as CSV
🎨 GUI version using Tkinter

👨‍💻 Author
Bunny Kukkunoori
DevOps & Python Learner 💻
GitHub: bunnykukkunoori-wq

