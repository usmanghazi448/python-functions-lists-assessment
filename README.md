# Student Marks Toolkit

## 1. Project Title and Overview

**Student Marks Toolkit** is a pair of beginner-friendly, console-based Python programs for working with student marks:

| Program | File | Purpose |
|---|---|---|
| Task 1 | `result_card.py` | Generates a formatted result card for **one** student |
| Task 2 | `class_marks_analyzer.py` | Analyzes the performance of an **entire class** |

The two programs are developed separately and do not depend on each other. Both validate every input, so the program keeps asking until it receives a valid value instead of crashing.

---

## 2. Description of the Programs

### Task 1: Student Result Card Generator (`result_card.py`)

Asks for a student's name, roll number and marks in five subjects (English, Mathematics, Physics, Chemistry, Computer Science), then prints a formatted result card.

**What it does**
- Cleans the name (`"  aLi rAzA "` becomes `"Ali Raza"`).
- Accepts a roll number only if it contains digits.
- Accepts marks only between 0 and 100 (decimals allowed).
- Calculates total marks and the percentage out of 500.
- Assigns a letter grade:

| Percentage | Grade |
|---|---|
| 90 and above | A+ |
| 80 to 89 | A |
| 70 to 79 | B |
| 60 to 69 | C |
| 50 to 59 | D |
| Below 50 | Fail |

- **Fail rule:** if any subject is below 40, the final status is **Fail** whatever the overall percentage is. The card also lists the subjects that were below 40.
- The letter grade comes from the percentage table only, so a student can show Grade A with Final Status Fail if one subject is below 40.

**Functions**

| Function | Purpose |
|---|---|
| `format_name(name)` | Strips extra spaces and capitalizes each word |
| `get_valid_name()` | Asks until the name is not empty |
| `get_valid_roll_number()` | Asks until the roll number is digits only |
| `get_valid_marks(subject)` | Asks until marks are a number from 0 to 100 |
| `calculate_percentage(total, max_total)` | Returns the percentage, guarding against division by zero |
| `get_grade(percentage)` | Converts a percentage into a letter grade |
| `get_failed_subjects(subjects, marks_list)` | Finds subjects scored below 40 |
| `get_final_status(grade, failed_subjects)` | Returns Pass or Fail |
| `format_mark(mark)` | Shows `85.0` as `85` and keeps real decimals like `85.5` |
| `print_result_card(...)` | Prints the result card using f-strings |
| `main()` | Runs the program from start to finish |

### Task 2: Class Marks Analyzer (`class_marks_analyzer.py`)

Asks how many students are in the class, reads each student's name and marks, and prints a full analysis report.

**What it does**
- Stores data in two parallel lists, `student_names` and `student_marks`, filled with `.append()`.
- Validates the class size (whole number above 0), each name (not empty) and each mark (0 to 100).
- Displays:
  - the class average
  - the highest marks and the student(s) who got them
  - the lowest marks and the student(s) who got them
  - the number of passing (50 or above) and failing (below 50) students
  - the students who scored above the class average
  - all students ranked from highest to lowest marks
- Handles ties: if several students share the highest or lowest mark, all of them are listed.

**Functions**

| Function | Purpose |
|---|---|
| `get_class_size()` | Asks until a whole number above 0 is entered |
| `get_valid_name(position)` | Asks until the student's name is not empty |
| `get_valid_marks(name)` | Asks until marks are a number from 0 to 100 |
| `find_students_with_marks(names, marks, target)` | Returns every student with the given marks (handles ties) |
| `count_pass_fail(student_marks)` | Returns the number of passing and failing students |
| `get_students_above_average(names, marks, average)` | Returns students who scored above the average |
| `get_ranked_students(names, marks)` | Returns (name, marks) pairs sorted highest to lowest |
| `main()` | Collects the data and prints the report |

---

## 3. Python Concepts and Functions Used

| Concept | Where it is used |
|---|---|
| Functions: `def`, parameters, `return` | Both programs |
| Returning more than one value (tuples) | `count_pass_fail()` |
| Module-level constants (`MAX_MARKS`, `PASS_MARK`, ...) | Both programs |
| `input()` and `print()` | Reading and showing data |
| `while True` loops with `return` / `continue` | Input validation |
| `for` loops, `range()`, `enumerate()`, `zip()` | Reading data, searching lists, printing tables |
| `if` / `elif` / `else` | Grading, validation, pass/fail logic |
| `try` / `except ValueError` | Rejecting non-numeric marks |
| String methods: `.strip()`, `.title()`, `.isdigit()`, `.join()` | Cleaning and validating text |
| f-strings with alignment and precision (`:<20`, `:>10`, `:^44`, `:.2f`, `:g`) | Formatting the result card and report |
| Lists and `.append()` | Task 2 data storage |
| `len()`, `sum()`, `max()`, `min()`, `sorted()` | Task 2 statistics and ranking |
| `lambda` as a sort `key` | Ranking students while keeping names linked to marks |
| List comprehension | Collecting marks in Task 1, building the ranked list in Task 2 |
| Chained comparison (`0 <= marks <= 100`) | Range validation |
| `if __name__ == "__main__":` | Running `main()` only when the file is run directly |

