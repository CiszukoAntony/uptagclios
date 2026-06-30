@echo off
chcp 65001 >nul
for /F "tokens=1,2 delims=#" %%a in ('"prompt $H#$E# & echo on & for %%b in (1) do rem"') do set "ESC=%%b"
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
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo %BLUE%============================================================%RESET%
    echo %RED%[ALERTA] %CYAN%Python%RESET% %RED%no está instalado en este equipo.%RESET%
    echo %BLUE%============================================================%RESET%
    echo Para ejecutar UPTAG CLI OS se requiere instalar %CYAN%Python%RESET%.
    echo.
    echo %WHITE%[1] Intentar instalar %CYAN%Python%RESET% automáticamente usando Winget%RESET%
    echo %WHITE%[2] Abrir la página oficial de descargas de %CYAN%Python%RESET% en el navegador%RESET%
    echo %WHITE%[3] Cancelar y salir%RESET%
    echo %BLUE%============================================================%RESET%
    choice /c 123 /n /m "Seleccione una opción [1, 2 o 3]: "
    
    if errorlevel 3 (
        echo Cancelando instalación y saliendo...
        timeout /t 3 >nul
        exit /b 1
    )
    if errorlevel 2 (
        echo Abriendo navegador en %CYAN%python.org%RESET%...
        start https://www.python.org/downloads/
        echo Instale %CYAN%Python%RESET% y vuelva a ejecutar este archivo.
        pause
        exit /b 1
    )
    if errorlevel 1 (
        echo %CYAN%Iniciando instalador automático...%RESET%
        echo.
        echo %YELLOW%[NOTA] Se solicitará confirmación de administrador de Windows si es necesario.%RESET%
        winget install --id Python.Python.3.12 --exact --accept-package-agreements --accept-source-agreements
        if errorlevel 1 (
            echo.
            echo %RED%[ERROR] La instalación automática de %CYAN%Python%RESET% %RED%falló o fue cancelada.%RESET%
            echo Abriendo la página de descargas en el navegador para instalación manual...
            start https://www.python.org/downloads/
            pause
            exit /b 1
        ) else (
            echo.
            echo %GREEN%[ÉXITO] %CYAN%Python%RESET% %GREEN%se instaló correctamente.%RESET%
            echo Por favor, cierre esta ventana y vuelva a ejecutar %CYAN%run_uptagclios_python.bat%RESET% para iniciar.
            pause
            exit /b 0
        )
    )
)

echo %GREEN%[ERES UN EXITOSO]%RESET% %CYAN%Python%RESET% %WHITE%detectado correctamente en el sistema.%RESET%
echo %WHITE%Iniciando UPTAG CLI OS...%RESET%
timeout /t 3 >nul
start python python/main.py
exit