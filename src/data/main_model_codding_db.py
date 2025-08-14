from model.FlutterModelView import FlutterModelView
from model.ModelDataView import ModelDataView
from .programing_codding_db.cpp_all import cpp_code, cpp_class, cpp_os
from .programing_codding_db.csharp_all import csharp_code, csharp_class, csharp_os
from .programing_codding_db.dart_all import dart_code, dart_class, dart_os
from .programing_codding_db.java_all import java_code, java_class, java_os
from .programing_codding_db.kotlin_all import kotlin_code, kotlin_class, kotlin_os
from .programing_codding_db.python_all import python_code, python_class, python_os
from .programing_codding_db.rust_all import rust_code, rust_class, rust_os
from .programing_codding_db.swift_all import swift_code, swift_class, swift_os
from .programing_codding_db.zig_all import zig_code, zig_class, zig_os

from .framework_codding_db.flutter_all import (
    flutter_class,
    flutter_async,
    flutter_ui,
    flutter_state,
    flutter_navigation,
    flutter_effects,
    flutter_lists,
    flutter_inputs,
    flutter_api,
    flutter_utilities,
)


# lenguajes codding  list
cpp = ModelDataView
csharp = ModelDataView
dart = ModelDataView
flutter = ModelDataView
java = ModelDataView
kotlin = ModelDataView
python = ModelDataView
rust = ModelDataView
swift = ModelDataView
zig = ModelDataView


# framework codding  list
flutter = FlutterModelView


def dict_object_seralization() -> dict:

    return {
        "cpp": cpp(code=cpp_code, class_oob=cpp_class, module_os=cpp_os),
        "csharp": csharp(code=csharp_code, class_oob=csharp_class, module_os=csharp_os),
        "dart": dart(code=dart_code, class_oob=dart_class, module_os=dart_os),
        "java": java(code=java_code, class_oob=java_class, module_os=java_os),
        "kotlin": kotlin(code=kotlin_code, class_oob=kotlin_class, module_os=kotlin_os),
        "python": python(code=python_code, class_oob=python_class, module_os=python_os),
        "rust": rust(code=rust_code, class_oob=rust_class, module_os=rust_os),
        "swift": swift(code=swift_code, class_oob=swift_class, module_os=swift_os),
        "zig": zig(code=zig_code, class_oob=zig_class, module_os=zig_os),
        "flutter": flutter(
            flutter_class=flutter_class,
            flutter_async=flutter_async,
            flutter_ui=flutter_ui,
            flutter_state=flutter_state,
            flutter_navigation=flutter_navigation,
            flutter_effects=flutter_effects,
            flutter_lists=flutter_lists,
            flutter_inputs=flutter_inputs,
            flutter_api=flutter_api,
            flutter_utilities=flutter_utilities,
        ),
    }


def show_only_frameworks() -> list:
    # its necessary separate framworks that will show
    # on secod screen

    return ["flutter"]
