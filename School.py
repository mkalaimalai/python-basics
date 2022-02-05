from enum import Enum
"""Python basics  coded for a School system with Class, Students, Subjects and Marks and methods to calculate  avg, 
max, main in a class and for a subject """


class Subject:
    Math = "Math"
    English = "English"


class Grade(Enum):
    I = 1
    II = 2
    III = 3
    IV = 4


class Student:
    def __init__(self, name):
        self.name = name


class Clasz:
    def __init__(self, grade, student: list, marks: list):
        self.grade = grade
        self.student = student
        self.marks = marks

    def calculate_marks(self, subject: Subject):
        total = 0
        total_count = 0
        maximum = 0
        minimum = 0
        subject_marks_total = 0
        subject_count = 0
        subject_max = 0
        subject_min = 0

        for student_marks in self.marks:
            for sub, mark in student_marks.items():
                total += mark
                total_count += 1
                if mark > maximum:
                    maximum = mark
                    minimum = mark
                elif mark < minimum:
                    minimum = mark
                if sub == subject:
                    subject_marks_total += mark
                    subject_count += 1
                    if mark > subject_max:
                        subject_max = mark
                    else:
                        subject_min = mark
        marks: Marks =  Marks(total, total / total_count, maximum, minimum, subject_marks_total, subject_marks_total / subject_count, subject_max, subject_min)
        return marks

    def subject_avg_marks(self, subject):
        subject_marks_total = 0
        student_count = 0
        for student_marks in self.marks:
            for sub, mark in student_marks.items():
                if sub == subject:
                    subject_marks_total += mark
                    student_count += 1
        return subject_marks_total / student_count


class Marks:
    def __init__(self, total, avg, maximum, minimum, subject_total, subject_avg, subject_max, subject_min):
        self.total = total
        self.avg = avg
        self.maximum = maximum
        self.minimum = minimum
        self.subject_total = subject_total
        self.subject_avg = subject_avg
        self.subject_max = subject_max
        self.subject_min = subject_min



