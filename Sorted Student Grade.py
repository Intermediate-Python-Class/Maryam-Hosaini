

def sort_grades(student_grades):
    
    sorted_grades = sorted(student_grades, key=lambda x: (x[1], x[0]))
    return sorted_grades

students = [
    ("Alice", 75),
    ("Bob", 90),
    ("Carol", 85),
    ("David", 85),
    ("Eve", 75)
]

sorted_students = sort_grades(students)
print(sorted_students)