# 0x06. Python - Classes and Objects
## Resources
* [Object Oriented Programming](https://python.swaroopch.com/oop.html) (_Everything until the paragraph "Inheritance" excluded._)
* [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE&)
* [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
* [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)
## Summary
* **Python Programming**: Python is a powerful and versatile programming language known for its simplicity and readability. It allows developers to write code that is concise and easy to understand, making it an excellent choice for beginners and experienced programmers alike.
* **Object-Oriented Programming (OOP)**: OOP is a programming paradigm that organizes data and behavior into reusable structures called objects. It focuses on modeling real-world entities as objects, allowing for better code organization, reusability, and modularity.
* **"First Class Everything"**: In Python, the term "first class everything" means that objects, functions, and classes are all treated as first-class citizens. This means they can be passed as arguments, returned from functions, assigned to variables, and stored in data structures, just like any other value.
* **Class**: A class is a blueprint or template that defines the structure and behavior of objects. It defines the attributes (data) and methods (functions) that an object of that class will have.
* **Object and Instance:** An object is a particular instance of a class. When a class is instantiated (created), it becomes an object. Objects are created based on the structure defined by the class and can have their own unique state and behavior.
* **Difference between a Class and an Object/Instance:** A class is a blueprint or template that defines the structure and behavior of objects, while an object/instance is a specific occurrence of a class. In other words, a class defines the properties and methods that objects will have, while objects are created based on that class.
* **Attribute**: An attribute is a characteristic or property of an object. It represents the state or data associated with an object and can be either data (variables) or behavior (methods).
* **Public, Protected, and Private Attributes**: In Python, there is no strict mechanism for enforcing access control to attributes. By convention, attributes that start with a single underscore (`_`) are considered "protected" and should only be accessed within the class or its subclasses. Attributes that start with two underscores (`__`) are considered "private" and should not be accessed directly from outside the class.
* **Self**: `self` is a conventional name used in Python for the first parameter of instance methods. It refers to the instance of the class itself and is used to access the instance's attributes and methods within the class.
* **Method**: A method is a function defined within a class. It is called on an object and can access and manipulate the object's attributes.
* **The special** `__init__` **method**: The `__init__` method is a special method in Python classes that is automatically called when an object is created from a class. It is used to initialize the object's attributes and perform any necessary setup.
* **Data Abstraction, Data Encapsulation, and Information Hiding**: Data abstraction is the process of hiding the internal implementation details of an object while providing a clean and simple interface for interacting with it. Data encapsulation is the practice of bundling data and methods together in a class. Information hiding refers to the concept of hiding the internal details of how an object works to prevent direct access and potential misuse.
* **Property**: A property is a way to define getter and setter methods for a class attribute. It allows for controlled access and modification of attributes, enabling validation, and customization of attribute behavior.
* **Difference between an Attribute and a Property in Python**: An attribute is a data or behavior associated with an object, while a property is a special attribute that defines custom getter, setter, and deleter methods to control access and modification of other attributes.
* **Pythonic way to write getters and setters**: In Python, the `@property` decorator is commonly used to define a getter method, and the `@attribute_name.setter` decorator is used to define a setter method. This allows attributes to be accessed and modified using dot notation, like normal attributes, while allowing additional logic to be executed.
* **Dynamically Creating Arbitrary Attributes for Existing Instances**: Python allows you to dynamically create new attributes for existing instances by simply assigning a value to a new attribute name. The new attribute will then be available for that specific instance.
* **Binding Attributes to Objects and Classes**: Attributes in Python are dynamically bound, which means they can be added to objects or classes at any time. When an attribute is accessed, Python first checks if it exists in the object's namespace (if accessed via an object) or the class's namespace (if accessed via a class).
* `__dict__` **of a Class/Instance**: The `__dict__` attribute of a class or instance is a dictionary that contains the attributes and their corresponding values for that class or instance.
* **Attribute Lookup in Python**: When an attribute is accessed, Python first looks for it in the object's namespace. If not found, it looks in the class's namespace. If still not found, it goes up the inheritance chain until it either finds the attribute or raises an AttributeError.
* **Using the** `getattr()` **Function**: The `getattr()` function is a built-in function in Python that is used to get the value of an object's attribute dynamically. It is useful in situations where the attribute name is not known until runntime or when accessing attributes conditionally based on some runtime condition. It provides a flexible way to access object attributes dynamically.

## Tasks
0. **My first square** ([0-square.py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/0-square.py)): An empty class `Square` that defines a square

1. **Square with size** ([1-square..py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/1-square.py)): Defines a class `Square`. This class represents a square and has a private attribute called `__size` that represents the size of a side of the square. The class also has a constructor method `__init__` that initializes the square object with a given size. The `__size` attribute is set to the provided size value.
Overall, this code serves as a basic structure for creating square objects with a specified size.

2. **Size validation** ([2-square.py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/2-square.py)):
This class represents a square and has a private attribute `__size` that represents size of a side of the square. The class includes a constructor method `__init__` that initializes the square object with a given size. The size parameter has a default value of 0, and error handling is implemented to ensure that the size is a non-negative integer. If the size is not an integer or is less than 0, appropriate exceptions are raised.
This code provides a more robust implementation for creating square objects with valid sizes.

3. **Area of a square** ([3-square.py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/3-square.py)): Defines a class called `Square`. This class represents a square and includes attributes and methods to work with square objects. The class has a private attribute `__size` that represents the size of a side of the square. Constructor method __init__ initializes the square object with a given size, performing error checks to ensure the size is a non-negative integer. The class also includes a method `area` that calculates area of the square. This code provides a more robust implementation for creating square objects, handling errors, and calculating their areas.

4. **Access and update private attribute** ([4-square.py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/4-square.py)): Defines a `Square` class in Python. It represents a square and has a private attribute `__size` that stores the size of the square's side. The class includes a constructor method to initialize the square with a given size, a getter and setter method for the size attribute with type and value validation, and a method to calculate the area of the square. This code demonstrates encapsulation and validation techniques in object-oriented programming.

5. **Printing a square** ([5-square.py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/5-square.py)): The updated code defines a `Square` class in Python, representing a square shape. It includes attributes for the size of the square's side and methods for initializing the square, getting and setting the size, calculating the area, and printing the square using the `#` character. The code demonstrates encapsulation, validation, and additional functionality for the `Square` class.

6. **Coordinates of a square** ([6-square.py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/6-square.py)): The code defines a `Square` class in Python, representing a square shape. It includes attributes for the size of one edge of the square and the position of the square. The class has methods for initializing the square, getting and setting the size and position, calculating the area, and printing the square using the `#` character. The code demonstrates encapsulation, validation, and additional functionality for the `Square` class.

7. **Singly linked list** ([100-singly_linked_list](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/100-singly_linked_list.py)): The code defines two classes: `Node` and `SinglyLinkedList`.
The `Node` class represents a node of a singly linked list and has attributes for the data value of the node and a reference to the next node in the list. It includes getter and setter methods for the `data` and `next_node` attributes, with type validation.
The `SinglyLinkedList` class represents a singly linked list and has an attribute `__head` that points to the first node in the list. It includes a `__str__` method to define the print behavior of the linked list, returning a string representation of the data values in each node.
The `SinglyLinkedList` class also includes a `sorted_insert` method that inserts a new node with a given value into the linked list while maintaining the sorted order. It traverses the list to find the appropriate position for insertion and updates the `next_node` references accordingly.
Overall, this code provides a basic implementation of a singly linked list with node insertion in sorted order.

8. **Print Square instance** ([101-square.py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/101-square.py)): The code defines a `Square` class in Python, representing a square shape. It includes attributes for the size of one edge of the square and the position of the square. The class has methods for initializing the square, getting and setting the size and position, calculating the area, printing the square using the `#` character, and defining the string representation of the square. The code demonstrates encapsulation, validation, and additional functionality for the `Square` class

9. **Compare 2 squares** ([102-square.py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/102-square.py)): The code defines a `Square` class in Python. This class represents a square shape and includes attributes for the size of the square and methods for calculating the area, comparing squares based on their size, and getting and setting the size attribute.
The `__init__` method initializes a `Square` object with a given size. The `area` method calculates the area of the square by squaring the `size` attribute. The `size` method is a getter and setter for the size attribute, performing type and value validation.
The class also includes comparison methods (`__lt__`, `__le__`, `__eq__`, `__ne__`, `__ge__`, `__gt__`) that allow for comparing squares based on their size.
Overall, this code provides a basic implementation of a `Square` class with size validation and comparison functionality.

10. **ByteCode -> Python #5** ([103-magic_class.py](https://github.com/Eyakenojnr/alx-higher_level_programming/blob/master/0x06-python-classes/103-magic_class.py)): This task involves the conversion of the byte code to python code:
```
Disassembly of __init__:
 10           0 LOAD_CONST               1 (0)
              3 LOAD_FAST                0 (self)
              6 STORE_ATTR               0 (_MagicClass__radius)

 11           9 LOAD_GLOBAL              1 (type)
             12 LOAD_FAST                1 (radius)
             15 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             18 LOAD_GLOBAL              2 (int)
             21 COMPARE_OP               9 (is not)
             24 POP_JUMP_IF_FALSE       60
             27 LOAD_GLOBAL              1 (type)
             30 LOAD_FAST                1 (radius)
             33 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             36 LOAD_GLOBAL              3 (float)
             39 COMPARE_OP               9 (is not)
             42 POP_JUMP_IF_FALSE       60

 12          45 LOAD_GLOBAL              4 (TypeError)
             48 LOAD_CONST               2 ('radius must be a number')
             51 CALL_FUNCTION            1 (1 positional, 0 keyword pair)
             54 RAISE_VARARGS            1
             57 JUMP_FORWARD             0 (to 60)

 13     >>   60 LOAD_FAST                1 (radius)
             63 LOAD_FAST                0 (self)
             66 STORE_ATTR               0 (_MagicClass__radius)
             69 LOAD_CONST               3 (None)
             72 RETURN_VALUE

Disassembly of area:
 17           0 LOAD_FAST                0 (self)
              3 LOAD_ATTR                0 (_MagicClass__radius)
              6 LOAD_CONST               1 (2)
              9 BINARY_POWER
             10 LOAD_GLOBAL              1 (math)
             13 LOAD_ATTR                2 (pi)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE

Disassembly of circumference:
 21           0 LOAD_CONST               1 (2)
              3 LOAD_GLOBAL              0 (math)
              6 LOAD_ATTR                1 (pi)
              9 BINARY_MULTIPLY
             10 LOAD_FAST                0 (self)
             13 LOAD_ATTR                2 (_MagicClass__radius)
             16 BINARY_MULTIPLY
             17 RETURN_VALUE
```

The provided code defines a `MagicClass` that represents a circle. It includes attributes for radius of the circle and methods for initializing the class, calculating the diameter of the circle, setting the radius, and getting the radius. The code demonstrates encapsulation by using private attributes and provides basic functionality for working with circles.
