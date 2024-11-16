# Chapter 15 - Exercise 01

## "What’s the difference between an instance method and a static method?"

In Python, instance methods and static methods are both types of methods that can be defined within a class, but they serve different purposes and have different characteristics.

### Instance Methods
- **Definition**: Instance methods are the most common type of methods in a class. They take `self` as the first parameter, which refers to the instance of the class.
- **Purpose**: Instance methods operate on instances of the class. They can access and modify the instance's attributes and other instance methods.
- **Usage**: They are used to perform operations that involve the instance's data.
- **Example**:
  ```python
  class MyClass:
      def __init__(self, value):
          self.value = value

      def instance_method(self):
          return self.value

  obj = MyClass(10)
  print(obj.instance_method())  # Output: 10
  ```

### Static Methods
- **Definition**: Static methods do not take `self` or `cls` as the first parameter. Instead, they are defined using the `@staticmethod` decorator.
- **Purpose**: Static methods do not operate on instances or the class itself. They are used for utility functions that are related to the class but do not need to access instance-specific data.
- **Usage**: They are used for operations that are logically related to the class but do not require access to instance or class variables.
- **Example**:
  ```python
  class MyClass:
      @staticmethod
      def static_method(value):
          return value * 2

  result = MyClass.static_method(10)
  print(result)  # Output: 20
  ```

### Key Differences
1. **Access to Instance Data**:
   - Instance methods can access and modify instance data using `self`.
   - Static methods cannot access instance data.

2. **Decorator**:
   - Instance methods do not require a decorator.
   - Static methods require the `@staticmethod` decorator.

3. **First Parameter**:
   - Instance methods take `self` as the first parameter.
   - Static methods do not take `self` or `cls` as the first parameter.

4. **Usage Context**:
   - Instance methods are used for operations that involve instance-specific data.
   - Static methods are used for utility functions that are related to the class but do not need instance-specific data.

### Example Comparison
```python
class MathOperations:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        return self.value * 2

    @staticmethod
    def static_method(value):
        return value * 2

# Instance method usage
obj = MathOperations(10)
print(obj.instance_method())  # Output: 20

# Static method usage
print(MathOperations.static_method(10))  # Output: 20
```

In this example, the instance method `instance_method` operates on the instance's `value` attribute, while the static method `static_method` performs a simple multiplication without needing access to any instance data.

## "Why are static methods called static?"

The term "static" in the context of static methods comes from the concept of "static" in programming, which originates from languages like C and C++. In these languages, the keyword `static` is used to define variables and methods that belong to the class itself rather than to instances of the class. This concept has been adopted in other programming languages, including Python, to describe methods that do not depend on instance-specific data.

### Key Characteristics of Static Methods
1. **Class-Level Association**: Static methods are associated with the class itself rather than with any particular instance of the class. This means they can be called on the class directly, without needing an instance.

2. **No Access to Instance Data**: Static methods do not have access to instance-specific data (`self`) or class-specific data (`cls`). They operate independently of any instance or class variables.

3. **Utility Functions**: Static methods are often used for utility or helper functions that perform tasks related to the class but do not require access to instance data.

### Historical Context
- **C and C++**: In C and C++, the `static` keyword is used to define variables and functions that have internal linkage, meaning they are limited to the scope of the file in which they are defined. For class members, `static` indicates that the member belongs to the class rather than to instances of the class.
- **Java**: In Java, static methods are defined using the `static` keyword and are called on the class itself. They do not have access to instance variables or methods.

### Python Adoption
Python adopted the concept of static methods to provide a way to define methods that are logically related to a class but do not need to access instance-specific data. The `@staticmethod` decorator is used to define such methods.

### Example in Python
```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Calling static methods
result_add = MathUtils.add(5, 3)
result_multiply = MathUtils.multiply(5, 3)

print(result_add)      # Output: 8
print(result_multiply)  # Output: 15
```

In this example, the `add` and `multiply` methods are static methods. They perform simple arithmetic operations that do not require access to any instance data, making them suitable candidates for static methods.

### Summary
Static methods are called "static" because they are designed to operate at the class level, independent of any instance-specific data. This concept is borrowed from languages like C and C++, where `static` indicates class-level association and limited scope. In Python, static methods are defined using the `@staticmethod` decorator and are used for utility functions related to the class.

## “Rewrite this function as a method of the Time class.”

```python
def subtract_time(t1, t2):
    return time_to_int(t1) - time_to_int(t2)
```

```python
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def time_to_int(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def subtract_time(self, other):
        return self.time_to_int() - other.time_to_int()

# Example usage:
t1 = Time(10, 30, 45)
t2 = Time(8, 15, 20)

result = t1.subtract_time(t2)
print(result)  # Output will be the difference in seconds
```