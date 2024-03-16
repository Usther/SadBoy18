import math
from .student import Student

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
            rounded_mark = math.floor(float(mark))  
            student.mark_dict[course_id] = rounded_mark      

    def sorted_gpa(self):
        sorted_list = sorted(self.list_dict.values(), key = lambda student: student.get_GPA())
        return sorted_list