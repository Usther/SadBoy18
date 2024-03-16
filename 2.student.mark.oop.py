class Student:
    def __init__(self, id, name, dob, subjects):
        self.__id = id
        self.__name = name
        self.__dob = dob
        self.mark_dict = {subject: None for subject in subjects}
    
    def get_info(self):
        print("ID:", self.__id, "| Name:", self.__name, "| DoB:", self.__dob)

    def get_subject(self):
        print("ID:", self.__id, "| Subject:", self.mark_dict)

class StudentList:
    def __init__(self, subjects):
        self.list_dict = {}
        self.subjects = subjects

    def add_student(self, id, name, dob):
        new_student = Student(id, name, dob, self.subjects)
        self.list_dict[id] = new_student

    def get_student(self):
        for id, student in self.list_dict.items():
            student.get_info()

    def get_subject(self):
        for id, student in self.list_dict.items():
            student.get_subject()   

    def add_mark(self, course_id):
        for id, student in self.list_dict.items():
            mark = input("Enter mark for student {} attending course {}: ".format(id, course_id))   
            student.mark_dict[course_id] = mark      

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