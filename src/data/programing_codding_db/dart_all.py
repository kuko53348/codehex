dart_code: dict = {
    "01. Variables and Assignments": """
```dart
// Basic data types
String name = 'David';      // String
bool state = true;          // Boolean

int age = 10;               // Integer
double temp = 18.5;         // Double
num intNumber = 24;         // Can be (int or double)

List<dynamic> mixedList = [1, 'Juan', 23, 'Juan'];
Set<int> numberSet = {1, 2, 3, 4, 5};
Map<String, dynamic> person = {'Name': names[3],'Age': numbers[3]};

// Dynamic typing
var inferredType = 1.2;     // Type inferred as double (can't change)
dynamic dynamicVar = 1.2;   // Type can change
dynamicVar = true;

const pi = 3.14;            // Compile-time constant
final now = DateTime.now(); // Runtime constant Compile
late String lateAssignation;// Declare now, initialize later

lateAssignation = 'assigned value';
```
""",
    "02. String Manipulation": """
```dart

String example = "hello world 12345";
List<String> words = example.split(' ');

// Basic operations
example.lenght           // <= string size
example.isEmpty()           // <= true or false
example.isNotEmpty()           // <= true or false
example.toLowerCase()           // <= to lower case
example.toUpperCase()           // <= to upper case
example.contains('h')           // <= Contains "h"
example.startsWith('h')         // <= Starts with "h"
example.endsWith('5')           // <= Ends with "5"
example.indexOf('h')            // <= First index of "h"
example.lastIndexOf('h')        // <= Last index of "h"

// Transformations
'  hello  '.trim()              // <= Trimmed
example.replaceAll('h', 'H')    // <= Replace all "h"
example.replaceFirst('h', 'H')  // <= Replace first "h"
example.substring(0, 5)         // <= Substring

// Padding
example.padRight(example.length + 3, '0') // <= Pad right
example.padLeft(example.length + 3, '0')  // <= Pad left

// Splitting and joining
example.split(' ')              // <= split
words.join('-')                 // <= join
```
""",
    "03. Collections: Lists, Sets, and Maps": """
```dart
// Lists (ordered, allows duplicates)
List<dynamic> mixedList = [1, 'Juan', 23, 'Juan'];
List<int> numbers = [1, 2, 23, 4];
List<String> names = ['Pedro', 'Juan', 'Cesar', 'Carlos'];

// to insert multiple values into a collection.
var list = [1, 2, 3];
var list2 = [0, ...list];

// List operations
numbers.sort();
names.add('Banana');
names.insert(0, 'Pineapple');
names.remove('Pineapple');
names.removeAt(0);
names.removeAt(names.length);#

names[0]                // <= Index
names[0] = 'New Value'  // <= Index
names.length            // <= length
names.contains("Juan")  // <= names contains Juan? true or false

// Sets (unordered, no duplicates)
Set<int> numberSet = {1, 2, 3, 4, 5};
Set<int> numberSet2 = {4, 5, 6, 7, 8};

// Sets operations
numberSet.add(25);                  // <= add
numberSet.remove(5);                // <= remove
numberSet.union(numberSet2);        // <= Union
numberSet.intersection(numberSet2); // <= Intersection
numberSet.difference(numberSet2);   // <= Difference


// Maps (key-value pairs)
Map<String, dynamic> person = {
  'Name': names[3],
  'Age': numbers[3],
};

// Map operations
person['height'] = 75.5;      // <= Add
person.remove('Name');        // <= Remove
person['Name'] = 'Luis';      // <= Update
person.containsKey('Name');   // <= Contains keyName? true or false
person.containsValue('Luis'); // <=  Contains valueName? true or false
```
""",
    "04. Key Concepts": """
```dart
// one line assigments
var doubled = List.generate(5, (index) => index * 2)                // <= List generation
doubled.forEach((num) => print('Number: $num'))                     // <= ForEach with arrow function
String greet(bool isMorning) => isMorning? 'Good Mornig': 'Hello';  // <= lambda fuction with null cheking
button.onPressed = () => print('Clicked Bro');                      // <= lambda fuction

// Null assigments
String? nullableVar;     // execute and if not exist return null
String! notNullableVar;  // execute only if not null
String?? acceptNullVar;  // execute only if it\'s null

// execute and if it's null return nullableString else notNullability
String? notNullVar : nullVar;

// if it's true return false

bool isTrue = true;
isTrue =! toFalse;
```
""",
    "05. Parsing and Type Conversion": """
```dart
// Parsing
int example = int.parse('12')         // <= String to int
double example = double.parse('12.5') // <= String to double
String example = 12.toString()        // <= Int to string
String example = 12.5.toString()      // <= Double to string

// String conversions
const fruitsString = 'apple,banana,orange';       // <= fruitsString
final listFromString = fruitsString.split(',');   // <= String to List
final setFromString = listFromString.toSet();     // <= String to Set
final mapFromString = listFromString.asMap();     // <= String to Map

// List conversions
final fruitsList = ['apple', 'banana', 'orange']; // <= fruitsList
final stringFromList = fruitsList.join(',');      // <= List to String
final setFromList = fruitsList.toSet();           // <= List to Set
final mapFromList = fruitsList.asMap();           // <= List to Map

// Set conversions
final fruitsSet = {'apple', 'banana', 'orange'};  // <= fruitsSet
final stringFromSet = fruitsSet.join(',');        // <= Set to String
final listFromSet = fruitsSet.toList();           // <= Set to List
final mapFromSet = listFromSet.asMap();           // <= Set to Map

// Map conversions
final fruitsMap = {0: 'apple', 1: 'banana'};      // <= fruitsMap
final stringFromMap = fruitsMap.values.join(','); // <= Map to String
final listFromMap = fruitsMap.values.toList();    // <= Map to List
final setFromMap = fruitsMap.values.toSet();      // <= Map to Set
```
""",
    "06. Conditionals": """
```dart
int condition1 = 10;
int condition2 = 5;

// Terniarie
String result = isTrue ? 'True case' : 'False case';

// If-else
if (condition1 == 10) {
  print("Condition1 is true");
} else if (condition2 == 5) {
  print("Condition2 is true");
} else {
  print("All conditions false");
}

// Switch-case
String value = 'case2';

switch (value) {
  case 'case1':
    print("Case 1 executed");
    break;
  case 'case2':
    print("Case 2 executed");
    break;
  case 'case3':
    print("Case 3 executed");
    break;
  default:
    print("Default case executed");
}
```
""",
    "07. Loops and Repetition": """
```dart
// For loop list.lenght
for (int i = 0; i < 5; i++) {
  if (i == 3) continue;
    print('For loop: $i');
  if (i == 4) break;
}
// For-in loop (lists)
List<String> names = ['Maria', 'Joaquin', 'Luisa'];
for (String name in names) {
  print('Hello $name');
}
// For-in loop (maps)
Map<String, int> ages = {'Maria': 20, 'Joaquin': 21, 'Luisa': 22};
for (var entry in ages.entries) {
  print('${entry.key} is ${entry.value} years old');
}

// While loop
int count = 0;
while (count < 3) {
  print('While loop: $count');
  count++;
}

// Do-while loop
do {
  print('Do-while loop: $count');
  count--;
} while (count > 0);
```
""",
    "08. Functions and Methods": """
```dart
// One line code
callFuction(parameter) => print('hello $parameter');

// Lambda fuction
(parameter) => print('hello $parameter');

// No return
void callFuction(String parameter){
  print('hello $parameter');
}

// Return String
String callStringFuction(String parameter){
  return 'hello $parameter'
}

// Return int
int callStringFuction(int parameter){
  return parameter
}

// Return Set
(int, String) callDynamicFuction(String parameter){
  return (123 , parameter)
}

// functions in dart are objects and have a type
int add(int a, int b){
  return a+b;
}

// functions can be assigned to variables
int sum = add(2,3); // <= returns: 5

// can be passed as arguments to other functions
int totalSum = add(2, add(2,3)); // <= returns : 7
```
""",
    "09. Error Handling": """
```dart
try {
  // Potentially error-prone code
  double result = int.parse('123') / 0;
  print(result);
} on IntegerDivisionByZeroException {
  print('Cannot divide by zero');
} on FormatException {
  print('Invalid number format');
} catch (e) {
  print('An error occurred: $e');
} finally {
  print('This always executes');
}
```
""",
}

