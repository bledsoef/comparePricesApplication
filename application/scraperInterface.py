from PyQt6.QtWidgets import QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from scraper import runScraper

class ScraperInterface(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(300, 300)
        self.setWindowTitle("Price Comparison")
        self.setStyleSheet(
        "background-color: #ffffff;"
        )
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.homePage()

    def clearLayout(self):
        """
        Removes all widgets on window
        """
        for i in reversed(range(self.layout.count())): 
            self.layout.itemAt(i).widget().deleteLater()

    def homePage(self):
        self.productText = QLabel("Input the product you're searching for:", self)
        self.productText.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.addWidget(self.productText)

        self.product = QLineEdit("Product")
        self.product.setFixedWidth(250)
        self.layout.addWidget(self.product, alignment= Qt.AlignmentFlag.AlignTop)

        self.priceText = QLabel("Input the price:", self)
        self.priceText.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.layout.addWidget(self.priceText)

        self.price = QLineEdit("Price")
        self.price.setFixedWidth(250)
        self.layout.addWidget(self.price, alignment= Qt.AlignmentFlag.AlignTop)

        button = QPushButton("Submit")
        button.clicked.connect(self.getUserInput)
        self.layout.addWidget(button)
 
    def getUserInput(self):
        product = self.product.text()
        price = self.price.text()
        runScraper(product, price)
        self.close()

    def resultsPage(self):
        self.clearLayout()
