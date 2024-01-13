# Serial Terminal
 
Serial Terminal created using pyQt6.
Program consists of a primary window for sending and displaying received data with an additional dialog for configuring the serial port used.
Serial port configuration dialog class can easily be reused in another application.

GUIs created using Qt Designer.
**compileSerialPortConfiguratorGUI.bat** and **compileSerialTerminalGUI.bat** scripts used for generating .py files from design files included in repo.
.ui files also included for editing.

Use requirement.txt file when creating python virtual environment.

Redistributable program can be generated using the **generateExecutable.bat** script, uses the serialTerminal.spec file.

Program icon, **terminalIcon.png**, generated using [Bing Image Creator]([https://](https://www.bing.com/images/create)).

[Null-modem emulator]([https://](https://sourceforge.net/projects/com0com/)) used to setup 2 connected serial ports for testing.


