class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda student: student.cgpa,reverse=True)
  return sorted_students


students = [
    Student("Sarathi", "22CS12", 8.5),
    Student("Jaya", "22CS13", 7.9),
    Student("Imran", "22CS14", 8.1),
    Student("Ananth", "22CS15", 9.2),
]

sorted_students = sort_students(students)


for student in sorted_students:
  print("\nName: {}| Roll Number: {}| CGPA: {}".format(student.name,student.roll_number,student.cgpa))

print("\nSayonera")