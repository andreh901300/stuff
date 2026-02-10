@echo off
echo Installing required Python packages...
echo --------------------------------------
echo Note: This may require administrator privileges. If errors occur, run as admin or add --user flag manually.
echo.

REM Upgrade pip first
python -m pip install --upgrade pip || (
    echo [!] Failed to upgrade pip. Continuing...
)

REM Install dependencies
python -m pip install pypiwin32 || (
    echo [!] Warning: pypiwin32 installation failed. Try running as admin.
)

python -m pip install pycryptodome || (
    echo [!] Warning: pycryptodome installation failed.
)

python -m pip install pyinstaller || (
    echo [!] Warning: pyinstaller installation failed. Install manually with:
    echo     python -m pip install pyinstaller
)

python -m pip install requests || (
    echo [!] Warning: requests installation failed.
)

echo.
echo --------------------------------------
echo Installation complete! Check for any warnings above.
echo If issues persist, ensure Python is in your PATH and try:
echo     python -m pip install --user [package]
echo.
echo If that didn't work, contact mystixx.dev on Discord,
echo tell me your error and send a screenshot if possible.
echo --------------------------------------
pause
