""0x08. Python - More Classes and Objects""

""Attributes:"" In Python, attributes are the variables that are associated with a particular object or class.
They store data and represent the state of the object. Attributes can be accessed and modified using dot notation.

""Methods:"" Methods are functions that are defined within a class and operate on objects of that class. 
They perform specific actions or provide functionality associated with the class. Methods can access and manipulate the attributes of an object.

""The __init__ Method:""
The __init__ method is a special method in Python classes that is automatically called when an object is created from a class.
It is used to initialize the attributes of the object. The __init__ method allows you to define the initial state of the object.


""Data Abstraction, Data Encapsulation, and Information Hiding"": 

These concepts are related to the principle of encapsulation in object-oriented programming. 

Data abstraction refers to the process of hiding the internal details and complexity of an object and 

exposing only the essential information or functionality. Data encapsulation is the bundling of data and 

methods within a class, providing the concept of data hiding and access control.


""__str__ "" and ""__repr__"" Methods: 

These are special methods in Python classes that provide string representations of objects. 

The __str__ method returns a human-readable string representation of the object, 

    while the __repr__ method returns an official string representation that can be used to recreate the object.

""Public, Protected, and Private Attributes:"" 

Attribute visibility can be controlled using naming conventions. 

By convention, attributes that are intended to be publicly accessible are prefixed with a single underscore (e.g., _attribute). 

Protected attributes are prefixed with a double underscore (e.g., __attribute), indicating that they should not be accessed directly outside the class.

Private attributes are prefixed with a double underscore and suffixed with a single underscore (e.g., __attribute__), 
	indicating that they are strongly private and should not be accessed or modified directly.


	""Destructor"": In Python, the destructor is a special method named __del__ that is automatically called 

	when an object is about to be destroyed or garbage collected. 

	It can be used to perform cleanup operations or release resources before the object is removed from memory.
