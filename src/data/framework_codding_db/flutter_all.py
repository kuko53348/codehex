flutter_class: dict = {
    "01. Basic Class": """
Defines a minimal structure with a positional constructor and a visual method.

`dart
class Person {
  final String name;
  final int age;

  Person(this.name, this.age);

  void build() => print('[+] >> name: $name age: $age');
}

final instance = Person('Javier', 35);
instance.build(); // [+] >> name: Javier age: 35
`
""",
    "02. Simple Serialization": """
A model-like structure with basic fields. Ideal for JSON mapping or service logic.

`dart
class ProductStore {
  final String name;
  final int age;
  final String occupation;
  final int number;

  ProductStore(this.name, this.age, this.occupation, this.number);
}
`
""",
    "03. Inheritance (extends)": """
The child class inherits and overrides the visual behavior.

`dart
class Person {
  final String name;
  final int age;

  Person(this.name, this.age);

  void build() => print('[•] >> name: $name age: $age');
}

class Manager extends Person {
  Manager(String name, int age) : super(name, age);

  @override
  void build() => print('[+] >> newName: $name newAge: $age');
}
`
""",
    "04. Interface Implementation": """
A class implements a contract, ensuring required methods exist.

`dart
class BuilderContract {
  void build() {}
}

class Architect implements BuilderContract {
  final String name;
  final int age;

  Architect(this.name, this.age);

  @override
  void build() => print('[•] >> Architect $name, age $age');
}
`
""",
    "Extras and Commentary": """
- The d.Class.* prefixes mirror IDE-friendly snippets or plugin triggers.
- extends lets you reuse and tailor class behavior.
- implements enforces structural contracts, promoting cleaner architecture.
- Using final fosters immutability and predictable migration.
- Any Dart class can be serialized using Map<String,dynamic> or jsonEncode.

🛠️ Migration tip: Dart classes can be conceptually mapped to:
  - struct in Go (for functional portability),
  - class in C# (for UI or service layers),
  - or interface contracts in Java, depending on behavioral goals.
""",
}

flutter_async: dict = {
    "01. Basic Async Function": """
Defines an asynchronous function with a delayed action.

`dart
Future<void> showNotification() async {
  await Future.delayed(Duration(seconds: 1));
  print('🔔 Notification sent');
}
`
""",
    "02. Async Function with Return": """
Simulates an async operation returning a message. Uses .then() without await.

`dart
Future<String> loadWelcomeMessage() async {
  await Future.delayed(Duration(seconds: 1));
  return '👋 Welcome, Javier!';
}

void executeAsyncTask() {
  loadWelcomeMessage().then((msg) {
    print('✅ Result: $msg');
  });
}
`
""",
    "03. Commentary and Notes": """
- Use Future<void> when no value needs to be returned.
- Prefer await for cleaner flow inside async functions.
- .then() is useful for quick chaining outside async contexts.
- Duration(...) controls delay or simulated response time.
- Ideal for services, UI feedback, and sequenced logic.

🔧 Editor Tip: These Dart snippets mirror async behavior in other ecosystems (like Task in C#, goroutines in Go), and offer migration clarity when designing cross-platform logic.
""",
}

