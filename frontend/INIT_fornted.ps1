# Script to initialize the Vue.js project

# Navigate to the project directory
$projectPath = "./frontend"
Set-Location -Path $projectPath

# Install dependencies
Write-Host "Installing dependencies..."
npm install

# Start the development server
Write-Host "Starting the development server..."
npm run dev

# Notify the user
Write-Host "Vue.js project has been started successfully."