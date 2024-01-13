import serial
import serial.tools.list_ports

from PyQt6.QtWidgets import (
    QDialog
)
from .SerialPortConfiguratorGUI import Ui_Dialog

class SerialPortConfigWindow(QDialog, Ui_Dialog):
    # Configuration options
    __baudRateOptions = ("75", "110", "300", "1200", "2400", "4800", "9600", "19200", "38400", "57600", "115200")
    __dataBitsOptions = ("5", "6", "7", "8")
    __stopBitsOptions = ("1","1.5","2")
    __parityOptions = {"None (N)":'N', "Odd (O)":'O', "Even (E)":'E', "Mark (M)":'M', "Space (S)":'S'}
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # Instance Attributes
        self.selectedComPortName = ""
        self.selectedBaud = "9600"
        self.selectedDataBits = "8"
        self.selectedParity = "N"
        self.selectedStopBits = "1"
        self.softwareFlowCtrl = False
        self.rtsCts = False
        self.dsrDtr = False
        
        # Setup configs
        self.__setupGUIValues()
        self.__loadConfig()
        
        # Setup GUI Signals
        self.bbConfirm.accepted.connect(self.__saveConfig)
        self.pbUpdatePorts.clicked.connect(self.__updateSerialList)
        
    # Adds all configuration options to GUI
    def __setupGUIValues(self):
        for comport in serial.tools.list_ports.comports():
            self.comboBox_Port.addItem(comport.name.strip("\r\n"))
        for baud in self.__baudRateOptions:
            self.comboBox_Baud.addItem(baud)
        for dataBits in self.__dataBitsOptions:
            self.comboBox_DataBits.addItem(dataBits)
        for parity in self.__parityOptions.keys():
            self.comboBox_Parity.addItem(parity)
        for stopBits in self.__stopBitsOptions:
            self.comboBox_StopBits.addItem(stopBits)
            
    # loads configuration options to display on GUI
    def __loadConfig(self):
        self.comboBox_Port.setCurrentText(self.selectedComPortName)
        self.comboBox_Baud.setCurrentText(self.selectedBaud)
        self.comboBox_DataBits.setCurrentText(self.selectedDataBits)
        self.comboBox_Parity.setCurrentText(self.selectedParity)
        self.comboBox_StopBits.setCurrentText(self.selectedStopBits)
        self.checkBox_SoftwareFlowCtrl.setChecked(self.softwareFlowCtrl)
        self.checkBox_RtsCts.setChecked(self.rtsCts)
        self.checkBox_DsrDtr.setChecked(self.dsrDtr)
        
    # Slot function, saves selected configuration options
    def __saveConfig(self):
        self.selectedComPortName = self.comboBox_Port.currentText()
        self.selectedBaud = self.comboBox_Baud.currentText()
        self.selectedDataBits = self.comboBox_DataBits.currentText()
        self.selectedParity = self.comboBox_Parity.currentText()
        self.selectedStopBits = self.comboBox_StopBits.currentText()
        self.softwareFlowCtrl = self.checkBox_SoftwareFlowCtrl.isChecked()
        self.rtsCts = self.checkBox_RtsCts.isChecked()
        self.dsrDtr = self.checkBox_DsrDtr.isChecked()
    
    # Slot function, refreshes serial port list on GUI
    def __updateSerialList(self, event):
        self.comboBox_Port.clear()
        for comport in serial.tools.list_ports.comports():
            self.comboBox_Port.addItem(comport.name.strip("\r\n"))
        self.comboBox_Port.setCurrentText(self.selectedComPortName)
        
    # Returns serial port object as configured
    def configuredSerialPort(self):
        configuredSP = serial.Serial()
        configuredSP.port = self.selectedComPortName
        configuredSP.baudrate = int(self.selectedBaud)
        configuredSP.bytesize = int(self.selectedDataBits)
        configuredSP.parity = self.__parityOptions[self.selectedParity]
        configuredSP.stopbits = int(self.selectedStopBits)
        configuredSP.xonxoff = self.softwareFlowCtrl
        configuredSP.rtscts = self.rtsCts
        configuredSP.dsrdtr = self.dsrDtr
        return configuredSP
    
    