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
import ad_doc_sch
import ad_pat_record
import history_show

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
        
        # Connect the login button to open the login dialog
        self.ui.pushButton.clicked.connect(self.open_login_dialog)
        
    def open_login_dialog(self):
        self.login_dialog = QtWidgets.QDialog()
        self.login_ui = LoginPageUI()
        self.login_ui.setupUi(self.login_dialog)
        
        # Connect login button in the login dialog
        self.login_ui.pushButton.clicked.connect(self.attempt_login)
        
        # Connect "Create one" button to open account creation
        self.login_ui.create_one.clicked.connect(self.open_create_account)
        
        self.login_dialog.exec()
    
    def open_create_account(self):
        self.create_account_dialog = QtWidgets.QDialog()
        self.create_ui = CreateAccountUI()
        self.create_ui.setupUi(self.create_account_dialog)
        
        # Connect OK button to create account
        self.create_ui.ok.accepted.connect(self.create_new_account)
        
        self.login_dialog.close()  # Close login dialog
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
        self.open_login_dialog()  # Return to login screen
    
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
        
        # Connect buttons in admin dashboard
        self.admin_ui.doc_sch.clicked.connect(self.open_doctor_schedule)
        self.admin_ui.home.clicked.connect(self.open_history_show)
        self.admin_ui.about.clicked.connect(self.open_patient_records)
        
        self.admin_window.show()
        self.close()  # Close the main window
    
    def open_patient_dashboard(self):
        self.patient_window = QtWidgets.QMainWindow()
        self.patient_ui = PatientDashboardUI()
        self.patient_ui.setupUi(self.patient_window)
        self.patient_window.show()
        self.close()  # Close the main window
    
    def open_doctor_schedule(self):
        """Open the doctor schedule window"""
        self.doctor_schedule_window = QtWidgets.QMainWindow()
        self.doctor_schedule_ui = ad_doc_sch.Ui_MainWindow()
        self.doctor_schedule_ui.setupUi(self.doctor_schedule_window)
        self.doctor_schedule_window.show()
    
    def open_history_show(self):
        """Open the patient history window"""
        self.history_dialog = QtWidgets.QDialog()
        self.history_ui = history_show.PatientHistoryDialog()
        self.history_ui.show()
    
    def open_patient_records(self):
        """Open the patient records window"""
        self.patient_records_window = QtWidgets.QMainWindow()
        self.patient_records_ui = ad_pat_record.AdminPatientCheck()
        self.patient_records_ui.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Create and show the main window
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())

