


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1288, 1036)
        Dialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1288, 81))
        self.widget.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(33, 48, 145, 255), stop:1 rgba(243, 243, 243, 255));\n"
"\n"
"border:none")
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_10 = QtWidgets.QLabel(parent=Dialog)
        self.label_10.setGeometry(QtCore.QRect(930, -50, 361, 191))
        self.label_10.setStyleSheet("\n"
"background:none;\n"
"border:none")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("C:/Users/Hp/OneDrive/Desktop/images for hms/logo-removebg-preview.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.home = QtWidgets.QPushButton(parent=Dialog)
        self.home.setGeometry(QtCore.QRect(420, 12, 77, 101))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(25)
        font.setBold(True)
        self.home.setFont(font)
        self.home.setStyleSheet("border:none;\n"
"color: rgb(0, 0, 0);\n"
" background-color:none")
        self.home.setObjectName("home")
        self.pat_dash = QtWidgets.QPushButton(parent=Dialog)
        self.pat_dash.setGeometry(QtCore.QRect(40, 2, 261, 121))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(25)
        font.setBold(True)
        self.pat_dash.setFont(font)
        self.pat_dash.setStyleSheet("border:none;\n"
"color: rgb(0, 0, 0);\n"
" background-color:none")
        self.pat_dash.setObjectName("pat_dash")
        self.widget_2 = QtWidgets.QWidget(parent=Dialog)
        self.widget_2.setGeometry(QtCore.QRect(290, 80, 681, 651))
        self.widget_2.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setGeometry(QtCore.QRect(90, 50, 461, 101))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setStyleSheet("background:none")
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(parent=self.widget_2)
        self.layoutWidget.setGeometry(QtCore.QRect(100, 280, 151, 161))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_2.setStyleSheet("background:none")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(parent=self.layoutWidget)
        self.label_3.setStyleSheet("background:none")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.widget_2)
        self.layoutWidget1.setGeometry(QtCore.QRect(300, 260, 271, 201))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pat_name = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.pat_name.setObjectName("pat_name")
        self.verticalLayout.addWidget(self.pat_name)
        self.CNIC = QtWidgets.QLineEdit(parent=self.layoutWidget1)
        self.CNIC.setObjectName("CNIC")
        self.verticalLayout.addWidget(self.CNIC)
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(470, 500, 75, 24))
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background:rgb(27, 39, 118);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.home.setText(_translate("Dialog", "Home"))
        self.pat_dash.setText(_translate("Dialog", "Patient\'s Dashboard"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700; font-style:italic; color:#1b2776;\">Patient\'s History </span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#1b2776;\">Patient\'s Name</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:700; color:#1b2776;\">Patients\'s  CNIC </span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Next"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
