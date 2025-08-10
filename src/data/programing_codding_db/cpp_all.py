cpp_code: dict = {
    "01. Variables and Assignments": """
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

std::string name = "David";      // String
bool state = true;               // Boolean
int age = 10;                    // Integer
double temp = 18.5;              // Double
float pi = 3.14f;                // Float constant

std::vector<std::string> mixedList = {"1", "Juan", "23", "Juan"};
std::set<int> numberSet = {1,2,3,4,5};
std::map<std::string, std::string> person = {{"Name", "Carlos"}, {"Age", "23"}};

// C++ has static and const for runtime and compile-time constants
const double PI = 3.1415;
std::string lateAssignation;
lateAssignation = "assigned value";
""",
    "02. String Manipulation": """
#include <algorithm>

std::string example = "hello world 12345";
std::vector<std::string> words; // manually split (requires function)

// Transformations
std::transform(example.begin(), example.end(), example.begin(), ::tolower);
std::transform(example.begin(), example.end(), example.begin(), ::toupper);

example.find("h");           // First index of 'h'
example.rfind("h");          // Last index
example.substr(0,5);         // Substring

// Replace all 'h' with 'H'
std::replace(example.begin(), example.end(), 'h', 'H');

// Padding (manual using string methods)
std::string padRight = example + std::string(3, '0');
std::string padLeft = std::string(3, '0') + example;
""",
    "03. Collections: Vectors, Sets, Maps": """
std::vector<int> numbers = {1,2,23,4};
std::vector<std::string> names = {"Pedro","Juan","Cesar","Carlos"};

std::sort(numbers.begin(), numbers.end());
names.push_back("Banana");
names.insert(names.begin(), "Pineapple");
names.erase(names.begin());
names[0] = "New";

bool contains = std::find(names.begin(), names.end(), "Juan") != names.end();

// Sets
std::set<int> set1 = {1,2,3,4,5};
std::set<int> set2 = {4,5,6,7,8};

// Set union/intersection/difference requires manual logic

// Maps
std::map<std::string, std::string> person;
person["Name"] = "Luis";
person["Height"] = "75.5";
person.erase("Name");
bool hasKey = person.find("Name") != person.end();
bool hasValue = std::any_of(person.begin(), person.end(),
  [](const auto& kv){ return kv.second == "Luis"; });
""",
    "04. Key Concepts": """
std::vector<int> doubled;
for (int i = 0; i < 5; ++i) doubled.push_back(i * 2);
for (int num : doubled) std::cout << "Number: " << num << "\\n";

std::string greet(bool isMorning) {
  return isMorning ? "Good Morning" : "Hello";
}

bool isTrue = true;
isTrue = !isTrue;
""",
    "05. Parsing and Type Conversion": """
std::string sInt = "12";
std::string sFloat = "12.5";
int intVal = std::stoi(sInt);
float floatVal = std::stof(sFloat);
std::string fromInt = std::to_string(12);
std::string fromFloat = std::to_string(12.5f);

// String splitting requires custom function (use stringstream)
""",
    "06. Conditionals": """
int condition1 = 10;
int condition2 = 5;

std::string result = true ? "True case" : "False case";

if (condition1 == 10) {
  std::cout << "Condition1 is true\\n";
} else if (condition2 == 5) {
  std::cout << "Condition2 is true\\n";
} else {
  std::cout << "All conditions false\\n";
}

std::string value = "case2";
if (value == "case1") std::cout << "Case 1 executed\\n";
else if (value == "case2") std::cout << "Case 2 executed\\n";
else std::cout << "Default case executed\\n";
""",
    "07. Loops and Repetition": """
for (int i = 0; i < 5; ++i) {
  if (i == 3) continue;
  std::cout << "For loop: " << i << "\\n";
  if (i == 4) break;
}

std::vector<std::string> names = {"Maria", "Joaquin", "Luisa"};
for (const std::string& name : names) {
  std::cout << "Hello " << name << "\\n";
}

std::map<std::string, int> ages = {{"Maria",20}, {"Joaquin",21}, {"Luisa",22}};
for (const auto& [name, age] : ages) {
  std::cout << name << " is " << age << " years old\\n";
}

int count = 0;
while (count < 3) {
  std::cout << "While loop: " << count << "\\n";
  ++count;
}

count = 3;
do {
  std::cout << "Do-while loop: " << count << "\\n";
  --count;
} while (count > 0);
""",
    "08. Functions and Methods": """
void greet(std::string param) {
  std::cout << "Hello " << param << "\\n";
}

std::string returnString(std::string param) {
  return "Hello " + param;
}

int returnInt(int param) {
  return param;
}

std::pair<int, std::string> returnTuple(std::string param) {
  return {123, param};
}

int add(int a, int b) { return a + b; }

int sumResult = add(2, 3);
int totalSum = add(2, add(2, 3));
""",
    "09. Error Handling": """
try {
  int result = std::stoi("123") / 0;
  std::cout << result << "\\n";
} catch (const std::exception& e) {
  std::cout << "An error occurred: " << e.what() << "\\n";
}
std::cout << "This always executes\\n";
""",
}

