import sqlite3
con = sqlite3.connect('data.db')
cursor = con.cursor()
#cursor.execute('CREATE TABLE Students (id int, name varchar(20), surname varchar(20), age int, city varchar(20))')
#cursor.execute('CREATE TABLE Courses (id int, name varchar(20), time_start, time_end)')
#cursor.execute('CREATE TABLE Student_courses (student_id int, course_id int)')

info_a = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
(3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')]

info_b = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]

info_c = [(1, 1), (2, 1), (3, 1), (4, 2)]

con.executemany('INSERT INTO Students (id, name, surname, age, city) VALUES (?, ?, ?, ?, ?)', info_a)
con.executemany('INSERT INTO Courses (id, name, time_start, time_end) VALUES (?, ?, ?, ?)', info_b)
con.executemany('INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)', info_c)

a = 30
b = 'python'
c = 'Spb'

cursor.execute('''SELECT Students.name, Students.surname FROM Students Where age > 30''')
cursor.execute('''SELECT * FROM Courses WHERE name="python"''')
cursor.execute('''SELECT * FROM Students JOIN Student_courses ON Students.id=Student_courses.student_id WHERE Student_courses.course_id = 1''')
cursor.execute('''SELECT Students.name, Students.surname FROM Students
JOIN Student_Courses ON Student_courses.student_id = Students.id
JOIN Courses ON Student_courses.course_id = Courses.id
WHERE Courses.name = \'python\' AND Students.city = \'Spb\'''')
data = cursor.fetchall()
print(data)
con.commit()
con.close()