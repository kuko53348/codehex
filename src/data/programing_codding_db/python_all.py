python_code: dict = {
    "01. Variables and Assignments": """
```python
# Python uses dynamic typing for variable assignment
name = "David"         # String
state = True           # Boolean
age = 10               # Integer
temp = 18.5            # Float

# Composite collections
mixed_list = [1, "Juan", 23, "Juan"]      # List with mixed types
number_set = {1, 2, 3, 4, 5}              # Set (no duplicates)
person = {"Name": "Carlos", "Age": 23}   # Dictionary (key-value)

# Constants by naming convention
PI = 3.14
now = datetime.now()   # Runtime constant (current timestamp)
```
""",
    "02. String Manipulation": """
```python
example = "hello world 12345"
words = example.split(" ")           # Split into list of words

# Transformations
example.lower()                      # Convert to lowercase
example.upper()                      # Convert to uppercase
example.startswith("h")              # Starts with "h"?
example.endswith("5")                # Ends with "5"?
example.find("h")                    # First index of "h"
example.rfind("h")                   # Last index of "h"
example.strip()                      # Remove outer spaces
example.replace("h", "H")            # Replace all "h" with "H"
example[0:5]                         # Substring

# Padding
example.rjust(len(example)+3, "0")   # Pad right with zeros
example.ljust(len(example)+3, "0")   # Pad left with zeros

# Rejoin after splitting
" ".join(words)
```
""",
    "03. Collections: Lists, Sets, and Dicts": """
```python
# Lists (ordered, allow duplicates)
numbers = [1, 2, 23, 4]
names = ["Pedro", "Juan", "Cesar", "Carlos"]

# Operations on lists
numbers.sort()                       # Sort list
names.append("Banana")              # Add to end
names.insert(0, "Pineapple")        # Insert at index
names.remove("Pineapple")           # Remove by value
del names[0]                        # Remove by index
names[0] = "New Value"              # Update value
"Juan" in names                     # Check membership

# Sets (unordered, no duplicates)
number_set.add(25)                  # Add element
number_set.remove(5)                # Remove element
number_set.union({4,5,6})           # Union with another set
number_set.intersection({4,5,6})    # Intersection
number_set.difference({4,5,6})      # Difference

# Dictionaries (key-value mappings)
person["height"] = 75.5             # Add key-value
person.pop("Name")                  # Remove key
person["Name"] = "Luis"             # Update value
"Name" in person                    # Check key
"Luis" in person.values()           # Check value
```
""",
    "04. Key Concepts": """
```python
# List comprehension to double values
doubled = [i * 2 for i in range(5)]

# Loop through list
for num in doubled:
    print(f"Number: {num}")

# Ternary function
def greet(is_morning):
    return "Good Morning" if is_morning else "Hello"

# Lambda function assigned to variable
button_click = lambda: print("Clicked Bro")

# Nullable assignment
nullable = None
not_nullable = "value" if nullable else "fallback"   # Fallback if null

# Boolean inversion
is_true = True
is_true = not is_true
```
""",
    "05. Parsing and Type Conversion": """
```python
# String to numeric
int_val = int("12")
float_val = float("12.5")

# Numeric to string
str_int = str(12)
str_float = str(12.5)

# String conversions
fruits_string = "apple,banana,orange"
list_from_string = fruits_string.split(",")
set_from_string = set(list_from_string)
dict_from_string = {i: v for i, v in enumerate(list_from_string)}

# List conversions
fruits_list = ["apple", "banana", "orange"]
string_from_list = ",".join(fruits_list)
set_from_list = set(fruits_list)
dict_from_list = {i: v for i, v in enumerate(fruits_list)}

# Set conversions
fruits_set = {"apple", "banana", "orange"}
string_from_set = ",".join(fruits_set)
list_from_set = list(fruits_set)
dict_from_set = {i: v for i, v in enumerate(list_from_set)}

# Dict conversions
fruits_dict = {0: "apple", 1: "banana"}
string_from_dict = ",".join(fruits_dict.values())
list_from_dict = list(fruits_dict.values())
set_from_dict = set(fruits_dict.values())
```
""",
    "06. Conditionals": """
```python
# Conditional assignment
result = "True case" if True else "False case"

# If-else block
if condition1 == 10:
    print("Condition1 is true")
elif condition2 == 5:
    print("Condition2 is true")
else:
    print("All conditions are false")

# Match-case (Python 3.10+)
value = "case2"
match value:
    case "case1":
        print("Case 1 executed")
    case "case2":
        print("Case 2 executed")
    case _:
        print("Default case executed")
```
""",
    "07. Loops and Repetition": """
```python
# For loop with continue and break
for i in range(5):
    if i == 3: continue
    print(f"For loop: {i}")
    if i == 4: break

# For-in loop over list
names = ["Maria", "Joaquin", "Luisa"]
for name in names:
    print(f"Hello {name}")

# For-in loop over dict
ages = {"Maria": 20, "Joaquin": 21, "Luisa": 22}
for name, age in ages.items():
    print(f"{name} is {age} years old")

# While loop
count = 0
while count < 3:
    print(f"While loop: {count}")
    count += 1

# Do-while emulation
count = 3
while True:
    print(f"Do-while loop: {count}")
    count -= 1
    if count == 0:
    break

```
""",
    "08. Functions and Methods": """
```python
# Define and call a function
def greet(parameter): print(f"hello {parameter}")
greet_lambda = lambda parameter: print(f"hello {parameter}")

# Functions with return values
def return_string(parameter): return f"hello {parameter}"
def return_int(parameter): return parameter
def return_tuple(parameter): return (123, parameter)

# Functions as first-class objects
def add(a, b): return a + b
sum_result = add(2, 3)
total_sum = add(2, add(2, 3))
```
""",
    "09. Error Handling": """
```python
# Exception handling with fallback
try:
    result = int("123") / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid number format")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("This always executes")
```
""",
}

