csharp_code: dict = {
    "01. Variables and Assignments": """
```c#
// Basic data types
string name = "David";               // String
bool state = true;                   // Boolean
int age = 10;                        // Integer
double temp = 18.5;                  // Double
int intNumber = 24;                  // Can be (int or double)

// Collections
List<object> mixedList = new List<object> { 1, "Juan", 23, "Juan" };
HashSet<int> numberSet = new HashSet<int> { 1, 2, 3, 4, 5 };
List<string> names = new List<string> { "Pedro", "Juan", "Cesar", "Carlos" };
List<int> numbers = new List<int> { 1, 2, 23, 4 };
Dictionary<string, object> person = new Dictionary<string, object> {
  ["Name"] = names[3],
  ["Age"] = numbers[3]
};

// Dynamic typing
var inferredType = 1.2;              // Type inferred as double (can't change)
dynamic dynamicVar = 1.2;            // Type can change
dynamicVar = true;

const double pi = 3.14;              // Compile-time constant
DateTime now = DateTime.Now;        // Runtime constant
string lateAssignation;             // Declare now, initialize later
lateAssignation = "assigned value";
```
""",
    "02. String Manipulation": """
```c#
string example = "hello world 12345";
string[] words = example.Split(' ');

// Basic operations
example.ToLower();                   // <= to lower case
example.ToUpper();                   // <= to upper case
example.Contains("h");               // <= Contains "h"
example.StartsWith("h");             // <= Starts with "h"
example.EndsWith("5");               // <= Ends with "5"
example.IndexOf("h");                // <= First index of "h"
example.LastIndexOf("h");            // <= Last index of "h"

// Transformations
"  hello  ".Trim();                  // <= Trimmed
example.Replace("h", "H");           // <= Replace all "h"
example.Replace("h", "H");           // <= Replace first "h" (same method)
example.Substring(0, 5);             // <= Substring

// Padding
example.PadRight(example.Length + 3, '0'); // <= Pad right
example.PadLeft(example.Length + 3, '0');  // <= Pad left

// Splitting and joining
example.Split(' ');                  // <= split
string.Join("-", words);            // <= join
```
""",
    "03. Collections: Lists, Sets, and Maps": """
```c#
// Lists (ordered, allows duplicates)
List<object> mixedList = new List<object> { 1, "Juan", 23, "Juan" };
List<int> numbers = new List<int> { 1, 2, 23, 4 };
List<string> names = new List<string> { "Pedro", "Juan", "Cesar", "Carlos" };

// to insert multiple values into a collection
List<int> list = new List<int> { 1, 2, 3 };
List<int> list2 = new List<int> { 0 };
list2.AddRange(list);

// List operations
numbers.Sort();
names.Add("Banana");
names.Insert(0, "Pineapple");
names.Remove("Pineapple");
names.RemoveAt(0);
if (names.Count > 0) names.RemoveAt(names.Count - 1);

names[0];                            // <= Index
names[0] = "New Value";              // <= Index
names.Count;                         // <= length
names.Contains("Juan");              // <= names contains Juan? true or false

// Sets (unordered, no duplicates)
HashSet<int> numberSet = new HashSet<int> { 1, 2, 3, 4, 5 };
HashSet<int> numberSet2 = new HashSet<int> { 4, 5, 6, 7, 8 };

// Sets operations
numberSet.Add(25);                   // <= add
numberSet.Remove(5);                 // <= remove
numberSet.UnionWith(numberSet2);    // <= Union
numberSet.IntersectWith(numberSet2);// <= Intersection
numberSet.ExceptWith(numberSet2);   // <= Difference

// Maps (key-value pairs)
Dictionary<string, object> person = new Dictionary<string, object> {
  ["Name"] = names[3],
  ["Age"] = numbers[3]
};

// Map operations
person["height"] = 75.5;             // <= Add
person.Remove("Name");               // <= Remove
person["Name"] = "Luis";             // <= Update
person.ContainsKey("Name");          // <= Contains keyName? true or false
person.ContainsValue("Luis");        // <= Contains valueName? true or false
```
""",
    "04. Key Concepts": """
```c#
// one line assignments
List<int> doubled = Enumerable.Range(0, 5).Select(index => index * 2).ToList(); // <= List generation
doubled.ForEach(num => Console.WriteLine($"Number: {num}"));                   // <= ForEach with arrow function
string Greet(bool isMorning) => isMorning ? "Good Morning" : "Hello";          // <= lambda function with null checking
button.Click += (sender, args) => Console.WriteLine("Clicked Bro");            // <= lambda function

// Null assignments and fallback
string? nullableVar = null;                            // execute and if not exist return null
string notNullableVar = "ready";                       // execute only if not null
string acceptNullVar = nullableVar ?? "default";       // execute only if it's null
string notNullVar = nullableVar != null ? nullableVar : "default"; // conditional fallback

// Boolean inversion
bool isTrue = true;
isTrue = !isTrue;                                      // if it's true return false
```
""",
    "05. Parsing and Type Conversion": """
```c#
// Parsing
int exampleInt = int.Parse("12");                      // <= String to int
double exampleDouble = double.Parse("12.5");           // <= String to double
string exampleStrFromInt = 12.ToString();              // <= Int to string
string exampleStrFromDouble = 12.5.ToString();         // <= Double to string

// String conversions
string fruitsString = "apple,banana,orange";           // <= fruitsString
var listFromString = fruitsString.Split(',');          // <= String to List
var setFromString = new HashSet<string>(listFromString); // <= String to Set
var mapFromString = listFromString
  .Select((value, index) => new { index, value })
  .ToDictionary(p => p.index, p => p.value);           // <= String to Map

// List conversions
List<string> fruitsList = new List<string> { "apple", "banana", "orange" }; // <= fruitsList
string stringFromList = string.Join(",", fruitsList);  // <= List to String
HashSet<string> setFromList = new HashSet<string>(fruitsList); // <= List to Set
var mapFromList = fruitsList
  .Select((value, index) => new { index, value })
  .ToDictionary(p => p.index, p => p.value);           // <= List to Map

// Set conversions
HashSet<string> fruitsSet = new HashSet<string> { "apple", "banana", "orange" }; // <= fruitsSet
string stringFromSet = string.Join(",", fruitsSet); // <= Set to String
List<string> listFromSet = fruitsSet.ToList();       // <= Set to List
var mapFromSet = listFromSet
  .Select((value, index) => new { index, value })
  .ToDictionary(p => p.index, p => p.value);          // <= Set to Map

// Map conversions
Dictionary<int, string> fruitsMap = new Dictionary<int, string> {
  [0] = "apple",
  [1] = "banana"
};                                                     // <= fruitsMap
string stringFromMap = string.Join(",", fruitsMap.Values); // <= Map to String
List<string> listFromMap = fruitsMap.Values.ToList();      // <= Map to List
HashSet<string> setFromMap = new HashSet<string>(fruitsMap.Values); // <= Map to Set
```
""",
    "06. Conditionals": """
```c#
int condition1 = 10;
int condition2 = 5;

// Ternary
string result = isTrue ? "True case" : "False case";

// If-else
if (condition1 == 10) {
  Console.WriteLine("Condition1 is true");
} else if (condition2 == 5) {
  Console.WriteLine("Condition2 is true");
} else {
  Console.WriteLine("All conditions false");
}

// Switch-case
string value = "case2";

switch (value) {
  case "case1":
    Console.WriteLine("Case 1 executed");
    break;
  case "case2":
    Console.WriteLine("Case 2 executed");
    break;
  case "case3":
    Console.WriteLine("Case 3 executed");
    break;
  default:
    Console.WriteLine("Default case executed");
    break;
}
```
""",
    "07. Loops and Repetition": """
```c#
// For loop
for (int i = 0; i < 5; i++) {
  if (i == 3) continue;
  Console.WriteLine($"For loop: {i}");
  if (i == 4) break;
}

// For-each loop (lists)
List<string> names = new List<string> { "Maria", "Joaquin", "Luisa" };
foreach (string name in names) {
  Console.WriteLine($"Hello {name}");
}

// For-each loop (maps)
Dictionary<string, int> ages = new Dictionary<string, int> {
  ["Maria"] = 20,
  ["Joaquin"] = 21,
  ["Luisa"] = 22
};
foreach (var entry in ages) {
  Console.WriteLine($"{entry.Key} is {entry.Value} years old");
}

// While loop
int count = 0;
while (count < 3) {
  Console.WriteLine($"While loop: {count}");
  count++;
}

// Do-while loop
do {
  Console.WriteLine($"Do-while loop: {count}");
  count--;
} while (count > 0);
```
""",
    "08. Functions and Methods": """
```c#
// One-line expression
void CallFunction(string parameter) => Console.WriteLine($"hello {parameter}");

// Lambda expression
Action<string> greet = (parameter) => Console.WriteLine($"hello {parameter}");
greet("world");

// No return
void CallFunctionVoid(string parameter) {
  Console.WriteLine($"hello {parameter}");
}

// Return String
string CallStringFunction(string parameter) {
  return $"hello {parameter}";
}

// Return int
int CallIntFunction(int parameter) {
  return parameter;
}

// Return tuple
(string, int) CallTupleFunction(string parameter) {
  return ($"hello {parameter}", 123);
}

// Functions as objects (delegates)
int Add(int a, int b) {
  return a + b;
}

// Assign to variable
Func<int, int, int> sum = Add;
Console.WriteLine(sum(2, 3)); // returns: 5

// Pass as argument
int TotalSum = Add(2, Add(2, 3)); // returns: 7
```
""",
    "09. Error Handling": """
```c#
try {
  // Potentially error-prone code
  double result = double.Parse("123") / 0;
  Console.WriteLine(result);
}
catch (DivideByZeroException) {
  Console.WriteLine("Cannot divide by zero");
}
catch (FormatException) {
  Console.WriteLine("Invalid number format");
}
catch (Exception e) {
  Console.WriteLine($"An error occurred: {e.Message}");
}
finally {
  Console.WriteLine("This always executes");
}
```
""",
}

