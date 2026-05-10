from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import sys

class AppointmentUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi(r"C:/Users/Hp/OneDrive/Desktop/FINAL_HMS.ui/send_email.ui", self)

        # Connect the send button to the email function
        self.send.clicked.connect(self.send_email_confirmation)

    def send_email_confirmation(self):
        print("Send button clicked!")
        to_email = self.emailofpat.text().strip()
        datetime_info = self.emailtopat.toPlainText().strip()
        print(f"Email entered: {to_email}")
        print(f"Date/time entered: {datetime_info}")

        if not to_email or not datetime_info:
            print("Email address or date/time is missing.")
            return

        subject = "Appointment Confirmation"
        message = (
            f"Dear Patient,\n\n"
            f"Your appointment has been confirmed for {datetime_info}.\n\n"
            f"Regards,\nCardiology Department"
        )
        print("Calling send_email...")
        self.send_email(to_email, subject, message)

    def send_email(self, to_email, subject, message):
        sender_email = "mahnoorbalochxx@outlook.com"
        sender_password = "punjabian58"

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.attach(MIMEText(message, "plain"))

        try:
            server = smtplib.SMTP("smtp.office365.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)
            server.quit()
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppointmentUI()
    window.show()
    sys.exit(app.exec())
