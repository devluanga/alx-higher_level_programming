 			0x04. Python - More Data Structures: Set, Dictionary

Certainly! Let's explore more about sets and dictionaries in Python.

**Set**:
A set is an unordered collection of unique elements. It is represented by curly braces `{}` or by using the `set()` function. Sets are useful when you want to store a collection of items where uniqueness is important, and the order of the elements doesn't matter.

Here's an example of creating a set:

	fruits = {"apple", "banana", "orange"}
	print(fruits)  # {'orange', 'banana', 'apple'}


You can also create a set from a list using the `set()` function:

	numbers = set([1, 2, 3, 4, 5])
	print(numbers)  # {1, 2, 3, 4, 5}

Sets support various operations like union, intersection, difference, and more. Here are a few examples:


	set1 = {1, 2, 3}
	set2 = {3, 4, 5}

	union = set1.union(set2)  # {1, 2, 3, 4, 5}
	intersection = set1.intersection(set2)  # {3}
	difference = set1.difference(set2)  # {1, 2}

You can add elements to a set using the `add()` method:


	fruits.add("mango")
	print(fruits)  # {'orange', 'banana', 'apple', 'mango'}


And you can remove elements using the `remove()` method:


	fruits.remove("banana")
	print(fruits)  # {'orange', 'apple', 'mango'}


**Dictionary**:

A dictionary is an unordered collection of key-value pairs. It is represented by curly braces `{}` and consists of keys and their corresponding values. Each key-value pair is separated by a colon `:`. 
Dictionaries are useful when you want to store data in a structured manner, where each piece of data has a unique identifier (key).

Here's an example of creating a dictionary:


	person = {"name": "John", "age": 25, "city": "New York"}
	print(person)  # {'name': 'John', 'age': 25, 'city': 'New York'}


You can access the values in a dictionary by specifying the corresponding key:


	print(person["name"])  # John
	print(person["age"])  # 25

You can also modify the values or add new key-value pairs:


	person["age"] = 30  # Modifying the 'age' value
	person["occupation"] = "Engineer"  # Adding a new key-value pair
	print(person)  # {'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}


Dictionaries also provide methods to retrieve keys, values, or both:


	keys = person.keys()  # returns dict_keys(['name', 'age', 'city', 'occupation'])
	values = person.values()  # returns dict_values(['John', 30, 'New York', 'Engineer'])
	items = person.items()  # returns dict_items([('name', 'John'), ('age', 30), ('city', 'New York'), ('occupation', 'Engineer')])
	

You can remove a key-value pair using the `del` statement:


	del person["city"]
	print(person)  # {'name': 'John', 'age': 30, 'occupation': 'Engineer'}


These are some basic operations and methods that this directory will be handling
