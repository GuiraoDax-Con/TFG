# Save the current directory
$currentDir = Get-Location

# Change to the script directory
Set-Location -Path "/c:/Users/6003451/OneDrive - ViewNext/Documentos/GitHub/TFG/backend/"

# Execute the commands
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
uvicorn api.main:app --host 0.0.0.0 --port 8000 --ssl-keyfile key.pem --ssl-certfile cert.pem

# Restore the original directory
Set-Location -Path $currentDir