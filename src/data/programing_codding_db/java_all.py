java_code: dict = {
    "01. Variables and Assignments": """
```java
String name = "David";           // String
boolean state = true;            // Boolean
int age = 10;                    // Integer
double temp = 18.5;              // Double

final double PI = 3.1415;        // Constant

Date now = new Date();           // Runtime timestamp
String lateValue = null;         // Declared, assigned later
lateValue = "assigned value";
```
""",
    "02. String Manipulation": """
```java
String example = "hello world 12345";
String[] words = example.split(" ");

// Basic operations
example.toLowerCase();
example.toUpperCase();
example.contains("h");
example.startsWith("h");
example.endsWith("5");
example.indexOf("h");
example.lastIndexOf("h");
example.trim();
example.replace("h", "H");
example.substring(0, 5);

// Padding (manual)
String padLeft = String.format("%1$" + (example.length()+3) + "s", example).replace(' ', '0');
String padRight = example + "000";

// Joining
String joined = String.join("-", words);
```
""",
    "03. Collections: Lists, Sets, Maps": """
```java
List<Integer> numbers = new ArrayList<>(Arrays.asList(1, 2, 23, 4));
List<String> names = new ArrayList<>(Arrays.asList("Pedro", "Juan", "Cesar", "Carlos"));

Collections.sort(numbers);
names.add("Banana");
names.add(0, "Pineapple");
names.remove(0);
names.set(0, "New");
boolean hasJuan = names.contains("Juan");

Set<Integer> set1 = new HashSet<>(Arrays.asList(1,2,3,4,5));
Set<Integer> set2 = new HashSet<>(Arrays.asList(4,5,6,7,8));

Set<Integer> union = new HashSet<>(set1); union.addAll(set2);
Set<Integer> intersect = new HashSet<>(set1); intersect.retainAll(set2);
Set<Integer> diff = new HashSet<>(set1); diff.removeAll(set2);

Map<String, Object> person = new HashMap<>();
person.put("Name", "Luis");
person.put("Height", 75.5);
person.remove("Name");
person.put("Name", "Luis");
boolean hasKey = person.containsKey("Name");
boolean hasValue = person.containsValue("Luis");
```
""",
    "04. Key Concepts": """
```java
List<Integer> doubled = IntStream.range(0, 5).map(i -> i * 2).boxed().collect(Collectors.toList());
doubled.forEach(num -> System.out.println("Number: " + num));

String greet(boolean isMorning) {
  return isMorning ? "Good Morning" : "Hello";
}

Runnable click = () -> System.out.println("Clicked Bro");

String nullable = null;
String notNull = (nullable != null) ? nullable : "Fallback";

boolean isTrue = true;
isTrue = !isTrue;
```
""",
    "05. Parsing and Type Conversion": """
```java
int intVal = Integer.parseInt("12");
double doubleVal = Double.parseDouble("12.5");
String strInt = Integer.toString(12);
String strDouble = Double.toString(12.5);

String fruits = "apple,banana,orange";
List<String> listFromStr = Arrays.asList(fruits.split(","));
Set<String> setFromStr = new HashSet<>(listFromStr);
Map<Integer, String> mapFromStr = IntStream.range(0, listFromStr.size())
  .boxed().collect(Collectors.toMap(i -> i, i -> listFromStr.get(i)));
```
""",
    "06. Conditionals": """
```java
int condition1 = 10;
int condition2 = 5;

String result = (true) ? "True case" : "False case";

if (condition1 == 10) {
  System.out.println("Condition1 is true");
} else if (condition2 == 5) {
  System.out.println("Condition2 is true");
} else {
  System.out.println("All conditions false");
}

String value = "case2";
switch (value) {
  case "case1": System.out.println("Case 1 executed"); break;
  case "case2": System.out.println("Case 2 executed"); break;
  default: System.out.println("Default case executed");
}
```
""",
    "07. Loops and Repetition": """
```java
for (int i = 0; i < 5; i++) {
  if (i == 3) continue;
  System.out.println("For loop: " + i);
  if (i == 4) break;
}

List<String> names = Arrays.asList("Maria", "Joaquin", "Luisa");
for (String name : names) {
  System.out.println("Hello " + name);
}

Map<String, Integer> ages = Map.of("Maria", 20, "Joaquin", 21, "Luisa", 22);
for (Map.Entry<String, Integer> entry : ages.entrySet()) {
  System.out.println(entry.getKey() + " is " + entry.getValue() + " years old");
}

int count = 0;
while (count < 3) {
  System.out.println("While loop: " + count);
  count++;
}

count = 3;
do {
  System.out.println("Do-while loop: " + count);
  count--;
} while (count > 0);
```
""",
    "08. Functions and Methods": """
```java
void greet(String param) {
  System.out.println("hello " + param);
}

Function<String, String> returnString = param -> "hello " + param;
Function<Integer, Integer> returnInt = param -> param;
BiFunction<Integer, String, Pair<Integer, String>> returnPair =
  (num, str) -> new Pair<>(num, str);

int add(int a, int b) { return a + b; }

int sumResult = add(2, 3);
int totalSum = add(2, add(2, 3));
```
""",
    "09. Error Handling": """
```java
try {
  int result = Integer.parseInt("123") / 0;
  System.out.println(result);
} catch (ArithmeticException e) {
  System.out.println("Cannot divide by zero");
} catch (NumberFormatException e) {
  System.out.println("Invalid number format");
} catch (Exception e) {
  System.out.println("An error occurred: " + e.getMessage());
} finally {
  System.out.println("This always executes");
}
```
""",
}

