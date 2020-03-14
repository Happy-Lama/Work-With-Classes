class student:
    number_of_students = 0
    def __init__(self,name,age,subjects):
        self.name = name
        self.age = age
        self.subjects = subjects
        student.number_of_students += 1
    @classmethod
    def create_student_profile(cls,student_info):
        name, age ,subjects = student_info.split('-')
        age = int(age)
        subjects = subjects.split(',')
        subjects[2] = subjects[2].replace('\n','')
        return cls(name, age, subjects)
std_number = {}
keys = []
index = 1
students = open('Students.txt','r')
for line in students:
    students_info = line
    std_number['Std_{}'.format(index)] = student.create_student_profile(students_info)
    keys.append('Std_{}'.format(index))
    index += 1
students.close()