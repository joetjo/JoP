from PySide6.QtWidgets import QApplication


class GhGuiApplication(QApplication):
    """
    Main Application ( Based on Qt through PySide6 )
    """

    def __init__(self):
        super().__init__()
