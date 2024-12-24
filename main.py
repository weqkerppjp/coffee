import sys
import sqlite3
from PyQt6 import QtWidgets, uic


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.connection = sqlite3.connect('coffee.sqlite')
        self.load_data_button.clicked.connect(self.load_data)

    def load_data(self):
        self.coffee_table.setRowCount(0)

        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()

        for row in rows:
            row_position = self.coffee_table.rowCount()
            self.coffee_table.insertRow(row_position)
            for column, data in enumerate(row):
                self.coffee_table.setItem(row_position, column, QtWidgets.QTableWidgetItem(str(data)))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
