def calculate_result():
    Student_Name = str(input("Enter Name : "))
    Student_RollNo = int(input("Enter RollNo : "))
    subjects = []
    marks = []
    TotalSujectmarks = []
    num_subjects = int(input("Enter the number of subjects: "))

    for i in range(num_subjects):
        subject = input("Enter subject name: ")
        totalmarks = int(input(f"Enter Total marks of {subject} : "))
        obtmark = int(input(f"Enter marks for {subject} : "))
        subjects.append(subject)
        TotalSujectmarks.append(totalmarks)
        marks.append(obtmark)

    total_marks = sum(marks)
    maximum_possible_marks = num_subjects * 100  
    percentage = (total_marks / maximum_possible_marks) * 100
    if percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    if percentage >= 50:
        result = "Pass"
    else:
        result = "Fail"

    return Student_Name,Student_RollNo,result, grade, percentage

Student_Name,Student_RollNo,result, grade, percentage = calculate_result()
print("\n-----------------Student Report------------------")
print(f"\nStudent Name: {Student_Name}")
print(f"Student Roll No: {Student_RollNo}")
print("-------------------------------------------------")
print(f"Result:{result} \t Grade:{grade} \t Percentage : {percentage}")