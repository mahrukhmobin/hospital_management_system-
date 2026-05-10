import sys
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6.QtWidgets import QMessageBox

# Import all the generated UI files
from mainpage import Ui_MainWindow as MainPageUI
from login_page import Ui_Dialog as LoginPageUI
from create_account import Ui_Dialog as CreateAccountUI
from admin_dashboard import Ui_MainWindow as AdminDashboardUI
from dashboard_for_patients import Ui_MainWindow as PatientDashboardUI

# Import the additional modules we need to connect
import pat_doc_sch
import patient_appoint_form
import mailing
import mainpage

class LoginSystem:
    # Hardcoded credentials (in a real app, use a database)
    ADMIN_CREDENTIALS = {"username": "admin", "password": "admin123"}
    PATIENT_CREDENTIALS = [
        {"username": "patient1", "password": "patient123"},
        {"username": "patient2", "password": "patient456"}
    ]

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainPageUI()
        self.ui.setupUi(self)
        
        # Maintain references to windows
        self.patient_window = None
        self.appointment_dialog = None
        self.mailing_window = None
        self.doctor_schedule_window = None
        
        # Connect the login button to open the login dialog
        self.ui.pushButton.clicked.connect(self.open_login_dialog)
        
    def open_login_dialog(self):
        self.login_dialog = QtWidgets.QDialog(self)
        self.login_ui = LoginPageUI()
        self.login_ui.setupUi(self.login_dialog)
        
        # Connect login button in the login dialog
        self.login_ui.pushButton.clicked.connect(self.attempt_login)
        
        # Connect "Create one" button to open account creation
        self.login_ui.create_one.clicked.connect(self.open_create_account)
        
        self.login_dialog.exec()
    
    def open_create_account(self):
        self.create_account_dialog = QtWidgets.QDialog(self)
        self.create_ui = CreateAccountUI()
        self.create_ui.setupUi(self.create_account_dialog)
        
        # Connect OK button to create account
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
            
        # Check if username already exists
        if any(user["username"] == username for user in LoginSystem.PATIENT_CREDENTIALS):
            QMessageBox.warning(self.create_account_dialog, "Error", "Username already exists!")
            return
            
        # Add new patient credentials
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
        
        # Check admin credentials
        if (username == LoginSystem.ADMIN_CREDENTIALS["username"] and 
            password == LoginSystem.ADMIN_CREDENTIALS["password"]):
            self.open_admin_dashboard()
            self.login_dialog.close()
            return
            
        # Check patient credentials
        for patient in LoginSystem.PATIENT_CREDENTIALS:
            if (username == patient["username"] and 
                password == patient["password"]):
                self.open_patient_dashboard()
                self.login_dialog.close()
                return
                
        # If no match found
        QMessageBox.warning(self.login_dialog, "Login Failed", "Invalid username or password!")
    
    def open_admin_dashboard(self):
        self.admin_window = QtWidgets.QMainWindow()
        self.admin_ui = AdminDashboardUI()
        self.admin_ui.setupUi(self.admin_window)
        self.admin_window.show()
        self.close()
    
    def open_patient_dashboard(self):
        if self.patient_window is None:
            self.patient_window = QtWidgets.QMainWindow()
            self.patient_ui = PatientDashboardUI()
            self.patient_ui.setupUi(self.patient_window)
            
            # Connect buttons in patient dashboard
            if hasattr(self.patient_ui, 'take_appoint'):
                self.patient_ui.take_appoint.clicked.connect(self.open_patient_appointment_form)
            if hasattr(self.patient_ui, 'home'):
                self.patient_ui.home.clicked.connect(self.open_main_page)
            if hasattr(self.patient_ui, 'doc_sch'):
                self.patient_ui.doc_sch.clicked.connect(self.open_patient_doctor_schedule)
            
            self.patient_window.destroyed.connect(lambda: setattr(self, 'patient_window', None))
        
        self.patient_window.show()
        self.close()
    
    def open_patient_appointment_form(self):
        """Open the patient appointment form"""
        if self.appointment_dialog is None:
            self.appointment_dialog = QtWidgets.QDialog(self.patient_window)
            self.appointment_ui = patient_appoint_form.Ui_Dialog()
            self.appointment_ui.setupUi(self.appointment_dialog)
            
            # Connect buttons in appointment form
            if hasattr(self.appointment_ui, 'pushButton_2'):
                self.appointment_ui.pushButton_2.clicked.connect(self.open_mailing)
            if hasattr(self.appointment_ui, 'home'):
                self.appointment_ui.home.clicked.connect(self.open_main_page)
            
            self.appointment_dialog.finished.connect(lambda: setattr(self, 'appointment_dialog', None))
        
        self.appointment_dialog.exec()
    
    def open_mailing(self):
        """Open the mailing window"""
        if self.mailing_window is None:
            self.mailing_window = mailing.AppointmentUI()
            self.mailing_window.destroyed.connect(lambda: setattr(self, 'mailing_window', None))
        
        self.mailing_window.show()
    
    def open_main_page(self):
        """Open the main page"""
        self.main_window = MainWindow()
        self.main_window.show()
        
        if self.patient_window:
            self.patient_window.close()
        if self.appointment_dialog:
            self.appointment_dialog.close()
    
    def open_patient_doctor_schedule(self):
        """Open the doctor schedule window for patients"""
        if self.doctor_schedule_window is None:
            self.doctor_schedule_window = QtWidgets.QMainWindow(self.patient_window)
            self.doctor_schedule_ui = pat_doc_sch.Ui_MainWindow()
            self.doctor_schedule_ui.setupUi(self.doctor_schedule_window)
            self.doctor_schedule_window.destroyed.connect(lambda: setattr(self, 'doctor_schedule_window', None))
        
        self.doctor_schedule_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())