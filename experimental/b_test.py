#!/usr/bin/python3

# from collections import OrderedDict
# import json

# def load_data():
#     try:
#         with open('data.json', 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return {}

# def save_data(data):
#     with open('data.json', 'w') as file:
#         json.dump(data, file)

# my_dict = load_data()

# key = input("Enter a key: ")
# value = int(input("Enter a value: "))

# my_dict[key] = value
# save_data(my_dict)
# print(my_dict)

# json.loads()

import json

json_string = '{"name":"Winnie", "age":23}'
py_dict = json.loads(json_string)
print(py_dict)