flutter_ui: dict = {
    "01. Container Basics": """
Creates a stylized box for layout and visual structure.

`dart
Container(
  padding: EdgeInsets.all(8),
  height: 320,
  width: 320,
  decoration: BoxDecoration(
    color: Colors.grey[900],
    borderRadius: BorderRadius.circular(34),
    boxShadow: [BoxShadow(color: Colors.black54, offset: Offset(0, 12), blurRadius: 6)],
  ),
  alignment: Alignment.center,
  child: Text('Container TextStyle', style: TextStyle(color: Colors.cyanAccent)),
);
`
""",
    "02. AnimatedContainer": """
Creates smooth transitions in size, color, shape.

`dart
AnimatedContainer(
  duration: Duration(seconds: 1),
  height: 320,
  width: 320,
  decoration: BoxDecoration(
    color: Colors.red[900],
    borderRadius: BorderRadius.circular(34),
  ),
  alignment: Alignment.center,
  child: Text('AnimatedContainer', style: TextStyle(color: Colors.cyanAccent)),
);
`
""",
    "03. Text Styling": """
Defines font weight, size, color, and alignment.

`dart
Text(
  'Sample Text',
  textAlign: TextAlign.left,
  style: TextStyle(
    fontWeight: FontWeight.w700,
    fontSize: 16,
    color: Colors.grey,
  ),
);
`
""",
    "04. Image Display": """
Includes network and asset images with decoration options.

`dart
Image.asset(
  'lib/images/demo.jpg',
  fit: BoxFit.cover,
);
`
""",
    "05. Layout Visual Hints": """
Helps position and align widgets across screen sizes.

`dart
AspectRatio(
  aspectRatio: 1/1,
  child: Container(color: Colors.red, child: Text('AspectRatio')),
);
`
""",
    "06. Alignment and Box Effects": """
Combines blur, clipping, alignment, scaling.

`dart
ImageFiltered(
  imageFilter: ImageFilter.blur(sigmaX: 12, sigmaY: 12),
  child: FlutterLogo(size: 100),
);

ClipRRect(
  borderRadius: BorderRadius.circular(32),
  child: Container(color: Colors.red, child: Text('Clipped')),
);

Transform.scale(
  scale: 1.0,
  child: Text('Scaled'),
);
`
""",
    "07. Theme and Style Control": """
Customizes color schemes and brightness settings.

`dart
ThemeData darkMode = ThemeData(
  brightness: Brightness.dark,
  colorScheme: ColorScheme.dark(
    surface: Colors.grey.shade900,
    primary: Colors.grey.shade800,
    secondary: Colors.grey.shade700,
  ),
);
`
""",
    "08. Visual Effects Commentary": """
- Use AnimatedContainer, ClipRRect, and Transform for layered motion.
- Theme.of(context) enables contextual design adaptation.
- Combine with SizedBox, Expanded, Spacer for spacing and responsiveness.

🪡 Editorial Tip: This capsule ties visual language to code. It’s excellent for learners migrating from HTML/CSS, UIKit, or GUI-centric languages like C# and JavaFX.
""",
}

flutter_state: dict = {
    "01. Stateful Widget": """
Creates a widget that can hold and update its internal state.

`dart
class CounterWidget extends StatefulWidget {
  const CounterWidget({super.key});

  @override
  State<CounterWidget> createState() => _CounterWidgetState();
}

class _CounterWidgetState extends State<CounterWidget> {
  int count = 0;

  void incrementCounter() {
    setState(() => count++);
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: incrementCounter,
      child: Text('Count: $count'),
    );
  }
}
`
""",
    "02. ValueNotifier (Reactive State)": """
A lightweight reactive variable. Listens for changes and rebuilds UI.

`dart
ValueNotifier<String> messageNotifier = ValueNotifier<String>('Hello world');

ValueListenableBuilder(
  valueListenable: messageNotifier,
  builder: (context, value, _) {
    return Text(value);
  },
);
`
""",
    "03. Update Notifier Value": """
Modify a ValueNotifier's value manually.

`dart
messageNotifier.value = 'Updated message';
`
""",
    "04. Notifier Class Structure": """
Encapsulate notifiers inside a dedicated reactive class.

`dart
class ReactiveStore {
  ValueNotifier<String> username = ValueNotifier<String>('Javier');
}
`
""",
    "05. Commentary and Notes": """
- setState(() => ...) rebuilds the widget when local data changes.
- ValueNotifier + ValueListenableBuilder is perfect for granular reactivity.
- Keep state isolated for easier migration between paradigms (MVU, Redux, BLoC).

🛠️ Migration Tip:
In Go, reactivity is achieved through channels and redraw triggers.
In C#, use INotifyPropertyChanged or ObservableCollection.

🎯 This Dart capsule helps bridge UI interactivity from imperative to reactive patterns—ideal for learners migrating from vanilla JS, SwiftUI, or desktop frameworks.
""",
}

