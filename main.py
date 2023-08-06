students_score = {
  "Thomas" : 57,
  "James": 80,
  "Jane": 95,
  "Lucas": 65
}

# Do not change the code above ☝️
#################################################################

# TODO 1: Create an empty dictionary, students_grade
students_grade={}
# TODO 2: Add each student name from students_score dictionary as the key
#         and the value is the grade of the student
for stu in students_score:
  score = students_score[stu]
  if score >= 80:
    students_grade[stu] = "A"
  elif score >= 60:
    students_grade[stu] = "B"
  elif score >= 55:
    students_grade[stu]="C"
  elif score >= 50:
    students_grade[stu]="D"
  else:
    students_score[stu]="F"
  #############################################################
# Do not change the code below
print(students_grade)