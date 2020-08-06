gradeArray=[]
numGrades=int(input("How many grades do you have? "))

print("")

for i in range(0,numGrades,1):
	grade=float(input("Input the grade: "))
	gradeArray.append(grade)

print("")

for i in range(0,numGrades,1):
	print("Your ",i+1," grade is ", gradeArray[i])

print("")

print("That's it boys; thank you for playing.")
print("")
print("The average grade is: ",sum(gradeArray)/len(gradeArray))
print("The lowest grade is ", min(gradeArray))
print("The highest grade is ", max(gradeArray))
print("")

print("Now, we are going to do this once more with a more manual way!")
print("")
lowGrade=100
highGrade=0

for i in range(0,numGrades,1):
	if lowGrade > gradeArray[i]:
		lowGrade=gradeArray[i]
	if highGrade < gradeArray[i]:
		highGrade=gradeArray[i]

print("The minimum grade, again, is ", lowGrade)
print("The maximum grade, again, is ", highGrade)

bucket=0

for i in range(0,numGrades,1):
	bucket=bucket+gradeArray[i]
average=bucket/numGrades

print("The average grade, again, is ", average)
# Homwwork done.
# now average all grades
# give min grade
# give max grade
