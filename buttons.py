from PyQt6 import QtWidgets

from excel import init_excel, read_excel_buttons


class DraggableButton(QtWidgets.QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dragging = False

    def mousePressEvent(self, event):
        self.dragging = False
        self.parent().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        self.dragging = True
        self.parent().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if not self.dragging:
            print(f"Button {self.objectName()} clicked")
            text, ok = QtWidgets.QInputDialog.getText(self, 'Ввод текста', 'Введите новый текст:')
            if ok:
                self.setText(str(text))
                buttons = read_excel_buttons('Расписание.xlsx')
                buttons[self.objectName()] = str(text)
                init_excel(buttons)
        self.parent().mouseReleaseEvent(event)
