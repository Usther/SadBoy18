from PW4.student_list import StudentList
from PW4.student import Student

# Initialize courses list
courses_num = int(input("Enter the number of courses: "))
subjects = []
for i in range(courses_num):
    new_course = input("Enter course {} ID: ".format(i + 1))
    subjects.append(new_course)

student_num = int(input("Enter the number of students: "))
students = StudentList(subjects)
print("------")

for k in range(student_num):
    student_id = input("Enter the student {} ID: ".format(k + 1))
    student_name = input("Enter the student {} name: ".format(k + 1))
    student_dob = input("Enter student {} DoB: ".format(k + 1))
    students.add_student(student_id, student_name, student_dob)
    print("------")

for l in range(courses_num):
    marked_course = input("Enter the course ID to input marks: ")
    students.add_mark(marked_course)
    print("------")

print("Student Information:")
students.get_student()
print("------")
print("Subject Information:")
students.get_subject()
print("------")

print("GPA sorted list:")
sorted_students = students.sorted_gpa()
for student in sorted_students:
    student_gpa = student.get_GPA()
    print("Student ID:", student._Student__id, "| GPA:", student_gpa)
    print("------")