flutter_navigation: dict = {
    "01. Navigate Between Screens": """
Push to a new route using Navigator.

`dart
Navigator.pop(context); // Closes current drawer or screen
Navigator.pushNamed(context, '/SecondPage'); // Navigates forward
`
""",
    "02. DefaultTabController": """
Creates swipeable tab-based navigation with shared layout.

`dart
DefaultTabController(
  length: 3,
  child: Scaffold(
    appBar: AppBar(
      bottom: TabBar(
        tabs: [
          Tab(icon: Icon(Icons.home)),
          Tab(icon: Icon(Icons.people)),
          Tab(icon: Icon(Icons.mail)),
        ],
      ),
      title: Text('Flutter Tabs Example'),
    ),
    body: TabBarView(
      children: [
        Container(color: Colors.blue[900]),
        Container(color: Colors.red[900]),
        Container(color: Colors.yellow[900]),
      ],
    ),
  ),
);
`
""",
    "03. BottomNavigationBar (Simple)": """
Provides persistent footer-based navigation.

`dart
BottomNavigationBar(
  items: [
    BottomNavigationBarItem(icon: Icon(Icons.home), label: 'Home'),
    BottomNavigationBarItem(icon: Icon(Icons.person), label: 'Profile'),
    BottomNavigationBarItem(icon: Icon(Icons.settings), label: 'Settings'),
  ],
);
`
""",
    "04. Drawer Menu": """
Side panel for contextual navigation.

`dart
Drawer(
  child: Column(
    children: [
      DrawerHeader(child: Icon(Icons.favorite)),
      ListTile(
        leading: Icon(Icons.home),
        title: Text('HOME'),
        onTap: () => print('Drawer'),
      ),
      ListTile(
        leading: Icon(Icons.settings),
        title: Text('SETTINGS'),
        onTap: () => print('Drawer'),
      ),
    ],
  ),
);
`
""",
    "05. SliverAppBar Scroll UI": """
Dynamic header that expands, collapses, and floats with content.

`dart
CustomScrollView(
  slivers: [
    SliverAppBar(
      floating: true,
      snap: true,
      expandedHeight: 160.0,
      flexibleSpace: FlexibleSpaceBar(
        title: Text('SliverAppBar'),
        background: FlutterLogo(size: 100),
      ),
    ),
    SliverFillRemaining(
      child: ListView.builder(
        itemCount: 12,
        itemBuilder: (context, index) => ListTile(
          title: Text('Sliver item ${index}'),
        ),
      ),
    ),
  ],
);
`
""",
    "06. Commentary and Tips": """
- Navigator.pushNamed() allows centralized route management.
- DefaultTabController is great for tabbed workflows (profiles, categories).
- BottomNavigationBar anchors navigation visually across screens.
- Use SliverAppBar for scroll-based visibility and motion.
- Modularize screens for clarity, especially in educational apps.

🧭 Migration Tip:
In C#, use Frame.Navigate() in UWP;
In Go (via Gio or Fyne), screens and routes are managed via event routing or tab abstraction.
This capsule introduces screen semantics, helping learners visualize and migrate UI flow logic.
""",
}

flutter_effects: dict = {
    "01. Blur Effect": """
Applies Gaussian blur to any widget.

`dart
ImageFiltered(
  imageFilter: ImageFilter.blur(sigmaX: 12.0, sigmaY: 12.0),
  child: FlutterLogo(size: 100),
);
`
""",
    "02. Animated Opacity": """
Fade in/out widgets smoothly.

`dart
AnimatedOpacity(
  opacity: isVisible ? 1.0 : 0.0,
  duration: Duration(seconds: 1),
  child: Text('Fade Text', style: TextStyle(color: Colors.cyanAccent)),
);
`
""",
    "03. Clip Rounded Corners": """
Renders a visually shaped child inside a rounded boundary.

`dart
ClipRRect(
  borderRadius: BorderRadius.circular(32),
  child: Container(
    color: Colors.red,
    child: Text('Clipped Text', style: TextStyle(color: Colors.cyanAccent)),
  ),
);
`
""",
    "04. Transform Scale": """
Scales content visually without changing layout.

`dart
Transform.scale(
  scale: 1.0,
  child: Text('Scaled Text', style: TextStyle(color: Colors.cyanAccent)),
);
`
""",
    "05. Hero Animation (Cross-screen transition)": """
Creates a shared widget transition across routes.

`dart
Hero(
  tag: 'HeroID',
  child: FlutterLogo(size: 100),
);
`
`dart
InkWell(
  onTap: () {
    Navigator.pop(context);
    Navigator.pushNamed(context, '/SecondPage');
  },
  child: Hero(
    tag: 'HeroID',
    child: Text('Tap to transition'),
  ),
);
`
""",
    "06. Tooltip": """
Displays a hover or long-press hint.

`dart
Tooltip(
  message: 'Tap to learn more',
  child: FlutterLogo(size: 100),
);
`
""",
    "07. Commentary and Tips": """
- Combine AnimatedOpacity + GestureDetector for fade-interactive effects.
- Use Hero to give context between screen transitions — perfect for apps with visual continuity.
- Blur and clip effects can elevate visual storytelling, especially for cards, dialogs, or overlays.
- Tooltips help users understand icons and gestures in minimalist UIs.

🎯 Migration Insight:
These Dart patterns mimic UI transitions in native Android/iOS, Qt, and C# WPF.
They bring precision and emotional clarity to visuals — ideal for migrants building multi-platform apps or tutorials.
""",
}

