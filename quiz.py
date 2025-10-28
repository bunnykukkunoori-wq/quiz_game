# quiz.py

import json
from questions import questions

# Load students data
def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save score to JSON
def save_score(name, score):
    students = load_students()
    students[name] = score
    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)

# Quiz function
def start_quiz():
    print("====== Welcome to the Quiz Game ======")
    name = input("Enter your name: ")
    score = 0

    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    print(f"\nYour final score is: {score}/{len(questions)}")
    save_score(name, score)
    print("Score saved ✅")

# Run the quiz
if __name__ == "__main__":
    start_quiz()
