"""Task 2: Class Marks Analyzer."""

MAX_MARKS = 100       # highest mark a student can get
PASS_MARK = 50        # marks needed to pass


def get_class_size():
    # Keep asking until the user enters a whole number greater than zero.
    while True:
        text = input("How many students are in the class? ").strip()
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("  Please enter a whole number greater than 0.")


def get_valid_name(position):
    # Keep asking until the user enters a non-empty name for student number `position`.
    while True:
        name = input(f"Enter name of student {position}: ").strip().title()
        if name:
            return name
        print("  Name cannot be empty.")


def get_valid_marks(name):
    # Keep asking until the marks for `name` are a number between 0 and 100.
    while True:
        text = input(f"  Enter marks for {name} (0-{MAX_MARKS}): ").strip()
        try:
            marks = float(text)
        except ValueError:
            # Letters, symbols or empty input cannot become a number
            print("  Invalid input. Please enter a number.")
            continue
        # Chained comparison also rejects 'nan' because nan compares False
        if 0 <= marks <= MAX_MARKS:
            return marks
        print(f"  Marks must be between 0 and {MAX_MARKS}.")


def find_students_with_marks(student_names, student_marks, target):
    # Return every student name whose marks equal `target` (handles ties).
    matches = []
    for i in range(len(student_marks)):
        if student_marks[i] == target:
            matches.append(student_names[i])
    return matches


def count_pass_fail(student_marks):
    # Return (passing, failing) student counts using the pass mark.
    passing = 0
    failing = 0
    for marks in student_marks:
        if marks >= PASS_MARK:
            passing += 1
        else:
            failing += 1
    return passing, failing


def get_students_above_average(student_names, student_marks, average):
    # Return a list of (name, marks) pairs for students scoring above `average`.
    above = []
    for i in range(len(student_marks)):
        if student_marks[i] > average:
            above.append((student_names[i], student_marks[i]))
    return above


def get_ranked_students(student_names, student_marks):
    # Return (name, marks) pairs sorted from highest to lowest marks.
    # Sort the index positions so each mark stays linked to its own name
    order = sorted(range(len(student_marks)),
                   key=lambda i: student_marks[i], reverse=True)
    return [(student_names[i], student_marks[i]) for i in order]


def main():
    # Collect class data, then display every required statistic.
    student_names = []
    student_marks = []

    print("--- Class Marks Analyzer ---")
    class_size = get_class_size()

    # Read each student's name and marks, storing them in the two lists
    for position in range(1, class_size + 1):
        name = get_valid_name(position)
        marks = get_valid_marks(name)
        student_names.append(name)
        student_marks.append(marks)

    # Basic statistics using built-in list functions
    total_students = len(student_marks)
    class_average = sum(student_marks) / total_students
    highest = max(student_marks)
    lowest = min(student_marks)

    print("\n" + "=" * 46)
    print(f"{'CLASS ANALYSIS REPORT':^46}")
    print("=" * 46)
    print(f"Total students : {total_students}")
    print(f"Class average  : {class_average:.2f}")

    top_students = find_students_with_marks(student_names, student_marks, highest)
    print(f"Highest marks  : {highest:g} -> {', '.join(top_students)}")

    bottom_students = find_students_with_marks(student_names, student_marks, lowest)
    print(f"Lowest marks   : {lowest:g} -> {', '.join(bottom_students)}")

    passing, failing = count_pass_fail(student_marks)
    print(f"Passing (>= {PASS_MARK}): {passing}")
    print(f"Failing (< {PASS_MARK}) : {failing}")

    print("\nStudents scoring above the class average:")
    above_average = get_students_above_average(student_names, student_marks, class_average)
    if above_average:
        for name, marks in above_average:
            print(f"  {name:<20}{marks:>8g}")
    else:
        # Happens when everyone scored exactly the same
        print("  None (no student is above the average).")

    print("\nMarks sorted from highest to lowest:")
    for rank, (name, marks) in enumerate(get_ranked_students(student_names, student_marks), start=1):
        print(f"  {rank:>2}. {name:<20}{marks:>8g}")
    print("=" * 46)


if __name__ == "__main__":
    main()