csharp_class: dict = {
    "01. Basic Classes": """
In C#, classes are defined using the keyword class and follow PascalCase naming. They group data and behavior into reusable objects.

```csharp
class Vehicle {
  public string Brand;
  public int Year;

  public void ShowInfo() {
    Console.WriteLine($"Brand: {Brand}, Year: {Year}");
  }
}

var myCar = new Vehicle {
  Brand = "Toyota",
  Year = 2020
};
myCar.ShowInfo(); // Brand: Toyota, Year: 2020
```
""",
    "02. Properties and Methods": """
Use properties (get and set) to manage access. readonly members can only be set once.

```csharp
class User {
  public string Id { get; }
  public string Name { get; set; }

  public User(string id, string name) {
    Id = id;
    Name = name;
  }

  public void Greet() {
    Console.WriteLine($"Hello, {Name}! (ID: {Id})");
  }
}

var u = new User("u123", "Ana");
u.Greet(); // Hello, Ana! (ID: u123)
```
""",
    "03. Constructors": """
```csharp
// Basic constructor
class Point {
  public double X, Y;
  public Point(double x, double y) {
    X = x;
    Y = y;
  }
}

// Named constructor via static method
class Point {
  public double X, Y;
  public Point(double x, double y) {
    X = x;
    Y = y;
  }

  public static Point Origin() => new Point(0, 0);
}

// Readonly constructor
class Coordinate {
  public readonly int X, Y;
  public Coordinate(int x, int y) {
    X = x;
    Y = y;
  }
}

// Factory constructor (singleton)
class Logger {
  private static Dictionary<string, Logger> _cache = new();
  public string Name;

  private Logger(string name) {
    Name = name;
  }

  public static Logger Create(string name) {
    if (!_cache.ContainsKey(name)) {
      _cache[name] = new Logger(name);
    }
    return _cache[name];
  }
}
```csharp
""",
    "04. Inheritance": """
```csharp
Inheritance is achieved using : and virtual/override for behavior customization.

`csharp
class Animal {
  public virtual void Move() => Console.WriteLine("The animal moves");
}

class Dog : Animal {
  public override void Move() => Console.WriteLine("The dog runs");
}

Animal a = new Dog();
a.Move(); // The dog runs
```

""",
    "05. Polymorphism": """
```csharp
Polymorphism enables flexible APIs via interfaces.

`csharp
interface IShape {
  double Area();
}

class Circle : IShape {
  public double Radius;
  public Circle(double radius) => Radius = radius;
  public double Area() => Math.PI  Radius  Radius;
}
```csharp
""",
    "06. Mixins": """
C# uses composition + interfaces to simulate mixins.

```csharp

interface IMusical {
  void PlayInstrument();
}

class MusicalTrait : IMusical {
  public void PlayInstrument() => Console.WriteLine("Playing instrument");
}

class Musician {
  private IMusical _musical = new MusicalTrait();
  public void Perform() => _musical.PlayInstrument();
}
```
""",
    "07. Interfaces": """
Interfaces define contracts. Implementing classes must fulfill them.

```csharp

interface IPerson {
  string Greet();
}

class Impostor : IPerson {
  public string Greet() => "I am an impostor!";
}
```
""",
    "08. Abstract Classes": """
Abstract classes define shared structure and force overrides.

```csharp

abstract class Vehicle {
  public abstract void Move();
}

class Bicycle : Vehicle {
  public override void Move() => Console.WriteLine("The bicycle moves");
}
```
""",
    "09. Encapsulation and Access": """
Use access modifiers to protect internal state.

```csharp
class Bank {
  private double _balance = 0;
  public void Deposit(double amount) => _balance += amount;
  public double Balance => _balance;
}
```
""",
    "10. Static Members and Constants": """
Static members belong to the class rather than the instance.

```csharp
class Utils {
  public const double Pi = 3.1416;
  public static double Square(double x) => x * x;
}

Console.WriteLine(Utils.Pi);      // 3.1416
Console.WriteLine(Utils.Square(5)); // 25
```
""",
    "11. Generics in Classes": """
Generics allow reusable, type-safe containers.

```csharp
class Box<T> {
  public T Content;
  public Box(T content) => Content = content;
}

var boxInt = new Box<int>(42);
var boxStr = new Box<string>("Hello");

Console.WriteLine(boxInt.Content); // 42
Console.WriteLine(boxStr.Content); // Hello
```
""",
    "Annotations and Extras": """
```csharp
// Metadata annotations
[Obsolete("Use NewMethod instead")]
void OldMethod() {}

// Design patterns
// Singleton, Factory, Strategy, Observer, Decorator
// All supported using interfaces, static constructors, and delegates

// Best practices
// Use PascalCase
// Prefer immutables with readonly
// Separate concerns (SRP)
// Document public APIs with XML comments

/// Adds two numbers
/// a and b: operands
/// Returns: sum
int Add(int a, int b) => a + b;
```
""",
}

