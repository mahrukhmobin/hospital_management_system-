import sys
import os
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from email.message import EmailMessage
import smtplib

class AppointmentUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Try to load UI file
        try:
            ui_path = os.path.join(os.path.dirname(__file__), "send_email.ui")
            uic.loadUi(ui_path, self)
            print("UI loaded successfully")
        except Exception as e:
            print(f"Error loading UI file: {e}")
            sys.exit(1)
        
        # Verify UI elements exist
        try:
            self.send.clicked.connect(self.send_email_confirmation)
            print("UI elements found")
        except AttributeError as e:
            print(f"Missing UI element: {e}")
            sys.exit(1)

    def send_email_confirmation(self):
        print("Send button clicked!")
        try:
            to_email = self.emailofpat.text().strip()
            datetime_info = self.emailtopat.toPlainText().strip()
            print(f"Email: {to_email}, Date: {datetime_info}")
            
            if not to_email or not datetime_info:
                print("Missing information")
                return
                
            self.send_email(to_email, "Appointment Confirmation", 
                           f"Your appointment is confirmed for {datetime_info}")
        except Exception as e:
            print(f"Error in confirmation: {e}")

    def send_email(self, to_email, subject, message):
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = "ahmedzewail712@gmail.com"
            msg["To"] = to_email
            msg.set_content(message)

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login("ahmedzewail712@gmail.com", "olwc lmzg nhbl qxku")
                smtp.send_message(msg)
                print("Email sent successfully")
        except Exception as e:
            print(f"Email sending failed: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppointmentUI()
    window.show()
    sys.exit(app.exec())
    