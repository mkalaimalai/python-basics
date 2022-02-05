from School import Clasz, Grade, Student, Subject, Marks

# Create Students
john = Student("John")
ram = Student("Ram")
sam = Student("Sam")

# Create Student Marks

john_marks = {Subject.Math: 95, Subject.English: 90}
ram_marks = {Subject.Math: 65, Subject.English: 60}
sam_marks = {Subject.Math: 55, Subject.English: 70}

# Create Class Marks for all students
grade_1_marks = [john_marks, ram_marks, sam_marks]

# Students in a class
students = [john, ram, sam]

# Creating a class
first_class = Clasz(Grade.I, students, grade_1_marks)

# Get Average marks of a suject, here it is for Math subject
marks: Marks = first_class.calculate_marks(Subject.Math)

# Printing the marks details
print(marks.total, marks.avg, marks.maximum, marks.minimum, marks.subject_total, marks.subject_avg, marks.subject_max, marks.subject_min)

