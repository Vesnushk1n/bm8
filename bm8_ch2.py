from peewee import *
con = SqliteDatabase('data')

class Courses (Model):
    id = PrimaryKeyField(column_name='id', unique=True)
    name = CharField(column_name = 'name')
    data_start = CharField(column_name = 'data_start')
    data_end = CharField(column_name = 'data_end')

    class Meta:
        database = con
Courses.create_table()

class Students (Model):
    id = PrimaryKeyField(column_name='id', unique=True)
    name = CharField(column_name= 'name')
    surname = CharField(column_name= 'surname')
    age = IntegerField(column_name= 'age')
    city = CharField(column_name= 'city')

    class Meta:
        database = con
Students.create_table()

class Student_Courses (Model):
    student_id = ForeignKeyField(Students, column_name='student_id')
    course_id = ForeignKeyField(Courses, column_name='course_id')

    class Meta:
        database = con

Student_Courses.create_table()

students = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
            (3, 'Andy', 'Wings', 45, 'Manhester'),(4, 'Kate', 'Brooks', 34, 'Spb')]

courses = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]

student_courses = [(1, 1), (2, 1), (3, 1), (4, 2)]

Students.insert_many(students).execute()
Courses.insert_many(courses).execute()
Student_Courses.insert_many(student_courses).execute()

a = Students.get(Students.age > 30)
b = Courses.get(Courses.name == 'python')
c = Students.get(Students.city == 'Spb') and Courses.get(Courses.name == 'python')