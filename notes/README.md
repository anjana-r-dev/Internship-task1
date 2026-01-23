
# Internship Task–1 Notes

## Overview

**Task Title:** Task–1: GitHub Usage and Python Fundamentals
**Objective:** Learn GitHub basics, Git workflow, and Python programming fundamentals, and submit working code in a professional repository structure.

---

## Tools & Environment

* **Language:** Python
* **Editor/IDE:** Visual Studio Code
* **Version Control:** Git
* **Platform:** GitHub (Web + GitHub Desktop)
* **OS:** Windows

---

## Repository Setup (GitHub)

* Created a GitHub account and a public repository named **`Internship-task1`**.
* Used **GitHub Desktop** to manage commits and push changes.
* Organized the repository with a clean folder structure.

### Recommended Structure

```
Internship-task1/
│
├── programs/
│   ├── 01_variables_and_type_conversion.py
│   ├── 02_data_types.py
│   ├── 03_conditional_statements.py
│   └── 04_loops.py
│
├── README.md
└── .gitattributes
```

> Note: GitHub does not track empty folders. Folders were created by adding files inside them (e.g., `programs/README.md`).

---

## Git & GitHub Basics (Conceptual Understanding)

### Key Git Commands (Conceptual)

* **`git init`**: Initializes a folder as a Git repository.
* **`git status`**: Shows the current state of files (modified, staged).
* **`git add`**: Stages files for commit.
* **`git commit`**: Saves changes locally with a message.
* **`git push`**: Uploads committed changes to GitHub.
* **`git pull`**: Downloads the latest changes from GitHub.
* **`git clone`**: Creates a local copy of a GitHub repository.

### Workflow Used (via GitHub Desktop)

1. Add or edit files in the local repository folder.
2. Review changes in GitHub Desktop.
3. Commit changes with a clear message.
4. Push to GitHub.

---

## Python Fundamentals Covered

### 1. Variables & Type Conversion

* Defined variables using assignment (`=`).
* Used meaningful, professional variable names.
* Demonstrated basic type conversion:

  * `int()`
  * `float()`
  * `str()`
  * `bool()`

**Key Takeaway:** Variables store data; type conversion changes the data type when required.

---

### 2. Data Types

#### Built-in Data Types

* **Numeric:** `int`, `float`
* **Text:** `str`
* **Boolean:** `bool`
* **Collections:** `list`, `tuple`, `set`, `dict`
* **Special:** `NoneType`

#### User-Defined Data Types

* Created using **classes**.
* Used to group related data into a single entity.

**Example Concept:**

* A `Student` or `Employee` class to store attributes like name, age, and department.

---

### 3. Conditional Statements

* Used decision-making constructs:

  * `if`
  * `if-else`
  * `if-elif-else`
* Implemented real-world logic such as eligibility checks.

**Key Operators:**

* Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
* Logical: `and`, `or`, `not`

---

### 4. Loops

#### Types of Loops in Python

* **`for` loop**: Used when the number of iterations is known.
* **`while` loop**: Used when the condition controls repetition.

#### Loop Control

* Used `break` and `continue` where required.
* Printed output on the same line using `end=""`.

**Important Note:** Python has only **two loop statements**: `for` and `while`.

---

## Classes, Objects, and Methods

* Created classes using the `class` keyword.
* Used the `__init__` constructor to initialize object data.
* Understood the role of `self` as a reference to the current object.
* Created objects **outside the class body** at the module level.

**Best Practice:**

* Avoid using built-in names like `id` for variables.
* Use clear names such as `student_id` or `employee_id`.

---

## Module Concept

* Each `.py` file is a **module**.
* Modules help organize code by functionality.
* Code executes top-to-bottom when a module is run.

---

## Common Issues Identified & Resolved

* Fixed syntax errors due to incorrect variable definitions.
* Resolved warnings for unused variables and shadowing built-ins.
* Corrected indentation and scope issues in classes.
* Understood that object creation must be outside the class body.

---

## Final Outcome

* A clean, public GitHub repository with organized Python programs.
* Demonstrated understanding of GitHub usage and Python basics.
* Task–1 completed as per the provided requirements and submission guidelines.

---

## One-Line Summary

> Task–1 involved setting up a GitHub repository, learning Git fundamentals, and implementing Python basics including variables, data types, conditions, loops, and user-defined data types in a clean and professional structure.
