rust_code: dict = {
    "01. Variables and Assignments": """
// Primitive values
let name = "David";              // &str
let state: bool = true;          // Boolean
let age: i32 = 10;               // Integer
let temp: f64 = 18.5;            // Float

// Collections
let mixed_list = vec![1, 2, 3];  // Rust doesn’t allow truly mixed lists
let number_set: HashSet<i32> = [1,2,3,4,5].iter().cloned().collect();
let mut person: HashMap<&str, i32> = HashMap::new();
person.insert("Age", 24);

// Constants
const PI: f64 = 3.1415;
let now = chrono::Local::now(); // Requires chrono crate
""",
    "02. String Manipulation": """
let example = String::from("hello world 12345");

// Basic operations
example.to_lowercase();        // Lowercase
example.to_uppercase();        // Uppercase
example.contains("h");         // Check existence
example.starts_with("h");      // Start condition
example.ends_with("5");        // End condition
example.find("h");             // Index position
example.rfind("h");            // Last index
example.trim();                // Trim spaces
example.replace("h", "H");     // Replace text
&example[0..5];                // Substring

// Padding & joining
let padded = format!("{:<width$}", example, width=example.len()+3);
let words: Vec<&str> = example.split(' ').collect();
let joined = words.join("-");
""",
    "03. Collections: Vectors, Sets, and Maps": """
let mut numbers = vec![1, 2, 23, 4];
let mut names = vec!["Pedro", "Juan", "Cesar", "Carlos"];

numbers.sort();
names.push("Banana");
names.insert(0, "Pineapple");
names.remove(0);
names[0] = "New";
names.contains(&"Juan");

let set1: HashSet<i32> = [1,2,3,4,5].iter().cloned().collect();
let set2: HashSet<i32> = [4,5,6,7,8].iter().cloned().collect();

let union = set1.union(&set2);
let intersection = set1.intersection(&set2);
let difference = set1.difference(&set2);

let mut person: HashMap<&str, &str> = HashMap::new();
person.insert("Name", "Luis");
person.remove("Name");
person.contains_key("Name");
person.values().any(|&v| v == "Luis");
""",
    "04. Key Concepts": """
let doubled: Vec<i32> = (0..5).map(|i| i * 2).collect();
doubled.iter().for_each(|num| println!("Number: {}", num));

fn greet(is_morning: bool) -> &'static str {
  if is_morning { "Good Morning" } else { "Hello" }
}

let click_button = || println!("Clicked Bro");

let nullable: Option<String> = None;
let fallback = nullable.unwrap_or_else(|| "fallback".to_string());

let mut is_true = true;
is_true = !is_true;
""",
    "05. Parsing and Type Conversion": """
let int_val: i32 = "12".parse().unwrap();
let float_val: f64 = "12.5".parse().unwrap();
let str_val = 12.to_string();

let fruits = "apple,banana,orange";
let list: Vec<&str> = fruits.split(',').collect();
let set: HashSet<&str> = list.iter().cloned().collect();
let map: HashMap<usize, &str> = list.iter().enumerate().collect();
""",
    "06. Conditionals": """
let condition1 = 10;
let condition2 = 5;

let result = if true { "True case" } else { "False case" };

if condition1 == 10 {
  println!("Condition1 is true");
} else if condition2 == 5 {
  println!("Condition2 is true");
} else {
  println!("All conditions false");
}

let value = "case2";
match value {
  "case1" => println!("Case 1 executed"),
  "case2" => println!("Case 2 executed"),
  _ => println!("Default case executed"),
}
""",
    "07. Loops and Repetition": """
for i in 0..5 {
  if i == 3 { continue; }
  println!("For loop: {}", i);
  if i == 4 { break; }
}

let names = vec!["Maria", "Joaquin", "Luisa"];
for name in &names {
  println!("Hello {}", name);
}

let ages: HashMap<&str, i32> = [("Maria", 20), ("Joaquin", 21), ("Luisa", 22)]
  .iter().cloned().collect();

for (name, age) in &ages {
  println!("{} is {} years old", name, age);
}

let mut count = 0;
while count < 3 {
  println!("While loop: {}", count);
  count += 1;
}

count = 3;
loop {
  println!("Do-while loop: {}", count);
  count -= 1;
  if count == 0 { break; }
}
""",
    "08. Functions and Methods": """
fn greet(param: &str) {
  println!("Hello {}", param);
}

let greet_lambda = |param: &str| println!("Hello {}", param);

fn return_string(param: &str) -> String {
  format!("Hello {}", param)
}

fn return_int(param: i32) -> i32 {
  param
}

fn return_tuple(param: &str) -> (i32, &str) {
  (123, param)
}

fn add(a: i32, b: i32) -> i32 {
  a + b
}

let sum = add(2, 3);
let total = add(2, add(2, 3));
""",
    "09. Error Handling": """
let result = std::panic::catch_unwind(|| {
  let parsed: i32 = "123".parse().unwrap();
  parsed / 0
});

match result {
  Ok(_) => println!("Success"),
  Err(_) => println!("An error occurred"),
}

println!("This always executes");
""",
}

