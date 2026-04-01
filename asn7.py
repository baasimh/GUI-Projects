import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QRadioButton,
    QGroupBox, QMessageBox
)
from PySide6.QtGui import QPixmap, QFont
from PySide6.QtCore import Qt


class ConverterWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Converter App")
        self.setGeometry(100, 100, 500, 500)

        #main container
        self.central = QWidget()
        self.setCentralWidget(self.central)

        self.mainLayout = QHBoxLayout()
        self.central.setLayout(self.mainLayout)

        #image
        self.imageLabel = QLabel()
        pixmap = QPixmap("house.png")
        self.imageLabel.setPixmap(pixmap)
        self.imageLabel.setScaledContents(True)
        self.imageLabel.setFixedSize(250, 200)

        self.mainLayout.addWidget(self.imageLabel)

        #right side
        self.rightLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.rightLayout)

        #title
        self.lblTitle = QLabel("Converter App")
        self.lblTitle.setFont(QFont("Arial", 18, QFont.Bold))
        self.lblTitle.setAlignment(Qt.AlignCenter)

        self.rightLayout.addWidget(self.lblTitle)

        #instruction & input
        self.topRow = QHBoxLayout()

        self.lblInstruction = QLabel("Enter a value and choose conversion")
        self.lblInstruction.setFont(QFont("Arial", 12))

        self.txtInput = QLineEdit()
        self.txtInput.setFixedWidth(200)

        self.topRow.addWidget(self.lblInstruction)
        self.topRow.addWidget(self.txtInput)

        self.rightLayout.addLayout(self.topRow)

        #radio buttons
        self.groupBox = QGroupBox("Convert Measurement")
        self.rbLayout = QVBoxLayout()

        self.rbInToM = QRadioButton("Inches to Meters")
        self.rbMToIn = QRadioButton("Meters to Inches")

        self.rbInToM.setChecked(True)

        self.rbLayout.addWidget(self.rbInToM)
        self.rbLayout.addWidget(self.rbMToIn)

        self.groupBox.setLayout(self.rbLayout)
        self.rightLayout.addWidget(self.groupBox)

        #result button
        self.lblResult = QLabel("")
        self.lblResult.setAlignment(Qt.AlignCenter)
        self.lblResult.setFont(QFont("Arial", 12))
        self.rightLayout.addWidget(self.lblResult)

        #buttons
        self.btnLayout = QHBoxLayout()

        self.btnConvert = QPushButton("Convert")
        self.btnClear = QPushButton("Clear")
        self.btnExit = QPushButton("Exit")

        self.btnLayout.addWidget(self.btnConvert)
        self.btnLayout.addWidget(self.btnClear)
        self.btnLayout.addWidget(self.btnExit)

        self.rightLayout.addLayout(self.btnLayout)

        #connections
        self.btnConvert.clicked.connect(self.convert)
        self.btnClear.clicked.connect(self.clear)
        self.btnExit.clicked.connect(self.close)

        #styling
        self.setStyleSheet("""
            QWidget {
                background-color: #444444;
                font-size: 14px;
            }

            QGroupBox {
                background-color: #000000;
                color: white;
                font-weight: bold;
                padding: 10px;
                border-radius: 6px;
            }

            QRadioButton {
                color: white;
            }

            QLineEdit {
                background-color: #000000;
                color: white;
                border: 2px solid #444444;
                padding: 5px;
            }

            QPushButton {
                background-color: #EDEDED;
                border: 2px solid #444444;
                padding: 8px;
                min-width: 100px;
                color: black;
                font-weight: bold;
            }

            QPushButton:hover {
                border: 2px solid #4FA3D1;
            }
        """)

    #conversion
    def convert(self):
        text = self.txtInput.text()

        if text == "":
            QMessageBox.critical(self, "Error", "Input cannot be empty.")
            return

        try:
            value = float(text)
        except:
            QMessageBox.critical(self, "Error", "Value entered is not numeric.")
            return

        if value <= 0:
            QMessageBox.critical(self, "Error", "Value must be positive.")
            return

        if self.rbInToM.isChecked():
            result = value * 0.0254
            self.lblResult.setText(f"{value} inches = {result:.3f} meters")
        else:
            result = value / 0.0254
            self.lblResult.setText(f"{value} meters = {result:.3f} inches")

    #clear
    def clear(self):
        self.txtInput.clear()
        self.lblResult.setText("")
        self.rbInToM.setChecked(True)
        self.txtInput.setFocus()


#app run
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ConverterWindow()
    window.show()
    sys.exit(app.exec())