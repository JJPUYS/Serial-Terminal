ECHO OFF
@REM ECHO Generating pyQt Files
pyinstaller serialTerminal.spec --noconfirm
@REM ECHO Finished Generating pyQt Files
PAUSE