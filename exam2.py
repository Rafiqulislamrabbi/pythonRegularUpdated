# 2. Create a Python program that uses a while loop to calculate the sum of the first 20 natural numbers.

# n=20
# sum=0
# while n>=0:
#     sum+=n
# print(sum)




# 3. Write a program that prints the following pattern using nested loops
#   *
#   **
#   ***
#   ****
#   *****


# n=4
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*", end='')
#     print(' ')




# 4. Write a program to print all even numbers between 1 and 50 using a for loop and an if    statement.

# for i in range(51):
#     if i % 2 == 0:
#         print(i)




# 5. Define a function greet that takes a name as an argument and prints a greeting message.

# def my_func(name):
#     print(f'my name is {name}')
#
# my_func('Rafiq')




# 6.Write a function factorial that takes an integer as input and returns its factorial.

# n=4
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)






# 7. Create a function power that takes two arguments, a base and an exponent, and returns the base raised to the power of the exponent. The exponent should have a default value of 2.


# def power(base, exponent=2):
#     return base ** exponent
#
# print(power(3))
#




# 8. Write a function find_max that takes any number of numerical arguments and returns the maximum value.

# def find_max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print(find_max(1,2))





# 9. Write a lambda function to add 10 to a given number.

# a=lambda:sum(range(10))
# print(a())







# 11. Write down a class that will have 3 methods, add, find, and remove method. For add method it will take two parameter, one is short url and another is a long url. You have to keep it as a key , value pair. A short url will be the key and a long url will be value. For the find method take a short url as a parameter and find it and return it.  For the find method take a short url as a parameter and remove it.

# class calculator:
#     def __init__(self,num):
#         self.num = num
#
#     def add(self,short_url,long_url):
#




# 12. Create an abstract base class Vehicle with an abstract method start_engine. Implement this method in two derived classes Car and Bike. Write a program to create instances of Car and Bike and call their start_engine methods.

# from abc import ABC, abstractmethod
# class Vehicle:
#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#
#
#     @abstractmethod
#     def start_engine(self):
#         pass
#
# class Car(Vehicle):
#     def __init__(self, model, year,price):
#         super().__init__(model, year)
#         self.price = price
#
#     def start_engine(self):
#         return f'Car model is {self.model}Year {self.year} and price {self.price}'
#
#
# class Bike(Vehicle):
#     def __init__(self, model, year,name):
#         super().__init__(model, year)
#         self.name = name
#
#     def start_engine(self):
#         return f'Car model is {self.model}Year {self.year} and name is {self.name}'
#
#
# car=Car('BMW','2021',1000000)
# bike=Bike('BMW','2021',500000)
#
# print(car.start_engine())
# print(bike.start_engine())




# 13. Create a class Animal with a method make_sound that prints "Some generic sound". Derive a class Dog from Animal and override the make_sound method to print "Bark". Demonstrate method overriding by creating an instance of Dog and calling the make_sound method.

# class Animal:
#     def __init__(self, name,sound):
#         self.name = name
#         self.sound = sound
#
#     def make_sound(self):
#         return self.sound
#
# class Dog(Animal):
#     def __init__(self, name,sound):
#         super().__init__(name,sound)
#     def make_sound(self):
#         return self.sound
#
# dog=Dog("Dog",'Bark')
# print(dog.make_sound())



# 14. Define two base classes Flyable and Swimmable with methods fly and swim respectively. Create a class Duck that inherits from both Flyable and Swimmable. Demonstrate calling both fly and swim methods using an instance of Duck.

# class Flyable:
#     def __init__(self,name):
#         self.name = name
#     def fly(self):
#         return f'{self.name} is flying'
#     def swim(self):
#         return f'{self.name} is swimming'
# class Swimmable:
#     def __init__(self,name):
#         self.name = name
#
#         def fly(self):
#             return f'{self.name} is flying'
#
#         def swim(self):
#             return f'{self.name} is swimming'
#
# class Duck(Flyable,Swimmable):
#     def __init__(self,name):
#         super().__init__(name)
#     def fly(self):
#         return f'{self.name} is flying'
#
#     def swim(self):
#         return f'{self.name} is swimming'
#
#
# duck = Duck('Duck')
# print(duck.fly())
# print(duck.swim())




# 15. Implement a class BankAccount with private attributes account_number and balance. Provide public methods to get the balance and deposit/withdraw money. Ensure that the balance cannot be accessed directly.

# class BankAccount:
#     def __init__(self,account_number,balance):
#         self.__account_number=account_number
#         self.__balance=balance
#
#     def get_the_balance(self):
#         return self.__balance
#     def deposit(self,amount):
#         self.__balance+=amount
#         return self.__balance
# bank_account=BankAccount("123456",100)
# print(bank_account.get_the_balance())
# print(bank_account.deposit(100))




# 16. Create a base class Printer with a method print_document that prints a generic message. Derive a class LaserPrinter that overrides the print_document method to print a message specific to laser printers. Demonstrate method overriding by creating instances of both Printer and LaserPrinter and calling their print_document methods.

# class Printer:
#     def __init__(self, name):
#         self.name = name
#
#     def print_documen(self):
#         print(f'Hello {self.name}')
#
# class LaserPrinter(Printer):
#     def __init__(self, name,price):
#         super().__init__(name)
#         self.price = price
#     def print_documen(self):
#         super().print_documen()
#         print(f'{self.name} price is {self.price}')
#
# printer= Printer("Samgsung")
# laser_printer=LaserPrinter("LG",10000)
# printer.print_documen()
# laser_printer.print_documen()



