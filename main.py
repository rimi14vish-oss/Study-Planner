from planner import *

def menu():
    while True:
        print('''
====== Smart Study Planner ======
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