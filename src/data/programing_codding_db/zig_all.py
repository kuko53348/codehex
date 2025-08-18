zig_code: dict = {
    "Vars Assigments": """
🔢 Enteros sin signo (uN)

| Tipo  | Bits | Rango de valores          |
|-------|------|---------------------------|
| u8  | 8    | 0 a 255                     |
| u16 | 16   | 0 a 65 k                    |
| u32 | 32   | 0 a 4,2 KM                  |
| u64 | 64   | 0 a (enorme)                |
| u128| 128  | 0 a 2¹²⁸−1 (enorme)         |

➖ Enteros con signo (iN)

| Tipo  | Bits | Rango de valores          |
|-------|------|---------------------------|
| i8  | 8    | −128 a 127                  |
| i16 | 16   | −32 k a 32 k                |
| i32 | 32   | −2,1 KM a 2,1 KM            |
| i64 | 64   | −(enorme) a (enorme)        |
| i128| 128  | −2¹²⁷ a 2¹²⁷−1              |

🌊 Tipos flotantes (fN)

| Tipo  | Bits | Precisión aproximada      |
|-------|------|---------------------------|
| f16 | 16   | ±65,504 (menos común)       |
| f32 | 32   | ±3.4 × 10³⁸                 |
| f64 | 64   | ±1.8 × 10³⁰⁸                |
| f128| 128  | ±1.2 × 10⁴⁹³² (experimental)|
    """,
    "00. Key Words": """
```rust
// zig is list of strings
const example:[_]const u8 = "hello world 12345";

// make shortcut
const print = std.debug.print;
print("Number: {}\\n", .{num});

const lowerString = std.ascii.lowerString
const upperString = std.ascii.upperString

const split = std.mem.split
const startsWith = std.mem.startsWith
const endsWith = std.mem.endsWith
const indexOf = std.mem.indexOf
const lastIndexOf = std.mem.lastIndexOf
const trim = std.mem.trim
const replace = std.mem.replace
const concat = std.mem.concat
const join = std.mem.join

// How use?
const isEmpty = example.len == 0;
const isNotEmpty = example.len != 0;
const substring = example[0..5];

const lower = lowerString(example);
const upper = upperString(example);

const words = split(u8, example, " ");
const startsWithH = startsWith(u8, example, "h");
const endsWith5 = endsWith(u8, example, "5");
const containsH = indexOf(u8, example, "h") != null;
const indexH = indexOf(u8, example, "h");
const lastIndexH = lastIndexOf(u8, example, "h");
const trimmed = trim(u8, "  hello  ", " ");
const replaced = replace(u8, example, "h", "H");
const paddedRight = concat(u8, &[_][]const u8{ example, "000" });
const paddedLeft = std.mem.concat(u8, &[_][]const u8{ "000", example });
const joined = std.mem.join(u8, "-", words);
```
    """,
    "01. Variables and Assignments": """
```rust
// Strings int floats
const name: []const u8 = "David";     // Cadena de texto

const age: @as(u32 ,10);              // Positive
const age: u32 = 10;                  // Positive
const age: i32 = -10;                 // Positive and negative Unsigned + -
const age: i32 = 10;                  // Positive and negative Unsigned + -
const range: f32 = 10.00;             // real Positive and negative Decimal + -

const state: bool = true;             // Booleano

// Dhynamyc and undefine
const var varName: i32 = undefine;    // Sin declarar
const var dynamyc: anytype = undefine;// Sin declarar
const intNumber: anytype = 24;        // Puede ser int o float (usamos anytype para flexibilidad)

// Tipado dinámico no existe en Zig, pero se puede usar union o anytype
var dynamicVar: anytype = 1.2;
dynamicVar = true;

var lateAssignation: []const u8 = undefined;
lateAssignation = "assigned value";

// Constantes
const pi = 3.14;
const now = std.time.timestamp(); // Tiempo actual

// Strings Listas y mapas simulados
const listNumbers = [3]u8{ 24, 48, 75 };
const strings =     [_]u8 = "Juan ,  Manuel";
const listStrings = [_]u8{ "Juan", "Manuel" };
const mixedList =   [_]anytype{ 1, "Juan", 23, "Juan" };

const numberSet = std.AutoHashMap(i32, void).init(std.heap.page_allocator); // Set simulado

const person = .{
    .Name = "Carlos",
    .Age = 23,
};
```
""",
    "0.1.1 Int Manipulation": """
```rust
const age: i32 = 31;

const isOdd = age % 2 != 0;
const isEven = age % 2 == 0;
```

---
""",
    "02. String Manipulation": """

```rust
const example:[_]const u8 = "hello world 12345";
const words = std.mem.split(u8, example, " ");

const len = example.len;
const isEmpty = len == 0;
const isNotEmpty = len != 0;

const lower = std.ascii.lowerString(example);
const upper = std.ascii.upperString(example);

const containsH = std.mem.indexOf(u8, example, "h") != null;
const startsWithH = std.mem.startsWith(u8, example, "h");
const endsWith5 = std.mem.endsWith(u8, example, "5");

const indexH = std.mem.indexOf(u8, example, "h");
const lastIndexH = std.mem.lastIndexOf(u8, example, "h");

const trimmed = std.mem.trim(u8, "  hello  ", " ");
const replaced = std.mem.replace(u8, example, "h", "H");

const substring = example[0..5];

const paddedRight = std.mem.concat(u8, &[_][]const u8{ example, "000" });
const paddedLeft = std.mem.concat(u8, &[_][]const u8{ "000", example });

const joined = std.mem.join(u8, "-", words);
```

---
""",
    "03. Collections: Lists, Sets, and Maps": """
```rust
const mixedList = [_]anytype{ 1, "Juan", 23, "Juan" };
var numbers = [_]i32{ 1, 2, 23, 4 };
var names = [_][]const u8{ "Pedro", "Juan", "Cesar", "Carlos" };

const list2 = [_]i32{ 0, numbers[0], numbers[1], numbers[2], numbers[3] };

// Operaciones de listas
std.sort.sort(i32, &numbers, std.sort.asc(i32));
names[0] = "New Value";
const length = names.len;
const containsJuan = std.mem.indexOf([]const u8, names[1], "Juan") != null;

// Sets simulados con HashMap
var numberSet = std.AutoHashMap(i32, void).init(std.heap.page_allocator);
try numberSet.put(25, {});
try numberSet.remove(5);

// Maps
var person = std.StringHashMap(anytype).init(std.heap.page_allocator);
try person.put("Name", "Luis");
try person.put("Age", 23);
```

---
""",
    "04. Key Concepts": """

```rust
const doubled = [_]i32{ 0, 2, 4, 6, 8 };
for (doubled) |num| {
    std.debug.print("Number: {}\\n", .{num});
}

for (doubled) |num, index| {
    std.debug.print("Num: {} index: {}\\n",.{num}, .{index});
}

for (doubled, 0..) |_num, index| {
    std.debug.print("index: {}\\n", .{index});
}

for (doubled, 1..) |num, index| {
    // puede tener al index que desees
    std.debug.print("Number: {}\\n", .{num});
}

fn greet(isMorning: bool) []const u8 {
    return if (isMorning) "Good Morning" else "Hello";
}

const buttonPressed = true;
if (buttonPressed) std.debug.print("Clicked Bro\\n", .{});

// Nullability en Zig se maneja con optional
var nullableVar: ?[]const u8 = null;
var notNullableVar: []const u8 = "value";

const result = nullableVar orelse notNullableVar;

var isTrue = true;
isTrue = !isTrue;
```

---
""",
    "05. Parsing and Type Conversion": """

```rust
const parsedInt = std.fmt.parseInt(i32, "12", 10);
const parsedDouble = std.fmt.parseFloat(f64, "12.5");

const intToStr = std.fmt.allocPrint(std.heap.page_allocator, "{}", .{12});
const doubleToStr = std.fmt.allocPrint(std.heap.page_allocator, "{}", .{12.5});

// String to List
const fruitsString = "apple,banana,orange";
const listFromString = std.mem.split(u8, fruitsString, ",");

// List to String
const joinedFruits = std.mem.join(u8, ",", listFromString);
```

---
""",
    "06. Conditionals": """

```rust
const condition1 = 10;
const condition2 = 5;

const result = if (isTrue) "True case" else "False case";

if (condition1 == 10) {
    std.debug.print("Condition1 is true\\n", .{});
} else if (condition2 == 5) {
    std.debug.print("Condition2 is true\\n", .{});
} else {
    std.debug.print("All conditions false\\n", .{});
}

const value = "case2";
switch (value) {
    "case1" => std.debug.print("Case 1 executed\\n", .{}),
    "case2" => std.debug.print("Case 2 executed\\n", .{}),
    "case3" => std.debug.print("Case 3 executed\\n", .{}),
    else => std.debug.print("Default case executed\\n", .{}),
}
```

---
""",
    "07. Loops and Repetition": """
```rust
for (std.math.min(5, 10)) |i| {
    if (i == 3) continue;
    std.debug.print("For loop: {}\\n", .{i});
    if (i == 4) break;
}

const names = [_][]const u8{ "Maria", "Joaquin", "Luisa" };
for (names) |name| {
    std.debug.print("Hello {}\\n", .{name});
}

const ages = [_]struct { name: []const u8, age: i32 }{
    .{ .name = "Maria", .age = 20 },
    .{ .name = "Joaquin", .age = 21 },
    .{ .name = "Luisa", .age = 22 },
};
for (ages) |entry| {
    std.debug.print("{} is {} years old\\n", .{entry.name, entry.age});
}

var count: i32 = 0;
while (count < 3) : (count += 1) {
    std.debug.print("While loop: {}\\n", .{count});
}

count = 3;
while (count > 0) : (count -= 1) {
    std.debug.print("Do-while loop: {}\\n", .{count});
}
```

---
""",
    "08. Functions and Methods": """

```rust
fn callFunction(parameter: []const u8) void {
    std.debug.print("hello {}\\n", .{parameter});
}

fn callStringFunction(parameter: []const u8) []const u8 {
    return parameter;
}

fn callIntFunction(parameter: i32) i32 {
    return parameter;
}

fn callDynamicFunction(parameter: []const u8) struct { a: i32, b: []const u8 } {
    return .{ .a = 123, .b = parameter };
}

fn add(a: i32, b: i32) i32 {
    defer std.debug.print("Solo se ejecuta terminado la funcion {}\\n", .{a});
    return a + b;
}

const sum = add(2, 3);
const totalSum = add(2, add(2, 3));
```

---
""",
    "09. Error Handling": """
```rust
const result = std.fmt.parseInt(i32, "123", 10) catch |err| {
    std.debug.print("Error: {}\\n", .{err});
    return;
};

const division = result / 0;
std.debug.print("Result: {}\\n", .{division});
```

---
""",
    "10. Structs, Enums, and Pointers": """
```rust
const std = @import("std");

pub fn main() void {
    const stdout = std.io.getStdOut().writer();

    // Struct usage
    const Person = struct {
        name: []const u8,
        age: u8,
    };

    const pedro = Person{
        .name = "Pedro",
        .age = 30,
    };

    stdout.print("Name: {}, Age: {}\\n", .{pedro.name, pedro.age});

    // Enum usage
    const Direction = enum {
        North,
        South,
        East,
        West,
    };

    const dir = Direction.North;
    switch (dir) {
        Direction.North => stdout.print("Going North\\n", .{}),
        Direction.South => stdout.print("Going South\\n", .{}),
        Direction.East => stdout.print("Going East\\n", .{}),
        Direction.West => stdout.print("Going West\\n", .{}),
    }

    // Pointers and memory
    var number: i32 = 42;
    const ptr = &number;

    stdout.print("Value: {}, Pointer: {*}\\n", .{number, ptr});
    ptr.* += 1;
    stdout.print("Updated Value: {}\\n", .{number});

    // Optional pointer
    var maybePtr: ?*i32 = null;
    if (maybePtr) |val| {
        stdout.print("Pointer value: {}\\n", .{val.*});
    } else {
        stdout.print("Pointer is null\\n", .{});
    }

    // Allocating memory manually
    const allocator = std.heap.page_allocator;
    const buffer = try allocator.alloc(u8, 10);
    defer allocator.free(buffer);

    for (buffer) |*b, i| {
        b.* = @intCast(u8, i);
    }

    stdout.print("Buffer: {}\\n", .{buffer});
}
```

---
""",
    "11. Pointers": """
```rust

// First exemple
var x: *u8 =0; // Create pinter
var y: u8=&x;  // refer pointer

// Second exemple
var x: u8 =0;
var ptr: *u8=&x; // Create pinter and refer pointer

std.debug.print("Pointer: {d}\\n", .{ptr});

```
""",
}

