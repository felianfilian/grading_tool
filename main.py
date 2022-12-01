
student_scores = {
    "Peter" : 83,
    "Luigi" : 76,
    "Mario" : 92,
    "Bowser" : 52
}

for student in student_scores:
    if student_scores[student] >= 91:
        print(student + " - excelent")
    elif student_scores[student] >= 81:
        print(student + " - good")
    elif student_scores[student] >= 71:
        print(student + " - ok")
    else:
        print(student + " - fail")
