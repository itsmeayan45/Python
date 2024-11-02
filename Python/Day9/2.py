student_scores={
    "Harry":81,
    "Ron":78,
    "Hermione":99,
    "Draco":74,
    "Neville":62
}
student_grades={}
for key in student_scores:
    if 91<=student_scores[key]<=100:
        student_grades[key]="Outstanding"
    elif 81<=student_scores[key]<=90:
        student_grades[key]="Excceeds Expectations"
    elif 71<=student_scores[key]<=80:
        student_grades[key]="Acceptable"
    else:
        student_grades[key]="Fail"
for key in student_grades:
    print(key) 
    print(student_grades[key])