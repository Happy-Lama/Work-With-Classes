from random import randint
def id(student_class):
    alphabet = ['A','B','C','D','E','F']
    id_no = ''
    while True:
        for index,char in enumerate(alphabet,1):
            if student_class == index:
                id_no = id_no + char
        for i in range(9):
            num = randint(0,9)
            id_no = id_no + str(num)
        return id_no