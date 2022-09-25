import sqlite3
con = sqlite3.connect('data.db')
cursor = con.cursor()
# con.execute('CREATE TABLE Students (id varchar(20), name varchar(20), surname varchar(20), age int, city varchar(20))')
# con.execute('CREATE TABLE Courses (id varchar(20), name varchar(20), time_start, time_end)')
# con.execute('CREATE TABLE Student_courses (student_id, course_id)')

info_a = [(1, 'Max', 'Brooks', 24, 'Spb'), (2, 'John', 'Stones', 15, 'Spb'),
(3, 'Andy', 'Wings', 45, 'Manhester'), (4, 'Kate', 'Brooks', 34, 'Spb')]

info_b = [(1, 'python', '21.07.21', '21.08.21'), (2, 'java', '13.07.21', '16.08.21')]

info_c = [(1, 1), (2, 1), (3, 1), (4, 2)]

con.executemany('INSERT INTO Students (id, name, surname, age, city) VALUES (?, ?, ?, ?, ?)', info_a)
con.executemany('INSERT INTO Courses (id, name, time_start, time_end) VALUES (?, ?, ?, ?)', info_b)
con.executemany('INSERT INTO Student_courses (student_id, course_id) VALUES (?, ?)', info_c)

a = con.execute('SELECT surname FROM Students')
print(a.fetchall())
con.commit()
con.close()