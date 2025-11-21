def clear():
    print("\n" * 50)

def start_exam():
    questions = [
        {"question": "What is 2 + 2?", "options": ["3", "4", "5", "6"], "answer": 2},
        {"question": "What is the capital of Ethiopia?", "options": ["Addis Ababa", "Nairobi", "Cairo", "Khartoum"], "answer": 1},
        {"question": "Which language is used for programming?", "options": ["Python", "English", "Spanish", "French"], "answer": 1}
    ]
    score = 0
    for q in questions:
        clear()
        print(q["question"])
        for i, opt in enumerate(q["options"], 1):
            print(f"{i}. {opt}")
        ans = input("Answer (1-4): ")
        if ans.isdigit() and int(ans) == q["answer"]:
            score += 1
    clear()
    print("Exam Finished!")
    print(f"Your Score: {score} / {len(questions)}")

def menu():
    clear()
    print("Offline Exam System")
    print("1. Start Exam")
    print("2. Exit")
    return input("Select: ")

def main():
    while True:
        choice = menu()
        if choice == "1":
            start_exam()
            input("Press Enter to continue...")
        elif choice == "2":
            break

main()
