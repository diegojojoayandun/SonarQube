# Instalación de SonarQube

## Opción 1: PowerShell

1. Ejecuta PowerShell como administrador
2. Pega el siguiente comando:

   ```powershell
   Set-ExecutionPolicy Bypass -Scope Process -Force
   .\install_sonar.ps1

   ```

3. Ingresa mediante http://localhost:9000

## Opción 2: Python

### Prerrequisitos:

- **Python 3.x**
- **pip**:
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

## Opción 3: DOCKER

### Prerrequisitos:

- **docker**

1. Ejecuta PowerShell como administrador
2. Pega el siguiente comando:

   ```powershell
   docker-compose up -d

   ```

3. accede a SonarQube http://localhost:9000
