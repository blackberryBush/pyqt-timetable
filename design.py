from PyQt6 import QtCore, QtGui, QtWidgets

from buttons import DraggableButton
from excel import init_excel, read_excel_buttons
from labels import RotatedLabel, DraggableLabel


class Ui_MainWindow(object):
    def __init__(self):
        self.push_button = None
        self.btns = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 736)

        # Central Widget
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Main Layout
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setSpacing(2)
        self.main_layout.setObjectName("main_layout")

        # Corner Button
        self.corner_button = DraggableButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.corner_button.sizePolicy().hasHeightForWidth())
        self.corner_button.setSizePolicy(sizePolicy)
        self.corner_button.setMinimumSize(QtCore.QSize(110, 27))
        self.corner_button.setMaximumSize(QtCore.QSize(110, 27))
        self.corner_button.setObjectName("corner_button")
        self.main_layout.addWidget(self.corner_button, 0, 0, 1, 1)

        # Upper Week Layout
        self.upper_week_layout = QtWidgets.QVBoxLayout()
        self.upper_week_layout.setSpacing(2)
        self.upper_week_layout.setObjectName("upper_week_layout")

        # Buttons in Upper Week Layout
        for i in range(1, 26):
            push_button = DraggableButton(parent=self.centralwidget)
            push_button.setMinimumSize(QtCore.QSize(0, 27))
            push_button.setMaximumSize(QtCore.QSize(16777215, 27))
            push_button.setObjectName(f"pushButton_{i}")
            setattr(self, f"pushButton_{i}", push_button)
            self.btns.append(push_button)
            self.upper_week_layout.addWidget(push_button)

        # Add Upper Week Layout to Main Layout
        self.main_layout.addLayout(self.upper_week_layout, 1, 1, 1, 1)

        # Lower Week Layout
        self.lower_week_layout = QtWidgets.QVBoxLayout()
        self.lower_week_layout.setSpacing(2)
        self.lower_week_layout.setObjectName("lower_week_layout")

        # Buttons in Lower Week Layout
        for i in range(26, 51):
            push_button = DraggableButton(parent=self.centralwidget)
            push_button.setMinimumSize(QtCore.QSize(0, 27))
            push_button.setMaximumSize(QtCore.QSize(16777215, 27))
            push_button.setObjectName(f"pushButton_{i}")
            setattr(self, f"pushButton_{i}", push_button)
            self.btns.append(push_button)
            self.lower_week_layout.addWidget(push_button)

        # Add Lower Week Layout to Main Layout
        self.main_layout.addLayout(self.lower_week_layout, 1, 2, 1, 1)

        # Day Time Options
        self.day_time_options = QtWidgets.QHBoxLayout()
        self.day_time_options.setSpacing(2)
        self.day_time_options.setObjectName("day_time_options")

        # Vertical Layout for Rotated Labels
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")

        # Rotated Labels
        for i in range(1, 6):
            label = RotatedLabel(parent=self.centralwidget, rotation=-90)
            label.setMinimumSize(QtCore.QSize(25, 0))
            label.setMaximumSize(QtCore.QSize(25, 16777215))
            font = QtGui.QFont()
            font.setFamily("Tahoma")
            font.setPointSize(11)
            label.setFont(font)
            label.setObjectName(f"label_{i}")
            setattr(self, f"label_{i}", label)
            self.verticalLayout.addWidget(label)

        # Add Vertical Layout to Day Time Options
        self.day_time_options.addLayout(self.verticalLayout)

        # Hours Layout
        self.hours = QtWidgets.QVBoxLayout()
        self.hours.setSpacing(2)
        self.hours.setObjectName("hours")

        # Hours Buttons
        for i in range(51, 76):
            push_button = DraggableButton(parent=self.centralwidget)
            push_button.setMinimumSize(QtCore.QSize(0, 27))
            push_button.setMaximumSize(QtCore.QSize(1000, 27))
            push_button.setObjectName(f"pushButton_{i}")
            setattr(self, f"pushButton_{i}", push_button)
            self.hours.addWidget(push_button)

        # Add Hours Layout to Day Time Options
        self.day_time_options.addLayout(self.hours)

        # Add Day Time Options to Main Layout
        self.main_layout.addLayout(self.day_time_options, 1, 0, 1, 1)

        # Upper week label
        self.label_6 = DraggableLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.main_layout.addWidget(self.label_6, 0, 1, 1, 1)

        # Lower week label
        self.label_7 = DraggableLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.main_layout.addWidget(self.label_7, 0, 2, 1, 1)

        self.verticalLayout_2.addLayout(self.main_layout)

        # Add Main Layout to Central Widget
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.buttons = read_excel_buttons('Расписание.xlsx')
        if self.buttons is None:
            self.buttons = {"corner_button": "Неделя 0", **{f"pushButton_{i}": '' for i in range(1, 51)},
                            **{f"pushButton_{i}": f"9:30 - 11:05" for i in [51, 56, 61, 66, 71]},
                            **{f"pushButton_{i}": f"11:20 - 12:55" for i in [52, 57, 62, 67, 72]},
                            **{f"pushButton_{i}": f"13:10 - 14:45" for i in [53, 58, 63, 68, 73]},
                            **{f"pushButton_{i}": f"15:25 - 17:00" for i in [54, 59, 64, 69, 74]},
                            **{f"pushButton_{i}": f"17:15 - 18:50" for i in [55, 60, 65, 70, 75]}}
            init_excel(self.buttons)

        for key, value in self.buttons.items():
            button = getattr(self, key)
            button.setText(_translate("MainWindow", value))

        day_labels = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница"]

        for index, day_label in enumerate(day_labels, start=1):
            label = getattr(self, f"label_{index}")
            label.setText(_translate("MainWindow", day_label))

        week_labels = [
            "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Верхняя (н) неделя</span></p></body></html>",
            "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Нижняя (ч) неделя</span></p></body></html>"
        ]

        for index, week_label in enumerate(week_labels, start=6):
            label = getattr(self, f"label_{index}")
            label.setText(_translate("MainWindow", week_label))

        init_excel(self.buttons)
