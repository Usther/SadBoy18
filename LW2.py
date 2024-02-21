#Define class Person
class Person:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
    
    def display_info(self):
        print("Name:", self.name, "|ID: ", self.id, "|Dob: ", self.dob)
        

#Define class Student
class Student(Person):
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.mark = {}

    def add_mark(self, n_sub):
        for i in range(n_sub):
            id_sub = input("Enter subject's ID: ")
            mark = input("Enter the mark for {}: ".format(id_sub))
            self.mark[id_sub] = mark
    
    def display_info(self):
        super().display_info()
        print("Courses: ", ', '.join(self.mark.keys()))

class Classroom:
    def __init__(self):
        self.students = {}

    def add_student(self, n_stu, n_sub):
        for k in range(n_stu):
            print("Information of student", k + 1)
            id = input("Enter student's ID: ")
            name = input("Enter name for student {}: ".format(id))
            dob = input("Enter dob for student {}: ".format(id))
            student = Student(id, name, dob)

            student.add_mark(n_sub)
            self.students[id] = student
    
    #Listing function
    def display_student_info(self):
        for id, student in self.students.items():
            student.display_info()

    def display_student_subject(self):
        for id, student in self.students.items():
            print("Courses for student", id, ": ", ', '.join(student.mark.keys()))

    def display_marks(self, id_sub):
        for id, student in self.students.items():
            if id_sub in student.mark:
                print("Student's name:",student.name ,"|ID:", id, "|", id_sub, ": ", student.mark[id_sub])

    def choice(self, choice):
        if choice == 1:
            self.display_student_subject()
        elif choice == 2:
            self.display_student_info()
        elif choice == 3:
            id_sub = input("Enter the subject to check: ")
            self.display_marks(id_sub)
        else:
            print("Invalid choice")

#User's input
n_stu = int(input("Enter the number of student: "))
n_sbj = int(input("Enter the number of subject: "))

#main
classroom = Classroom()
classroom.add_student(n_stu, n_sbj)

print("1: List all the courses.\n2: List all the students.\n3: List all the marks of subject of choice.")
choice = int(input("Your choice: "))
classroom.choice(choice)

