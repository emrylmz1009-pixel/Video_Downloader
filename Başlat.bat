@echo off
chcp 65001 >nul
title AI Universal Video Downloader
cd /d "%~dp0"
 
echo ==================================================
echo        AI Universal Video Downloader
echo ==================================================
echo.
 
rem --- Dosya kontrolleri ---
if not exist "video_indirici.py" goto :nofile
if not exist "requirements.txt" goto :nofile
 
rem --- Python bulma ---
set "PY="
where py >nul 2>nul && set "PY=py"
if not defined PY where python >nul 2>nul && set "PY=python"
if not defined PY goto :nopython
 
rem --- Daha önce kurulum yapıldıysa doğrudan başlat ---
if exist ".kurulum_tamam" goto :run
 
echo [1/2] Gerekli kütüphaneler kuruluyor, lütfen bekleyin...
echo.
%PY% -m pip install --upgrade pip
%PY% -m pip install -r requirements.txt
if errorlevel 1 goto :pipfail
 
echo kurulum tamamlandi> ".kurulum_tamam"
echo.
echo Kurulum tamamlandı!
echo.
 
:run
echo [2/2] Program başlatılıyor...
%PY% video_indirici.py
if errorlevel 1 goto :apperr
exit /b 0
 
:nofile
echo HATA: video_indirici.py veya requirements.txt bulunamadı.
echo Bu BAT dosyasını diğer proje dosyalarıyla aynı klasöre koyun.
echo.
pause
exit /b 1
 
:nopython
echo HATA: Python bulunamadı.
echo Python'u https://www.python.org/downloads/ adresinden indirin.
echo Kurulum sırasında "Add Python to PATH" kutusunu işaretlemeyi unutmayın.
echo.
pause
exit /b 1
 
:pipfail
echo.
echo HATA: Kütüphaneler kurulamadı. İnternet bağlantınızı kontrol edip tekrar deneyin.
echo.
pause
exit /b 1
 
:apperr
echo.
echo Program bir hata ile kapandı. Yukarıdaki hata mesajını kontrol edin.
echo Sorun devam ederse kütüphaneleri güncellemek için ".kurulum_tamam" dosyasını silip BAT dosyasını tekrar çalıştırın.
echo.
pause
exit /b 1
 
