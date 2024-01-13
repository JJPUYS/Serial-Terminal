# Form implementation generated from reading ui file 'SerialTerminalGUI.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 379)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("terminalIcon.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.togglePort = QtWidgets.QPushButton(parent=self.centralwidget)
        self.togglePort.setGeometry(QtCore.QRect(110, 10, 80, 24))
        self.togglePort.setCheckable(True)
        self.togglePort.setObjectName("togglePort")
        self.configurePort = QtWidgets.QPushButton(parent=self.centralwidget)
        self.configurePort.setGeometry(QtCore.QRect(10, 10, 90, 24))
        self.configurePort.setCheckable(False)
        self.configurePort.setObjectName("configurePort")
        self.txData = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.txData.setEnabled(False)
        self.txData.setGeometry(QtCore.QRect(10, 350, 500, 22))
        self.txData.setObjectName("txData")
        self.rxData = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.rxData.setEnabled(False)
        self.rxData.setGeometry(QtCore.QRect(10, 40, 580, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rxData.sizePolicy().hasHeightForWidth())
        self.rxData.setSizePolicy(sizePolicy)
        self.rxData.setAutoFillBackground(False)
        self.rxData.setFrameShape(QtWidgets.QFrame.Shape.Panel)
        self.rxData.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.rxData.setObjectName("rxData")
        self.sendTxData = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sendTxData.setEnabled(False)
        self.sendTxData.setGeometry(QtCore.QRect(520, 350, 70, 24))
        self.sendTxData.setObjectName("sendTxData")
        self.feedbackDisplay = QtWidgets.QLabel(parent=self.centralwidget)
        self.feedbackDisplay.setGeometry(QtCore.QRect(200, 10, 390, 24))
        self.feedbackDisplay.setText("")
        self.feedbackDisplay.setObjectName("feedbackDisplay")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial Terminal"))
        self.togglePort.setText(_translate("MainWindow", "Open Port"))
        self.configurePort.setText(_translate("MainWindow", "Configure Port"))
        self.rxData.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:\'Segoe UI\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.sendTxData.setText(_translate("MainWindow", "Send"))