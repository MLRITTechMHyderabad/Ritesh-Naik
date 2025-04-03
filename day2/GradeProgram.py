students = [
    ("Alice", [85, 90, 78, 92]),
    ("Bob", [60, 65, 70, 75]),
    ("Charlie", [40, 45, 50, 55]),
    ("David", [95, 100, 98, 92])
]

student_dic=dict(students)
print(student_dic)

alice_grade = student_dic["Alice"]
bob_grade=student_dic["Bob"]
charlie_grade=student_dic["Charlie"]
david_grade=student_dic["David"]


def getavg(student_grade):
    avg_grade=(sum(student_grade))/len(student_grade)
    return avg_grade

alice_avg=getavg(alice_grade)
bob_avg=getavg(bob_grade)
charlie_avg=getavg(charlie_grade)
david_avg=getavg(david_grade)

print("Average Grade for Bob",bob_avg)

average_grades = {
    "Alice": alice_avg,
    "Bob": bob_avg,
    "Charlie": charlie_avg,
    "David": david_avg
}

highest_avg = max(average_grades, key=average_grades.get)

print("Student with Highest Average Grade:", highest_avg)





    