rust_class: dict = {
    "01. Basic Structs and Methods": """
// Define a basic struct and method
struct Vehicle {
    brand: String,
    year: u32,
}

impl Vehicle {
    fn show_info(&self) {
        println!("Brand: {}, Year: {}", self.brand, self.year);
    }
}

// Instantiate and use
let my_car = Vehicle {
    brand: "Toyota".to_string(),
    year: 2020,
};

my_car.show_info();     // Brand: Toyota, Year: 2020
""",
    "02. Fields and Visibility": """
struct User {
    id: String,
    name: String,
}

impl User {
    fn greet(&self) {
        println!("Hello, {}! (ID: {})", self.name, self.id);
    }
}

let u = User {
    id: "u123".to_string(),
    name: "Ana".to_string(),
};

u.greet(); // Hello, Ana! (ID: u123)
""",
    "03. Constructors with impl blocks": """
struct Point {
    x: f64,
    y: f64,
}

impl Point {
    fn new(x: f64, y: f64) -> Self {
        Self { x, y }
    }

    fn origin() -> Self {
        Self { x: 0.0, y: 0.0 }
    }
}

let p1 = Point::new(2.0, 3.0);
let p2 = Point::origin(); // (0.0, 0.0)
""",
    "04. Inheritance via Traits": """
trait Movable {
    fn move_it(&self);
}

struct Dog;

impl Movable for Dog {
    fn move_it(&self) {
        println!("The dog runs");
    }
}

let a = Dog;
a.move_it(); // The dog runs
""",
    "05. Polymorphism with Trait Objects": """
trait Shape {
    fn area(&self) -> f64;
}

struct Circle {
    radius: f64,
}

impl Shape for Circle {
    fn area(&self) -> f64 {
        3.1416 * self.radius * self.radius
    }
}

let c = Circle { radius: 2.0 };
println!("Area: {}", c.area());
""",
    "06. Mixins using Traits": """
trait Musical {
    fn play(&self) {
        println!("Playing instrument");
    }
}

struct Musician;

impl Musical for Musician {}

let m = Musician;
m.play();
""",
    "07. Interface Contracts": """
trait Person {
    fn greet(&self);
}

struct Impostor;

impl Person for Impostor {
    fn greet(&self) {
        println!("I'm an impostor!");
    }
}

let i = Impostor;
i.greet();
""",
    "08. Abstract-like via Traits": """
trait Vehicle {
    fn move_it(&self);
}

struct Bike;

impl Vehicle for Bike {
    fn move_it(&self) {
        println!("The bike moves forward");
    }
}

let b = Bike;
b.move_it();
""",
    "09. Encapsulation with Privacy": """
mod bank {
    pub struct Bank {
        balance: f64,
    }

    impl Bank {
        pub fn new() -> Self {
            Self { balance: 0.0 }
        }

        pub fn deposit(&mut self, amount: f64) {
            self.balance += amount;
        }

        pub fn get_balance(&self) -> f64 {
            self.balance
        }
    }
}

let mut my_bank = bank::Bank::new();
my_bank.deposit(50.0);
println!("Balance: {}", my_bank.get_balance());
""",
    "10. Static Methods and Constants": """
struct Utilities;

impl Utilities {
    const PI: f64 = 3.1416;

    fn square(x: f64) -> f64 {
        x * x
    }
}

println!("{}", Utilities::PI);         // 3.1416
println!("{}", Utilities::square(5.0)); // 25.0
""",
    "11. Generics in Structs": """
struct Box<T> {
    content: T,
}

let box_int = Box { content: 42 };
let box_str = Box { content: "Hello" };

println!("{}", box_int.content);  // 42
println!("{}", box_str.content);  // Hello
""",
    "12. Documentation Comments": """
/// A calculator for basic operations
struct Calculator;

impl Calculator {
    /// Adds two numbers
    fn add(a: i32, b: i32) -> i32 {
        a + b
    }
}

// Accessing doc (used in cargo doc)
let result = Calculator::add(2, 3);
""",
    "13. Design Patterns": """
// Singleton-like pattern
struct Logger {
    name: String,
}

impl Logger {
    fn new(name: &str) -> &'static Self {
        use std::sync::OnceLock;
        static INSTANCE: OnceLock<Logger> = OnceLock::new();
        INSTANCE.get_or_init(|| Logger {
            name: name.to_string(),
        })
    }
}

let log1 = Logger::new("main");
let log2 = Logger::new("backup");

println!("{}", log1.name);  // main
println!("{}", log2.name);  // main (shared instance)
""",
    "14. Best Practices": """
// ✅ Use CamelCase for struct and trait names
// ✅ Keep fields private unless exposing via methods
// ✅ Prefer trait-based composition over deep inheritance
// ✅ Document public APIs using /// comments
// ✅ Avoid logic inside constructors—favor builders if complex
""",
}

