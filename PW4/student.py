import numpy as np 

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

    def get_GPA(self):
        marks_list = np.array(list(self.mark_dict.values()))
        gpa = np.sum(marks_list) / len(marks_list)
        return gpa