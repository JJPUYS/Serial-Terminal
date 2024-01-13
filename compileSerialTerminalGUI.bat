ECHO OFF
ECHO Generating pyQt Files
pyuic6 -o SerialTerminalGUI.py SerialTerminalGUI.ui -d
ECHO Finished Generating pyQt Files
PAUSE