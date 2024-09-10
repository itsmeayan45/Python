student_heights=input("Input a list of student heights seperated by a space ").split()
sum=0
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
for i in range(0,len(student_heights)):
    sum+=student_heights[i]
avg=sum/len(student_heights)
print(avg)
