@echo off
chcp 65001 >nul
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
 py -3 download_real_photos.py
) else (
 python download_real_photos.py
)
echo.
echo Da hoan tat. Mo index.html de xem web.
pause
