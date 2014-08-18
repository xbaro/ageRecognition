@echo off
REM This is the developer setup script for windows.
REM We assume you installed python in C:\Python27
SET PYTHON=C:\Python27
REM Skip following two steps to match docs: https://github.com/codalab/codalab/wiki/Dev:-Getting-Started-on-Windows
REM %PYTHON%\Scripts\easy_install pip
REM %PYTHON%\Scripts\pip install virtualenv
REM Create the virtual environment named venv
%PYTHON%\Scripts\virtualenv --clear venv
REM Activate the virtual environment
CALL venv\Scripts\activate.bat
REM Update pip and distribute in venv
pip install --upgrade distribute
REM Install development requirements
pip install -r ageRecognition\requirements\common.txt
ECHO "One time setup is complete. You are ready to proceed."
