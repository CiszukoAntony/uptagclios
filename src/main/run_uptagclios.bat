@echo off
chcp 65001 >nul

:: Método de asignación limpia para el carácter ESC (Evita bugs de variables no encontradas)
for /F %%A in ('"prompt $E & for %%B in (1) do rem"') do set "ESC=%%A"
set "RESET=%ESC%[0m"
set "WHITE=%ESC%[97m"
set "BLACK=%ESC%[30m"
set "GRAY=%ESC%[90m"
set "BLUE=%ESC%[34m"
set "RED=%ESC%[31m"
set "YELLOW=%ESC%[33m"
set "ORANGE=%ESC%[38;5;208m"
set "CYAN=%ESC%[36m"
set "MAGENTA=%ESC%[35m"
set "GREEN=%ESC%[32m"

cls
echo %RESET%============================================================%RESET%
echo            %ORANGE%UPTAG CLI OS VERSION CMD%RESET%
echo %RESET%============================================================%RESET%

:: Verificación inicial de Python
python --version >nul 2>&1
if %errorlevel% equ 0 goto :PYTHON_OK
goto :PYTHON_MISSING

:PYTHON_MISSING
echo %BLUE%============================================================%RESET%
echo %RED%[ALERTA] Python no está instalado en este equipo.%RESET%
echo %BLUE%============================================================%RESET%
echo Para ejecutar UPTAG CLI OS se requiere instalar Python.
echo.
echo %WHITE%[1] Intentar instalar Python automáticamente (Última versión estable)%RESET%
echo %WHITE%[2] Abrir la página oficial de descargas de Python en el navegador%RESET%
echo %WHITE%[3] Cancelar y salir%RESET%
echo %BLUE%============================================================%RESET%

choice /c 123 /n /m "Seleccione una opción [1, 2 o 3]: "
if errorlevel 3 goto :EXIT_CANCEL
if errorlevel 2 goto :OPEN_BROWSER
if errorlevel 1 goto :INSTALL_WINGET

:EXIT_CANCEL
echo Cancelando instalación y saliendo...
timeout /t 3 >nul
exit /b 1

:OPEN_BROWSER
echo Abriendo navegador en python.org...
start https://www.python.org/downloads/
echo Instale Python manualmente y vuelva a ejecutar este archivo (%~nx0).
pause
exit /b 1

:INSTALL_WINGET
echo %CYAN%Iniciando instalador automático...%RESET%
echo.
echo %YELLOW%[NOTA] Se solicitará confirmación de administrador de Windows si es necesario.%RESET%
:: ID genérico cambiado a 'Python.Python.3' para garantizar la descarga de la rama más reciente (3.13/3.14)
winget install --id Python.Python.3 --exact --accept-package-agreements --accept-source-agreements
if %errorlevel% neq 0 goto :INSTALL_ERROR

echo.
echo %GREEN%[ÉXITO] Python se instaló correctamente.%RESET%
echo %YELLOW%[IMPORTANTE] Windows requiere refrescar el entorno para mapear los nuevos comandos.%RESET%
echo Por favor, cierre por completo esta ventana y vuelva a abrir '%~nx0' para iniciar el sistema.
pause
exit /b 0

:INSTALL_ERROR
echo.
echo %RED%[ERROR] La instalación automática falló o fue cancelada.%RESET%
echo Abriendo la página de descargas en el navegador para instalación manual...
start https://www.python.org/downloads/
pause
exit /b 1

:PYTHON_OK
echo %GREEN%[ÉXITO]%RESET% %CYAN%Python%RESET% %WHITE%detectado correctamente en el sistema.%RESET%
echo %WHITE%Iniciando UPTAG CLI OS...%RESET%
timeout /t 2 >nul
:: CORRECCIÓN CRÍTICA DE RUTA: Se eliminó la carpeta virtual '\python' para apuntar al main.py real en el directorio raíz del script.
start "UPTAG CLI OS" /MAX /D "%~dp0" cmd /k "python main.py"
exit