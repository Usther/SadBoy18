#Number of students and courses
n_stu = int(input("Enter the number of student: "))
n_sbj = int(input("Enter the number of subject: "))

#Dictionary for student
student = {}
for i in range(n_stu):
    print("Infor of student", i + 1)
    id = input("Enter student's ID: ")
    name = input("Enter name for student {}: ".format(id))
    dob = input("Enter dob for student {}: ".format(id))

    #Dictionary for marks
    marks = {}
    print("Mark of student", i + 1)
    for k in range(n_sbj):
        id_sub = input("Enter subject's ID: ")
        mark = input("Enter mark for {}: ".format(id_sub))
        marks[id_sub] = mark

    student[id] = name, dob, marks

#Listing function
def list_course(): 
    for id, (name, dob, marks) in student.items():
        print("Courses for student", id, ": ", ', '.join(marks.keys()))

def list_student():
    for id, (name, dob, marks) in student.items():
        print("ID: ", id," Name: ", name)

def list_mark(id_sub):
    for id, (name, dob, marks) in student.items():
        if id_sub in marks:
            print("Student", name,"|Id", id, "|Subject:", id_sub, ": ", marks[id_sub])

print("1: List all the courses.\n2: List all the students.\n3: List all the marks of subject of choice.")
choice = int(input("Enter:"))
if choice == 1:
    list_course()
elif choice == 2:
    list_student()
elif choice == 3:
    subject = input("Enter the subject to read: ")
    list_mark(subject)
else:
    print("Invalid choice.")
