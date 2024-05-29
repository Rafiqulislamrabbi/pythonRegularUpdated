# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))




# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])




# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])


# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list)



# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list)



# my_list = [1, 2, 3]
# my_list.insert(1, 10)
# print(my_list)



# my_list = [1, 2, 3, 4, 3]
# my_list.remove(3)
# print(my_list)



# my_list = [1, 2, 3, 4, 5]
# popped_element = my_list.pop(0)
# print(popped_element)
# print(my_list)
#
#
#
# my_list = [1, 2, 3, 4, 5]
# index = my_list.index(3)
# print(index)

#
#
# my_list = [1, 2, 3, 4, 3, 5]
# count = my_list.count(3)
# print(count)

#
#
# my_list = [1, 2, 3, 4, 5]
# my_list.reverse()
# print(my_list)

#
#
# my_list = [3, 1, 4, 2, 5]
# my_list.sort()
# print(my_list)



# thislist = ["apple", "banana", "cherry"]
# del thislist
#
#
#
#
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()
# print(thislist)




# my_list=["orange", "mango", "kiwi"]
# new_list=[]
#
# for i in my_list:
#     if "a" in i:
#         new_list.append(i)
# print(new_list)
#
#
#
#
# my_list=["orange", "mango", "kiwi"]
# new_list=[i for i in my_list if "a" in i]
# print(new_list)
#
#
#
#
#
# thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# thislist.sort()
# print(thislist)
#
#
#
#
# thislist = [100, 50, 65, 82, 23]
# thislist.sort(reverse = True)
# print(thislist)
#
#
#
# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort(key = str.lower)
# print(thislist)
#
#
#
# thislist = ["apple", "banana", "cherry"]
# mylist = thislist.copy()
# print(mylist)
#
#
#
# fruits = ['apple', 'banana', 'cherry']
# x = fruits.count("cherry")




# fruits = ['apple', 'banana', 'cherry']
# x = fruits.index("cherry")
# print(x)








# my_list= [100,200,300,400,"500"]
# string_numbers=[]
# for i in my_list:
#     if isinstance(i,str):
#         string_numbers.append(i)
# print(string_numbers)




# my_list= [100,200,300,400,50,35,111,155]
# for i in my_list:
#     if i>100 and i%2==0:
#         print(i)
#
#
#
#
# data = [("samrat", 10), ("rafiq", 10), ("mamun", 20), ("rafiq", 70), ("samrat", 50), ("azad", 50)]
# my_dict = {}
#
# for key, value in data:
#     if key in my_dict:
#         my_dict[key] += value
#     else:
#         my_dict[key] = value
#
# for key, total in my_dict.items():
#     if total >= 100:
#         print(key)




#
# l = ["rabbi 20", "rafiq 20", "aaaa 30", "rafiq 20"]
#
# sum_dict = {}
#
# for item in l:
#     key, value = item.split()
#     value = int(value)
#
#     if key in sum_dict:
#         sum_dict[key] += value
#     else:
#         sum_dict[key] = value
#
# for key, total_value in sum_dict.items():
#     if total_value > 20:
#         print(f"{key}: {total_value}")
#
#
#
# fruits=["fdf","apple","banana","cherry"]
# n=[ i.upper() for  i in fruits  ]
#
# print(n)
#
#
# n= ["banana", "Orange", "Kiwi", "cherry"]
# b=[]
# for i in n:
#     a=i.lower()
#     b.append(a)
#
# b.sort(reverse=True)
# print(b)
