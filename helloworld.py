from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication([])

button = QPushButton("Click Me")
button.clicked.connect(lambda: print("Button clicked!"))
button.setFixedSize(400, 200)
button.show()

app.exec()
