from PyQt6 import QtWidgets, QtCore, QtGui


class DraggableLabel(QtWidgets.QLabel):
    def mousePressEvent(self, event):
        self.parent().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.parent().mouseMoveEvent(event)


class RotatedLabel(DraggableLabel):
    def __init__(self, parent=None, rotation=0):
        super().__init__(parent)
        self.rotation = rotation

        # Загрузить QSS из файла
        with open("styles.qss", "r") as f:
            self.setStyleSheet(f.read())

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setPen(QtCore.Qt.GlobalColor.white)  # Измените цвет пера на белый, чтобы соответствовать стилю QSS
        painter.translate(20, 100)
        painter.rotate(self.rotation)
        painter.drawText(0, 0, self.text())
        painter.end()
