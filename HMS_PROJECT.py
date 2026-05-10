import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

from mainpage import Ui_MainWindow as MainPageUI
from login_page import Ui_Dialog as LoginPageUI
from create_account import Ui_Dialog as CreateAccountUI
from admin_dashboard import Ui_MainWindow as AdminDashboardUI
from dashboard_for_patients import Ui_MainWindow as PatientDashboardUI

# Modules
import ad_doc_sch
import send_email
import pat_doc_sch
import patient_appoint_form
import pat_his_log
import history_show
import mainpage
import ad_pat_record


class LoginSystem:
    ADMIN_CREDENTIALS = {"username": "admin", "password": "admin123"}
    PATIENT_CREDENTIALS = [
        {"username": "patient1", "password": "patient123"},
        {"username": "patient2", "password": "patient456"}
    ]


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):  # ✅ FIXED: Correct constructor
        super().__init__()
        self.ui = MainPageUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_login_dialog)

    def open_login_dialog(self):
        self.login_dialog = QtWidgets.QDialog()
        self.login_ui = LoginPageUI()
        self.login_ui.setupUi(self.login_dialog)
        self.login_ui.pushButton.clicked.connect(self.attempt_login)
        self.login_ui.create_one.clicked.connect(self.open_create_account)
        self.login_dialog.exec()

    def open_create_account(self):
        self.create_account_dialog = QtWidgets.QDialog()
        self.create_ui = CreateAccountUI()
        self.create_ui.setupUi(self.create_account_dialog)
        self.create_ui.ok.accepted.connect(self.create_new_account)
        self.login_dialog.close()
        self.create_account_dialog.exec()

    def create_new_account(self):
        username = self.create_ui.userline.text()
        password = self.create_ui.pass_line.text()
        confirm_password = self.create_ui.chline.text()

        if not username or not password:
            QMessageBox.warning(self.create_account_dialog, "Error", "Username and password cannot be empty!")
            return

        if password != confirm_password:
            QMessageBox.warning(self.create_account_dialog, "Error", "Passwords do not match!")
            return

        if any(user["username"] == username for user in LoginSystem.PATIENT_CREDENTIALS):
            QMessageBox.warning(self.create_account_dialog, "Error", "Username already exists!")
            return

        LoginSystem.PATIENT_CREDENTIALS.append({
            "username": username,
            "password": password
        })

        QMessageBox.information(self.create_account_dialog, "Success", "Account created successfully!")
        self.create_account_dialog.close()
        self.open_login_dialog()

    def attempt_login(self):
        username = self.login_ui.lineEdit.text()
        password = self.login_ui.lineEdit_2.text()

        if (username == LoginSystem.ADMIN_CREDENTIALS["username"] and
                password == LoginSystem.ADMIN_CREDENTIALS["password"]):
            self.open_admin_dashboard()
            self.login_dialog.close()
            return

        for patient in LoginSystem.PATIENT_CREDENTIALS:
            if (username == patient["username"] and
                    password == patient["password"]):
                self.open_patient_dashboard()
                self.login_dialog.close()
                return

        QMessageBox.warning(self.login_dialog, "Login Failed", "Invalid username or password!")

    def open_admin_dashboard(self):
        self.admin_window = QtWidgets.QMainWindow()
        self.admin_ui = AdminDashboardUI()
        self.admin_ui.setupUi(self.admin_window)

        if hasattr(self.admin_ui, 'doc_sch'):
            self.admin_ui.doc_sch.clicked.connect(self.open_admin_doc_schedule)
        if hasattr(self.admin_ui, 'send_mail'):
            self.admin_ui.send_mail.clicked.connect(self.open_mailing)
        if hasattr(self.admin_ui, 'home'):
            self.admin_ui.home.clicked.connect(self.open_pat_history_login)
        if hasattr(self.admin_ui, 'about'):
            self.admin_ui.about.clicked.connect(self.open_admin_patient_record)

        self.admin_window.show()
        self.close()

    def open_pat_history_login(self):
        self.pat_history_login = QtWidgets.QDialog()
        self.pat_history_ui = pat_his_log.Ui_Dialog()
        self.pat_history_ui.setupUi(self.pat_history_login)

        if hasattr(self.pat_history_ui, 'pushButton'):
            self.pat_history_ui.pushButton.clicked.connect(self.open_history_show_from_login)

        self.pat_history_login.exec()

    def open_history_show_from_login(self):
        cnic = self.pat_history_ui.CNIC.text().strip()
        patient_name = self.pat_history_ui.pat_name.text().strip()

        self.history_window = QtWidgets.QMainWindow()
        self.history_ui = history_show.Ui_MainWindow()
        self.history_ui.setupUi(self.history_window)
        self.history_window.show()

        self.pat_history_login.close()

    def open_admin_patient_record(self):
        self.admin_patient_record = QtWidgets.QMainWindow()
        self.admin_patient_ui = ad_pat_record.AdminPatientCheck()
        self.admin_patient_ui.show()

    def open_admin_doc_schedule(self):
        self.doc_schedule_window = QtWidgets.QMainWindow()
        self.doc_schedule_ui = ad_doc_sch.Ui_MainWindow()
        self.doc_schedule_ui.setupUi(self.doc_schedule_window)
        self.doc_schedule_window.show()

    def open_mailing(self):
        self.mailing_window = send_email.AppointmentUI()
        self.mailing_window.show()

    def open_history_show(self):
        self.history_window = QtWidgets.QMainWindow()
        self.history_ui = history_show.Ui_MainWindow()
        self.history_ui.setupUi(self.history_window)
        self.history_window.show()

    def open_patient_dashboard(self):
        self.patient_window = QtWidgets.QMainWindow()
        self.patient_ui = PatientDashboardUI()
        self.patient_ui.setupUi(self.patient_window)

        if hasattr(self.patient_ui, 'take_appoint'):
            self.patient_ui.take_appoint.clicked.connect(self.open_patient_appointment_form)
        if hasattr(self.patient_ui, 'doc_sch'):
            self.patient_ui.doc_sch.clicked.connect(self.open_patient_doctor_schedule)
        if hasattr(self.patient_ui, 'home'):
            self.patient_ui.home.clicked.connect(self.open_main_page)

        self.patient_window.show()
        self.close()

    def open_patient_appointment_form(self):
        self.appointment_dialog = QtWidgets.QDialog()
        self.appointment_ui = patient_appoint_form.Ui_Dialog()
        self.appointment_ui.setupUi(self.appointment_dialog)

        if hasattr(self.appointment_ui, 'pushButton_2'):
            self.appointment_ui.pushButton_2.clicked.connect(self.open_mailing)
        if hasattr(self.appointment_ui, 'home'):
            self.appointment_ui.home.clicked.connect(self.open_main_page)

        self.appointment_dialog.exec()

    def open_main_page(self):
        self.main_window = QtWidgets.QMainWindow()
        self.main_ui = mainpage.Ui_MainWindow()
        self.main_ui.setupUi(self.main_window)
        self.main_window.show()

        if hasattr(self, 'patient_window'):
            self.patient_window.close()
        if hasattr(self, 'appointment_dialog'):
            self.appointment_dialog.close()

    def open_patient_doctor_schedule(self):
        self.doctor_schedule_window = QtWidgets.QMainWindow()
        self.doctor_schedule_ui = pat_doc_sch.Ui_MainWindow()
        self.doctor_schedule_ui.setupUi(self.doctor_schedule_window)
        self.doctor_schedule_window.show()


# ✅ FIXED: Entry point
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