flutter_lists: dict = {
    "01. ListView (Simple)": """
Horizontal or vertical list of widgets.

`dart
ListView(
  scrollDirection: Axis.horizontal,
  children: [
    Text('Item A'),
    Text('Item B'),
  ],
);
`
""",
    "02. ListView.builder": """
Efficient builder pattern from iterable data.

`dart
List<String> names = ['Javier', 'Dianelys', 'Christian'];

ListView.builder(
  itemCount: names.length,
  itemBuilder: (context, index) => ListTile(
    title: Text(names[index]),
  ),
);
`
""",
    "03. GridView.builder": """
Creates a visual grid layout with reusable cell logic.

`dart
List<String> names = ['Javier', 'Dianelys', 'Christian'];

GridView.builder(
  gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2),
  itemCount: names.length,
  itemBuilder: (context, index) => ListTile(
    title: Text(names[index]),
  ),
);
`
""",
    "04. DataTable": """
Structured tabular layout. Ideal for admin, reports, or models.

`dart
DataTable(
  columns: [
    DataColumn(label: Text('Name')),
    DataColumn(label: Text('Age')),
    DataColumn(label: Text('Occupation')),
    DataColumn(label: Text('Phone')),
  ],
  rows: [
    DataRow(cells: [
      DataCell(Text('Javier')),
      DataCell(Text('35')),
      DataCell(Text('Manager')),
      DataCell(Text('+53 84248235')),
    ])
  ],
);
`
""",
    "05. PageView (Scroll Pages)": """
Scroll between full-screen widgets.

`dart
PageView(
  scrollDirection: Axis.vertical,
  children: [
    Container(color: Colors.amber[900], child: Text('Page 1')),
    Container(color: Colors.red[900], child: Text('Page 2')),
    Container(color: Colors.blue[900], child: Text('Page 3')),
  ],
);
`
""",
    "06. PageView.builder": """
Dynamic paging from iterable structure.

`dart
PageView.builder(
  itemCount: 12,
  scrollDirection: Axis.vertical,
  itemBuilder: (context, index) => Container(
    color: Colors.amber[900],
    alignment: Alignment.center,
    child: Text('Page $index'),
  ),
);
`
""",
    "07. Responsive Scroll Composition": """
Combines layout responsiveness with scroll logic.

`dart
LayoutBuilder(
  builder: (context, constraints) {
    return SingleChildScrollView(
      child: ConstrainedBox(
        constraints: BoxConstraints(minHeight: constraints.maxHeight),
        child: Column(children: [Text('Responsive content')]),
      ),
    );
  },
);
`
""",
    "08. DraggableScrollableSheet": """
Creates overlay panel that can be dragged upward, great for search or filters.

`dart
DraggableScrollableSheet(
  initialChildSize: 0.2,
  minChildSize: 0.2,
  maxChildSize: 0.8,
  builder: (context, scrollController) {
    return ListView.builder(
      controller: scrollController,
      itemCount: 20,
      itemBuilder: (context, index) => ListTile(
        title: Text('Item $index'),
      ),
    );
  },
);
`
""",
    "09. Commentary and Tips": """
- Use ListView.builder for optimized performance with long lists.
- GridView.builder offers visual structure for product cards or galleries.
- DataTable shines in structured datasets and educational panels.
- Combine PageView with animation for tutorial or onboarding flows.
- DraggableScrollableSheet creates dynamic panels familiar to mobile UX.

🧶 Editorial Insight:
These data capsules bridge between visual composition, reactive iteration, and responsive storytelling. Ideal for migrants coming from web (HTML/React), CLI tools, or desktop UIs.
""",
}

