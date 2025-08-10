swift_code: dict = {
    "01. Variables and Assignments": """
// Immutable vs Mutable
let name = "David"           // Constant (String)
var state = true             // Variable (Bool)
var age: Int = 10            // Integer
var temp: Double = 18.5      // Double
var pi = 3.1415              // Inferred as Double

// Collections
var mixedArray: [Any] = [1, "Juan", 23, "Juan"]
var numberSet: Set<Int> = [1, 2, 3, 4, 5]
var person: [String: Any] = ["Name": "Carlos", "Age": 23]

// Constants and late assignments
let now = Date()             // Runtime constant
var lateValue: String!       // Implicitly unwrapped optional
lateValue = "Assigned later"
""",
    "02. String Manipulation": """
let example = "hello world 12345"
let words = example.split(separator: " ")     // Returns [Substring]

// Basic operations
example.lowercased()
example.uppercased()
example.contains("h")
example.hasPrefix("h")
example.hasSuffix("5")
example.firstIndex(of: "h")
example.lastIndex(of: "h")
example.trimmingCharacters(in: .whitespaces)
example.replacingOccurrences(of: "h", with: "H")
example.prefix(5)                              // Substring

// Padding
String(repeating: "0", count: 3) + example     // Pad left
example + String(repeating: "0", count: 3)     // Pad right

// Splitting and joining
let joined = words.joined(separator: "-")
""",
    "03. Collections: Arrays, Sets, Dictionaries": """
var numbers = [1, 2, 23, 4]
var names = ["Pedro", "Juan", "Cesar", "Carlos"]

numbers.sort()
names.append("Banana")
names.insert("Pineapple", at: 0)
names.remove(at: 0)
names[0] = "New"
names.contains("Juan")

var numberSet: Set<Int> = [1,2,3,4,5]
let numberSet2: Set<Int> = [4,5,6,7,8]

numberSet.insert(25)
numberSet.remove(5)
numberSet.union(numberSet2)
numberSet.intersection(numberSet2)
numberSet.subtracting(numberSet2)

var person: [String: Any] = ["Name": "Luis"]
person["Height"] = 75.5
person.removeValue(forKey: "Name")
person["Name"] = "Luis"
person.keys.contains("Name")
person.values.contains(where: { ($0 as? String) == "Luis" })
""",
    "04. Key Concepts": """
let doubled = (0..<5).map { $0 * 2 }
doubled.forEach { print("Number: \\($0)") }

func greet(isMorning: Bool) -> String {
  return isMorning ? "Good Morning" : "Hello"
}

let buttonAction = { print("Clicked Bro") }

// Optionals
var nullable: String? = nil
let notNull = nullable ?? "Fallback"

var isTrue = true
isTrue.toggle()
""",
    "05. Parsing and Type Conversion": """
let intVal = Int("12")
let doubleVal = Double("12.5")
let strInt = String(12)
let strDouble = String(12.5)

let fruitsString = "apple,banana,orange"
let listFromString = fruitsString.split(separator: ",").map(String)
let setFromString = Set(listFromString)
let mapFromString = Dictionary(uniqueKeysWithValues: listFromString.enumerated().map { ($0.offset, $0.element) })

let fruitsList = ["apple", "banana", "orange"]
let stringFromList = fruitsList.joined(separator: ",")
let setFromList = Set(fruitsList)
let mapFromList = Dictionary(uniqueKeysWithValues: fruitsList.enumerated().map { ($0.offset, $0.element) })
""",
    "06. Conditionals": """
let condition1 = 10
let condition2 = 5

let result = true ? "True case" : "False case"

if condition1 == 10 {
  print("Condition1 is true")
} else if condition2 == 5 {
  print("Condition2 is true")
} else {
  print("All conditions false")
}

let value = "case2"
switch value {
case "case1":
  print("Case 1 executed")
case "case2":
  print("Case 2 executed")
default:
  print("Default case executed")
}
""",
    "07. Loops and Repetition": """
for i in 0..<5 {
  if i == 3 { continue }
  print("For loop: \\(i)")
  if i == 4 { break }
}

let names = ["Maria", "Joaquin", "Luisa"]
for name in names {
  print("Hello \\(name)")
}

let ages = ["Maria": 20, "Joaquin": 21, "Luisa": 22]
for (name, age) in ages {
  print("\\(name) is \\(age) years old")
}

var count = 0
while count < 3 {
  print("While loop: \\(count)")
  count += 1
}

repeat {
  print("Do-while loop: \\(count)")
  count -= 1
} while count > 0
""",
    "08. Functions and Closures": """
func greet(param: String) {
  print("hello \\(param)")
}

let greetClosure: (String) -> Void = { param in
  print("hello \\(param)")
}

func returnString(param: String) -> String {
  return "hello \\(param)"
}

func returnInt(param: Int) -> Int {
  return param
}

func returnTuple(param: String) -> (Int, String) {
  return (123, param)
}

func add(_ a: Int, _ b: Int) -> Int {
  return a + b
}

let sumResult = add(2, 3)
let totalSum = add(2, add(2, 3))
""",
    "09. Error Handling": """
enum DivisionError: Error {
  case divideByZero
}

func safeDivide(_ a: Int, _ b: Int) throws -> Double {
  guard b != 0 else { throw DivisionError.divideByZero }
  return Double(a) / Double(b)
}

do {
  let result = try safeDivide(123, 0)
  print(result)
} catch DivisionError.divideByZero {
  print("Cannot divide by zero")
} catch {
  print("An error occurred: \\(error)")
} finally {
  print("This always executes")
}
""",
}