---

## 4. Instructions for Running the Programs

**Requirements:** Python 3.6 or newer. No external libraries are needed.

1. Put `result_card.py` and `class_marks_analyzer.py` in the same folder.
2. Open a terminal in that folder.
3. Run the program you want:

```bash
# Task 1: Student Result Card Generator
python result_card.py

# Task 2: Class Marks Analyzer
python class_marks_analyzer.py
```

On some systems the command is `python3` instead of `python`.

Follow the prompts. If you enter an invalid value, the program tells you what is wrong and asks again.

---

## 5. Sample Input and Output

### Task 1: `result_card.py`

**Input** (the name has extra spaces and lower-case letters, and Physics is below 40):

```
--- Student Result Card Generator ---
Enter student name:   sara khan 
Enter roll number: 1023
Enter marks for English (0-100): 90
Enter marks for Mathematics (0-100): 100
Enter marks for Physics (0-100): 35
Enter marks for Chemistry (0-100): 100
Enter marks for Computer Science (0-100): 100
```

**Output:**

```
============================================
            STUDENT RESULT CARD             
============================================
Name              : Sara Khan
Roll Number       : 1023
--------------------------------------------
Subject                  Marks    Out of
--------------------------------------------
English                     90       100
Mathematics                100       100
Physics                     35       100
Chemistry                  100       100
Computer Science           100       100
--------------------------------------------
Total Obtained    : 425 / 500
Percentage        : 85.00%
Grade             : A
Final Status      : Fail
Below 40 in       : Physics
============================================
```

The percentage is high enough for Grade A, but the final status is **Fail** because Physics is below 40.

**Example of invalid input being handled:**

```
Enter roll number: 12 3
  Roll number must contain digits only (no spaces, letters or symbols).
Enter marks for English (0-100): 101
  Marks must be between 0 and 100.
Enter marks for English (0-100): abc
  Invalid input. Please enter a number.
```

### Task 2: `class_marks_analyzer.py`

**Input:**

```
--- Class Marks Analyzer ---
How many students are in the class? 5
Enter name of student 1: ali
  Enter marks for Ali (0-100): 80
Enter name of student 2: sara
  Enter marks for Sara (0-100): 45
Enter name of student 3: bilal
  Enter marks for Bilal (0-100): 80
Enter name of student 4: hina
  Enter marks for Hina (0-100): 45
Enter name of student 5: usman
  Enter marks for Usman (0-100): 62.5
```

**Output:**

```
==============================================
            CLASS ANALYSIS REPORT             
==============================================
Total students : 5
Class average  : 62.50
Highest marks  : 80 -> Ali, Bilal
Lowest marks   : 45 -> Sara, Hina
Passing (>= 50): 3
Failing (< 50) : 2

Students scoring above the class average:
  Ali                       80
  Bilal                     80

Marks sorted from highest to lowest:
   1. Ali                       80
   2. Bilal                     80
   3. Usman                   62.5
   4. Sara                      45
   5. Hina                      45
==============================================
```

**Example of invalid input being handled:**

```
How many students are in the class? 0
  Please enter a whole number greater than 0.
How many students are in the class? abc
  Please enter a whole number greater than 0.
  Enter marks for Ali (0-100): -1
  Marks must be between 0 and 100.
```

---

## Test Scenarios Covered

| Program | Scenario | Expected result |
|---|---|---|
| Task 1 | Messy name and invalid roll number or marks | Name cleaned, bad input re-asked |
| Task 1 | High percentage but one subject below 40 | Final status Fail |
| Task 1 | Exactly 50% and 49.8% | Grade D / Pass, and Grade Fail / Fail |
| Task 1 | All zeros, decimal marks | 0.00% Fail, and 74.15% Grade B |
| Task 2 | Invalid class size and invalid marks | Re-asked until valid |
| Task 2 | Ties for highest and lowest marks | All tied students listed |
| Task 2 | One student only | No students above average |
| Task 2 | Everyone has the same marks | No students above average |
| Task 2 | Marks of 50 and 49.9 | 50 passes, 49.9 fails |