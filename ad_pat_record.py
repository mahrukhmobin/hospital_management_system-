import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6 import uic

class AdminPatientCheck(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:\Users\Hp\OneDrive\Desktop\FINAL_HMS.ui\admin_pat_check.ui", self)  # Load the UI file

        # Connect to the SQLite database
        try:
            self.conn = sqlite3.connect(r"C:\Users\Hp\OneDrive\Desktop\FINAL_HMS.ui\hospital.db")
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            QMessageBox.critical(self, "Database Error", str(e))
            sys.exit(1)

        # Load data from the 'admin_pat' table automatically
        self.load_data()

    def load_data(self):
        try:
            self.cursor.execute("SELECT * FROM patients_list")  # Use the correct table name
            records = self.cursor.fetchall()

            self.tableWidget.setRowCount(len(records))
            self.tableWidget.setColumnCount(len(records[0]) if records else 0)

            for row_idx, row_data in enumerate(records):
                for col_idx, col_data in enumerate(row_data):
                    self.tableWidget.setItem(row_idx, col_idx, 
                        QTableWidgetItem(str(col_data)))

        except sqlite3.Error as e:
            QMessageBox.critical(self, "Query Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdminPatientCheck()
    window.show()
    sys.exit(app.exec())
