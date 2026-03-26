import json
from datetime import datetime
DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def add_subject(name, difficulty, hours, exam_date):
    data = load_data()
    
    subject = {
        "name": name,
        "difficulty": difficulty.lower(),
        "hours": int(hours),
        "exam_date": exam_date
    }
    
    data.append(subject)
    save_data(data)
    print(f"{name} added successfully!")

def view_subjects():
    data = load_data()
    
    if not data:
        print("No subjects found.")
        return
    
    for i, sub in enumerate(data, 1):
        print(f"{i}. {sub['name']} | {sub['difficulty']} | {sub['hours']} hrs | Exam: {sub['exam_date']}")

def calculate_priority(subject):
    # Difficulty score
    diff_map = {"easy": 1, "medium": 2, "hard": 3}
    difficulty_score = diff_map.get(subject["difficulty"], 1)
    
    # Urgency score (days left)
    today = datetime.today()
    exam = datetime.strptime(subject["exam_date"], "%Y-%m-%d")
    days_left = (exam - today).days
    
    if days_left <= 5:
        urgency_score = 3
    elif days_left <= 10:
        urgency_score = 2
    else:
        urgency_score = 1
    
    # Hours weight (more hours = more priority)
    hours_score = subject["hours"] / 10
    
    return difficulty_score + urgency_score + hours_score

def generate_plan():
    data = load_data()
    
    if not data:
        print("No subjects available.")
        return
    
    # Calculate priority
    for sub in data:
        sub["priority"] = calculate_priority(sub)
    
    # Sort by priority
    sorted_data = sorted(data, key=lambda x: x["priority"], reverse=True)
    
    print("\n Study Plan (High → Low Priority):\n")
    for i, sub in enumerate(sorted_data, 1):
        print(f"{i}. {sub['name']} (Priority: {round(sub['priority'],2)})")

def today_recommendation():
    data = load_data()
    
    if not data:
        print("No subjects available.")
        return
    
    for sub in data:
        sub["priority"] = calculate_priority(sub)
    
    best = max(data, key=lambda x: x["priority"])
    
    print("\n Today's Focus:")
    print(f" {best['name']} (Priority: {round(best['priority'],2)})")

def delete_subject():
    data = load_data()
    
    if not data:
        print("No subjects available.")
        return
    
    print("\nSelect subject to delete:\n")
    for i, sub in enumerate(data, 1):
        print(f"{i}. {sub['name']}")
    
    try:
        choice = int(input("Enter subject number: ")) - 1
        
        if choice < 0 or choice >= len(data):
            print("Invalid selection.")
            return
        
        removed = data.pop(choice)
        save_data(data)
        
        print(f"{removed['name']} deleted successfully!")
    
    except ValueError:
        print("Invalid input. Please enter a number.")

def edit_subject():
    data = load_data()
    
    if not data:
        print("No subjects available.")
        return
    
    print("\nSelect subject to edit:\n")
    for i, sub in enumerate(data, 1):
        print(f"{i}. {sub['name']}")
    
    try:
        choice = int(input("Enter subject number: ")) - 1
        
        if choice < 0 or choice >= len(data):
            print("Invalid selection.")
            return
        
        subject = data[choice]
        
        print("\nLeave blank to keep current value.\n")
        
        new_name = input(f"New name ({subject['name']}): ") or subject['name']
        new_diff = input(f"New difficulty ({subject['difficulty']}): ") or subject['difficulty']
        new_hours = input(f"New hours ({subject['hours']}): ") or subject['hours']
        new_exam = input(f"New exam date ({subject['exam_date']}): ") or subject['exam_date']
        
        # Update values
        subject['name'] = new_name
        subject['difficulty'] = new_diff.lower()
        subject['hours'] = int(new_hours)
        subject['exam_date'] = new_exam
        
        save_data(data)
        
        print("Subject updated successfully!")
    
    except ValueError:
        print("Invalid input. Please enter a number.")


def menu():
    while True:
        print('''
===== Study Planner =====
              ''')
        print("1. Add Subject")
        print("2. View Subjects")
        print("3. Generate Study Plan")
        print("4. Today's Recommendation")
        print("5. Edit Subject")
        print("6. Delete Subject")
        print("7. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            name = input("Subject name: ")
            difficulty = input("Difficulty (easy/medium/hard): ")
            hours = input("Hours required: ")
            exam_date = input("Exam date (YYYY-MM-DD): ")
            
            add_subject(name, difficulty, hours, exam_date)
        
        elif choice == "2":
            view_subjects()
        
        elif choice == "3":
            generate_plan()
        
        elif choice == "4":
            today_recommendation()
        
        elif choice == "5":
            edit_subject()

        elif choice == "6":
            delete_subject()

        elif choice == "7":
            print("Good luck with your studies!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()