python_class: dict = {
    "01. Basic Classes": """
```python
# Define a class with properties and a method
class Vehicle:
    def __init__(self):
        self.brand = ""
        self.year = 0

    def show_info(self):
        print(f"Brand: {self.brand}, Year: {self.year}")

# Instantiate and assign values
my_car = Vehicle()
my_car.brand = "Toyota"
my_car.year = 2020
my_car.show_info()      # Brand: Toyota, Year: 2020
```
""",
    "02. Properties and Methods": """
```python
class User:
    def __init__(self, user_id, name):
        self._id = user_id    # underscore implies internal use
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! (ID: {self._id})")

# Create instance
u = User("u123", "Ana")
u.greet()                 # Hello, Ana! (ID: u123)
```
""",
    "03. Constructors": """
```python
# Python uses __init__ for constructors
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

p1 = Point(2, 3)
p2 = Point()              # Uses default origin
```
""",
    "04. Inheritance": """
```python
# Child class inherits from Parent class
class Animal:
    def move(self):
        print("The animal moves")

class Dog(Animal):
    def move(self):
        print("The dog runs")

a = Dog()
a.move()                  # The dog runs
```
""",
    "05. Polymorphism": """
```python
# Define a shared interface
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2
```
""",
    "06. Mixins": """
```python
class Musical:
    def play_instrument(self):
        print("Playing instrument")

class Musician(Musical):
    pass

m = Musician()
m.play_instrument()
```
""",
    "07. Interfaces": """
# Python uses abstract base classes for interfaces
```python
from abc import ABC, abstractmethod

class Person(ABC):
    @abstractmethod
    def greet(self): pass

class Impostor(Person):
    def greet(self):
        print("I'm an impostor!")

i = Impostor()
i.greet()
```
""",
    "08. Abstract Classes": """
```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self): pass

class Bike(Vehicle):
    def move(self):
        print("The bike moves forward")
```
""",
    "09. Encapsulation": """
```python
class Bank:
    def __init__(self):
        self._balance = 0     # private by convention

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance
```
""",
    "10. Static Members and Constants": """
```python
class Utilities:
    PI = 3.1416                          # constant
    @staticmethod
    def square(x):
        return x * x

print(Utilities.PI)
print(Utilities.square(5))
```
""",
    "11. Generics with Typing": """
```python
from typing import Generic, TypeVar
T = TypeVar("T")

class Box(Generic[T]):
    def __init__(self, content: T):
        self.content = content

box_int = Box(42)
box_str = Box("Hello")

print(box_int.content)      # 42
print(box_str.content)      # Hello
```
""",
    "12. Docstrings and Metadata": '''
```python
class Calculator:
    """Performs arithmetic operations."""

    def add(self, a, b):
        """Adds two numbers and returns the result."""
        return a + b

# Access docstrings
print(Calculator.__doc__)
print(Calculator.add.__doc__)
```
''',
    "13. Design Patterns": """
# Singleton via module-level instance
```python
class Logger:
    _instance = None

    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
        return cls._instance

log1 = Logger("main")
log2 = Logger("backup")
print(log1.name)           # main
print(log2.name)           # main (shared)
```
""",
    "14. Best Practices": """
```python
# ✅ Use descriptive class and method names
# ✅ Favor composition over inheritance
# ✅ Use properties for clean getters/setters
# ✅ Group related behaviors in methods
# ✅ Write docstrings for public APIs
```
""",
}

