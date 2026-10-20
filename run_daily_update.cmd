@echo off
REM Daily: re-verify sources -> rebuild -> selfcheck -> deploy -> live check.
REM Called by scheduled task furadvisor-daily-update; safe to run by hand.
REM Keep this file pure ASCII: cmd.exe decodes batch files in the OEM codepage,
REM and non-ASCII text here gets mangled into broken commands.
REM Python writes docs\daily-update.log itself, so no redirection here
REM (redirecting would hold the file open and collide with Python's own write).

setlocal
cd /d "%~dp0"

set PY=python
where python >nul 2>nul
if errorlevel 1 set PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe

"%PY%" "%~dp0daily_update.py"
exit /b %ERRORLEVEL%