java_class: dict = {
    "01. Basic Class and Instantiation": """
```java
public class Vehicle {
  String brand;
  int year;

  void showInfo() {
    System.out.println("Brand: " + brand + ", Year: " + year);
  }
}

Vehicle myCar = new Vehicle();
myCar.brand = "Toyota";
myCar.year = 2020;
myCar.showInfo(); // Brand: Toyota, Year: 2020
```
""",
    "02. Properties and Methods": """
```java
public class User {
  private String id;
  public String name;

  public User(String id, String name) {
    this.id = id;
    this.name = name;
  }

  public void greet() {
    System.out.println("Hello, " + name + "! (ID: " + id + ")");
  }
}

User u = new User("u123", "Ana");
u.greet(); // Hello, Ana! (ID: u123)
```
""",
    "03. Constructors": """
```java
public class Point {
  double x, y;

  public Point(double x, double y) {
    this.x = x;
    this.y = y;
  }

  public Point() {
    this(0, 0); // Origin
  }
}

Point p1 = new Point(2, 3);
Point p2 = new Point(); // (0,0)
```
""",
    "04. Inheritance": """
```java
class Animal {
  void move() {
    System.out.println("The animal moves");
  }
}

class Dog extends Animal {
  @Override
  void move() {
    System.out.println("The dog runs");
  }
}

Animal a = new Dog();
a.move(); // The dog runs
```
""",
    "05. Polymorphism": """
```java
interface Shape {
  double area();
}

class Circle implements Shape {
  double radius;

  Circle(double r) { radius = r; }

  public double area() {
    return 3.1416 * radius * radius;
  }
}

Shape s = new Circle(2.0);
System.out.println("Area: " + s.area());
```
""",
    "06. Mixins via Interfaces": """
```java
interface Musical {
  void playInstrument();
}

class Musician implements Musical {
  public void playInstrument() {
    System.out.println("Playing instrument");
  }
}

Musician m = new Musician();
m.playInstrument();
```
""",
    "07. Interface Contracts": """
```java
interface Person {
  String greet();
}

class Impostor implements Person {
  public String greet() {
    return "I'm an impostor!";
  }
}

Person i = new Impostor();
System.out.println(i.greet());
```
""",
    "08. Abstract Classes": """
```java
abstract class Vehicle {
  abstract void move();
}

class Bike extends Vehicle {
  void move() {
    System.out.println("The bike moves forward");
  }
}

Vehicle b = new Bike();
b.move();
```
""",
    "09. Encapsulation": """
```java
class Bank {
  private double balance = 0;

  public void deposit(double amount) {
    balance += amount;
  }

  public double getBalance() {
    return balance;
  }
}

Bank myBank = new Bank();
myBank.deposit(100);
System.out.println(myBank.getBalance()); // 100.0
```
""",
    "10. Static Members and Constants": """
```java
class Utilities {
  public static final double PI = 3.1416;

  public static double square(double x) {
    return x * x;
  }
}

System.out.println(Utilities.PI);
System.out.println(Utilities.square(5));
```
""",
    "11. Generics in Classes": """
```java
class Box<T> {
  T content;

  Box(T content) {
    this.content = content;
  }
}

Box<Integer> boxInt = new Box<>(42);
Box<String> boxStr = new Box<>("Hello");

System.out.println(boxInt.content); // 42
System.out.println(boxStr.content); // Hello
```
""",
    "12. Documentation Comments": """
```java
/**
 * A calculator that performs arithmetic operations.
 */
class Calculator {

  /**
   * Adds two integers.
   */
  public int add(int a, int b) {
    return a + b;
  }
}
```
""",
    "13. Design Patterns (Singleton)": """
```java
class Logger {
  private static Logger instance;
  private String name;

  private Logger(String name) {
    this.name = name;
  }

  public static Logger getInstance(String name) {
    if (instance == null) {
      instance = new Logger(name);
    }
    return instance;
  }

  public String getName() {
    return name;
  }
}

Logger log1 = Logger.getInstance("main");
Logger log2 = Logger.getInstance("backup");

System.out.println(log1.getName()); // main
System.out.println(log2.getName()); // main (shared)
```
""",
    "14. Best Practices": """
```java
// ✅ Use PascalCase for class and interface names
// ✅ Keep fields private and expose via getters/setters
// ✅ Use final for constants
// ✅ Document public methods with /** */
// ✅ Prefer interfaces for abstraction
```
""",
}

