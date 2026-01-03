@echo off
REM Batch script to run the Todo application with proper Python path
set PYTHONPATH=%~dp0src;%PYTHONPATH%
python src/main.py %*