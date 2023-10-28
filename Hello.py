print("Hello World")
# variable declaration in python
name_student = 'Denis Ouma'
name_career = 'Android Developer'
# the print function
print(f"My name is {name_student}\n I am an {name_career}")

# enter inputs
course_name = input("Enter the course you take :\n")
academic_year = int(input("Enter the Academic year you in:\n"))


# function to generate a report on the year of study
def academic_details():
    print("THE REPORT OF THE STUDENT DETAILS..")
    report_result = f'{course_name} {academic_year}'
    print(report_result)

# academic report of the student  
# output of the function
# invoke/ call the function
academic_details()  