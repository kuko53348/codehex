app_info_deb: dict = {
    "App version": """
    CODEHEX:

        APP version: 1.1.0
        FLET SDK version: 0.27.6
        PYTHON version: 3.12.8
        FLET-BOX version: 0.1.3 (April 18, 2025)""",
    "Developer": """
Dev:  Maenys Javier Quesada Reyes.
Whatsapp:  +53 54047170

Soy Desarrollador de software especializado en la creación de aplicaciones innovadoras. Con un enfoque en la calidad y la experiencia del usuario, aprovecha las tecnologías modernas para ofrecer soluciones eficientes.
""",
    "CodexLobby": """
🧠 CodeHex is more than an app:
it’s an interactive programming‑language museum built with Flet (Python), capturing the visual, syntactic, and conceptual essence of multiple languages in 🧩 modular visual capsules.

🎓 Designed for self‑taught learners
🌍 Technical migrants
🎨 Digital creatives

who want to learn from an elegant, 📱 portable, and 🔧 adaptable interface.
""",
}


def get_database(index: str = ""):
    return app_info_deb.get(
        index, "✨ You’re Invited to an Unforgettable Dining Experience! ✨"
    )
