kotlin_code: dict = {
    "01. Variables and Assignments": """
// Immutable vs mutable
val name: String = "David"     // Constant (String)
var state: Boolean = true      // Variable (Boolean)
val age = 10                   // Type inferred as Int
val temp = 18.5                // Inferred as Double

// Collections
val mixedList = listOf(1, "Juan", 23, "Juan")  // List of Any
val numberSet = setOf(1, 2, 3, 4, 5)
val person = mapOf("Name" to "Carlos", "Age" to 23)

// Constants
const val PI = 3.1415          // Compile-time constant
val now = java.time.LocalDateTime.now() // Runtime value
""",
    "02. String Manipulation": """
val example = "hello world 12345"
val words = example.split(" ")

// Basic operations
example.lowercase()
example.uppercase()
example.contains("h")
example.startsWith("h")
example.endsWith("5")
example.indexOf("h")
example.lastIndexOf("h")
example.trim()
example.replace("h", "H")
example.substring(0, 5)

// Padding
example.padEnd(example.length + 3, '0')
example.padStart(example.length + 3, '0')

// Joining
words.joinToString("-")
""",
    "03. Collections: Lists, Sets, Maps": """
val numbers = mutableListOf(1, 2, 23, 4)
val names = mutableListOf("Pedro", "Juan", "Cesar", "Carlos")

numbers.sort()
names.add("Banana")
names.add(0, "Pineapple")
names.removeAt(0)
names[0] = "New"
names.contains("Juan")

val set1 = mutableSetOf(1, 2, 3, 4, 5)
val set2 = setOf(4, 5, 6, 7, 8)

set1.add(25)
set1.remove(5)
set1.union(set2)
set1.intersect(set2)
set1.subtract(set2)

val person = mutableMapOf("Name" to "Luis")
person["height"] = 75.5
person.remove("Name")
person["Name"] = "Luis"
person.containsKey("Name")
person.containsValue("Luis")
""",
    "04. Key Concepts": """
val doubled = List(5) { it * 2 }
doubled.forEach { println("Number: $it") }

fun greet(isMorning: Boolean) = if (isMorning) "Good Morning" else "Hello"

val click = { println("Clicked Bro") }

var nullable: String? = null
val notNull = nullable ?: "Fallback"

var isTrue = true
isTrue = !isTrue
""",
    "05. Parsing and Type Conversion": """
val intVal = "12".toInt()
val doubleVal = "12.5".toDouble()
val strInt = 12.toString()
val strDouble = 12.5.toString()

val fruitsString = "apple,banana,orange"
val listFromString = fruitsString.split(",")
val setFromString = listFromString.toSet()
val mapFromString = listFromString.mapIndexed { i, v -> i to v }.toMap()

val fruitsList = listOf("apple", "banana", "orange")
val stringFromList = fruitsList.joinToString(",")
val setFromList = fruitsList.toSet()
val mapFromList = fruitsList.mapIndexed { i, v -> i to v }.toMap()
""",
    "06. Conditionals": """
val condition1 = 10
val condition2 = 5

val result = if (true) "True case" else "False case"

if (condition1 == 10) {
  println("Condition1 is true")
} else if (condition2 == 5) {
  println("Condition2 is true")
} else {
  println("All conditions false")
}

val value = "case2"
when (value) {
  "case1" -> println("Case 1 executed")
  "case2" -> println("Case 2 executed")
  else -> println("Default case executed")
}
""",
    "07. Loops and Repetition": """
for (i in 0..4) {
  if (i == 3) continue
  println("For loop: $i")
  if (i == 4) break
}

val names = listOf("Maria", "Joaquin", "Luisa")
for (name in names) {
  println("Hello $name")
}

val ages = mapOf("Maria" to 20, "Joaquin" to 21, "Luisa" to 22)
for ((name, age) in ages) {
  println("$name is $age years old")
}

var count = 0
while (count < 3) {
  println("While loop: $count")
  count++
}

count = 3
do {
  println("Do-while loop: $count")
  count--
} while (count > 0)
""",
    "08. Functions and Lambdas": """
fun greet(param: String) {
  println("hello $param")
}

val greetLambda: (String) -> Unit = { param ->
  println("hello $param")
}

fun returnString(param: String): String = "hello $param"
fun returnInt(param: Int): Int = param
fun returnPair(param: String): Pair<Int, String> = 123 to param

fun add(a: Int, b: Int): Int = a + b

val sumResult = add(2, 3)
val totalSum = add(2, add(2, 3))
""",
    "09. Error Handling": """
try {
  val result = "123".toInt() / 0
  println(result)
} catch (e: ArithmeticException) {
  println("Cannot divide by zero")
} catch (e: NumberFormatException) {
  println("Invalid number format")
} catch (e: Exception) {
  println("An error occurred: ${e.message}")
} finally {
  println("This always executes")
}
""",
}

