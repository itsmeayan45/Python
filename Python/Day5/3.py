student_scores=input("Input a list of student scores seperated by a space: ").split()
for n in range(0,len(student_scores)):
    student_scores[n]=int(student_scores[n])
print(student_scores)
#using sorting method
# student_scores.sort()
# print(f"The highest score in the class is:{student_scores[len(student_scores)-1]}")
highest_score=0
for score in student_scores:
    if score>highest_score:
        highest_score=score
print(f"The highest score in the class is: {highest_score}")