swift_class: dict = {
    "01. Basic Classes": """
class Vehicle {
  var brand: String = ""
  var year: Int = 0

  func showInfo() {
    print("Brand: \\(brand), Year: \\(year)")
  }
}

let myCar = Vehicle()
myCar.brand = "Toyota"
myCar.year = 2020
myCar.showInfo() // Brand: Toyota, Year: 2020
""",
    "02. Properties and Methods": """
class User {
  let id: String        // Immutable
  var name: String      // Mutable

  init(id: String, name: String) {
    self.id = id
    self.name = name
  }

  func greet() {
    print("Hello, \\(name)! (ID: \\(id))")
  }
}

let u = User(id: "u123", name: "Ana")
u.greet() // Hello, Ana! (ID: u123)
""",
    "03. Constructors (Initializers)": """
struct Point {
  var x: Double
  var y: Double

  init(x: Double = 0, y: Double = 0) {
    self.x = x
    self.y = y
  }
}

let p1 = Point(x: 2, y: 3)
let p2 = Point() // Defaults to origin (0,0)
""",
    "04. Inheritance": """
class Animal {
  func move() {
    print("The animal moves")
  }
}

class Dog: Animal {
  override func move() {
    print("The dog runs")
  }
}

let a: Animal = Dog()
a.move() // The dog runs
""",
    "05. Polymorphism": """
protocol Shape {
  func area() -> Double
}

class Circle: Shape {
  var radius: Double
  init(radius: Double) { self.radius = radius }

  func area() -> Double {
    return 3.1416 * radius * radius
  }
}
""",
    "06. Mixins via Protocol Extensions": """
protocol Musical {
  func playInstrument()
}

extension Musical {
  func playInstrument() {
    print("Playing instrument")
  }
}

class Musician: Musical {}

let m = Musician()
m.playInstrument() // Playing instrument
""",
    "07. Protocols as Interfaces": """
protocol Person {
  func greet() -> String
}

class Impostor: Person {
  func greet() -> String {
    return "I'm an impostor!"
  }
}

let i = Impostor()
print(i.greet())
""",
    "08. Abstract Behavior via Protocols": """
protocol Vehicle {
  func move()
}

class Bike: Vehicle {
  func move() {
    print("The bike moves forward")
  }
}

let b = Bike()
b.move()
""",
    "09. Encapsulation and Access": """
class Bank {
  private var balance: Double = 0

  func deposit(_ amount: Double) {
    balance += amount
  }

  func getBalance() -> Double {
    return balance
  }
}

let myBank = Bank()
myBank.deposit(100)
print(myBank.getBalance()) // 100.0
""",
    "10. Static Members and Constants": """
class Utilities {
  static let pi = 3.1416

  static func square(_ x: Double) -> Double {
    return x * x
  }
}

print(Utilities.pi)              // 3.1416
print(Utilities.square(5))       // 25.0
""",
    "11. Generics in Classes": """
class Box<T> {
  var content: T
  init(content: T) {
    self.content = content
  }
}

let boxInt = Box(content: 42)
let boxStr = Box(content: "Hello")

print(boxInt.content) // 42
print(boxStr.content) // Hello
""",
    "12. Documentation Comments": """
/// A calculator that performs arithmetic
class Calculator {
  /// Adds two integers
  func add(_ a: Int, _ b: Int) -> Int {
    return a + b
  }
}
""",
    "13. Design Patterns (Singleton)": """
class Logger {
  static let shared = Logger(name: "Main")
  let name: String

  private init(name: String) {
    self.name = name
  }
}

let log1 = Logger.shared
let log2 = Logger.shared

print(log1.name) // Main
print(log2.name) // Main (shared instance)
""",
    "14. Best Practices": """
// ✅ Use PascalCase for class and protocol names
// ✅ Prefer structs for value types
// ✅ Use access modifiers like private and public
// ✅ Document public APIs with /// comments
// ✅ Avoid logic in initializers—use factories or setup methods
""",
}

