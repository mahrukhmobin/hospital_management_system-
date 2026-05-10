import sys
import os
import json
from PyQt6 import uic, QtWidgets

# 🔁 Map departments to their corresponding doctor UI files
DEPARTMENT_UIS = {
    "cardiology": r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/card.appoint.ui",
    "neurology": r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/neuro_appoint.ui",
    "endocrinology": r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/endoro_appoint.ui",
    "ent": r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/ent_appoint.ui",
    "dermatology": r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/dermatologo_appoi.ui",
    "medicine": r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/gener_phy_appoint.ui",
    "gynaecology": r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/gyni_appoint.ui",
    "orthopaedics":r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/ortho_appoint.ui",
    "paediatrics": r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/pedet_appoint.ui",
    "psychiatry": r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/psychat_appoint.ui"
}


class AppointmentForm(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/patient_appoint_form.ui", self)

        self.nameField = self.findChild(QtWidgets.QLineEdit, "lineEdit")
        self.ageField = self.findChild(QtWidgets.QSpinBox, "spinBox")
        self.genderField = self.findChild(QtWidgets.QComboBox, "comboBox")
        self.addressField = self.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        self.emailField = self.findChild(QtWidgets.QLineEdit, "lineEdit_3")
        self.noteField = self.findChild(QtWidgets.QTextEdit, "textEdit")
        self.cnicField = self.findChild(QtWidgets.QLineEdit, "lineEdit_4")
        self.contactField = self.findChild(QtWidgets.QLineEdit, "lineEdit_6")
        self.departmentField = self.findChild(QtWidgets.QComboBox, "comboBox_2")

        self.buttonBox = self.findChild(QtWidgets.QDialogButtonBox, "box_for_appoint")
        self.buttonBox.accepted.connect(self.save_appointment)
        self.buttonBox.rejected.connect(self.reject)

    def save_appointment(self):
        self.selected_department = self.departmentField.currentText().lower()
        filename = f"appointments_{self.selected_department}.json"

        appointment = {
            "name": self.nameField.text(),
            "cnic": self.cnicField.text(),
            "contact": self.contactField.text(),
            "age": self.ageField.value(),
            "gender": self.genderField.currentText(),
            "address": self.addressField.text(),
            "email": self.emailField.text(),
            "notes": self.noteField.toPlainText(),
            "department": self.selected_department
        }

        # Load existing or create new
        appointments = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                appointments = json.load(f)

        appointments.append(appointment)
        with open(filename, "w") as f:
            json.dump(appointments, f, indent=2)

        QtWidgets.QMessageBox.information(self, "Success", "Appointment saved!")
        self.accept()


class AppointmentViewer(QtWidgets.QMainWindow):
    def __init__(self, department):
        super().__init__()
        self.department = department.lower()

        ui_path = DEPARTMENT_UIS.get(self.department)
        if not ui_path:
            QtWidgets.QMessageBox.critical(self, "Error", f"No UI file mapped for department: {self.department}")
            sys.exit(1)

        uic.loadUi(ui_path, self)
        self.table = self.findChild(QtWidgets.QTableWidget, "patforapp")
        self.load_appointments()

    def load_appointments(self):
        filename = f"appointments_{self.department}.json"
        if not os.path.exists(filename):
            return

        with open(filename, "r") as f:
            appointments = json.load(f)

        self.table.setRowCount(len(appointments))
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["NAME", "CNIC", "AGE", "GENDER", "CONTACT", "ADDRESS", "E-MAIL", "NOTES"])

        for row, appt in enumerate(appointments):
            self.table.setItem(row, 0, QtWidgets.QTableWidgetItem(appt.get("name", "")))
            self.table.setItem(row, 1, QtWidgets.QTableWidgetItem(appt.get("cnic", "")))
            self.table.setItem(row, 2, QtWidgets.QTableWidgetItem(str(appt.get("age", ""))))
            self.table.setItem(row, 3, QtWidgets.QTableWidgetItem(appt.get("gender", "")))
            self.table.setItem(row, 4, QtWidgets.QTableWidgetItem(appt.get("contact", "")))
            self.table.setItem(row, 5, QtWidgets.QTableWidgetItem(appt.get("address", "")))
            self.table.setItem(row, 6, QtWidgets.QTableWidgetItem(appt.get("email", "")))
            self.table.setItem(row, 7, QtWidgets.QTableWidgetItem(appt.get("notes", "")))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    form = AppointmentForm()
    if form.exec():
        department = form.selected_department
        viewer = AppointmentViewer(department)
        viewer.show()
        sys.exit(app.exec())