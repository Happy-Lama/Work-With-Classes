from identification import id
class student:
    number_of_students = 0
    def __init__(self,name,age,subjects,student_class):
        self.name = name
        self.age = age
        self.subjects = subjects
        self.std_id = id(student_class)
        student.number_of_students += 1
    @classmethod
    def create_student_profile(cls,students_info):
        name, age, subjects, student_class = students_info.split('-')
        age = int(age)
        student_class = int(student_class)
        subjects = subjects.split(',')
        subjects[2] = subjects[2].replace('\n','')
        return cls(name, age, subjects, student_class)
_stdts_ = {}
keys = []
with open('Students.txt','r') as students:
    for index,line in enumerate(students,1):
        students_info = line
        stdt = student.create_student_profile(students_info)
        _stdts_[stdt.std_id] = stdt
        keys.append(stdt.std_id)
for key in keys:
    print( key,', ',_stdts_[key])