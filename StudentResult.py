Student_Name = str(input("Enter Name : "))
Student_RollNo = int(input("Enter RollNo : "))
num_subjects = int(input("Enter the number of subjects: "))
subjects = []
Subject_Total_Marks = []
Obtained_Marks = []
grades = []
TotalNumbers = 0
Obtained = 0

for i in range(num_subjects):
    subject_name = input(f"Enter subject {i + 1}: ")
    subjects.append(subject_name)
    SubjectNumbers = int(input(f"Enter Total Number of {subject_name}: "))
    Subject_Total_Marks.append(SubjectNumbers)
    result = int(input(f"Enter result for {subject_name}: "))
    Obtained_Marks.append(result)

    # Calculate Grade for One Subject
    if result >= 80:
        grade = "A+"
    elif result >= 70:
        grade = "A"
    elif result >= 60:
        grade = "B"
    elif result >= 50:
        grade = "C"
    else:
        grade = "F"

    grades.append(grade)

    # Calculate Sum of Numbers
    TotalNumbers += SubjectNumbers
    Obtained += result

#Calculate Percentage
Percentage = (Obtained / TotalNumbers) * 100
# Grades
if Percentage >= 80:
    Grades = "A+"
elif Percentage >= 70:
    Grades = "A"
elif Percentage >= 60:
    Grades = "B"
elif Percentage >= 50:
    Grades = "C"
else:
    Grades = "F"

# Calculate Percentage

print("\n-----------------Student Report------------------")
print(f"\nStudent Name: {Student_Name}")
print(f"Student Roll No: {Student_RollNo}")
print("-------------------------------------------------")
print(f"\nSubjects \t Total Marks  \t\t Results \t\tGrades")
print("---------------------------------------------------------------------------------------------")
for i in range(num_subjects):
    print(f"\n{subjects[i]:<20} {Subject_Total_Marks[i]:<20} {Obtained_Marks[i]:<20} {grades[i]:<20}")
print("----------------------------------------------------------------------------------------------------------------------")
print(f"\nTotal Marks = {TotalNumbers}  \t Obtained Marks = {Obtained} \t Grades = {Grades} \t Percentage = {Percentage:.2f}%")