dart_class: dict = {
    "01. Basic Classes": """

Las clases en Dart se definen con la palabra clave `class` seguida de su nombre en **CamelCase**. Una clase simple agrupa propiedades y métodos, sirviendo como modelo para instanciar objetos. A continuación, un ejemplo que ilustra la estructura mínima de una clase y su uso:

```dart
class Vehiculo {
  String marca;
  int anho;

  void mostrarInfo() {
    print('Marca: $marca, Año: $anho');
  }
}

void main() {
  var miCarro = Vehiculo()
    ..marca = 'Toyota'
    ..anho = 2020;
  miCarro.mostrarInfo(); // Marca: Toyota, Año: 2020
}
```

En este ejemplo, `Vehiculo` define dos propiedades (`marca`, `anho`) y un método (`mostrarInfo`). Con el operador `..` podemos inicializar múltiples campos en cascada.



""",
    "02. Properties and Methods": """

Las **propiedades** de instancia representan el estado de un objeto, mientras que los **métodos** definen su comportamiento. Dart genera automáticamente getters y, si no son `final`, setters para cada propiedad. Para propiedades que no cambian, podemos usar `final` o `const`.

```dart
class Usuario {
  final String id;
  String nombre;

  Usuario(this.id, this.nombre);

  void saludar() {
    print('¡Hola, $nombre! (ID: $id)');
  }
}

void main() {
  var u = Usuario('u123', 'Ana');
  u.saludar(); // ¡Hola, Ana! (ID: u123)
}
```

Aquí, `id` es inmutable tras la creación del objeto, garantizando integridad de datos. El método `saludar` accede a estas propiedades para generar un mensaje.


""",
    "03. Constructors": """

Dart permite varios tipos de constructores para controlar la creación de instancias.


03.1 Basic Constructor

El **constructor por defecto** recibe parámetros que asigna directamente a las propiedades:

```dart
class Punto {
  double x, y;
  Punto(this.x, this.y);
}

void main() {
  var p = Punto(2, 3);
  print('($p.x, $p.y)'); // (2.0, 3.0)
}
```

03.2 Named Constructors

Permiten múltiples formas de inicializar una clase:

```dart
class Punto {
  double x, y;
  Punto(this.x, this.y);
  Punto.origen() : x = 0, y = 0;
}
```

`Punto.origen()` delega en la lista de inicializadores para establecer valores constantes.

03.3 Constant Constructor (const)

Crea instancias inmutables en tiempo de compilación:

```dart
class Coordenada {
  final int x, y;
  const Coordenada(this.x, this.y);
}

void main() {
  const c1 = Coordenada(0, 0);
  const c2 = Coordenada(0, 0);
  print(identical(c1, c2)); // true
}
```

03.4 Factory Constructor

Controla la creación de instancias, por ejemplo para implementar un singleton:

```dart
class Logger {
  static final Map<String, Logger> _cache = {};
  final String nombre;
  factory Logger(String nombre) =>
    _cache.putIfAbsent(nombre, () => Logger._internal(nombre));
  Logger._internal(this.nombre);
}
```

Con `factory`, podemos reutilizar objetos ya creados o crear subclases si se desea.

---

""",
    "04. Inheritance": """

Dart soporta **herencia simple** con `extends`. Una subclase hereda propiedades y métodos de la clase base, pudiendo sobrescribirlos con `@override`.

```dart
class Animal {
  void moverse() => print('El animal se mueve');
}

class Perro extends Animal {
  @override
  void moverse() => print('El perro corre');
}

void main() {
  Animal a = Perro();
  a.moverse(); // El perro corre
}
```

La palabra clave `super` permite invocar la implementación de la clase padre.

---

""",
    "05. Polymorphism": """

El **polimorfismo** permite que un método opere con instancias de distintas clases que comparten una interfaz o herencia común. Al usar `implements`, una clase “actúa como” otra:

```dart
abstract class Figura {
  double area();
}

class Circulo implements Figura {
  double radio;
  Circulo(this.radio);
  @override
  double area() => 3.1416 * radio * radio;
}
```

Aquí, cualquier `Figura` puede ser un `Circulo`, `Cuadrado` u otra clase que implemente `area()`.

---

""",
    "06. Mixins": """

Los **mixins** agregan funcionalidades a múltiples clases sin herencia directa. Se usan con `with`.

```dart
mixin Musical {
  void tocarInstrumento() => print('Tocando instrumento');
}

class Musico with Musical {}

void main() {
  Musico m = Musico();
  m.tocarInstrumento(); // Tocando instrumento
}
```

Un mixin no puede declarar constructores y se define con `mixin`.

---

""",
    "07. Interfaces": """

Todas las clases en Dart son **interfaces implícitas**. Para obligar a una clase a cumplir una API sin heredar implementación, se usa `implements`:

```dart
class Persona {
  String saludar() => 'Hola';
}

class Impostor implements Persona {
  @override
  String saludar() => '¡Soy un impostor!';
}
```

`Impostor` debe proveer `saludar()` para cumplir la interfaz de `Persona`.

---

""",
    "08. Abstract Classes": """

Una **clase abstracta** puede declarar métodos sin implementación que las subclases deben implementar:

```dart
abstract class Vehiculo {
  void mover();
}

class Bicicleta extends Vehiculo {
  @override
  void mover() => print('La bicicleta avanza');
}
```

No puedes instanciar `Vehiculo` directamente, pero sí su subclase `Bicicleta`.

---

""",
    "09. Encapsulation and Access": """

En Dart, el **encapsulamiento** se logra con miembros privados, precedidos por guión bajo:

```dart
class Banco {
  double _saldo = 0;
  void depositar(double monto) => _saldo += monto;
  double get saldo => _saldo;
}
```

`_saldo` no es accesible fuera de `Banco`. Solo a través de getters y setters públicos.

---

""",
    "10. Static Members and Constants": """

Los miembros estáticos (`static`) pertenecen a la clase, no a instancias. Útiles para constantes o métodos de utilidad:

```dart
class Utilidades {
  static const pi = 3.1416;
  static double cuadrado(double x) => x * x;
}

void main() {
  print(Utilidades.pi);             // 3.1416
  print(Utilidades.cuadrado(5));    // 25.0
}
```

---

""",
    "11. Generics in Classes": """

Con **genéricos** (`<T>`), tus clases trabajan con cualquier tipo sin duplicar código:

```dart
class Caja<T> {
  T contenido;
  Caja(this.contenido);
}

void main() {
  var cajaInt = Caja<int>(42);
  var cajaStr = Caja<String>('Hola');
  print(cajaInt.contenido);  // 42
  print(cajaStr.contenido);  // Hola
}
```

Puedes restringir el tipo con `extends`, por ejemplo `class CajaNum<T extends num>`.

---

""",
    "Annotations and Extras": """

12. Annotations and Metadata

Dart soporta **anotaciones** con `@`, incluyendo:

- `@override` para métodos que sobrescriben.
- `@Deprecated('Mensaje')` para marcar APIs obsoletas.
- Anotaciones personalizadas vía constructores constantes.

```dart
/// @Deprecated('Usa nuevoMetodo en su lugar')
void metodoAntiguo() {}
```

---

13. Design Patterns with Dart Classes

Dart facilita patrones comunes:

- **Singleton** (constructor factory y campo estático).
- **Factory** (constructor `factory` para elegir subclases).
- **Observer** (listas de callbacks o `Stream`).
- **Decorator** (envolver un objeto con otro que implemente la misma interfaz).
- **Strategy** (inyectar comportamientos mediante interfaces).

Estos patrones mejoran la escalabilidad y mantenibilidad de tu código.

---

14. Best Practices in Class Design

- Usa nombres claros y descriptivos en **CamelCase**.
- Prefiere propiedades **final** cuando no cambien.
- Aplica **encapsulamiento** para proteger el estado interno.
- Divide clases grandes en responsabilidades más pequeñas (principio SRP).
- Documenta métodos y propiedades públicas (ver siguiente sección).

---

15. Documentation and Doc Comments

Emplea comentarios de documentación `///` para detallar APIs:

```dart
/// Calcula la suma de dos números.
/// [a], [b]: operandos para la suma.
/// Retorna el resultado de la operación.
int sumar(int a, int b) => a + b;
```
""",
}

