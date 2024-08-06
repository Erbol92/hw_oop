class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and list(set(lecturer.courses_attached) & set(self.courses_in_progress)) and course in self.courses_in_progress:
            if lecturer.grades.get(course, None):
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            print('вы не можете оценить преподавателя')

    def __str__(self):
        total = self.get_score()
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {round(total, 1)} \nКурсы в процессе изучения:{", ".join(self.courses_in_progress)} \nЗавершенные курсы:{", ".join(self.finished_courses)}'

    def get_score(self):
        total = float(0)
        if self.grades:
            for value in self.grades.values():
                total += sum(value)
            total = total/len(self.grades)
        return total

    def __lt__(self, other):
        return self.get_score() < other.get_score()

    def __le__(self, other):
        return self.get_score() <= other.get_score()

    def __gt__(self, other):
        return self.get_score() > other.get_score()

    def __ge__(self, other):
        return self.get_score() >= other.get_score()

    def __eq__(self, other):
        return self.get_score() == other.get_score()

    def __ne__(self, other):
        return self.get_score() != other.get_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, *args):
        Mentor.__init__(self, *args)
        self.grades = {}

    def get_score(self):
        total = float(0)
        if self.grades:
            for value in self.grades.values():
                total += sum(value)
            total = total/len(self.grades)
        return total

    def __lt__(self, other):
        return self.get_score() < other.get_score()

    def __le__(self, other):
        return self.get_score() <= other.get_score()

    def __gt__(self, other):
        return self.get_score() > other.get_score()

    def __ge__(self, other):
        return self.get_score() >= other.get_score()

    def __eq__(self, other):
        return self.get_score() == other.get_score()

    def __ne__(self, other):
        return self.get_score() != other.get_score()

    def __str__(self):
        total = self.get_score()
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {round(total, 1)}'


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка', student.name, course)


# первый студент
some_student_1 = Student('Some', 'Buddy', 'м')
some_student_1.finished_courses = ['Основы Git']
some_student_1.courses_in_progress = ['Python', 'Java']
print(some_student_1)

# второй студент
some_student_2 = Student('Emma', 'Down', 'ж')
some_student_2.finished_courses = ['Введение в программирование']
some_student_2.courses_in_progress = ['Python', 'Git']
print(some_student_2)

# первый лектор
lecturer_1 = Lecturer('Albert', 'Einstein')
lecturer_1.courses_attached = ['Python']
print(lecturer_1)

# второй лектор
lecturer_2 = Lecturer('Nikola', 'Tesla')
lecturer_2.courses_attached = ['Git']
print(lecturer_2)

# первый ревьювер
reviewer_1 = Reviewer('Jonny', 'Monny')
reviewer_1.courses_attached = ['Python']
print(reviewer_1)

# второй ревьювер
reviewer_2 = Reviewer('Bob', 'Marley')
reviewer_2.courses_attached = ['Git']
print(reviewer_2)

# проверка методов
some_student_1.rate_lecturer(lecturer_1, 'Git', 10)  # несотв. лектора и курса
some_student_1.rate_lecturer(lecturer_1, 'Python', 8)
some_student_2.rate_lecturer(lecturer_1, 'Python', 10)
some_student_2.rate_lecturer(lecturer_2, 'Git', 5)
print('Оценки 1-го преподавателя', lecturer_1.grades)

reviewer_1.rate_hw(some_student_1, 'Python', 7)
reviewer_1.rate_hw(some_student_1, 'Git', 7)
print(f'Оценки 1-го студента {some_student_1.grades}')

reviewer_2.rate_hw(some_student_2, 'Git', 9)
reviewer_1.rate_hw(some_student_2, 'Python', 6)
print(f'Оценки 2-го студента {some_student_2.grades}')

# сравнение студентов
print(some_student_1.get_score(), some_student_2.get_score())
print(some_student_1 > some_student_2)
print(some_student_1 == some_student_2)
print(some_student_1 < some_student_2)

# сравнение лекторов
print(lecturer_1.get_score(), lecturer_2.get_score())
print(lecturer_1 > lecturer_2)
print(lecturer_1 == lecturer_2)
print(lecturer_1 < lecturer_2)

# методы подсчета средней оценки


def average_rating_hw(students: list, course: str):
    rating, count = 0, 0
    for student in students:
        if student.grades.get(course, None):
            rating += sum(student.grades[course])
            count += 1
    return rating/count if count != 0 else 'нет данных'


def average_rating_lr(lectors: list, course: str):
    rating, count = 0, 0
    for lector in lectors:
        if lector.grades.get(course, None):
            rating += sum(lector.grades[course])
            count += 1
    return rating/count if count != 0 else 'нет данных'


print(average_rating_hw([some_student_1, some_student_2], 'Python'))
print(average_rating_hw([some_student_1, some_student_2], 'Git'))
print(average_rating_hw([some_student_1, some_student_2], 'Java'))
print()
print(average_rating_lr([lecturer_1, lecturer_2], 'Python'))
print(average_rating_lr([lecturer_1, lecturer_2], 'Git'))
print(average_rating_lr([lecturer_1, lecturer_2], 'Java'))