flutter_inputs: dict = {
    "01. TextField (Input)": """
A customizable text entry widget, suitable for login forms, search bars, and comments.

`dart
TextField(
  obscureText: true,
  decoration: InputDecoration(
    border: OutlineInputBorder(),
    hintText: 'Enter password',
    filled: true,
    fillColor: Colors.grey.shade900,
  ),
);
`
""",
    "02. GestureDetector": """
Captures touch and gesture events.

`dart
GestureDetector(
  onTap: () => print('Gesture tapped'),
  child: Text('Touch me'),
);
`
""",
    "03. Dismissible (Swipe to Delete)": """
Allows swipe-to-remove behavior in lists.

`dart
Dismissible(
  key: Key('item'),
  onDismissed: (direction) {
    print('Item dismissed');
  },
  background: Container(color: Colors.red),
  child: ListTile(title: Text('Swipe Me')),
);
`
""",
    "04. RadioListTile": """
Displays a radio button with label.

`dart
RadioListTile(
  title: Text('Option A'),
  value: 1,
  groupValue: selectedValue,
  onChanged: (v) => setState(() => selectedValue = v),
);
`
""",
    "05. Checkbox, Switch, and Slider": """
Common toggles with reactive values.

`dart
Checkbox(
  value: true,
  onChanged: (v) => print('Checkbox changed'),
);

Switch(
  value: true,
  onChanged: (v) => print('Switch toggled'),
);

Slider(
  value: sliderValue,
  onChanged: (v) => setState(() => sliderValue = v),
  min: 0,
  max: 100,
);
`
""",
    "06. Commentary and Tips": """
- Combine GestureDetector + AnimatedOpacity for motion-reactive input.
- Dismissible is perfect for swipe-based UX in lists and cards.
- Group RadioListTile with groupValue logic for elegant selection.
- Slider, Switch, and Checkbox provide smooth UI control points.

🎛️ Migration Tip:
Most of these controls translate smoothly into iOS (SwiftUI), Android (Jetpack Compose), or desktop UIs (WPF/XAML). Dart's declarative style simplifies input logic for cross-platform learners.
""",
}

flutter_api: dict = {
    "01. HttpClient Class (GET)": """
Creates a reusable HTTP handler using Dart’s dart:io.

`dart
import 'dart:io';
import 'dart:convert';

class HttpModule {
  final HttpClient _client = HttpClient();

  Future<String> get({required String url, Map<String, String>? headers}) async {
    final request = await _client.getUrl(Uri.parse(url));
    headers?.forEach((key, value) => request.headers.add(key, value));
    final response = await request.close();
    return await response.transform(utf8.decoder).join();
  }
}
`
""",
    "02. POST, PUT, DELETE Methods": """
Implements other verbs with payload and headers.

`dart
Future<String> post({required String url, required Map<String, dynamic> data}) async {
  final request = await _client.postUrl(Uri.parse(url));
  request.headers.contentType = ContentType.json;
  request.write(jsonEncode(data));
  final response = await request.close();
  return await response.transform(utf8.decoder).join();
}
`
""",
    "03. JsonConvert Class": """
Convert between string and JSON objects.

`dart
class HttpModuleJsonConvert {
  dynamic payload;

  HttpModuleJsonConvert({required this.payload});

  Map<String, dynamic> stringToJson() => jsonDecode(payload);
  String jsonToString() => jsonEncode(payload);
}
`
""",
    "04. Request Headers": """
Add custom headers to simulate browser or token auth.

`dart
final headers = {
  'User-Agent': 'Mozilla/5.0',
  'Authorization': 'Bearer my_token',
  'Accept': 'application/json',
};
`
""",
    "05. Usage Example (All Methods)": """
Calls to API with chained .then() for quick execution.

`dart
final api = HttpModule();

api.get(url: 'https://jsonplaceholder.typicode.com/posts/1').then((msg) {
  print('GET ✅ $msg');
});

api.post(
  url: 'https://jsonplaceholder.typicode.com/posts',
  data: {'title': 'foo', 'body': 'bar', 'userId': 1},
).then((msg) => print('POST ✅ $msg'));
`
""",
    "06. IMC Color/Text Switch": """
Simple switch selector based on body metric.

`dart
Color getColorByImc(double imc) => switch (imc) {
  < 18.5 => Colors.blue,
  < 28.5 => Colors.green,
  < 38.5 => Colors.orange,
  _ => Colors.red,
};
`
""",
    "07. Commentary and Tips": """
- Use HttpClient for full control over headers and low-level behavior.
- Prefer jsonEncode and jsonDecode from dart:convert for clean serialization.
- Wrap HTTP logic into classes for plugin-style reuse across apps.
- Use named parameters for clear API contracts and IDE tooling.

🌍 Migration Tip:
- Dart's request model resembles fetch in JavaScript and HttpClient in C#.
- In Go, you'd use http.NewRequest(...), paired with custom headers and body marshaling.

🎯 This capsule builds bridges from local UI to remote services—perfect for learners integrating APIs, form submissions, or mobile dashboards.
""",
}

