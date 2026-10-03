# student-management-system
# Student Management System

A simple command-line application for managing student records and marks, written in Python. Data is stored in a local JSON file, so your records are saved between runs.

## Features

- **Add** a student with ID, name, age, branch, and marks in Maths, Python, and English
- **View** all students with their details and marks
- **Search** for a student by ID
- **Update** a student's name, age, and branch
- **Delete** a student by ID
- **Calculate** a student's total, average, and grade
- **Persistent storage** using `students.json`

## Requirements

- Python 3.6 or higher
- No external libraries needed (uses only `json` and `os` from the standard library)

## Getting Started

1. Save the program as `student.py` (or any name you like).
2. Open a terminal in the same folder.
3. Run:

```bash
python student.py
```

The file `students.json` is created automatically the first time you add a student.

## Usage

When the program starts you will see this menu:

```
===== STUDENT MANAGEMENT SYSTEM =====
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Calculate Average
7. Exit
```

Type the number of the option you want and press Enter.

| Option | What it does |
|--------|--------------|
| 1 | Asks for ID, name, age, branch, and three subject marks, then saves the student |
| 2 | Lists every student with their details and marks |
| 3 | Finds a student by exact ID |
| 4 | Replaces the name, age, and branch of the student with the given ID |
| 5 | Permanently removes a student by ID |
| 6 | Shows the total marks, average, and grade for a student |
| 7 | Exits the program |

## Grading Scale

Grades are based on the average of the three subjects.

| Average | Grade |
|---------|-------|
| 90 and above | A |
| 75 to 89 | B |
| 60 to 74 | C |
| 40 to 59 | D |
| Below 40 | F |

## Data Format

Each student is stored in `students.json` like this:

```json
{
    "id": "101",
    "name": "Asha",
    "age": "20",
    "branch": "CSE",
    "marks": {
        "maths": 85.0,
        "python": 92.0,
        "english": 78.0
    }
}
```

## Project Structure

```
.
├── student.py       # Main program
├── students.json    # Auto-generated data file
└── README.md
```

## Known Limitations

- Entering non-numeric marks crashes the program, and marks are not limited to 0-100.
- Student IDs are not checked for duplicates, so use unique IDs.
- Age is stored as text rather than a number.
- Updating a student overwrites the name, age, and branch (pressing Enter leaves them blank), and marks cannot be updated.
- Deleting a student does not ask for confirmation.
- If `students.json` becomes corrupted, the program may fail to start; delete or fix the file to continue.

## Future Improvements

- Validate marks, age, and duplicate IDs
- Let blank input keep existing values when updating
- Allow updating marks
- Add a class-wide report (topper, subject averages)
- Move storage to SQLite

## License

This project is free to use and modify for learning purposes.
