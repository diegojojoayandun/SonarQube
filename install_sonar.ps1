# Configuración
$sonarqubeVersion = "10.2.1.78527"  # Cambia a la última versión disponible
$downloadUrl = "https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-$sonarqubeVersion.zip"
$installPath = "C:\SonarQube"
$javaVersion = "jdk-17"
$javaPath = "C:\Program Files\Eclipse Adoptium\jdk-17.0.13.11-hotspot"

# Verifica permisos de administrador
if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Host "Este script debe ejecutarse como Administrador" -ForegroundColor Red
    exit
}

# Instalar Chocolatey si no está instalado
if (-not (Get-Command choco -ErrorAction SilentlyContinue)) {
    Write-Host "Instalando Chocolatey..."
    Set-ExecutionPolicy Bypass -Scope Process -Force
    [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
    Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
}

# Instalar Java 17 si no está instalado
if (-not (Test-Path $javaPath)) {
    Write-Host "Instalando Java 17..."
    choco install openjdk17 -y
}

# Descargar SonarQube
if (-not (Test-Path $installPath)) {
    Write-Host "Descargando SonarQube..."
    Invoke-WebRequest -Uri $downloadUrl -OutFile "$env:TEMP\sonarqube.zip"
    Expand-Archive -Path "$env:TEMP\sonarqube.zip" -DestinationPath "C:\"
    Rename-Item -Path "C:\sonarqube-$sonarqubeVersion" -NewName "SonarQube"
}

# Configurar JAVA_HOME
[System.Environment]::SetEnvironmentVariable("JAVA_HOME", $javaPath, [System.EnvironmentVariableTarget]::Machine)
$env:JAVA_HOME = $javaPath
$env:Path += ";$javaPath\bin"

# Iniciar SonarQube
Write-Host "Iniciando SonarQube..."
Start-Process -FilePath "$installPath\bin\windows-x86-64\StartSonar.bat" -NoNewWindow

Write-Host "Instalación completa. Accede a SonarQube en: http://localhost:9000" -ForegroundColor Green