cpp_class: dict = {
    "01. Basic Class and Instantiation": """
#include <iostream>
#include <string>

class Vehicle {
public:
  std::string brand;
  int year;

  void showInfo() {
    std::cout << "Brand: " << brand << ", Year: " << year << std::endl;
  }
};

Vehicle myCar;
myCar.brand = "Toyota";
myCar.year = 2020;
myCar.showInfo(); // Brand: Toyota, Year: 2020
""",
    "02. Properties and Methods": """
class User {
private:
  std::string id;

public:
  std::string name;

  User(std::string user_id, std::string user_name)
    : id(user_id), name(user_name) {}

  void greet() {
    std::cout << "Hello, " << name << "! (ID: " << id << ")" << std::endl;
  }
};

User u("u123", "Ana");
u.greet(); // Hello, Ana! (ID: u123)
""",
    "03. Constructors": """
class Point {
public:
  double x, y;

  Point(double x_, double y_) : x(x_), y(y_) {}
  Point() : x(0), y(0) {} // Origin
};

Point p1(2, 3);
Point p2; // Default origin (0,0)
""",
    "04. Inheritance": """
class Animal {
public:
  virtual void move() {
    std::cout << "The animal moves" << std::endl;
  }
};

class Dog : public Animal {
public:
  void move() override {
    std::cout << "The dog runs" << std::endl;
  }
};

Animal* a = new Dog();
a->move(); // The dog runs
""",
    "05. Polymorphism": """
class Shape {
public:
  virtual double area() const = 0; // Pure virtual
};

class Circle : public Shape {
private:
  double radius;
public:
  Circle(double r) : radius(r) {}
  double area() const override {
    return 3.1416 * radius * radius;
  }
};
""",
    "06. Mixins via Multiple Inheritance": """
class Musical {
public:
  void playInstrument() {
    std::cout << "Playing instrument" << std::endl;
  }
};

class Musician : public Musical {};

Musician m;
m.playInstrument(); // Playing instrument
""",
    "07. Interface via Abstract Class": """
class Person {
public:
  virtual std::string greet() const = 0;
};

class Impostor : public Person {
public:
  std::string greet() const override {
    return "I'm an impostor!";
  }
};

Impostor i;
std::cout << i.greet() << std::endl;
""",
    "08. Abstract Class Usage": """
class Vehicle {
public:
  virtual void move() const = 0;
};

class Bike : public Vehicle {
public:
  void move() const override {
    std::cout << "The bike moves forward" << std::endl;
  }
};

Bike b;
b.move();
""",
    "09. Encapsulation": """
class Bank {
private:
  double balance = 0;

public:
  void deposit(double amount) {
    balance += amount;
  }

  double getBalance() const {
    return balance;
  }
};

Bank myBank;
myBank.deposit(100.0);
std::cout << myBank.getBalance() << std::endl;
""",
    "10. Static Members and Constants": """
class Utilities {
public:
  static const double PI;
  static double square(double x) {
    return x * x;
  }
};

const double Utilities::PI = 3.1416;

std::cout << Utilities::PI << std::endl;
std::cout << Utilities::square(5.0) << std::endl;
""",
    "11. Generics via Templates": """
template <typename T>
class Box {
public:
  T content;
  Box(T c) : content(c) {}
};

Box<int> boxInt(42);
Box<std::string> boxStr("Hello");

std::cout << boxInt.content << std::endl;
std::cout << boxStr.content << std::endl;
""",
    "12. Documentation via Comments": """
// Calculator class that performs arithmetic
class Calculator {
public:
  // Adds two numbers
  int add(int a, int b) {
    return a + b;
  }
};
""",
    "13. Design Patterns: Singleton": """
class Logger {
private:
  std::string name;
  static Logger* instance;
  Logger(std::string n) : name(n) {}

public:
  static Logger* getInstance(std::string n) {
    if (!instance)
      instance = new Logger(n);
    return instance;
  }

  std::string getName() const { return name; }
};

Logger* Logger::instance = nullptr;

Logger* log1 = Logger::getInstance("main");
Logger* log2 = Logger::getInstance("backup");

std::cout << log1->getName() << std::endl; // main
std::cout << log2->getName() << std::endl; // main (singleton)
""",
    "14. Best Practices": """
// ✅ Use PascalCase for class names
// ✅ Keep data members private
// ✅ Use const for immutability
// ✅ Prefer abstract classes and interfaces for polymorphism
// ✅ Document public methods with comments
""",
}

