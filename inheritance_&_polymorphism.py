# class LibraryItem:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         self.is_available = True
#
#     def display_info(self):
#         print(f"Title: {self.title}, Author: {self.author}, Available: {self.is_available}")
#
#     def check_out(self):
#         if self.is_available:
#             self.is_available = False
#             print(f"{self.title} checked out.")
#         else:
#             print(f"{self.title} is not available.")
#
#     def return_item(self):
#         self.is_available = True
#         print(f"{self.title} returned.")
#
# class Book(LibraryItem):
#     def __init__(self, title, author, isbn):
#         super().__init__(title, author)
#         self.isbn = isbn
#
#     def display_info(self):
#         super().display_info()
#         print(f"ISBN: {self.isbn}")
#
# class Magazine(LibraryItem):
#     def __init__(self, title, author, issue_number):
#         super().__init__(title, author)
#         self.issue_number = issue_number
#
#     def display_info(self):
#         super().display_info()
#         print(f"Issue Number: {self.issue_number}")
#
# class DVD(LibraryItem):
#     def __init__(self, title, director, duration):
#         super().__init__(title, director)
#         self.duration = duration
#
#     def display_info(self):
#         super().display_info()
#         print(f"Director: {self.author}, Duration: {self.duration} minutes")
#
# # Test the system
# book = Book("1984", "George Orwell", "123456789")
# # magazine = Magazine("Nature", "Various Authors", "2023-05")
# # dvd = DVD("Inception", "Christopher Nolan", 148)
#
# items = [book]
#
# for item in items:
#     item.display_info()
#     item.check_out()
#     item.display_info()
#     item.return_item()
#     item.display_info()









# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     def calculate_bonus(self):
#         return self.salary * 0.1
#
#     def display_info(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")
#
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#
#     def calculate_bonus(self):
#         return self.salary * 0.2
#
#     def display_info(self):
#         super().display_info()
#         print(f"Department: {self.department}")
#
# class Developer(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, salary)
#         self.programming_language = programming_language
#
#     def display_info(self):
#         super().display_info()
#         print(f"Programming Language: {self.programming_language}")
#
# # Test the system
# manager = Manager("Alice", 80000, "HR")
# # developer = Developer("Bob", 60000, "Python")
#
# employees = [manager]
#
# for employee in employees:
#     employee.display_info()
#     print(f"Bonus: {employee.calculate_bonus()}\n")








# class Versity:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
# class Teacher(Versity):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department
#
#     def get_salary(self):
#         print(f"Teacher name is {self.name} and salary is {self.salary}. Department is {self.department}")
#
# class Student(Versity):
#     def __init__(self, name, salary, section):
#         super().__init__(name, salary)
#         self.section = section
#
#     def get_salary(self):
#         print(f"Student name is {self.name} and section is {self.section}.")
#
# teacher = Teacher("Sahin", 20000, "CSE")
# student = Student("Rafiq", 12, "A")
#
# for person in [teacher, student]:
#     person.get_salary()









# class Versity:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#
# class Teacher(Versity):
#     def __init__(self,name,salary,depertment):
#         super().__init__(name,salary)
#         self.depertment=depertment
#
#     def get_salary(self):
#         print(f"Teacher name is {self.name} and salary is {self.salary} .Depertment is {self.depertment}")
#
# class Student(Versity):
#     def __init__(self,name,salary,section,id):
#         super().__init__(name,salary)
#         self.section=section
#         self.id=id
#     def get_salary(self):
#         print(f"Student name is {self.name} section is {self.section} and id is {self.id}")
#
# teacher=Teacher("sahin",20000,"CSE")
# teacher1=Teacher("Virat",20000,"EEE")
# student=Student("Rafiq",12,"A",1)
# student1=Student("Samrat",12,"A",1)
#
# for i in [teacher,teacher1,student,student1]:
#     i.get_salary()








# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def display_info(self):
#         print(f"Product Name: {self.name}, Price: ${self.price:.2f}")
#
#     def calculate_discounted_price(self, discount_percentage):
#         return self.price * (1 - discount_percentage / 100)
#
# class Electronics(Product):
#     def __init__(self, name, price, brand, warranty_period):
#         super().__init__(name, price)
#         self.brand = brand
#         self.warranty_period = warranty_period
#
#     def display_info(self):
#         super().display_info()
#         print(f"Brand: {self.brand}, Warranty Period: {self.warranty_period} years")
#
# class Clothing(Product):
#     def __init__(self, name, price, size, material):
#         super().__init__(name, price)
#         self.size = size
#         self.material = material
#
#     def display_info(self):
#         super().display_info()
#         print(f"Size: {self.size}, Material: {self.material}")
#
# class Book(Product):
#     def __init__(self, name, price, author, isbn):
#         super().__init__(name, price)
#         self.author = author
#         self.isbn = isbn
#
#     def display_info(self):
#         super().display_info()
#         print(f"Author: {self.author}, ISBN: {self.isbn}")
#
# # Test the system
# electronics = Electronics("Smartphone", 699.99, "BrandX", 2)
# clothing = Clothing("T-shirt", 19.99, "L", "Cotton")
# book = Book("Python Programming", 39.99, "John Doe", "978-3-16-148410-0")
#
# products = [electronics, clothing, book]
#
# for product in products:
#     product.display_info()
#     discounted_price = product.calculate_discounted_price(10)














class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Name: {self.name}, Email: {self.email}")

class Student(Person):
    def __init__(self, name, email, student_id, grades):
        super().__init__(name, email)
        self.student_id = student_id
        self.grades = grades

    def calculate_gpa(self):
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}, GPA: {self.calculate_gpa():.2f}")

class Professor(Person):
    def __init__(self, name, email, employee_id, publications):
        super().__init__(name, email)
        self.employee_id = employee_id
        self.publications = publications

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}, Publications: {len(self.publications)}")

# Test the system
student = Student("Alice", "alice@example.com", "S12345", [3.5, 3.7, 4.0])
professor = Professor("Dr. Bob", "bob@example.com", "P98765", ["Paper1", "Paper2", "Paper3"])

people = [student, professor]

for person in people:
    person.display_info()
    print()
