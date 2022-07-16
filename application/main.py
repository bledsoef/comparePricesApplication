from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
import sys
from scraper import runScraper
 
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)
        self.setWindowTitle("priceComparison")
 
        layout = QVBoxLayout()
        self.setLayout(layout)
 
        self.input = QLineEdit()
        self.input.setFixedWidth(350)
        layout.addWidget(self.input, alignment= Qt.AlignmentFlag.AlignCenter)
 
        button = QPushButton("Submit")
        button.clicked.connect(self.get)
        layout.addWidget(button)
 
        button = QPushButton("Clear Text")
        button.clicked.connect(self.input.clear)
        layout.addWidget(button)
 
    def get(self):
        text = self.input.text()
        runScraper(str(text))
        self.close()

app = QApplication(sys.argv)
window = Window()
window.show()

sys.exit(app.exec())