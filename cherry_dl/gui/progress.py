
from PyQt5 import (
    QtWidgets,
)

from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
)

from ..ui.progress_ui import Ui_Progress

class Progress(QWidget, Ui_Progress):

    def __init__(self, parent):
        super().__init__(parent)

        self.setupUi(self)

    def setupConfig(self):
        for child in self.widget.children():
            if child.objectName() == "pushButton_3":
                print("foo")
                print(type(child))
                child.clicked.connect(self.foo)
    
    def foo(self):
        print("Button 3 clicked")