python_os: dict = {
    "01. Files and Directories": """
```python
import os

# 📖 Read file content
with open("text.txt", "r") as f:
    content = f.read()

# ✍️ Write to file
with open("new.txt", "w") as f:
    f.write("Hello world")

# ✅ Check if file exists
exists = os.path.exists("new.txt")

# 🧹 Delete file
os.remove("new.txt")

# 📍 Current working directory
current_dir = os.getcwd()

# 🗂️ List directory contents
dir_contents = os.listdir(current_dir)
```
""",
    "02. Paths and Manipulation": """
```python
import os

# 📎 File name
name = os.path.basename("/folder/file.txt")

# 🧩 File extension
ext = os.path.splitext("file.tar.gz")[1]

# 📍 Absolute path
full_path = os.path.abspath("data.txt")

# 🔗 Join paths
joined = os.path.join("folder", "file.txt")
```
""",
    "03. Date and Time": """
```python
from datetime import datetime

# ⏰ Current date and time
now = datetime.now()

# 🌐 UTC version
utc_now = datetime.utcnow()

# 📅 Parse string to date
parsed = datetime.strptime("2025-08-01", "%Y-%m-%d")

# ⏳ Time difference
diff = now - parsed

# 🧾 Simple format
formatted = f"{now.day}/{now.month}/{now.year}"
```
""",
    "04. System Processes": """
```python
import subprocess

# 🖥️ Run shell command
result = subprocess.run(["echo", "Hello Python"], capture_output=True, text=True)

# 📡 Print output
print(result.stdout)
""",
    "05. Environment Variables": """
import os

# 🌍 All environment variables
env_vars = os.environ

# 🏡 HOME directory (Unix)
home_dir = env_vars.get("HOME")
```
""",
    "06. Operating System Detection": """
```python
import platform
import sys

# 🪟 Windows
is_windows = sys.platform.startswith("win")

# 🐧 Linux
is_linux = sys.platform.startswith("linux")

# 🍎 macOS
is_mac = sys.platform.startswith("darwin")
```
""",
    "07. Continuous Reading / Streams": """
```python
import subprocess

# 🔁 Start real-time process
process = subprocess.Popen(["ping", "localhost"], stdout=subprocess.PIPE, text=True)

# 🖥️ Stream and display output
for line in process.stdout:
    print(f"📡 {line.strip()}")
```
""",
}
