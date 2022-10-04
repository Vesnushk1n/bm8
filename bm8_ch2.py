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

students = [
{ 'id': 1, 'name':'Max', 'surname':'Brooks', 'age': 24, 'city':'Spb'},
{'id': 2, 'name':'John', 'surname':'Stones', 'age': 15, 'city':'Spb'},
{'id': 3, 'name':'Andy', 'surname':'Wings', 'age': 45, 'city':'Manchester'},
{'id': 4, 'name':'Kate', 'surname':'Brooks', 'age': 34, 'city':'Spb'}
]

courses = [
{'id':1, 'name':'python', 'data_start':'21.07.21', 'data_end':'21.08.21'},
{'id':2, 'name':'java', 'data_start':'13.07.21', 'data_end':'16.08.21'}
]

student_courses = [
{ 'student_id': 1, 'course_id': 1},
{ 'student_id': 2, 'course_id': 1},
{ 'student_id': 3, 'course_id': 1},
{ 'student_id': 4, 'course_id': 2}
]

Students.insert_many(students).execute()
Courses.insert_many(courses).execute()
Student_Courses.insert_many(student_courses).execute()

a = Students.select().where(Students.age > 30)
for info in a:
    print(info.name, info.surname)

b = Students.select().join(Student_Courses).join(Courses).where(Courses.name == 'python')
for info in b:
    print(info.name, info.surname)

c = Students.select().join(Student_Courses).join(Courses).where((Courses.name == 'python') & (Students.city == 'Spb'))
for info in c:
    print(info.name, info.surname)
