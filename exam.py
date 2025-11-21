import json
import random
import time
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def load_quiz(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def start_exam(data):
    questions = data["questions"]
    score = 0
    total = len(questions)
    random.shuffle(questions)
    for q in questions:
        clear()
        print(q["question"])
        for i, opt in enumerate(q["options"], 1):
            print(str(i) + ". " + opt)
        ans = input("Answer (1-4): ")
        if ans.isdigit():
            if int(ans) == q["answer"]:
                score += 1
        time.sleep(0.5)
    clear()
    print("Exam Finished")
    print("Your Score:", score, "/", total)

def menu():
    clear()
    print("Offline Exam System")
    print("1. Start Exam")
    print("2. Exit")
    choice = input("Select: ")
    return choice

def main():
    if not os.path.exists("quiz.json"):
        print("quiz.json missing")
        return
    data = load_quiz("quiz.json")
    while True:
        c = menu()
        if c == "1":
            start_exam(data)
            input("Enter to continue...")
        elif c == "2":
            break

main()
