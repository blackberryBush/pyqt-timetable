from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QPoint, Qt

import design


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.Tool | QtCore.Qt.WindowType.FramelessWindowHint)
        self.mpos = QPoint()
        self.setWindowOpacity(0.8)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.mpos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.MouseButton.LeftButton:
            diff = event.pos() - self.mpos
            new_pos = self.pos() + diff

            self.move(new_pos)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    with open('styles.qss', 'r') as f:
        style = f.read()

        # Set the stylesheet of the application
        app.setStyleSheet(style)
    window = MainWindow()
    window.show()
    app.exec()