java_os: dict = {
    "01. Files and Directories": """
```java
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

// 📖 Read file content
String content = Files.readString(Paths.get("text.txt"));

// ✍️ Write to file
Files.writeString(Paths.get("new.txt"), "Hello world");

// ✅ Check if file exists
boolean exists = Files.exists(Paths.get("new.txt"));

// 🧹 Delete file
Files.delete(Paths.get("new.txt"));

// 📍 Current directory
String currentDir = new File(".").getAbsolutePath();

// 🗂️ List directory contents
File dir = new File(currentDir);
for (File file : dir.listFiles()) {
  System.out.println(file.getName());
}
```
""",
    "02. Paths and Manipulation": """
```java
import java.nio.file.Path;
import java.nio.file.Paths;

// 📎 File name
String name = Paths.get("/folder/file.txt").getFileName().toString();

// 🧩 File extension
String ext = new File("file.tar.gz").getName().replaceAll("^.*\\.", "");

// 📍 Absolute path
Path fullPath = Paths.get("data.txt").toAbsolutePath();

// 🔗 Join paths
Path joined = Paths.get("folder", "file.txt");
```
""",
    "03. Date and Time": """
```java
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.time.Duration;

// ⏰ Current date
LocalDateTime now = LocalDateTime.now();

// 📅 Parse string to date
LocalDate parsed = LocalDate.parse("2025-08-01");

// ⏳ Time difference
Duration diff = Duration.between(parsed.atStartOfDay(), now);

// 🧾 Simple format
String formatted = now.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"));
```
""",
    "04. System Processes": """
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;

// 🖥️ Run shell command
Process process = Runtime.getRuntime().exec("echo Hello Java");

// 📡 Print output
BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
reader.lines().forEach(System.out::println);
```
""",
    "05. Environment Variables": """
```java
// 🌍 All environment variables
Map<String, String> env = System.getenv();

// 🏡 HOME directory (Unix)
String home = env.get("HOME");
```
""",
    "06. Operating System Detection": """
```java
String os: dict = System.getProperty("os.name").toLowerCase();

if (os.contains("win")) {
  System.out.println("🪟 Windows");
} else if (os.contains("mac")) {
  System.out.println("🍎 macOS");
} else if (os.contains("nix") || os.contains("nux")) {
  System.out.println("🐧 Linux");
}
```
""",
    "07. Continuous Reading / Streams": """
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;

// 🔁 Start ping process
Process process = Runtime.getRuntime().exec("ping -c 4 localhost");

// 🖥️ Stream and display output
BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
reader.lines().forEach(line -> System.out.println("📡 " + line));
```
""",
}
