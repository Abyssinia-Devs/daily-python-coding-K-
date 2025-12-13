# ======================================================
# STUDENT PERFORMANCE ANALYZER SYSTEM 
# Author: Kiya
# ======================================================

MAX_SCORE = 100
PASS_MARK = 60

students = {}


# -------------------- Input Utilities --------------------
def get_valid_name(prompt):
    while True:
        name = input(prompt).strip().title()
        if name.replace(" ", ""):
            return name
        print("❗ Input cannot be empty or spaces only.")


def get_valid_subject(prompt):
    while True:
        subject = input(prompt).strip().title()
        if subject:
            return subject
        print("❗ Subject name cannot be empty.")


def get_valid_score(subject):
    while True:
        try:
            score = float(input(f"Enter score for {subject} (0-100): "))
            if 0 <= score <= MAX_SCORE:
                return score
            print("❗ Score must be between 0 and 100.")
        except ValueError:
            print("❗ Please enter a valid number.")


# -------------------- Core Logic --------------------
def calculate_average(subjects):
    return sum(subjects.values()) / len(subjects) if subjects else 0


def predict_grade(average):
    if average >= 90:
        return "A+", "Excellent performance"
    elif average >= 80:
        return "A", "Very good work"
    elif average >= 70:
        return "B", "Good, keep improving"
    elif average >= PASS_MARK:
        return "C", "Pass, but needs more effort"
    else:
        return "F", "Fail, improvement required"


# -------------------- Student Management --------------------
def add_student():
    name = get_valid_name("\nEnter student name: ")

    if name in students:
        print("❗ Student already exists.\n")
        return

    students[name] = {"subjects": {}}
    print(f"✔ Student '{name}' added successfully!\n")


def add_score():
    name = get_valid_name("\nEnter student name: ")

    if name not in students:
        print("❗ Student not found.\n")
        return

    subject = get_valid_subject("Enter subject name: ")
    score = get_valid_score(subject)

    students[name]["subjects"][subject] = score
    print(f"✔ Score updated for {name} in {subject}.\n")


# -------------------- Reporting --------------------
def show_report():
    name = get_valid_name("\nEnter student name: ")

    if name not in students:
        print("❗ Student not found.\n")
        return

    subjects = students[name]["subjects"]

    if not subjects:
        print("❗ No subjects available for this student.\n")
        return

    print("\n================ REPORT =================")
    print(f"Student: {name}")
    print("----------------------------------------")

    best = max(subjects, key=subjects.get)
    worst = min(subjects, key=subjects.get)

    for subject, score in subjects.items():
        print(f"{subject:<15}: {score}")

    avg = calculate_average(subjects)
    grade, remark = predict_grade(avg)

    print("----------------------------------------")
    print(f"Average Score : {avg:.2f}")
    print(f"Best Subject  : {best} ({subjects[best]})")
    print(f"Weakest      : {worst} ({subjects[worst]})")
    print(f"Grade        : {grade}")
    print(f"Status       : {'PASS' if avg >= PASS_MARK else 'FAIL'}")
    print(f"Remark       : {remark}")
    print("========================================\n")


def show_leaderboard():
    ranked = [
        (name, calculate_average(data["subjects"]))
        for name, data in students.items()
        if data["subjects"]
    ]

    if not ranked:
        print("\n❗ No students with scores yet.\n")
        return

    ranked.sort(key=lambda x: x[1], reverse=True)

    print("\n============== LEADERBOARD ==============")
    for idx, (name, avg) in enumerate(ranked, start=1):
        print(f"{idx}. {name:<15} - {avg:.2f}")
    print("========================================\n")


# -------------------- Main Menu --------------------
def main():
    while True:
        print("=========== STUDENT ANALYZER ===========")
        print("1. Add Student")
        print("2. Add / Update Score")
        print("3. Show Student Report")
        print("4. Show Leaderboard")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            add_score()
        elif choice == "3":
            show_report()
        elif choice == "4":
            show_leaderboard()
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("❗ Invalid choice. Try again.\n")


main()
