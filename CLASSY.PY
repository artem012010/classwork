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


class Rectangle():
   def __init__(self, length, width):
       self.length = length
       self.width = width
   def print_info(self):
       print('Дан прямоугольник с длиной', self.length, 'и шириной', self.width)
   def calc_perimeter(self):
       self.perimeter = (self.length + self.width) * 2
       return self.perimeter
   def calc_area(self):
       self.area = self.length * self.width
       return self.area
 
a = int(input('Введите длину:'))
b = int(input('Введите ширину:'))
rect = Rectangle(a, b)
rect.print_info()
print('Его периметр:', rect.calc_perimeter())
print('Его площадь:', rect.calc_area())