zig_class: dict = {
    "📘 Zig Class Concepts Dictionary": """
```rust
const std = @import("std");

pub fn main() void {
    const stdout = std.io.getStdOut().writer();
    // You can test each section below
}
```
---
""",
    "01. Basic Classes": """

```rust
// In Zig, we use structs to model classes
const Vehiculo = struct {
    marca: []const u8,
    anho: i32,

    pub fn mostrarInfo(self: Vehiculo) void {
        std.debug.print("Marca: {}, Año: {}\\n", .{self.marca, self.anho});
    }
};

pub fn main() void {
    const miCarro = Vehiculo{
        .marca = "Toyota",
        .anho = 2020,
    };
    miCarro.mostrarInfo();
}
```

---
""",
    "02. Properties and Methods": """

```rust
const Usuario = struct {
    id: []const u8,
    nombre: []const u8,

    pub fn saludar(self: Usuario) void {
        std.debug.print("¡Hola, {}! (ID: {})\\n", .{self.nombre, self.id});
    }
};

pub fn main() void {
    const u = Usuario{ .id = "u123", .nombre = "Ana" };
    u.saludar();
}
```

---
""",
    "03. Constructors": """
Zig doesn’t have constructors like Dart, but we use factory functions or `init` methods.

03.1 Basic Constructor

```rust
const Punto = struct {
    x: f64,
    y: f64,

    pub fn init(x: f64, y: f64) Punto {
        return Punto{ .x = x, .y = y };
    }
};

const p = Punto.init(2, 3);
std.debug.print("({}, {})\\n", .{p.x, p.y});
```

03.2 Named Constructors

```rust
pub fn origen() Punto {
    return Punto{ .x = 0, .y = 0 };
}
```

03.3 Constant Constructor

```rust
const Coordenada = struct {
    x: i32,
    y: i32,
};

const c1 = Coordenada{ .x = 0, .y = 0 };
const c2 = Coordenada{ .x = 0, .y = 0 };
// Zig compares structs by value
const areEqual = std.meta.eql(c1, c2);
```

#03.4 Factory Constructor

```rust
const Logger = struct {
    nombre: []const u8,
};

var cache = std.StringHashMap(Logger).init(std.heap.page_allocator);

pub fn getLogger(nombre: []const u8) Logger {
    return cache.get(nombre) orelse blk: {
        const logger = Logger{ .nombre = nombre };
        cache.put(nombre, logger) catch {};
        break :blk logger;
    };
}
```

---
""",
    "04. Inheritance": """
Zig doesn’t support inheritance. Use composition and interfaces via `struct` and `fn`.

```rust
const Animal = struct {
    pub fn moverse() void {
        std.debug.print("El animal se mueve\\n", .{});
    }
};

const Perro = struct {
    pub fn moverse() void {
        std.debug.print("El perro corre\\n", .{});
    }
};

const a = Perro{};
a.moverse();
```

---
""",
    "05. Polymorphism": """
```rust
const Figura = struct {
    pub fn area(self: *Figura) f64 {
        return 0.0;
    }
};

const Circulo = struct {
    radio: f64,

    pub fn area(self: Circulo) f64 {
        return 3.1416 * self.radio * self.radio;
    }
};

const c = Circulo{ .radio = 2.0 };
const area = c.area();
```

---
""",
    "06. Mixins": """

Zig doesn’t have mixins, but you can simulate them with reusable functions or embedded structs.

```rust
const Musical = struct {
    pub fn tocarInstrumento() void {
        std.debug.print("Tocando instrumento\\n", .{});
    }
};

const Musico = struct {
    musical: Musical,
};

const m = Musico{ .musical = Musical{} };
m.musical.tocarInstrumento();
```

---
""",
    "07. Interfaces": """

Zig uses duck typing. You define behavior via functions.

```rust
const Persona = struct {
    pub fn saludar() []const u8 {
        return "Hola";
    }
};

const Impostor = struct {
    pub fn saludar() []const u8 {
        return "¡Soy un impostor!";
    }
};

const impostor = Impostor{};
std.debug.print("{}\\n", .{impostor.saludar()});
```

---
""",
    "08. Abstract Classes": """
Zig doesn’t have abstract classes, but you can define required behavior via function signatures.

```rust
const Vehiculo = struct {
    pub fn mover() void {}
};

const Bicicleta = struct {
    pub fn mover() void {
        std.debug.print("La bicicleta avanza\\n", .{});
    }
};

const b = Bicicleta{};
b.mover();
```

---
""",
    "09. Encapsulation and Access": """

```rust
const Banco = struct {
    saldo: f64,

    pub fn depositar(self: *Banco, monto: f64) void {
        self.saldo += monto;
    }

    pub fn getSaldo(self: Banco) f64 {
        return self.saldo;
    }
};

var banco = Banco{ .saldo = 0 };
banco.depositar(100);
std.debug.print("Saldo: {}\\n", .{banco.getSaldo()});
```

---
""",
    "10. Static Members and Constants": """

```rust
const Utilidades = struct {
    pub const pi = 3.1416;

    pub fn cuadrado(x: f64) f64 {
        return x * x;
    }
};

std.debug.print("{}\\n", .{Utilidades.pi});
std.debug.print("{}\\n", .{Utilidades.cuadrado(5)});
```

---
""",
    "11. Generics in Classes": """

Zig uses `comptime` generics.

```rust
fn Caja(comptime T: type) type {
    return struct {
        contenido: T,

        pub fn mostrar(self: @This()) void {
            std.debug.print("{}\\n", .{self.contenido});
        }
    };
}

const cajaInt = Caja(i32){ .contenido = 42 };
const cajaStr = Caja([]const u8){ .contenido = "Hola" };

cajaInt.mostrar();
cajaStr.mostrar();
```

---
""",
    "Annotations and Extras": """
Zig doesn’t use annotations like Dart, but you can use attributes and comments.

```rust
/// Deprecated: use nuevoMetodo instead
pub fn metodoAntiguo() void {
    std.debug.print("Método antiguo\\n", .{});
}
```

---
""",
    "Design Patterns with Zig Structs": """

- **Singleton**: Use global `var` or `const` with lazy init.
- **Factory**: Use `init()` or `get()` functions.
- **Observer**: Use function callbacks or event queues.
- **Decorator**: Wrap structs with other structs.
- **Strategy**: Pass behavior as function pointers or interfaces.

---
""",
    "Best Practices in Struct Design": """

- Use clear names in `CamelCase`.
- Prefer `const` and `pub const` for immutable values.
- Encapsulate internal state with private fields.
- Split large structs into smaller responsibilities.
- Document public APIs with `///`.

---
""",
    "Documentation and Doc Comments": """

```rust
/// Calculates the sum of two numbers.
/// [a], [b]: operands for the sum.
/// Returns the result of the operation.
pub fn sumar(a: i32, b: i32) i32 {
    return a + b;
}
```

---
""",
}

