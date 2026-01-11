
# End of PythonTraining.py
# Additional comment: This is a simple addition operation in Python.
# Additional comment: This is a simple addition operation in Python.
# Additional comment: This is a simple addition operation in Python.
# Additional comment: This is a simple addition operation in Python.
# Additional comment: This is a simple addition operation in Python.

string_example = "hello, world!"
string_length = len(string_example)
print("The length of the string is:", string_length)
print("This line was added later.", string_example[0:2])
print("This line was added later.", string_example[0:string_length:2])
new_string = string_example.capitalize()
print("Capitalized string:", new_string)
new_string = string_example.islower()
print("Is the string lowercase?", new_string)
new_string = string_example.replace("world", "Python")
new_string = string_example[0:5]
print("Replaced string:", new_string)
list_example = [1, 2, 3, 4, 5]
#print("Original list:", list_example.count())
tuple_example = (10, 20, 30, 40, 50)
print("Tuple example:", tuple_example.index(30))
print("tuple", tuple_example[0])
tuple_example = tuple_example + tuple_example
print("Combined tuple and list:", tuple_example)    
set_example = {100, 200, 300, 400, 500}