dart_os: dict = {
    "01. Files and Directories": """markdown
```dart
import 'dart:io';

// 📖 Read file content
String content = File('text.txt').readAsStringSync();

// ✍️ Write to file
File('new.txt').writeAsStringSync('Hello world');

// ✅ Check if file exists
bool exists = File('new.txt').existsSync();

// 🧹 Delete file
File('new.txt').deleteSync();

// 📍 Current directory
Directory dir = Directory.current;

// 🗂️ List directory contents
List<FileSystemEntity> dirContents = dir.listSync();
```
""",
    "02. Paths and Manipulation": """markdown
```dart
import 'package:path/path.dart' as p;

// 📎 File name
String name = p.basename('/folder/file.txt');

// 🧩 File extension
String ext = p.extension('file.tar.gz');

// 📍 Absolute path
String fullPath = p.absolute('data.txt');

// 🔗 Join paths
String joined = p.join('folder', 'file.txt');
```
""",
    "03. Date and Time": """markdown
```dart
// ⏰ Current date
DateTime now = DateTime.now();

// 🌐 UTC version
DateTime utc = DateTime.now().toUtc();

// 📅 Parse string to date
DateTime parsed = DateTime.parse('2025-08-01');

// ⏳ Time difference
Duration diff = DateTime.now().difference(parsed);

// 🧾 Simple format
String format = '${now.day}/${now.month}/${now.year}';
```
""",
    "04. System Processes": """markdown
```dart
import 'dart:io';

void main() async {
  // 🖥️ Run shell command
  var result = await Process.run('echo', ['Hello Dart']);

  // 📡 Print output
  print(result.stdout);
}
```
""",
    "05. Environment Variables": """markdown
```dart
import 'dart:io';

// 🌍 All environment variables
Map<String, String> env = Platform.environment;

// 🏡 HOME directory (Unix)
String? home = env['HOME'];
```
""",
    "06. Operating System Detection": """markdown
```dart
import 'dart:io';

// 🪟 Windows
bool isWindows = Platform.isWindows;

// 🐧 Linux
bool isLinux = Platform.isLinux;

// 🍎 macOS
bool isMac = Platform.isMacOS;
```
""",
    "07. Continuous Reading / Streams": """markdown
```dart
import 'dart:io';

void main() async {
  // 🔁 Start real-time process
  var process = await Process.start('ping', ['localhost']);

  // 🖥️ Stream and display output
  process.stdout
    .transform(SystemEncoding().decoder)
    .listen((data) => print('📡 $data'));
```
""",
}
