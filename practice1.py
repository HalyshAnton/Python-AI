class Person:
    def __init__(self, name, age, gender):
        self._name = name
        self._age = age
        self._gender = gender

    def get_name(self):
        return self._name


class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self._student_id = student_id

    def get_id(self):
        return self._student_id

    def set_id(self, new_id):
        self._student_id = new_id

    def get_info(self, objects):
        print(f'Студент {self._name} вивчає:')

        for i, object in enumerate(objects):
            print(f'{i+1}. {object}')
        '''
        for i in range(len(objects)):
            object = objects[i]
        '''


class Teacher(Person):
    def __init__(self, name, age, gender, employee_id):
        super().__init__(name, age, gender)
        self._employee_id = employee_id
        self._students = []

    def get_id(self):
        return self._employee_id

    def set_id(self, new_id):
        self._employee_id = new_id

    def add_student(self, student:Student):
        self._students.append(student)

    def add_grade(self, grade):
        for student in self._students:
            print(f'{student.get_name()} отримав {grade}')


student1 = Student('John', 27, 'male', '00012345')
student2 = Student('Mike', 27, 'male', '00012345')

#student.get_info(['Math', 'Python', 'C++'])
teacher = Teacher('Anna', 35, 'female', '999789456')
teacher.add_student(student1)
teacher.add_student(student2)

teacher.add_grade(12)
