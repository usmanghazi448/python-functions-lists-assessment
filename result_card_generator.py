"""Task 1: Student Result Card Generator."""

NUM_SUBJECTS = 5          # number of subjects every student has
MAX_MARKS = 100           # maximum marks per subject
SUBJECT_PASS_MARK = 40    # minimum marks needed in each subject


def format_name(name):
    # Remove extra spaces around the name and capitalise each word.
    return name.strip().title()


def get_valid_name():
    # Keep asking until the user enters a non-empty name.
    while True:
        name = format_name(input("Enter student name: "))
        if name:
            return name
        print("  Name cannot be empty. Please try again.")


def get_valid_roll_number():
    # Keep asking until the roll number contains digits only.
    while True:
        roll_no = input("Enter roll number: ").strip()
        if roll_no.isdigit():
            return roll_no
        print("  Roll number must contain digits only (no spaces, letters or symbols).")


def get_valid_marks(subject):
    # Keep asking until the marks for the subject are a number from 0 to 100.
    while True:
        text = input(f"Enter marks for {subject} (0-{MAX_MARKS}): ").strip()
        try:
            marks = float(text)
        except ValueError:
            # Letters, empty input, or symbols cannot be converted to a number
            print("  Invalid input. Please enter a number.")
            continue
        # Chained comparison also rejects 'nan' because nan compares False
        if 0 <= marks <= MAX_MARKS:
            return marks
        print(f"  Marks must be between 0 and {MAX_MARKS}.")


def calculate_percentage(total, max_total):
    # Return the percentage of total out of max_total (guards against division by zero).
    if max_total <= 0:
        return 0.0
    return (total / max_total) * 100


def get_grade(percentage):
    # Convert an overall percentage into a letter grade using the grading table.
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    return "Fail"


def get_failed_subjects(subjects, marks_list):
    # Return the names of subjects where the student scored below the pass mark.
    return [sub for sub, mark in zip(subjects, marks_list) if mark < SUBJECT_PASS_MARK]


def get_final_status(grade, failed_subjects):
    # Fail if the grade is Fail OR any single subject is below 40, otherwise Pass.
    if grade == "Fail" or failed_subjects:
        return "Fail"
    return "Pass"


def format_mark(mark):
    # Show whole numbers without decimals (85.0 -> 85) and keep real decimals (85.5).
    return f"{mark:g}"


def print_result_card(name, roll_no, subjects, marks_list, total,
                      max_total, percentage, grade, status, failed_subjects):
    # Print the complete, neatly aligned result card using f-strings.
    width = 44
    line = "=" * width
    print()
    print(line)
    print(f"{'STUDENT RESULT CARD':^{width}}")
    print(line)
    print(f"{'Name':<18}: {name}")
    print(f"{'Roll Number':<18}: {roll_no}")
    print("-" * width)
    print(f"{'Subject':<20}{'Marks':>10}{'Out of':>10}")
    print("-" * width)
    for sub, mark in zip(subjects, marks_list):
        print(f"{sub:<20}{format_mark(mark):>10}{MAX_MARKS:>10}")
    print("-" * width)
    print(f"{'Total Obtained':<18}: {format_mark(total)} / {max_total}")
    print(f"{'Percentage':<18}: {percentage:.2f}%")
    print(f"{'Grade':<18}: {grade}")
    print(f"{'Final Status':<18}: {status}")
    if failed_subjects:
        # Explain why the student failed even if the percentage was high enough
        print(f"{'Below 40 in':<18}: {', '.join(failed_subjects)}")
    print(line)


def main():
    # Collect input, run the calculations, and show the result card.
    subjects = ["English", "Mathematics", "Physics", "Chemistry", "Computer Science"]

    print("--- Student Result Card Generator ---")
    name = get_valid_name()
    roll_no = get_valid_roll_number()

    # Collect validated marks for each subject into a list
    marks_list = [get_valid_marks(sub) for sub in subjects]

    total = sum(marks_list)
    max_total = NUM_SUBJECTS * MAX_MARKS
    percentage = calculate_percentage(total, max_total)
    grade = get_grade(percentage)
    failed_subjects = get_failed_subjects(subjects, marks_list)
    status = get_final_status(grade, failed_subjects)

    print_result_card(name, roll_no, subjects, marks_list, total,
                      max_total, percentage, grade, status, failed_subjects)


if __name__ == "__main__":
    main()