csharp_os: dict = {
    "01. Path and File Management": """
Use System.IO to interact with paths and files.

```csharp

using System.IO;

// Get current directory
string dir = Directory.GetCurrentDirectory();

// Create a path
string path = Path.Combine(dir, "data.txt");

// Write to file
File.WriteAllText(path, "Hello world");

// Read from file
string content = File.ReadAllText(path);
```
""",
    "02. Environment Variables": """
Access system-wide environment info via Environment.

```csharp

string os: dict = Environment.OSVersion.ToString();
string user = Environment.UserName;
string tempPath = Path.GetEnvironmentVariable("TEMP");
```
""",
    "03. Process Execution": """
Run external programs with Process.

```csharp

using System.Diagnostics;

ProcessStartInfo psi = new ProcessStartInfo("notepad.exe");
Process.Start(psi);
```
""",
    "04. Async File IO": """
Use async versions for non-blocking operations.

```csharp

using System.IO;
using System.Threading.Tasks;

async Task SaveFileAsync(string path, string data) {
  await File.WriteAllTextAsync(path, data);
}
```
""",
    "05. Directory Traversal": """
Explore folders and files.

```csharp

string[] files = Directory.GetFiles("docs");
string[] folders = Directory.GetDirectories("docs");
```
""",
    "06. Temporary Files": """
C# provides APIs for temp files via Path and File.

`csharp
string temp = Path.GetTempFileName();
File.WriteAllText(temp, "Temp data");
`
""",
    "07. OS Detection": """
Use Environment to detect OS family.

```csharp

bool isWindows = Environment.OSVersion.Platform == PlatformID.Win32NT;
bool isUnix = Environment.OSVersion.Platform == PlatformID.Unix;
```
""",
    "08. Permissions & Access Control": """
Use file attributes and exceptions to check access.

`csharp
bool isWritable = File.Exists("file.txt") &&
  (File.GetAttributes("file.txt") & FileAttributes.ReadOnly) == 0;
`
""",
    "09. File Metadata": """
Access creation/modification dates and sizes.

```csharp

DateTime created = File.GetCreationTime("file.txt");
DateTime modified = File.GetLastWriteTime("file.txt");
long size = new FileInfo("file.txt").Length;
```
""",
    "10. Symbolic Links": """
Requires .NET 6+ with platform-specific flags.

```csharp

Directory.CreateSymbolicLink("link", "target");
```
Windows requires admin rights. Use with care.
""",
    "11. Serialization (JSON)": """
Use System.Text.Json for JSON files.

```csharp

using System.Text.Json;

var person = new { Name = "Ana", Age = 30 };
string json = JsonSerializer.Serialize(person);
File.WriteAllText("person.json", json);
```
""",
    "Annotations and Extras": """
```csharp
// Use using System.IO for most I/O
// Prefer async methods for responsiveness
// Use Path.Combine() to avoid platform-specific issues
// Check existence before reading/writing
// Wrap file access in try/catch

/// Loads a config file
/// path: path to file
/// Returns: file content as string
string LoadConfig(string path) =>
  File.Exists(path) ? File.ReadAllText(path) : "";
```
""",
}
