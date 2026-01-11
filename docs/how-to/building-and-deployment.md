# Guía de Construcción y Despliegue

Esta guía práctica (How-to Guide) te acompaña paso a paso en la instalación, compilación y despliegue del Generador de QR WiFi. Combina instrucciones para Windows y Linux, asegurando un proceso fluido desde el código fuente hasta el ejecutable final.

## Instalación desde Código Fuente

### Requisitos Previos

#### Para Todos los Sistemas
- **Python 3.7 o superior**
- **Pip** (gestor de paquetes de Python)
- **Git** (para clonar el repositorio)

#### Verificación de Python
```bash
# Windows (PowerShell)
py --version

# Linux/macOS
python3 --version
```

### Instalación de Dependencias

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Reyes-1718/Generador-de-QR-Wifi.git
   cd Generador-de-QR-Wifi
   ```

2. **Instala las dependencias:**
   ```bash
   # Windows
   py -m pip install -r requirements.txt

   # Linux/macOS
   python3 -m pip install -r requirements.txt
   ```

3. **Verifica la instalación:**
   ```bash
   # Windows
   py -c "import qrcode; from PIL import Image; print('Instalación exitosa')"

   # Linux/macOS
   python3 -c "import qrcode; from PIL import Image; print('Instalación exitosa')"
   ```

## Compilación de Ejecutables

### Usando el Script Automatizado (Recomendado)

El proyecto incluye `build_exe.py`, un script que automatiza la compilación usando PyInstaller.

```bash
# Desde la raíz del proyecto
python build_exe.py
```

**Qué hace el script:**
- Verifica e instala PyInstaller si es necesario
- Configura parámetros de compilación (ícono incluido)
- Genera ejecutable en `dist/GeneradorQR-WiFi.exe`
- Proporciona feedback detallado del proceso

### Compilación Manual con PyInstaller

Si prefieres control manual o el script falla:

#### Windows
```powershell
# Instalar PyInstaller (si no está instalado)
py -m pip install pyinstaller

# Compilar con ícono
pyinstaller --onefile --noconsole --icon=icons/icono.ico --name GeneradorQR-WiFi QR.py
```

#### Linux/macOS
```bash
# Instalar PyInstaller
python3 -m pip install pyinstaller

# Compilar con ícono (principalmente para Windows, pero incluido por consistencia)
python3 -m PyInstaller --onefile --noconsole --icon=icons/icono.ico --name GeneradorQR-WiFi QR.py

# Hacer ejecutable (Linux/macOS)
chmod +x dist/GeneradorQR-WiFi
```

### Parámetros de PyInstaller Explicados
- `--onefile`: Genera un único archivo ejecutable
- `--noconsole`: Oculta la ventana de terminal (interfaz gráfica pura)
- `--icon=icons/icono.ico`: Incluye ícono personalizado
- `--name GeneradorQR-WiFi`: Nombre del ejecutable resultante

## Verificación del Ejecutable

Después de la compilación:

1. **Navega a la carpeta `dist/`**
2. **Ejecuta el archivo:**
   - Windows: Haz doble clic en `GeneradorQR-WiFi.exe`
   - Linux: `./GeneradorQR-WiFi`

3. **Prueba funcional:**
   - Ingresa un SSID largo como "Internet Movil Claro_C2B4"
   - Selecciona tipo de seguridad WPA
   - Genera el código QR
   - Verifica que el texto se divida correctamente y sea visible

## Despliegue y Distribución

### Para Usuarios Finales

Los ejecutables generados son independientes y no requieren Python instalado. Distribúyelos a través de:

- **GitHub Releases**: Sube el `.exe` como asset de release
- **Descargas directas**: Comparte el archivo desde `dist/`
- **Instaladores**: Empaqueta con herramientas como Inno Setup (Windows)

### Para Desarrolladores

Si otros desarrolladores necesitan contribuir:

1. **Clonan el repositorio**
2. **Instalan dependencias** (`pip install -r requirements.txt`)
3. **Pueden compilar localmente** usando `build_exe.py`

### Estrategia de Sincronización (SSOT)

Para evitar duplicados entre documentación y assets de release:

1. **Documentación centralizada** en `/docs`
2. **Script de preparación** (futuro: `prepare_release.py`) que copie automáticamente archivos desde `/docs` a `/release assets`
3. **No editar manualmente** archivos en `/release assets`

## Solución de Problemas Comunes

### Errores de Compilación

#### "PyInstaller no encontrado"
```bash
py -m pip install pyinstaller
```

#### "Ícono no encontrado"
- Verifica que `icons/icono.ico` existe
- Asegúrate de ejecutar desde la raíz del proyecto

#### Ejecutable no se inicia
- **Windows**: Verifica permisos de ejecución
- **Linux**: `chmod +x dist/GeneradorQR-WiFi`

### Errores de Dependencias

#### Tkinter faltante (Linux)
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

#### PIL/Pillow problemas
```bash
py -m pip install --upgrade Pillow
```

### Problemas de Rendimiento

Si la compilación es lenta:
- Cierra otras aplicaciones
- Asegúrate de tener suficiente espacio en disco
- Considera usar `--upx-dir` para compresión adicional

## Próximos Pasos

Después de la compilación exitosa:
- ✅ Prueba el ejecutable en diferentes sistemas
- ✅ Crea un GitHub Release con el ejecutable
- ✅ Actualiza la documentación si hay cambios
- ✅ Comparte con usuarios finales

Para documentación técnica detallada, consulta:
- [Referencia de API](../reference/api-reference.md)
- [Arquitectura del Sistema](../explanation/architecture.md)