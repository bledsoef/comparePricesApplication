from PyQt6.QtWidgets import QApplication
from scraperInterface import ScraperInterface
import sys

def main():
    # initializes application
    app = QApplication(sys.argv)
    window = ScraperInterface()
    window.show()
    app.setStyle('Fusion')
    sys.exit(app.exec())

main()