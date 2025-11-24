# Initialize dictionary to store student grades
STOPWORD = "stop"
ADD = "insert"
AVG = "average"
grades = {}

action = input("Choose an action ('insert', 'average', 'stop'): ").strip().lower()
while action != STOPWORD:
    student_id = input("Enter student ID: ").strip()
    if action == ADD:
        grade = float(input("Enter grade: "))    
        # Insert or update grades
        if student_id not in grades:
            grades[student_id] = [grade] # add new student          
        else:
            grades[student_id].append(grade) # append new grade                
    elif action == AVG:
        if student_id in grades:
            student_grades = grades[student_id]
            student_avg = sum(student_grades) / len(student_grades)
            print(f"Average grade for student {student_id}: {student_avg}")
        else:
            print("Error: Student ID not found.")
    else:
        print("Invalid action. Please choose 'insert', 'average', or 'stop'.")
    action = input("Choose an action ('insert', 'average', 'stop'): ").strip().lower()
    