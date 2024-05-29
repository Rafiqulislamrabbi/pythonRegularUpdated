# l=[2,7,11,15]
# target = 9
# for i in l:
#     for j in l:
#         if i+j==target:
#             print(l.index(i),l.index(j))


# n = [1,2,1,1,5,6,6]
# new_list=[]
# for i in n:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)


# l=[1,2,3,4,5,6,7]
# count=0
# for _ in l:
#     count+=1
# print(count)


#
# a="rabbi"
# print(a[::-1])


# a = 'python oop course'
# d={}
# for i in a:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
#
# sorting = sorted(d.items(), key=lambda kv:kv[1], reverse=True)
#
#
#
# print(sorting[0][0])


# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#     def get_salary(self):
#         return f'{self.name} salary is {self.salary}'
#
# employee1 = Employee('rafiq', 20000)
# employee2 = Employee('shamrat', 20000)
#
# print(employee1.get_salary())
# print(employee2.get_salary())
# print(employee1.name)
# print(employee2.name)
# print(employee1.salary)
# print(employee2.salary)


# class CardPayment:
#     def make_payment(self):
#         print('pay with card')
#
#
# class CashPayment:
#     def make_payment(self):
#         print('pay with cash')
#
#
# class Rocket:
#     def make_payment(self):
#         print('pay with rocket')
#
#
# card_pay = CardPayment()
# cash_pay = CashPayment()
# rocket_pay = Rocket()
#
#
# def pay():
#     for i in [card_pay, cash_pay, rocket_pay]:
#         i.make_payment()


# pay()


class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def work(self):
        return f"{self.name} is working"

    def get_salary(self):
        return f"{self.name} is getting salary {self.salary}"


class Manager(Employee):
    def __init__(self, name, id, salary, department):
        super().__init__(name, id, salary)
        self.department = department

    def work(self):
        return f"{self.name} is managing {self.department} department"


class Engineer(Employee):
    def __init__(self, name, id, salary, specialty):
        super().__init__(name, id, salary)
        self.specialty = specialty

    def work(self):
        return f"{self.name} has specialty in {self.specialty}"


manager = Manager('Samrat', 1, 1000, 'Finance')
engineer = Engineer("Rafiq", 2, 2000, 'IT')

for employee in [manager, engineer]:
    print(employee.work())
