# ======================================================
# STUDENT PERFORMANCE ANALYZER SYSTEM 
# Author: Kiya
# ======================================================

MAX_SCORE = 100
PASS_MARK = 60

students = {}


# ---------- Utility Functions ----------
def get_valid_score(subject):
    """Keep asking until user enters a valid score."""
    while True:
        try:
            score = float(input(f"Enter score for {subject} (0-100): "))
            if 0 <= score <= MAX_SCORE:
                return score
            print("❗ Score must be between 0 and 100.")
        except ValueError:
            print("❗ Please enter a valid number.")


def calculate_average(subjects):
    """Calculate average score safely."""
    return sum(subjects.values()) / len(subjects) if subjects else 0


# ---------- Student Management ----------
def add_student():
    name = input("\nEnter student name: ").title()

    if not name:
        print("❗ Name cannot be empty.\n")
        return

    if name in students:
        print("❗ Student already exists.\n")
        return

    students[name] = {"subjects": {}}
    print(f"✔ Student '{name}' added successfully!\n")


def add_score():
    name = input("\nEnter student name: ").title()

    if name not in students:
        print("❗ Student not found.\n")
        return

    subject = input("Enter subject name: ").title()
    score = get_valid_score(subject)

    students[name]["subjects"][subject] = score
    print(f"✔ Score updated for {name} in {subject}.\n")


# ---------- Prediction Logic ----------
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


# ---------- Reporting ----------
def show_report():
    name = input("\nEnter student name: ").title()

    if name not in students:
        print("❗ Student not found.\n")
        return

    subjects = students[name]["subjects"]
    if not subjects:
        print("❗ No subjects available.\n")
        return

    print("\n================ REPORT =================")
    print(f"Student: {name}")
    print("----------------------------------------")

    best = min(subjects, key=subjects.get)
    worst = max(subjects, key=subjects.get)

    for subject, score in subjects.items():
        print(f"{subject:<15}: {score}")

    avg = calculate_average(subjects)
    grade, remark = predict_grade(avg)

    print("----------------------------------------")
    print(f"Average Score : {avg:.2f}")
    print(f"Grade         : {grade}")
    print(f"Status        : {'PASS' if avg >= PASS_MARK else 'FAIL'}")
    print(f"Remark        : {remark}")
    print("========================================\n")


def show_leaderboard():
    if not students:
        print("\n❗ No students available.\n")
        return

    print("\n============== LEADERBOARD ==============")
    ranked = sorted(
        students.items(),
        key=lambda x: calculate_average(x[1]["subjects"]),
        reverse=True
    )

    for index, (name, data) in enumerate(ranked, start=1):
        avg = calculate_average(data["subjects"])
        print(f"{index}. {name:<15} - {avg:.2f}")

    print("========================================\n")


# ---------- Main Menu ----------
def main():
    while True:
        print("=========== STUDENT ANALYZER ===========")
        print("1. Add Student")
        print("2. Add / Update Score")
        print("3. Show Student Report")
        print("4. Show Leaderboard")
        print("5. Exit")

        choice = input("Choose an option: ")

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
            print("❗ Invalid choice.\n")


main()
