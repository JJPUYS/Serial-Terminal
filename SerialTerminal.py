import serial
import serial.tools.list_ports

import sys, os, time
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QObject, QThread, pyqtSignal, QTimer
from PyQt6.QtGui import QIcon

from SerialTerminalGUI import Ui_MainWindow as Ui_SerialTerminalGUI
from SerialPortConfigurator.SerialPortConfiguratorClass import SerialPortConfigWindow

basedir = os.path.dirname(__file__)

try:
    from ctypes import windll  # Only exists on Windows.
    # arbitrary string so we can set the windows taskbar icon
    myappid = 'mycompany.myproduct.subproduct.version'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
except ImportError:
    pass



# Global serial port
serialPort = serial.Serial()
        
# Main window class
# sets up GUI using files generated from QT Designer .ui Files
class Window(QMainWindow, Ui_SerialTerminalGUI):
    sig_closePort = pyqtSignal()
    sig_newTxData = pyqtSignal(str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.spConfig = SerialPortConfigWindow(self)
        
        # Setup Local GUI Slots
        self.configurePort.clicked.connect(self.openSerialPortConfig)
        self.togglePort.clicked.connect(self.toggleSerialPort)
        self.sendTxData.clicked.connect(self.updateTx)
        
        # Setup serial worker thread
        self.workerThread = QThread()
        self.worker = SerialPortWorker()
        self.worker.moveToThread(self.workerThread)
        
        # Setup Signals and Slots between main window and serial worker thread
        self.workerThread.started.connect(self.worker.setupWorker)
        self.worker.sig_portOpen.connect(self.openSerialUpdate)
        self.worker.sig_portClosed.connect(self.closeSerialUpdate)
        self.worker.sig_newRxData.connect(self.updateRx)
        self.worker.sig_DisplayFeedback.connect(self.updateFeedbackDisplay)
        self.sig_closePort.connect(self.worker.closePort)
        self.sig_newTxData.connect(self.worker.writeSerialPort)
        
    # Slot function, toggles visibility of serial port config dialog
    def openSerialPortConfig(self):
        global serialPort
        if self.spConfig.isVisible():
            self.spConfig.hide()
        else:
            self.spConfig.show()
            if serialPort.is_open:
                self.sig_closePort.emit()
            
    
    # Slot function, toggles serial port state
    def toggleSerialPort(self):
        global serialPort
        if  serialPort.is_open:
            self.sig_closePort.emit()
        else:
            if self.spConfig.selectedComPortName != "":
                self.feedbackDisplay.clear()
                serialPort = self.spConfig.configuredSerialPort()
                self.workerThread.start() 
            else:
                self.feedbackDisplay.setText("Serial Port not configured!")
                self.togglePort.setChecked(False)
    
    # Slot function, updates GUI when serial port is successfully opened
    def openSerialUpdate(self):
        self.togglePort.setText("Close Port")
        self.togglePort.setChecked(True)
        self.txData.setEnabled(True)
        self.txData.clear()
        self.rxData.setEnabled(True)
        self.rxData.clear()
        self.sendTxData.setEnabled(True)
        
    # Slot function, updates GUI when serial port is successfully closed
    def closeSerialUpdate(self):
        self.workerThread.quit()
        self.togglePort.setText("Open Port")
        self.togglePort.setChecked(False)
        self.txData.setEnabled(False)
        self.rxData.setEnabled(False)
        self.sendTxData.setEnabled(False)
        
    # Slot function, updates GUI RxData
    def updateRx(self, newText):
        self.rxData.append(newText)
        
    # Slot function, signals serial worker to send TX data and update GUI
    def updateTx(self):
        self.sig_newTxData.emit(self.txData.text())
        self.txData.clear()
        
    # Slot function, updates GUI feedback Display
    def updateFeedbackDisplay(self, feedbackText):
        self.feedbackDisplay.setText(feedbackText)
        
    # Slot function, override closeEvent function to ensure serial port gets closed properly before exit
    def closeEvent(self, event):
        global serialPort
        if serialPort.is_open:
            self.sig_closePort.emit()

# Background serial worker controlling the main serial port
class SerialPortWorker(QObject):
    sig_portOpen = pyqtSignal()
    sig_portClosed = pyqtSignal()
    sig_newRxData = pyqtSignal(str)
    sig_DisplayFeedback = pyqtSignal(str)

    # Slot function, setup worker and serial port 
    def setupWorker(self):
        global serialPort
        # attempts opening serial port, signals on success and starts read timer
        try:
            serialPort.open()
        except Exception as error:
            print("Failed to open serial Port\r\n", error)
            self.sig_DisplayFeedback.emit("Failed to open serial Port")
            return
        self.sig_portOpen.emit()
        # Setup serial port read timer
        self.readTimer=QTimer()
        self.readTimer.setInterval(10)
        self.readTimer.timeout.connect(self.readSerialPort)
        self.readTimer.start()
    
    # Slot function, reads and signals new data when available on serial port
    def readSerialPort(self):
        global serialPort
        if serialPort.in_waiting:
            self.sig_newRxData.emit(serialPort.read_all().decode())
 
    # Slot function, writes new data to serial port
    def writeSerialPort(self, txData = ""):
        global serialPort
        if serialPort.is_open:
            serialPort.write(txData.encode())

    # Slot function, stops read timer, attempts closing serial port and signals accordingly
    def closePort(self):
        global serialPort
        self.readTimer.stop()
        if serialPort.is_open:
            try:
                serialPort.close()
                self.sig_portClosed.emit()
            except Exception as error:
                print("Failed to close serial Port\r\n", error)
                self.sig_DisplayFeedback.emit("Failed to close serial Port")
        
# Main Function, Setup application, spawn main program window
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.setWindowIcon(QIcon(os.path.join(basedir, "icons", "terminalIcon.ico")))
    win.show()
    sys.exit(app.exec())
