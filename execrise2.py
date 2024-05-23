# Given three lists, find the common elements among them.

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# list3 = [5, 6, 7, 8, 9]
#
# new_list=[]
# for element in list1:
#     if element in list2 and element in list3:
#         new_list.append(element)
#
# print(new_list)





# Merge two dictionaries and sum the values of common keys.

# dict1 = {'a': 10, 'b': 20, 'c': 30}
# dict2 = {'b': 15, 'c': 25, 'd': 35}
# new_dict=dict1.copy()
#
# for key,value in dict2.items():
#     if key in new_dict:
#         new_dict[key]+=value
#     else:
#         new_dict[key]=value
# print(new_dict)





# Remove duplicates from a list while maintaining the order of elements

# list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
# unique_list = []
# for i in list_with_duplicates:
#     if i not in unique_list:
#         unique_list.append(i)
# print(unique_list)





# Compute the Cartesian product of two tuples.

# tuple1 = (1, 2)
# tuple2 = ('a', 'b')
# tuple3=[]
# for i in tuple1:
#     for j in tuple2:
#         r=(i,j)
#         tuple3.append(r)
# print(tuple3)





# Group elements of a list based on their first letter using a dictionary.

# words = ["apple", "banana", "cherry", "avocado", "blueberry", "cranberry"]
# grouped_words = {}
# for i in words:
#     first_letter=i[0]
#     if first_letter not in grouped_words:
#         grouped_words[first_letter]=[]
#
#     grouped_words[first_letter].append(i)
# print(grouped_words)





# Find all pairs of numbers in a list that sum up to a given value.

# numbers = [1, 2, 3, 4, 5, 6,7,9]
# target_sum = 7
#
# pairs = []
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target_sum:
#             pairs.append((numbers[i], numbers[j]))
#
# print(pairs)





# Given a list of numbers, find the missing elements within a given range.

# numbers = [1, 3, 5, 7, 9]
# missing_num=[]
# for i in range(11):
#     if i not in numbers:
#         missing_num.append(i)
# print(missing_num)




# Flatten a nested list (a list of lists) into a single list.

# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
#
# flattened_list = []
# for sublist in nested_list:
#     for item in sublist:
#         flattened_list.append(item)
#
# print(flattened_list)




# Count Frequency of Elements in a List

# elements = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
#
# frequency = {}
# for element in elements:
#     if element in frequency:
#         frequency[element] += 1
#     else:
#         frequency[element] = 1
#
# print(frequency)




# Given a 2D matrix (list of lists), transpose it.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transposed_matrix = []
for i in range(len(matrix[0])):
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    transposed_matrix.append(new_row)

print(transposed_matrix)






# Merge Two Lists into a Dictionary

# keys = ['a', 'b', 'c']
# values = [1, 2, 3]
#
# merged_dict = {}
# for i in range(len(keys)):
#     merged_dict[keys[i]] = values[i]
#
# print(merged_dict)




# Convert a list of tuples into a dictionary where each tuple contains a key-value pair.

# tuple_list = [('a', 1), ('b', 2), ('c', 3)]
#
# dictionary = {}
# for key, value in tuple_list:
#     dictionary[key] = value
#
# print(dictionary)





# Given a list of dictionaries, merge them into a single dictionary. If there are duplicate keys, sum their values.
# dict_list = [{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'a': 2, 'c': 1}]
#
# merged_dict = {}
# for d in dict_list:
#     for key, value in d.items():
#         if key in merged_dict:
#             merged_dict[key] += value
#         else:
#             merged_dict[key] = value
#
# print(merged_dict)