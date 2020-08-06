# Lets create an empty array to store the grades provided by the user.
gradeArray=[]
# Lets ask the user for the number of grades he is going to input.
numGrades=int(input('How many grades do you have? '))

print('')

# Loop to the number of grades user gave us.
for i in range(0,numGrades,1):
	# Ask for grade.
	grade=float(input('Input grade '))
	# Save grade to array.
	gradeArray.append(grade)

print('')

# Print the grades, as input.
print('All    grades ',gradeArray)

# Setting up a breadcrumb for sorting exercise.
bc=1
while (bc==1):
	bc=0
	# Lets loop all grades given. 
	# We do NOT want to get to the end of the list because i+1 does not exist.
	# This would make comparison i vs i+1 fail, out of range.
	# We want to stop one before this...
	for i in range(0,numGrades-1,1):
		# If current grade is greater than the next grade.
		if gradeArray[i] > gradeArray[i+1]:
			# Save this value in pocket.
			pocketGrade=gradeArray[i]
			# Take the next value, which is lower, and 'swap back' to current location.
			gradeArray[i]=gradeArray[i+1]
			# Take pocketed value and put in next location, ahead of smalle value.
			gradeArray[i+1]=pocketGrade
			bc=1

# Print the grades, now sorted.
print('Sorted grades ',gradeArray)