flutter_utilities: dict = {
    "01. SnackBar": """
Displays lightweight feedback at the bottom of the screen.

`dart
final snackBar = SnackBar(content: Text('Tap confirmed'));
ScaffoldMessenger.of(context).showSnackBar(snackBar);
`
""",
    "02. AlertDialog": """
Creates a pop-up modal with title, content, and actions.

`dart
showDialog(
  context: context,
  builder: (context) => AlertDialog(
    title: Text('Cheat Sheet'),
    content: Text('Do you approve this message?'),
    actions: [
      ElevatedButton(
        child: Text('Close'),
        onPressed: () => Navigator.of(context).pop(),
      ),
    ],
  ),
);
`
""",
    "03. showAboutDialog": """
Displays app metadata with icon and additional links.

`dart
showAboutDialog(
  context: context,
  applicationName: 'App Name',
  applicationVersion: 'v0.01',
  applicationIcon: FlutterLogo(size: 50),
  children: [
    ListTile(
      leading: Icon(Icons.code),
      title: Text('Github repository'),
    ),
  ],
);
`
""",
    "04. Stepper": """
Visualizes a multi-step process (vertical or horizontal).

`dart
Stepper(
  type: StepperType.vertical,
  currentStep: 2,
  onStepContinue: () => setState(() => step++),
  onStepCancel: () => setState(() => step--),
  steps: [
    Step(title: Text('Step 1'), content: Text('Enter your name')),
    Step(title: Text('Step 2'), content: Text('Enter your age')),
    Step(title: Text('Step 3'), content: Text('Enter your phone')),
  ],
);
`
""",
    "05. FloatingActionButton": """
Creates a circular button floating above layout.

`dart
FloatingActionButton(
  backgroundColor: Colors.grey[800],
  onPressed: () => print('FAB tapped'),
  child: Icon(Icons.add, color: Colors.white),
);
`
""",
    "06. AndroidView": """
Embeds native Android view (web, camera, etc.).

`dart
AndroidView(
  viewType: 'webview',
  creationParams: {'url': 'https://example.com'},
);
`
""",
    "07. ReorderableListView": """
Allows drag-and-drop list rearrangement.

`dart
ReorderableListView(
  onReorder: (oldIndex, newIndex) => print('Reordered'),
  children: [
    Text('Item 1', key: ValueKey(1)),
    Text('Item 2', key: ValueKey(2)),
  ],
);
`
""",
    "08. Commentary and Tips": """
- Use SnackBar for non-intrusive feedback, ideal for mobile UX.
- AlertDialog is perfect for confirmation, errors, or tutorials.
- Stepper helps visualize progress in onboarding, forms, or wizards.
- FloatingActionButton anchors key user actions visually.
- AndroidView bridges platform-specific features like embedded media.
- ReorderableListView supports sorting and customization—great for interactive dashboards.

📦 Migration Insight:
These utility snippets bring accessibility, polish, and adaptability to apps. Whether you're migrating from HTML modals, Android Toast, or desktop toolkits, Dart’s declarative layout simplifies user interaction design.
""",
}
