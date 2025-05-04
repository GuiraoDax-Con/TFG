#Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
python.exe -m pip install --upgrade pip

# Comprueba si el entrono virtual ya existe
$answer
if (Test-Path -Path ".\La_guarida_del_DM") {
    Write-Host "Entrando al entorno virtual 'La_guarida_del_DM'."
    $answer = "n"
} else {
    Write-Host "Creando el entorno virtual 'La_guarida_del_DM'."
    
    # Crear entorno virtual con el nombre "La_guaridad_del_DM"
    python.exe -m venv La_guarida_del_DM

    $answer = "y"
}

# Activar el entorno virtual
.\La_guarida_del_DM\Scripts\Activate.ps1

if ($answer -eq "y") {
    # Instalar las librerías necesarias
    python.exe -m pip install -r .\backend\requirements.txt
    Write-Host "fastapi y uvicorn han sido instalados."
} elseif ($answer -eq "n") {
    Write-Host "Instalación de fastapi y uvicorn omitida."
} else {
    Write-Host "Valor de 'answer' no válido. Por favor, asegúrate de que sea 'y' o 'n'."
}

uvicorn backend.api.main:app --reload