# Instalación de SonarQube

## Opción 1: Script de PowerShell

1. Ejecuta PowerShell como administrador
2. Pega el siguiente comando:

   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force
   .\install_sonar.ps1

   ```

3. Ingresa mediante http://localhost:9000

## Opción 2: Script en Python (Python 3 requerido)

### Prerrequisitos:

- Tener **Python 3.x** instalado y agregado a las variables de entorno del sistema.
- Asegurarte de que **pip** esté actualizado ejecutando el siguiente comando en la terminal de Windows (CMD o PowerShell):
  ```powershell
  python -m pip install --upgrade pip
  ```

1. Instala las dependencias necesarias:

   ```powershell
   pip install requests psutil

   ```

2. Ejecuta script:

   ```powershell
   python install_sonarqube.py

   ```

3. accede a SonarQube http://localhost:9000
