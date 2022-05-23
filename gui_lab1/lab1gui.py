# Задание:
# Дан одномерный массив Xn. Найти произведение элементов массива, кратных 3.
# Сформировать новый массив из элементов массива Xn, значения которых меньше А.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem

from qt_frames.bdLab1Complete import Ui_MainWindow
import sys


class AdditionFunctions(Ui_MainWindow):
    def __init__(self):
        self.xr_output_components = None
        self.create_xn_array_components = None
        self.create_xn_array_params_components = None

        self.xn_array = []
        self.xr_array = []
        self.xn_array_capacity = None
        self.a_number = None

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)

        self.create_xn_array_params_components = [
            self.xn_array_capacity_label,
            self.xn_array_capacity_line_edit,
            self.a_number_label,
            self.a_number_line_edit,
            self.create_xn_array_push_button
        ]

        self.create_xn_array_components = [
            self.xn_input_label,
            self.xn_table_widget,
            self.back_push_button,
            self.calculate_push_button
        ]

        self.xr_output_components = [
            self.xr_output_label,
            self.xr_table_widget,
            self.mult_3_label,
            self.mult_3_line_edit,
            self.clear_push_button
        ]

        # self.task_horizontal_layout.setEnabled(False)
        self.switch_componetns(self.create_xn_array_components)
        self.switch_componetns(self.xr_output_components)

        self.create_xn_array_push_button.clicked.connect(self.create_xn_array)
        self.back_push_button.clicked.connect(self.go_back)
        self.calculate_push_button.clicked.connect(self.calculate)
        self.clear_push_button.clicked.connect(self.clear_all)

        self.xn_array_capacity_line_edit.text()

    def create_xn_array(self):
        print("Кнопка создания массива нажата")
        if self.check_input_lines(
            self.xn_array_capacity_line_edit,
            self.a_number_line_edit
        ):
            self.xn_array_capacity = int(self.xn_array_capacity_line_edit.text())
            self.a_number = int(self.a_number_line_edit.text())
            self.xn_array = [None] * self.xn_array_capacity
            print("Массив создан")
            self.show_input_array(self.xn_array_capacity)

    def show_input_array(self, xn_capacity):
        self.xn_table_widget.setRowCount(1)
        self.xn_table_widget.setColumnCount(xn_capacity)
        self.xn_table_widget.setVerticalHeaderLabels(
            ["Значение"]
        )
        xn_elements_titles = []
        for i in range(xn_capacity):
            xn_elements_titles.append(f"Xn[{i}]")
        self.xn_table_widget.setHorizontalHeaderLabels(xn_elements_titles)

        self.switch_componetns(self.create_xn_array_params_components)
        self.switch_componetns(self.create_xn_array_components)

    def go_back(self):
        print("Кнопка Вернуться нажата")
        self.xn_table_widget.clear()
        self.xn_table_widget.setRowCount(0)
        self.xn_table_widget.setColumnCount(0)
        # self.xn_table_widget.clearContents()
        self.switch_componetns(self.create_xn_array_components)
        self.switch_componetns(self.create_xn_array_params_components)

    def calculate(self):
        if self.check_input_array_data():
            print("Всё ок")
            self.xn_array = []
            for i in range(self.xn_array_capacity):
                self.xn_array.append(int(self.xn_table_widget.item(0, i).text()))
            print(self.xn_array)

            self.switch_componetns(self.create_xn_array_components)
            self.switch_componetns(self.xr_output_components)
            self.xr_array_creation()
            self.mult_of_tree()

    def check_input_lines(self, capacity, a_number):
        try:
            int(capacity.text())
            int(a_number.text())
            return True
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Ошибка!")
            msg_box.setText("Значения должны быть заданы натуральными числами!")
            msg_box.exec_()

    def check_input_array_data(self):
        try:
            for i in range(self.xn_array_capacity):
                int(self.xn_table_widget.item(0, i).text())
                print(self.xn_table_widget.item(0, i).text())
            print("Все элементы таблицы ок")
            return True
        except:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Ошибка!")
            msg_box.setText("Значения должны быть заданы натуральными числами!")
            msg_box.exec_()

    def switch_componetns(self, components):
        for i in components:
            i.setEnabled(not i.isEnabled())

    def xr_array_creation(self):
        self.xr_array = [x for x in self.xn_array if x < self.a_number]
        if len(self.xr_array) > 0:
            print(self.xr_array)
            print("Создаём таблицу")
            self.xr_table_widget.setRowCount(1)
            self.xr_table_widget.setColumnCount(len(self.xr_array))
            self.xr_table_widget.setVerticalHeaderLabels(
                ["Значение"]
            )
            xr_elements_titles = []
            for i in range(len(self.xr_array)):
                xr_elements_titles.append(f"Xr[{i}]")
            self.xr_table_widget.setHorizontalHeaderLabels(xr_elements_titles)
            for i in range(len(self.xr_array)):
                item = QTableWidgetItem(str(self.xr_array[i]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.xr_table_widget.setItem(0, i, item)
        else:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Ошибка!")
            msg_box.setText(f"Ошибка! Элементов, меньше {self.a_number} не найдено. Новый массив пуст.")
            msg_box.exec_()

    def mult_of_tree(self):
        mult_of_tree_arr = [x for x in self.xn_array if x % 3 == 0]
        if len(mult_of_tree_arr) > 0:
            mult_of_tree = 1
            for i in mult_of_tree_arr:
                mult_of_tree *= i
            self.mult_3_line_edit.setText(str(mult_of_tree))
        else:
            self.mult_3_line_edit.setText("0")

    def clear_all(self):
        self.switch_componetns(self.create_xn_array_params_components)
        self.switch_componetns(self.xr_output_components)
        self.xn_array_capacity_line_edit.setText("")
        self.a_number_line_edit.setText("")
        self.xn_table_widget.clear()
        self.xn_table_widget.setRowCount(0)
        self.xn_table_widget.setColumnCount(0)
        self.xr_table_widget.clear()
        self.xr_table_widget.setRowCount(0)
        self.xr_table_widget.setColumnCount(0)
        self.mult_3_line_edit.setText("")


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = AdditionFunctions()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
