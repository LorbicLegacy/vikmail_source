# -*- coding: utf-8 -*-

"""
name : VikMail - Emailer App
coder : Vikas Patel
twitter / linkedIn / github : vikaspatelp83

"""
# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

# import
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from tkinter import filedialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time


class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        aboutWindow.setObjectName("aboutWindow")
        aboutWindow.resize(400, 300)
        aboutWindow.setMinimumSize(QtCore.QSize(400, 300))
        aboutWindow.setMaximumSize(QtCore.QSize(401, 301))
        self.stylesheet =  """
        QLabel#image{
                background-image : url("images/image.png");
            }  
        QLabel#name{
                background-image : url("images/bg2.jpg");
                border : 2px dashed blue;
        }

        """
        self.name = QtWidgets.QLabel(aboutWindow)
        self.name.setGeometry(QtCore.QRect(60, 10, 268, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        self.name.setFont(font)
        self.name.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.name.setObjectName("name")
        self.label = QtWidgets.QLabel(aboutWindow)
        self.label.setGeometry(QtCore.QRect(10, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(11)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(aboutWindow)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 231, 16))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(10)
        font.setItalic(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.image = QtWidgets.QLabel(aboutWindow)
        self.image.setGeometry(QtCore.QRect(30, 140, 341, 141))
        self.image.setText("")
        self.image.setObjectName("image")
        self.label_3 = QtWidgets.QLabel(aboutWindow)
        self.label_3.setGeometry(QtCore.QRect(330, 260, 71, 20))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(aboutWindow)
        self.label_4.setGeometry(QtCore.QRect(330, 280, 61, 16))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(aboutWindow)
        aboutWindow.setStyleSheet(self.stylesheet)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        _translate = QtCore.QCoreApplication.translate
        aboutWindow.setWindowTitle(_translate("aboutWindow", "About the app"))
        aboutWindow.setWindowIcon(QtGui.QIcon('images/icon.png'))
        self.name.setText(_translate("aboutWindow", "**VikMail : Emailer App **"))
        self.label.setText(_translate("aboutWindow", "Developer:   Vikas Patel "))
        self.label_2.setText(_translate("aboutWindow", "At : www.github.com/vikaspatelp83"))
        self.label_3.setText(_translate("aboutWindow", "Version : 1.1"))
        self.label_4.setText(_translate("aboutWindow", "Build : 123"))


# *********************************
class Ui_VikMail(object):

    # used variables
    # ********************************
    file = "blank.txt"
    attachment = "blank.txt"
    email_user = ""         #sender account
    email_password = ""     #sender password
    email_send = ""         #reciever 
    subject_msg = ""            #subject
    body = ""               #email body

    # ui setup ************************
    
    def setupUi(self, VikMail):
        VikMail.setObjectName("VikMail")
        VikMail.resize(520, 351)
        VikMail.setMinimumSize(QtCore.QSize(520, 350))
        VikMail.setMaximumSize(QtCore.QSize(520, 351))
        #@@@@@@@@@@@@@@@@@@ stylesheet @@@@@@@@@@@@@
        self.stylesheet = """
            QWidget{
                background-image: url("images/bg2.jpg");
            }
            QWidget.QPlainTextEdit,QWidget.QLineEdit{
                background : clear;
                background-color: white;
                border : 2px solid black;
            }
            QPushButton#send_button{
                background : clear;
                background : qlineargradient(x1:1 y1:1, x2:0 y2:1, stop:0 lightblue, stop:1 wheat);
                text-transform: uppercase;
                color: darkslategray;
	            font-family : "halvatica";
                font-size : 20px;
                border-radius : 20%;
            }
            QPushButton#send_button:hover{
                border : .5px solid white;
                background : qlineargradient(x1:1 y1:1, x2:0 y2:0, stop:0 blue, stop:1 violet);
                color : wheat;
                font-size: 18px;
                font-weight: 100;
                font-style : bold;
            }
            QLabel#output_display,QLabel#attatchment_place {
                background : clear;
                background-image : url("images/namebg.jpg"); 
                border-radius : 10%;           
            } 
            QLabel#app_name,QLabel#developer_name{
                background : clear;
                background-image : url("images/namebg.jpg");
            }
            QLabel#app_name:hover,QLabel#developer_name:hover{
                color : blue;
            }
            QLabel#attatchment_place,QLabel#output_display{
                border : 1px solid darkslategray;
            }
            QPushButton#aboutApp,QPushButton#file_button{
                color: darkslategray;
                background : clear;
                background-color: white;
                font-size: 15px;
                border-radius : 10%;
            }
            QPushButton#aboutApp:hover,QPushButton#file_button:hover{
                border : .5px solid white;
                background : clear;
                background : qlineargradient(x1:1 y1:1, x2:0 y2:0, stop:0 blue, stop:1 violet);
                color : white;
                font-size: 16px;
                font-weight: 100;
            }
            QLineEdit#recipient_email,QPlainTextEdit#subject_place,QPlainTextEdit#plainTextEdit{
                border-radius : 10%;
                border : 2px solid darkslategray;
                background: qlineargradient( x1:0 y1:0, x2:1 y2:0, stop:0 wheat, stop:1 lightpink);
            }
        """

        self.centralwidget = QtWidgets.QWidget(VikMail)
        self.centralwidget.setMinimumSize(QtCore.QSize(520, 310))
        self.centralwidget.setMaximumSize(QtCore.QSize(520, 312))
        self.centralwidget.setObjectName("centralwidget")

        # recipient email field
        self.recipient_email = QtWidgets.QLineEdit(self.centralwidget)
        self.recipient_email.setGeometry(QtCore.QRect(110, 80, 181, 31))
        self.recipient_email.setObjectName("recipient_email")   
        font = QtGui.QFont()  
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.recipient_email.setFont(font)
        # subject field
        self.subject_place = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.subject_place.setGeometry(QtCore.QRect(110, 130, 401, 31))
        self.subject_place.setObjectName("subject_place")
        font = QtGui.QFont()  
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.subject_place.setFont(font)

        # message body
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(110, 170, 401, 91))
        self.plainTextEdit.setObjectName("plainTextEdit")
        font = QtGui.QFont()  
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)

        # label recipient
        self.recipient_lbl = QtWidgets.QLabel(self.centralwidget)
        self.recipient_lbl.setGeometry(QtCore.QRect(10, 80, 94, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recipient_lbl.setFont(font)
        self.recipient_lbl.setObjectName("recipient_lbl")

        # label subject
        self.subject_lbl = QtWidgets.QLabel(self.centralwidget)
        self.subject_lbl.setGeometry(QtCore.QRect(10, 140, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)      
        self.subject_lbl.setFont(font)
        self.subject_lbl.setObjectName("subject_lbl")

        # label message body
        self.message_lbl = QtWidgets.QLabel(self.centralwidget)
        self.message_lbl.setGeometry(QtCore.QRect(10, 200, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)   
        self.message_lbl.setFont(font)
        self.message_lbl.setObjectName("message_lbl")
        
        # label attatchment
        self.attatchment_lbl = QtWidgets.QLabel(self.centralwidget)
        self.attatchment_lbl.setGeometry(QtCore.QRect(10, 280, 111, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)      
        self.attatchment_lbl.setFont(font)
        self.attatchment_lbl.setObjectName("attatchment_lbl")

        # about button 
        self.aboutApp = QtWidgets.QPushButton(self.centralwidget)
        self.aboutApp.setGeometry(QtCore.QRect(440, 10, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.aboutApp.setFont(font)
        self.aboutApp.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.aboutApp.setObjectName("aboutApp")

        # output diaplay
        font = QtGui.QFont()
        font.setPointSize(15)
        self.output_display = QtWidgets.QLabel(self.centralwidget)
        self.output_display.setAlignment(QtCore.Qt.AlignCenter)
        self.output_display.setFont(font)
        self.output_display.setGeometry(QtCore.QRect(300, 40, 211, 81))
        self.output_display.setFrameShape(QtWidgets.QFrame.Box)
        self.output_display.setText("")
        self.output_display.setObjectName("output_display")

        # label appname
        self.app_name = QtWidgets.QLabel(self.centralwidget)
        self.app_name.setGeometry(QtCore.QRect(5, 10, 292, 30))
        font = QtGui.QFont()
        font.setFamily("NewRocker")
        font.setPointSize(18)        
        self.app_name.setFont(font)
        self.app_name.setObjectName("app_name")

        # label developer name        
        self.developer_name = QtWidgets.QLabel(self.centralwidget)
        self.developer_name.setGeometry(QtCore.QRect(5, 40, 292, 30))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(True)
        self.developer_name.setAlignment(QtCore.Qt.AlignCenter)
        self.developer_name.setFont(font)
        self.developer_name.setObjectName("developer_name")

        # file button
        self.file_button = QtWidgets.QPushButton(self.centralwidget)
        self.file_button.setGeometry(QtCore.QRect(250, 280, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)     
        self.file_button.setFont(font)
        self.file_button.setObjectName("file_button")
        self.file_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        # attatchment place
        self.attatchment_place = QtWidgets.QLabel(self.centralwidget)
        self.attatchment_place.setGeometry(QtCore.QRect(120, 280, 121, 21))
        self.attatchment_place.setFrameShape(QtWidgets.QFrame.Panel)
        self.attatchment_place.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.attatchment_place.setText("")
        self.attatchment_place.setObjectName("attatchment_place")

        # send button
        self.send_button = QtWidgets.QPushButton(self.centralwidget)
        self.send_button.setGeometry(QtCore.QRect(380, 270, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Lucida Handwriting")
        font.setPointSize(10)
        self.send_button.setFont(font)
        self.send_button.setAutoFillBackground(True)
        self.send_button.setAutoDefault(False)
        self.send_button.setDefault(False)
        self.send_button.setFlat(False)
        self.send_button.setObjectName("send_button") 
        self.send_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # other
        VikMail.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VikMail)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 520, 21))
        self.menubar.setObjectName("menubar")
        VikMail.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VikMail)
        self.statusbar.setObjectName("statusbar")
        VikMail.setStatusBar(self.statusbar)

        # retranslateui
        self.retranslateUi(VikMail)
        QtCore.QMetaObject.connectSlotsByName(VikMail)

    #********************************************************
        # main actions
       # print(self.file)

        self.centralwidget.setStyleSheet(self.stylesheet)
        self.file_button.clicked.connect(self.file_select)  
        self.output_display.setText(self.file)
       # print(self.file)
        self.login_info()
        self.send_button.clicked.connect(self.send_email)
       # about window
        self.aboutApp.clicked.connect(self.about_app)

        
    #*******************************************************
    def retranslateUi(self, VikMail):
        _translate = QtCore.QCoreApplication.translate
        VikMail.setWindowTitle(_translate("VikMail", "VikMail - Emailer App"))
        VikMail.setWindowIcon(QtGui.QIcon('images/icon.png'))
        self.app_name.setText(_translate("VikMail", "VIKMAIL - EMAILER APP"))
        self.developer_name.setText(_translate("VikMail", "Developed by Vikas Patel"))
        self.recipient_lbl.setText(_translate("VikMail", "Recipient Email"))
        self.subject_lbl.setText(_translate("VikMail", "Subject"))
        self.message_lbl.setText(_translate("VikMail", "Message Body"))
        self.attatchment_lbl.setText(_translate("VikMail", "Attatchment File"))
        self.file_button.setText(_translate("VikMail", "Add File"))
        self.send_button.setText(_translate("VikMail", "Send Mail"))
        self.aboutApp.setText(_translate("VikMail", "About"))


    # ******* MAIN FUNCTIONALITY RELATED METHODS *************
    def file_select(self):
        try:
            self.file = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
            self.attatchment_place.setText(self.file)
            if self.file == "":
                self.file = "blank.txt"
        except Exception as e:
            self.file = "blank.txt"
        #self.open_file(self.file)
    
    def open_file(self,file_name):
        try:
            self.attachment  = open(file_name,'rb')
        except Exception as e:
            self.attachment = "blank.txt"
       # print(self.attachment)
        self.attatchment_place.setText(file_name)


    def login_info(self):
        file = open("loginfile.txt","r")
        login = []
        for line in file:
            login.append(line)
        file.close()
        self.email_user = login[0]
        self.email_password = login[1]
       # print(login)

    def read_data(self):

        self.email_send = self.recipient_email.text()
        self.subject_msg = self.subject_place.toPlainText()
        self.body = self.plainTextEdit.toPlainText()

       # print(self.email_send)
       # print(self.subject_msg)
       # print(self.body)


    def send_email(self):

        self.read_data()
        self.output_display.setText("Starting ")
        email_user = self.email_user                #sender account
        email_password = self.email_password        #sender password
        email_send = self.email_send                #receiver account
        subject = self.subject_msg
        body = self.body
        attachment = open(self.file,"rb")
        
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'plain'))

        print(attachment.name)

        if attachment.name != "blank.txt":
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+attachment.name)
            msg.attach(part)
        else:
            part = MIMEBase('application','octet-stream')
            part.set_payload((attachment).read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition',"attachment; filename= "+"blank.txt")
            msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        self.output_display.setText("Starting Server...")
        server.starttls()
        self.output_display.setText("Logging in...")
        server.login(email_user,email_password)
        self.output_display.setText("Sending Email...")
        server.sendmail(email_user,email_send,text)
        self.output_display.setText("Email Sent")
        server.quit()

    def about_app(self):      
        aboutWindow.show()


# END OF THE FUNCTIONALITY CODING
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    VikMail = QtWidgets.QMainWindow()
    ui = Ui_VikMail()
    ui.setupUi(VikMail)
    ## tray icon


    # splash image #
    splash_image = QtGui.QPixmap("images/splash.png")
    splash = QtWidgets.QSplashScreen(splash_image,)
    splash.show()
    time.sleep(2)
    splash.hide()

    VikMail.show()

    app1 = QtWidgets.QApplication(sys.argv)
    aboutWindow = QtWidgets.QDialog()
    ui1 = Ui_aboutWindow()
    ui1.setupUi(aboutWindow)
    #aboutWindow.show()


    sys.exit(app.exec_())