cpp_os: dict = {
    "01. Files and Directories": """
#include <fstream>
#include <filesystem>
#include <iostream>
#include <string>

namespace fs = std::filesystem;

// 📖 Read file content
std::ifstream file("text.txt");
std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

// ✍️ Write to file
std::ofstream out("new.txt");
out << "Hello world";

// ✅ Check if file exists
bool exists = fs::exists("new.txt");

// 🧹 Delete file
fs::remove("new.txt");

// 📍 Current directory
fs::path current_dir = fs::current_path();

// 🗂️ List directory contents
for (const auto& entry : fs::directory_iterator(current_dir)) {
    std::cout << entry.path() << std::endl;
}
""",
    "02. Paths and Manipulation": """
#include <filesystem>
#include <iostream>
namespace fs = std::filesystem;

// 📎 File name
auto name = fs::path("/folder/file.txt").filename();

// 🧩 File extension
auto ext = fs::path("file.tar.gz").extension();

// 📍 Absolute path
fs::path full_path = fs::absolute("data.txt");

// 🔗 Join paths
fs::path joined = fs::path("folder") / "file.txt";
""",
    "03. Date and Time": """
#include <chrono>
#include <ctime>
#include <iomanip>
#include <sstream>

// ⏰ Current time
auto now = std::chrono::system_clock::now();
std::time_t t_now = std::chrono::system_clock::to_time_t(now);

// 🌐 UTC version
std::tm utc_tm = *std::gmtime(&t_now);

// 📅 Parse string to time (manual, needs stringstream)
std::tm parsed_tm = {};
std::istringstream ss("2025-08-01");
ss >> std::get_time(&parsed_tm, "%Y-%m-%d");

// ⏳ Time difference (chrono duration)
auto then = std::chrono::system_clock::from_time_t(std::mktime(&parsed_tm));
auto diff = std::chrono::duration_cast<std::chrono::hours>(now - then).count();

// 🧾 Simple format
std::ostringstream format;
format << utc_tm.tm_mday << "/" << utc_tm.tm_mon + 1 << "/" << utc_tm.tm_year + 1900;
""",
    "04. System Processes": """
#include <cstdlib>
#include <iostream>

// 🖥️ Run shell command
int result = std::system("echo Hello C++");

// 📡 Output is shown in terminal directly
std::cout << "Command returned code: " << result << std::endl;
""",
    "05. Environment Variables": """
#include <cstdlib>
#include <iostream>

// 🌍 Read environment variable
const char* home = std::getenv("HOME");
if (home)
  std::cout << "HOME: " << home << std::endl;
""",
    "06. Operating System Detection": """
#ifdef _WIN32
std::cout << "🪟 Windows" << std::endl;
#elif __linux__
std::cout << "🐧 Linux" << std::endl;
#elif __APPLE__
std::cout << "🍎 macOS" << std::endl;
#endif
""",
    "07. Continuous Reading / Streams": """
#include <iostream>
#include <cstdio>
#include <memory>
#include <string>

// 🔁 Launch process with pipe
std::unique_ptr<FILE, decltype(&pclose)> pipe(popen("ping -c 4 localhost", "r"), pclose);

// 🖥️ Read line-by-line
char buffer[128];
while (fgets(buffer, sizeof(buffer), pipe.get()) != nullptr) {
    std::cout << "📡 " << buffer;
}
""",
}
