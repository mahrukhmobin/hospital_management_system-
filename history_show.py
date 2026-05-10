from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow

import sys

class PatientHistoryDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        
    def setup_ui(self):
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        # Connect the Next button to check patient info
        self.ui.pushButton.clicked.connect(self.check_patient_info)
        
    def check_patient_info(self):
        cnic = self.ui.CNIC.text().strip()
        
        # Check which report to show based on CNIC
        if cnic == "34101-5627962-9":
            self.show_report(report_history1o.Ui_MainWindow)
        elif cnic == "35202-1844423-8":
            self.show_report(report_history2.Ui_MainWindow)
        elif cnic == "16102-4678644-7":
            self.show_report(report_history3.Ui_MainWindow)
        elif cnic == "16102-1980230-3":
            self.show_report(report_history4.Ui_MainWindow)
        elif cnic == "34101-8756559-5":
            self.show_report(report_history5.Ui_MainWindow)
        elif cnic == "61101-6112880-6":
            self.show_report(report_history6.Ui_MainWindow)
        elif cnic == "34104-5776710-2":
            self.show_report(report_history7.Ui_MainWindow)
        elif cnic == "16102-9155649-0":
            self.show_report(report_history8.Ui_MainWindow)
        elif cnic == "34101-6320447-8":
            self.show_report(report_history9.Ui_MainWindow)
        elif cnic == "16102-7414513-3":
            self.show_report(report_history10.Ui_MainWindow)
        elif cnic == "33101-8435316-9":
            self.show_report(report_history11.Ui_MainWindow)
        elif cnic == "35202-3676515-3":
            self.show_report(report_history12.Ui_MainWindow)
        elif cnic == "16102-1881353-9":
            self.show_report(report_history13.Ui_MainWindow)
        elif cnic == "54401-4680649-1":
            self.show_report(report_history14.Ui_MainWindow)
        elif cnic == "54401-9977705-7":
            self.show_report(report_history15.Ui_MainWindow)
        elif cnic == "34104-4483363-2":
            self.show_report(report_history16.Ui_MainWindow)
        elif cnic == "34104-5870662-0":
            self.show_report(report_history17.Ui_MainWindow)
        elif cnic == "35202-3664059-5":
            self.show_report(report_history18.Ui_MainWindow)
        elif cnic == "42101-4929403-3":
            self.show_report(report_history19.Ui_MainWindow)
        elif cnic == "42101-9727307-4":
            self.show_report(report_history20.Ui_MainWindow)
        else:
            QtWidgets.QMessageBox.warning(self, "Not Found", "No report found for this CNIC")
    
    def show_report(self, report_class):
        self.report_window = QMainWindow()
        self.report_ui = report_class()
        self.report_ui.setupUi(self.report_window)
        self.report_window.show()
        self.close()

if __name__ == "__main__":
    # Import the UI files
    from pat_his_log import Ui_Dialog
    import report_history1o
    import report_history2
    import report_history3
    import report_history3
    import report_history4
    import report_history5
    import report_history6
    import report_history7
    import report_history8
    import report_history9
    import report_history10
    import report_history11
    import report_history12
    import report_history13
    import report_history14
    import report_history15
    import report_history16
    import report_history17
    import report_history18
    import report_history19
    import report_history20
    
    app = QtWidgets.QApplication(sys.argv)
    
    # Create and show the patient login dialog
    dialog = PatientHistoryDialog()
    dialog.show()
    
    sys.exit(app.exec())