swift_os: dict = {
    "01. Files and Directories": """
import Foundation

// 📖 Read file content
let content = try String(contentsOfFile: "text.txt")

// ✍️ Write to file
try "Hello world".write(toFile: "new.txt", atomically: true, encoding: .utf8)

// ✅ Check if file exists
let exists = FileManager.default.fileExists(atPath: "new.txt")

// 🧹 Delete file
try FileManager.default.removeItem(atPath: "new.txt")

// 📍 Current directory
let currentDir = FileManager.default.currentDirectoryPath

// 🗂️ List directory contents
let contents = try FileManager.default.contentsOfDirectory(atPath: currentDir)
""",
    "02. Paths and Manipulation": """
import Foundation

// 📎 File name
let name = URL(fileURLWithPath: "/folder/file.txt").lastPathComponent

// 🧩 File extension
let ext = URL(fileURLWithPath: "file.tar.gz").pathExtension

// 📍 Absolute path
let fullPath = URL(fileURLWithPath: "data.txt").absoluteURL

// 🔗 Join paths
let joined = URL(fileURLWithPath: "folder").appendingPathComponent("file.txt")
""",
    "03. Date and Time": """
import Foundation

// ⏰ Current date
let now = Date()

// 🌐 UTC version
let utc = now.timeIntervalSince1970

// 📅 Parse string to date
let formatter = DateFormatter()
formatter.dateFormat = "yyyy-MM-dd"
let parsed = formatter.date(from: "2025-08-01")

// ⏳ Time difference
let diff = now.timeIntervalSince(parsed ?? Date())

// 🧾 Simple format
formatter.dateFormat = "dd/MM/yyyy"
let formatted = formatter.string(from: now)
""",
    "04. System Processes": """
import Foundation

// 🖥️ Run shell command
let task = Process()
task.executableURL = URL(fileURLWithPath: "/bin/echo")
task.arguments = ["Hello Swift"]

let pipe = Pipe()
task.standardOutput = pipe

try task.run()
task.waitUntilExit()

let data = pipe.fileHandleForReading.readDataToEndOfFile()
let output = String(data: data, encoding: .utf8)
print(output ?? "")
""",
    "05. Environment Variables": """
import Foundation

// 🌍 All environment variables
let env = ProcessInfo.processInfo.environment

// 🏡 HOME directory (Unix)
let home = env["HOME"]
""",
    "06. Operating System Detection": """
#if os(macOS)
print("🍎 This is macOS")
#elseif os(Linux)
print("🐧 This is Linux")
#elseif os(Windows)
print("🪟 This is Windows")
#endif
""",
    "07. Continuous Reading / Streams": """
import Foundation

// 🔁 Start real-time process
let task = Process()
task.executableURL = URL(fileURLWithPath: "/sbin/ping")
task.arguments = ["localhost"]

let pipe = Pipe()
task.standardOutput = pipe

try task.run()

pipe.fileHandleForReading.readabilityHandler = { handle in
  if let line = String(data: handle.availableData, encoding: .utf8) {
    print("📡 \\(line)")
  }
}
""",
}
