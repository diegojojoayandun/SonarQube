import os
import subprocess
import requests
import zipfile
import shutil
import ctypes
import psutil

# Configuración
sonarqube_version = "10.2.1.78527"  # Cambia a la última versión disponible
download_url = f"https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-{sonarqube_version}.zip"
install_path = "C:\\SonarQube"
java_path = "C:\\Program Files\\Eclipse Adoptium\\jdk-17.0.13.11-hotspot"

# Verifica permisos de administrador
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0
    except:
        return False

if not is_admin():
    print("Este script debe ejecutarse como Administrador")
    exit()

# Instalar Chocolatey si no está instalado
def install_chocolatey():
    if shutil.which("choco") is None:
        print("Instalando Chocolatey...")
        subprocess.run(
            "Set-ExecutionPolicy Bypass -Scope Process -Force; "
            "[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; "
            "Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))",
            shell=True
        )

install_chocolatey()

# Instalar Java 17 si no está instalado
def install_java():
    if not os.path.exists(java_path):
        print("Instalando Java 17...")
        subprocess.run("choco install openjdk17 -y", shell=True)

install_java()

# Descargar SonarQube
def download_sonarqube():
    if not os.path.exists(install_path):
        print("Descargando SonarQube...")
        response = requests.get(download_url, stream=True)
        zip_path = os.path.join(os.environ["TEMP"], "sonarqube.zip")
        with open(zip_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall("C:\\")

        os.rename(f"C:\\sonarqube-{sonarqube_version}", install_path)
        print("SonarQube descargado y extraído.")

download_sonarqube()

# Configurar variables de entorno JAVA_HOME y SONAR_JAVA_PATH
def set_environment_variable(name, value):
    os.environ[name] = value
    subprocess.run(f'setx {name} "{value}" /M', shell=True)

print("Configurando JAVA_HOME y SONAR_JAVA_PATH...")
set_environment_variable("JAVA_HOME", java_path)
set_environment_variable("SONAR_JAVA_PATH", f"{java_path}\\bin\\java.exe")
set_environment_variable("Path", f"{java_path}\\bin")

# Iniciar SonarQube
def start_sonarqube():
    print("Iniciando SonarQube...")
    start_script = os.path.join(install_path, "bin", "windows-x86-64", "StartSonar.bat")
    if os.path.exists(start_script):
        subprocess.run(f'start /B {start_script}', shell=True)
        print("SonarQube iniciado. Accede a http://localhost:9000")
    else:
        print("No se encontró el script StartSonar.bat.")

start_sonarqube()
