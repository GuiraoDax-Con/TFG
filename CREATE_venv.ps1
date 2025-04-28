#Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
python.exe -m pip install --upgrade pip

# Crear entorno virtual con el nombre "La_guaridad_del_DM"
python.exe -m venv La_guarida_del_DM
# Activar el entorno virtual
.\La_guarida_del_DM\Scripts\Activate.ps1

# Preguntar al usuario si desea instalar fastapi y uvicorn
$answer
while ($answer -ne "y" -and $answer -ne "n") {
    $answer = Read-Host "¿Quieres instalar fastapi y uvicorn? (y/n)"
    if ($answer -eq "y") {
        # Instalar las librerías necesarias
        python.exe -m pip install -r .\backend\requirements.txt
        Write-Host "fastapi y uvicorn han sido instalados."
    } elseif ($answer -eq "n") {
        Write-Host "Instalación de fastapi y uvicorn omitida."
    } else {
        Write-Host "Entrada no válida. Por favor, ejecuta el script nuevamente."
    }
}




