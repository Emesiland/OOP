class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecture_grades = {}

    def add_lecture_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total_sum = sum(sum(grade_list) for grade_list in self.grades.values())
        total_count = sum(len(grade_list) for grade_list in self.grades.values())
        return round(total_sum / total_count, 1) if total_count > 0 else 0.0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов.")
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов.")
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только студентов.")
        return self.average_grade() == other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total_sum = sum(sum(grade_list) for grade_list in self.grades.values())
        total_count = sum(len(grade_list) for grade_list in self.grades.values())
        return round(total_sum / total_count, 1) if total_count > 0 else 0.0

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов.")
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов.")
        return self.average_grade() > other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только лекторов.")
        return self.average_grade() == other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
 
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_lecturer = Lecturer('Jim', 'Green')
cool_lecturer.courses_attached += ['Python']
 
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
 
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)

best_student.add_lecture_grade(cool_lecturer, 'Python', 5)
best_student.add_lecture_grade(cool_lecturer, 'Python', 7)
best_student.add_lecture_grade(cool_lecturer, 'Python', 9)

print(f'Оценки студента: {best_student.grades}')
print(f'Оценки лектора: {cool_lecturer.grades}')

student1 = Student('Ivan', 'Ivanov', 'Male')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в Python']

student2 = Student('Kate', 'Mamaeva', 'Female')
student2.courses_in_progress += ['Python', 'Java'] 
student2.finished_courses += ['Алгоритмы и структуры данных']

reviewer1 = Reviewer('Some', 'Buddy')
reviewer1.courses_attached += ['Python', 'Git']

lecturer1 = Lecturer('Jim', 'Green')
lecturer1.courses_attached += ['Python', 'Git']

lecturer2 = Lecturer('Anna', 'Blue')
lecturer2.courses_attached += ['Python', 'Java'] 

reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Git', 8)
reviewer1.rate_hw(student1, 'Git', 9)

reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Java', 9) 

student1.add_lecture_grade(lecturer1, 'Python', 7)
student1.add_lecture_grade(lecturer1, 'Python', 8)
student1.add_lecture_grade(lecturer1, 'Python', 9)

student2.add_lecture_grade(lecturer2, 'Python', 6)
student2.add_lecture_grade(lecturer2, 'Java', 7)

print(student1)
print(student2)
print(reviewer1)
print(lecturer1)
print(lecturer2)

if student1 > student2:
    print("Первый студент лучше второго")
elif student1 < student2:
    print("Второй студент лучше первого")
else:
    print("Они равны")

if lecturer1 > lecturer2:
    print("Первый лектор лучше второго")
elif lecturer1 < lecturer2:
    print("Второй лектор лучше первого")
else:
    print("Они равны")