rust_os: dict = {
    "01. Files and Directories": """
use std::fs::{read_to_string, write, remove_file};
use std::env;
use std::path::Path;

// 📖 Read file content
let content = read_to_string("text.txt").unwrap();

// ✍️ Write to file
write("new.txt", "Hello world").unwrap();

// ✅ Check if file exists
let exists = Path::new("new.txt").exists();

// 🧹 Delete file
remove_file("new.txt").unwrap();

// 📍 Current directory
let current_dir = env::current_dir().unwrap();

// 🗂️ List directory contents
for entry in current_dir.read_dir().unwrap() {
    let path = entry.unwrap().path();
    println!("{:?}", path);
}
""",
    "02. Paths and Manipulation": """
use std::path::{Path, PathBuf};

// 📎 File name
let name = Path::new("/folder/file.txt").file_name().unwrap();

// 🧩 File extension
let ext = Path::new("file.tar.gz").extension().unwrap();

// 📍 Absolute path
let full = env::current_dir().unwrap().join("data.txt");

// 🔗 Join paths
let joined = PathBuf::from("folder").join("file.txt");
""",
    "03. Date and Time": """
use chrono::{Local, NaiveDate, Duration};

// ⏰ Current date
let now = Local::now();

// 🌐 UTC version
let utc = now.naive_utc();

// 📅 Parse string to date
let parsed = NaiveDate::parse_from_str("2025-08-01", "%Y-%m-%d").unwrap();

// ⏳ Time difference
let diff = now.date_naive().signed_duration_since(parsed);

// 🧾 Simple format
let format = format!("{}/{}/{}", now.day(), now.month(), now.year());
""",
    "04. System Processes": """
use std::process::Command;

// 🖥️ Run shell command
let output = Command::new("echo")
    .arg("Hello Rust")
    .output()
    .expect("Failed");

// 📡 Print output
println!("{}", String::from_utf8_lossy(&output.stdout));
""",
    "05. Environment Variables": """
use std::env;

// 🌍 All environment variables
let env_vars = env::vars();

// 🏡 HOME directory (Unix-like)
let home = env::var("HOME").unwrap_or("N/A".into());
""",
    "06. Operating System Detection": """
#[cfg(target_os: dict = "windows")]
println!("🪟 This is Windows");

#[cfg(target_os: dict = "linux")]
println!("🐧 This is Linux");

#[cfg(target_os: dict = "macos")]
println!("🍎 This is macOS");
""",
    "07. Continuous Reading / Streams": """
use std::process::{Command, Stdio};
use std::io::{BufReader, BufRead};

// 🔁 Start ping process
let process = Command::new("ping")
    .arg("localhost")
    .stdout(Stdio::piped())
    .spawn()
    .expect("Failed to start");

// 🖥️ Read real-time output
if let Some(stdout) = process.stdout {
    let reader = BufReader::new(stdout);
    for line in reader.lines() {
        println!("📡 {}", line.unwrap());
    }
}
""",
}