zig_os: dict = {
    "🧭 Zig OS Concepts Dictionary": """
```rust
const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    // You can test each section below
}
```

---
""",
    "01. Files and Directories": """
```rust
const fs = std.fs;

pub fn fileOps() !void {
    const cwd = fs.cwd();

    // 📖 Read file content
    const file = try cwd.openFile("text.txt", .{});
    defer file.close();
    const content = try file.readToEndAlloc(std.heap.page_allocator, 1024);
    std.debug.print("Content: {}\\n", .{content});

    // ✍️ Write to file
    try cwd.writeFile("new.txt", "Hello world");

    // ✅ Check if file exists
    const exists = cwd.statFile("new.txt") catch |err| switch (err) {
        error.FileNotFound => false,
        else => return err,
    };
    std.debug.print("Exists: {}\\n", .{exists});

    // 🧹 Delete file
    try cwd.deleteFile("new.txt");

    // 📍 Current directory
    const dir = cwd;

    // 🗂️ List directory contents
    var it = try dir.openDir(".", .{ .iterate = true }).iterator();
    while (try it.next()) |entry| {
        std.debug.print("Found: {}\\n", .{entry.name});
    }
}
```

---
""",
    "02. Paths and Manipulation": """
```rust
const path = struct {
    pub fn basename(p: []const u8) []const u8 {
        return std.fs.path.basename(p);
    }

    pub fn extension(p: []const u8) []const u8 {
        const dot = std.mem.lastIndexOfScalar(u8, p, '.');
        return if (dot) |i| p[i..] else "";
    }

    pub fn join(a: []const u8, b: []const u8) []const u8 {
        return std.fs.path.join(std.heap.page_allocator, &[_][]const u8{a, b}) catch unreachable;
    }
};

pub fn pathOps() void {
    // 📎 File name
    const name = path.basename("/folder/file.txt");

    // 🧩 File extension
    const ext = path.extension("file.tar.gz");

    // 🔗 Join paths
    const joined = path.join("folder", "file.txt");

    std.debug.print("Name: {}, Ext: {}, Joined: {}\\n", .{name, ext, joined});
}
```

---
""",
    "03. Date and Time": """

```rust
const time = std.time;

pub fn timeOps() void {
    // ⏰ Current date
    const now = time.timestamp();

    // 🌐 UTC version (same in Zig)
    const utc = now;

    // 📅 Parse string to date (manual parsing required)
    const parsed = time.Timestamp{ .secs = 1754006400 }; // 2025-08-01 approx

    // ⏳ Time difference
    const diff = now - parsed.secs;

    // 🧾 Simple format
    std.debug.print("Now: {}, Diff: {}\\n", .{now, diff});
}
```

---
""",
    "04. System Processes": """

```rust
const process = std.process;

pub fn runCommand() !void {
    // 🖥️ Run shell command
    var result = try process.run(.{
        .allocator = std.heap.page_allocator,
        .argv = &[_][]const u8{"echo", "Hello Zig"},
        .max_output_bytes = 1024,
    });

    // 📡 Print output
    std.debug.print("Output: {}\\n", .{result.stdout});
}
```

---
""",
    "05. Environment Variables": """

```rust
pub fn envVars() void {
    // 🌍 All environment variables
    const env = std.os.environ;

    // 🏡 HOME directory (Unix)
    const home = std.os.getenv("HOME") orelse "Unknown";

    std.debug.print("HOME: {}\\n", .{home});
}
```

---
""",
    "06. Operating System Detection": """

```rust
pub fn osDetect() void {
    // 🪟 Windows
    const isWindows = std.os.tag == .windows;

    // 🐧 Linux
    const isLinux = std.os.tag == .linux;

    // 🍎 macOS
    const isMac = std.os.tag == .macos;

    std.debug.print("Windows: {}, Linux: {}, macOS: {}\\n", .{isWindows, isLinux, isMac});
}
```

---
""",
    "07. Continuous Reading / Streams": """

```rust
pub fn streamPing() !void {
    var process = try std.process.Child.run(.{
        .allocator = std.heap.page_allocator,
        .argv = &[_][]const u8{"ping", "localhost"},
        .max_output_bytes = 4096,
    });

    std.debug.print("📡 {}\\n", .{process.stdout});
}
```

---
""",
}
