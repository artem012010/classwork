class Student():
   def __init__(self, name, average_grade):
       self.name = name
       self.average_grade = average_grade  
       self.course = '-'
   def print_info(self):
       print('Студент(-ка)', self.name)
       print('Имеет средний балл:', self.average_grade)
       print('Посещает курс по выбору:', self.course)
   def select_course(self):
       course = input('Введите название курса:')
       self.course = course

student = Student('Степанова Дарья', '4.8')
student.print_info()
student.select_course()
student.print_info()

