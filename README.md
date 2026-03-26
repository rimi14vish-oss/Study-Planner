# Smart Study Planner (CLI-Based AI Project)

## Overview

Smart Study Planner is a Command Line Interface (CLI) based application that helps students plan and prioritize their studies efficiently. The system uses a simple rule-based AI approach to analyze subject difficulty, available study time, and exam deadlines to generate an optimized study plan.

This project is developed as part of the **Fundamentals of AI and ML (CSA2001)** course.

---

## Problem Statement

Students often struggle with time management and deciding what to study first, especially when multiple subjects and deadlines are involved. This leads to inefficient preparation and increased stress.

---

## Solution

This application acts as a **rule-based intelligent agent** that:

* Takes subject details as input
* Evaluates priority based on difficulty, urgency, and workload
* Generates a structured study plan
* Recommends what to study daily

---

## AI Concept Used

The project implements a **Rule-Based Intelligent Agent**, which:

* Assigns priority scores using predefined rules
* Simulates human decision-making for study planning

Priority is calculated using:

* Difficulty level (easy, medium, hard)
* Days left until exam
* Estimated study hours required

---

## Features

* Add subjects with difficulty, hours, and exam date
* View all subjects
* Edit subject details
* Delete subjects
* Generate prioritized study plan
* Get today's study recommendation
* Data stored using JSON file

---

## Tech Stack

* Language: Python
* Interface: Command Line Interface (CLI)
* Storage: JSON file

---

## Project Structure

```
study_planner/
│
├── main.py          # CLI interface
├── planner.py       # Core logic and AI decision making
├── data.json        # Stores subject data
├── README.md
├── Project Report
├── screenshots
```

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/rimi14vish-oss/study-planner
cd study-planner
```

### 2. Run the Program

```
python main.py
```

---

## Usage Instructions

After running the program, you will see:

```
===== Smart Study Planner =====
1. Add Subject
2. View Subjects
3. Generate Study Plan
4. Today's Recommendation
5. Edit Subject
6. Delete Subject
7. Exit
```

### Example Workflow:

1. Add subjects with details
2. View saved subjects
3. Generate study plan
4. Follow daily recommendation

---

## Example Output

```
Study Plan (High → Low Priority):

1. Physics (Priority: 6.5)
2. Mathematics (Priority: 5.2)
3. Chemistry (Priority: 4.8)
```

---

## Key Implementation Details

* Priority calculation based on multiple weighted factors
* Sorting algorithm used to rank subjects
* File handling for persistent storage
* Modular code structure for maintainability

---

## Real-World Applicability

This system can be used by:

* Students preparing for exams
* Individuals managing multiple tasks
* Anyone needing structured planning assistance

---

## Limitations

* Uses rule-based logic (no advanced ML model)
* Requires manual input of data
* No graphical interface

---

## Future Enhancements

* Integration with calendar APIs
* Machine learning-based prediction
* GUI-based version
* Topic-level planning

---

## Author

* Name: Rimi Vishwakarma
* Reg No: 25BCE11228
* Course: CSA2001 - Fundamentals of AI and ML

---

## Conclusion

This project demonstrates how basic AI concepts like rule-based systems can be applied to solve real-world problems effectively. It highlights the importance of structured decision-making in improving productivity and reducing stress.

---
