# 0x06. Python - Classes and Objects
# Resources
* [Object Oriented Programming](https://python.swaroopch.com/oop.html) (_Everything until the paragraph "Inheritance" excluded._)
* [Object-Oriented Programming](https://python-course.eu/oop/object-oriented-programming.php)
* [Properties vs. Getters and Setters](https://python-course.eu/oop/properties-vs-getters-and-setters.php)
* [Learn to Program 9 : Object Oriented Programming](https://www.youtube.com/watch?v=1AGyBuVCTeE&)
* [Python Classes and Objects](https://www.youtube.com/watch?v=apACNr7DC_s)
* [Object Oriented Programming](https://www.youtube.com/watch?v=-DP1i2ZU9gk)
# Summary
1. **Python Programming**: Python is a powerful and versatile programming language known for its simplicity and readability. It allows developers to write code that is concise and easy to understand, making it an excellent choice for beginners and experienced programmers alike.

2. **Object-Oriented Programming (OOP)**: OOP is a programming paradigm that organizes data and behavior into reusable structures called objects. It focuses on modeling real-world entities as objects, allowing for better code organization, reusability, and modularity.

3. **"First Class Everything"**: In Python, the term "first class everything" means that objects, functions, and classes are all treated as first-class citizens. This means they can be passed as arguments, returned from functions, assigned to variables, and stored in data structures, just like any other value.

4. **Class**: A class is a blueprint or template that defines the structure and behavior of objects. It defines the attributes (data) and methods (functions) that an object of that class will have.

5. Object and Instance: An object is a particular instance of a class. When a class is instantiated (created), it becomes an object. Objects are created based on the structure defined by the class and can have their own unique state and behavior.

6. Difference between a Class and an Object/Instance: A class is a blueprint or template that defines the structure and behavior of objects, while an object/instance is a specific occurrence of a class. In other words, a class defines the properties and methods that objects will have, while objects are created based on that class.

7. Attribute: An attribute is a characteristic or property of an object. It represents the state or data associated with an object and can be either data (variables) or behavior (methods).

8. Public, Protected, and Private Attributes: In Python, there is no strict mechanism for enforcing access control to attributes. By convention, attributes that start with a single underscore (_) are considered "protected" and should only be accessed within the class or its subclasses. Attributes that start with two underscores (__) are considered "private" and should not be accessed directly from outside the class.

9. Self: "self" is a conventional name used in Python for the first parameter of instance methods. It refers to the instance of the class itself and is used to access the instance's attributes and methods within the class.

10. Method: A method is a function defined within a class. It is called on an object and can access and manipulate the object's attributes.

11. The special __init__ method: The __init__ method is a special method in Python classes that is automatically called when an object is created from a class. It is used to initialize the object's attributes and perform any necessary setup.

12. Data Abstraction, Data Encapsulation, and Information Hiding: Data abstraction is the process of hiding the internal implementation details of an object while providing a clean and simple interface for interacting with it. Data encapsulation is the practice of bundling data and methods together in a class. Information hiding refers to the concept of hiding the internal details of how an object works to prevent direct access and potential misuse.

13. Property: A property is a way to define getter and setter methods for a class attribute. It allows for controlled access and modification of attributes, enabling validation, and customization of attribute behavior.

14. Difference between an Attribute and a Property in Python: An attribute is a data or behavior associated with an object, while a property is a special attribute that defines custom getter, setter, and deleter methods to control access and modification of other attributes.

15. Pythonic way to write getters and setters: In Python, the @property decorator is commonly used to define a getter method, and the @attribute_name.setter decorator is used to define a setter method. This allows attributes to be accessed and modified using dot notation, like normal attributes, while allowing additional logic to be executed.

16. Dynamically Creating Arbitrary Attributes for Existing Instances: Python allows you to dynamically create new attributes for existing instances by simply assigning a value to a new attribute name. The new attribute will then be available for that specific instance.

17. Binding Attributes to Objects and Classes: Attributes in Python are dynamically bound, which means they can be added to objects or classes at any time. When an attribute is accessed, Python first checks if it exists in the object's namespace (if accessed via an object) or the class's namespace (if accessed via a class).

18. __dict__ of a Class/Instance: The __dict__ attribute of a class or instance is a dictionary that contains the attributes and their corresponding values for that class or instance.

19. Attribute Lookup in Python: When an attribute is accessed, Python first looks for it in the object's namespace. If not found, it looks in the class's namespace. If still not found, it goes up the inheritance chain until it either finds the attribute or raises an AttributeError.

20. Using the getattr() Function: The getattr() function in Python is

