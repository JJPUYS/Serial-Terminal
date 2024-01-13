ECHO OFF
ECHO Generating pyQt Files
pyuic6 -o SerialPortConfiguratorGUI.py SerialPortConfiguratorGUI.ui -d
ECHO Finished Generating pyQt Files
PAUSE