kotlin_class: dict = {
    "01. Basic Classes": """
class Vehicle {
  var brand: String = ""
  var year: Int = 0

  fun showInfo() {
    println("Brand: $brand, Year: $year")
  }
}

val myCar = Vehicle()
myCar.brand = "Toyota"
myCar.year = 2020
myCar.showInfo() // Brand: Toyota, Year: 2020
""",
    "02. Properties and Methods": """
class User(val id: String) {
  var name: String = ""

  fun greet() {
    println("Hello, $name! (ID: $id)")
  }
}

val u = User("u123")
u.name = "Ana"
u.greet() // Hello, Ana! (ID: u123)
""",
    "03. Constructors": """
class Point(val x: Double = 0.0, val y: Double = 0.0)

val p1 = Point(2.0, 3.0)
val p2 = Point() // Default to origin
""",
    "04. Inheritance": """
open class Animal {
  open fun move() {
    println("The animal moves")
  }
}

class Dog : Animal() {
  override fun move() {
    println("The dog runs")
  }
}

val a: Animal = Dog()
a.move() // The dog runs
""",
    "05. Polymorphism": """
interface Shape {
  fun area(): Double
}

class Circle(val radius: Double) : Shape {
  override fun area() = 3.1416 * radius * radius
}

val c: Shape = Circle(2.0)
println("Area: ${c.area()}")
""",
    "06. Mixins via Interfaces and Extensions": """
interface Musical {
  fun playInstrument()
}

class Musician : Musical {
  override fun playInstrument() {
    println("Playing instrument")
  }
}

val m = Musician()
m.playInstrument()
""",
    "07. Interface Contracts": """
interface Person {
  fun greet(): String
}

class Impostor : Person {
  override fun greet() = "I'm an impostor!"
}

val i = Impostor()
println(i.greet())
""",
    "08. Abstract Classes": """
abstract class Vehicle {
  abstract fun move()
}

class Bike : Vehicle() {
  override fun move() {
    println("The bike moves forward")
  }
}

val b = Bike()
b.move()
""",
    "09. Encapsulation": """
class Bank {
  private var balance: Double = 0.0

  fun deposit(amount: Double) {
    balance += amount
  }

  fun getBalance() = balance
}

val myBank = Bank()
myBank.deposit(100.0)
println(myBank.getBalance()) // 100.0
""",
    "10. Static Members and Constants": """
object Utilities {
  const val PI = 3.1416

  fun square(x: Double) = x * x
}

println(Utilities.PI)
println(Utilities.square(5.0))
""",
    "11. Generics in Classes": """
class Box<T>(val content: T)

val boxInt = Box(42)
val boxStr = Box("Hello")

println(boxInt.content) // 42
println(boxStr.content) // Hello
""",
    "12. Documentation Comments": """
/**
 * A simple calculator class.
 */
class Calculator {

  /**
   * Adds two numbers and returns the result.
   */
  fun add(a: Int, b: Int): Int = a + b
}
""",
    "13. Design Patterns (Singleton)": """
object Logger {
  val name = "Main"
}

val log1 = Logger
val log2 = Logger

println(log1.name) // Main
println(log2.name) // Main (shared instance)
""",
    "14. Best Practices": """
// ✅ Use PascalCase for class and interface names
// ✅ Keep properties private unless needed
// ✅ Favor data classes for simple models
// ✅ Use interfaces for polymorphism
// ✅ Document with /** */ for public APIs
""",
}

kotlin_os: dict = {
    "01. Files and Directories": """
import java.io.File

// 📖 Read file content
val content = File("text.txt").readText()

// ✍️ Write to file
File("new.txt").writeText("Hello world")

// ✅ Check if file exists
val exists = File("new.txt").exists()

// 🧹 Delete file
File("new.txt").delete()

// 📍 Current directory
val currentDir = File(".").absolutePath

// 🗂️ List directory contents
val files = File(currentDir).listFiles()?.forEach {
  println(it.name)
}
""",
    "02. Paths and Manipulation": """
import java.nio.file.Paths

// 📎 File name
val name = Paths.get("/folder/file.txt").fileName.toString()

// 🧩 File extension
val ext = File("file.tar.gz").extension

// 📍 Absolute path
val fullPath = Paths.get("data.txt").toAbsolutePath()

// 🔗 Join paths
val joined = Paths.get("folder", "file.txt")
""",
    "03. Date and Time": """
import java.time.LocalDateTime
import java.time.format.DateTimeFormatter
import java.time.Duration

// ⏰ Current date
val now = LocalDateTime.now()

// 📅 Parse string to date
val parsed = LocalDateTime.parse("2025-08-01T00:00:00")

// ⏳ Time difference
val diff = Duration.between(parsed, now).toHours()

// 🧾 Simple format
val format = now.format(DateTimeFormatter.ofPattern("dd/MM/yyyy"))
""",
    "04. System Processes": """
import java.io.BufferedReader
import java.io.InputStreamReader

// 🖥️ Run shell command
val process = Runtime.getRuntime().exec("echo Hello Kotlin")
val reader = BufferedReader(InputStreamReader(process.inputStream))

// 📡 Print output
reader.lines().forEach { println(it) }
""",
    "05. Environment Variables": """
// 🌍 All environment variables
val envVars = System.getenv()

// 🏡 HOME directory (Unix)
val home = envVars["HOME"]
""",
    "06. Operating System Detection": """
val osName = System.getProperty("os.name")

when {
  osName.contains("Windows", ignoreCase = true) -> println("🪟 Windows")
  osName.contains("Linux", ignoreCase = true) -> println("🐧 Linux")
  osName.contains("Mac", ignoreCase = true) -> println("🍎 macOS")
}
""",
    "07. Continuous Reading / Streams": """
import java.io.BufferedReader
import java.io.InputStreamReader

// 🔁 Start ping process
val process = Runtime.getRuntime().exec("ping -c 4 localhost")
val reader = BufferedReader(InputStreamReader(process.inputStream))

// 🖥️ Stream and display output
reader.lines().forEach { println("📡 $it") }
""",
}
