# Generador de Códigos QR para Conexión Wi-Fi

## Resumen del Proyecto

El **Generador de QR WiFi** es una aplicación de escritorio desarrollada en Python que facilita la creación de códigos QR compatibles con el estándar WiFi QR. Su propósito principal es generar códigos QR que permitan a los usuarios conectarse automáticamente a redes Wi-Fi mediante el escaneo con dispositivos móviles, eliminando la necesidad de ingresar manualmente credenciales de red.

### Funcionalidad Principal
- Generación de códigos QR con formato estándar WiFi QR (`WIFI:S:<SSID>;T:<TIPO>;P:<PASSWORD>;H:<OCULTA>;;`)
- Soporte para múltiples tipos de seguridad: WPA/WPA2, WEP y redes abiertas
- Interfaz gráfica intuitiva con validación de entradas
- Manejo inteligente de nombres de red largos con división automática de texto
- Ocultamiento automático de campos irrelevantes (ej. contraseña para redes abiertas)
- Generación de imágenes PNG con el código QR y el nombre de la red superpuesto

### Caso de Uso
Ideal para administradores de red, cafeterías, hoteles, oficinas y usuarios domésticos que desean compartir credenciales de Wi-Fi de manera segura y conveniente. Los códigos QR generados son compatibles con la mayoría de los smartphones modernos.

## Requisitos del Sistema

### Software Necesario
- **Python 3.7 o superior** (para ejecución desde código fuente)
- **Sistema Operativo**: Windows 10/11, macOS 10.15+, Linux (Ubuntu, Fedora, Arch, etc.)
- **Pip** (gestor de paquetes de Python)

### Dependencias de Python
Las dependencias principales se especifican en `requirements.txt`:
```
qrcode[pil]>=7.0.0
```

Esto incluye automáticamente:
- `qrcode`: Para la generación de códigos QR
- `Pillow (PIL)`: Para manipulación de imágenes y texto

### Verificación de Tkinter
Para la interfaz gráfica, se requiere Tkinter (incluido por defecto en Python para Windows y macOS):
```bash
# Verificar Tkinter
python -c "import tkinter; print('Tkinter disponible')"
```

En Linux, instalar si es necesario:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```

## Estructura de Archivos y Carpetas

```
Generador de QR Wifi/
├── icons/
│   └── icono.ico              # Ícono de la aplicación (32x32 píxeles)
├── QR.py                      # Script principal con interfaz gráfica
├── build_exe.py               # Script para generar ejecutables
├── test_qr.py                 # Suite de pruebas unitarias
├── requirements.txt           # Lista de dependencias Python
├── .gitignore                 # Configuración de archivos ignorados por Git
├── README.md                  # Esta documentación
├── LINUX.md                   # Guía específica para Linux
├── instrucciones_actualizacion.md  # Instrucciones para actualizar ejecutables
├── QR.spec                    # Archivo de configuración PyInstaller (Windows)
├── GeneradorQR-WiFi.spec      # Archivo de configuración PyInstaller (actual)
├── build/                     # Archivos temporales de compilación (ignorados)
├── dist/                      # Ejecutables generados (ignorados)
├── pruebas_qr/                # Imágenes de prueba generadas (ignoradas)
├── __pycache__/               # Archivos de caché Python (ignorados)
└── .git/                      # Control de versiones
```

### Descripción de Archivos Clave
- `icons/icono.ico`: Recurso visual para el ícono de la aplicación y ejecutables
- `.gitignore`: Define qué archivos/carpetas no deben versionarse en Git
- `*.spec`: Archivos de configuración para PyInstaller, definen parámetros de compilación
- `build/`: Directorio temporal usado durante la compilación (no versionado)
- `dist/`: Contiene los ejecutables finales generados (no versionado)
- `pruebas_qr/`: Almacena códigos QR generados durante las pruebas (no versionado)
- `__pycache__/`: Archivos de bytecode Python generados automáticamente (no versionado)

## Descripción de Scripts Principales

### QR.py
**Función**: Script principal que contiene toda la lógica de la aplicación.

**Características principales**:
- Interfaz gráfica basada en Tkinter
- Funciones de validación y escape de caracteres especiales
- Generación de códigos QR con superposición de texto
- Manejo de errores y excepciones
- Soporte para diferentes tipos de seguridad Wi-Fi

**Funciones clave**:
- `generar_qr_wifi()`: Genera y guarda el código QR
- `interfaz_grafica()`: Crea la GUI completa
- `actualizar_campos()`: Gestiona la visibilidad de campos según el tipo de red

### build_exe.py
**Función**: Automatiza la creación de ejecutables independientes usando PyInstaller.

**Características**:
- Verifica e instala PyInstaller si es necesario
- Configura parámetros de compilación (ícono, nombre, opciones)
- Genera ejecutables sin consola para distribución
- Proporciona feedback detallado del proceso

**Uso típico**:
```bash
python build_exe.py
```

### test_qr.py
**Función**: Suite de pruebas unitarias para validar la funcionalidad del generador.

**Características**:
- Pruebas de generación de QR con diferentes SSID
- Validación de texto en imágenes generadas
- Pruebas de casos edge (nombres largos, caracteres especiales)
- Integración con unittest framework

**Ejecución**:
```bash
python test_qr.py
```

## Configuración de Git (.gitignore)

### Propósito del .gitignore
El archivo `.gitignore` es crucial en proyectos de desarrollo para especificar qué archivos y carpetas deben ser **ignorados** por el sistema de control de versiones Git. Esto mantiene el repositorio limpio, enfocado en el código fuente y evita versionar archivos temporales, compilados o generados automáticamente.

### Configuración Actual
El proyecto incluye un `.gitignore` completo optimizado para Python y PyInstaller:

```gitignore
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
*.manifest
*.spec

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Archivos generados por el proyecto
pruebas_qr/
qr_wifi_*.png

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

### Explicación de las Reglas Principales

#### 🐍 **Archivos Python**
- `__pycache__/`: Carpetas de bytecode generadas por Python
- `*.py[cod]`: Archivos compilados (.pyc, .pyo)

#### 📦 **Distribución y Compilación**
- `build/`: Archivos temporales de PyInstaller
- `dist/`: **Ejecutables finales** (evita versionar binarios grandes)
- `*.spec`: Configuraciones de PyInstaller

#### 🧪 **Pruebas y Desarrollo**
- `pruebas_qr/`: **Imágenes de QR generadas en pruebas**
- `qr_wifi_*.png`: **Códigos QR individuales**
- Archivos de cobertura y caché de pruebas

#### 🌍 **Entornos Virtuales**
- `.env`, `.venv`, `venv/`: Variables de entorno y entornos virtuales

#### 🖥️ **IDE y Sistema Operativo**
- `.vscode/`, `.idea/`: Configuraciones de editores
- `.DS_Store`, `Thumbs.db`: Archivos del sistema

### Beneficios de Esta Configuración
- **Repositorio limpio**: Solo código fuente versionado
- **Colaboración eficiente**: Evita conflictos con archivos generados
- **Seguridad**: No expone variables de entorno o datos sensibles
- **Rendimiento**: Reduce tamaño del repositorio y velocidad de clonado

## Instrucciones de Instalación y Ejecución

### Instalación en Windows

#### Opción 1: Ejecutable Pre-compilado (Recomendado)
1. Descarga `GeneradorQR-WiFi.exe` desde la carpeta `dist/`
2. Haz doble clic para ejecutar (no requiere instalación adicional)

#### Opción 2: Desde Código Fuente
```powershell
# Verificar Python
py --version

# Instalar dependencias
py -m pip install -r requirements.txt

# Verificar instalación
py -c "import qrcode; from PIL import Image; print('Listo')"
```

### Instalación en Linux

#### Desde Código Fuente
```bash
# Verificar Python y Tkinter
python3 --version
python3 -c "import tkinter; print('Tkinter OK')"

# Instalar dependencias
python3 -m pip install -r requirements.txt
```

#### Ejecutable para Linux
```bash
# Instalar PyInstaller
python3 -m pip install pyinstaller

# Generar ejecutable
python3 -m PyInstaller --onefile --noconsole --name GeneradorQR-WiFi QR.py

# Hacer ejecutable
chmod +x dist/GeneradorQR-WiFi
```

### Ejecución del Programa

#### Windows
```powershell
# Desde código fuente
py QR.py

# Desde ejecutable
.\dist\GeneradorQR-WiFi.exe
```

#### Linux
```bash
# Desde código fuente
python3 QR.py

# Desde ejecutable
./dist/GeneradorQR-WiFi
```

### Interfaz de Usuario
La aplicación presenta una interfaz gráfica con:
1. Campo para el nombre de la red (SSID)
2. Selector de tipo de seguridad (WPA/WPA2, WEP, Ninguna)
3. Campo de contraseña (oculto automáticamente para redes abiertas)
4. Checkbox para redes ocultas
5. Botones para generar QR y limpiar campos

## Proceso de Compilación y Empaquetado

### Uso de PyInstaller
El proyecto utiliza PyInstaller para crear ejecutables independientes que no requieren Python instalado en el sistema destino.

### Archivos .spec
Los archivos `.spec` contienen la configuración de PyInstaller:
- `QR.spec`: Configuración básica
- `GeneradorQR-WiFi.spec`: Configuración actualizada con ícono

**Nota**: Los archivos `.spec` son ignorados por `.gitignore` ya que se generan automáticamente, pero se incluyen versiones específicas para referencia.

**Contenido típico de un .spec**:
```python
a = Analysis(
    ['QR.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='GeneradorQR-WiFi',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Sin ventana de consola
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icons/icono.ico',  # Ícono incluido
)
```

### Comando de Compilación Manual
```bash
pyinstaller --onefile --noconsole --icon=icons/icono.ico --name GeneradorQR-WiFi QR.py
```

### Parámetros Importantes
- `--onefile`: Genera un único archivo ejecutable
- `--noconsole`: Oculta la ventana de terminal
- `--icon`: Especifica el archivo de ícono
- `--name`: Nombre del ejecutable resultante

### Actualización de Ejecutables
Para generar nuevas versiones:
1. Ejecutar `python build_exe.py`
2. Verificar el ejecutable en `dist/`
3. Probar con SSID largos para validar funcionalidad

## Guía de Pruebas

### Propósito de las Pruebas
El archivo `test_qr.py` contiene pruebas unitarias que validan:
- Generación correcta de códigos QR
- Manejo de SSID largos y caracteres especiales
- Superposición correcta de texto en imágenes
- Funcionalidad de escape de caracteres

### Ejecución de Pruebas
```bash
# Ejecutar todas las pruebas
python test_qr.py

# Con salida detallada
python -m unittest test_qr.py -v
```

### Carpeta pruebas_qr/
Durante la ejecución de pruebas, se generan códigos QR de ejemplo en `pruebas_qr/`:
- `qr_wifi_RedCorta.png`
- `qr_wifi_RedMuyMuyLargaConMuchosCaracteres.png`
- Archivos con caracteres especiales y espacios

**Nota**: Esta carpeta está configurada para ser ignorada por Git (`.gitignore`) ya que contiene archivos generados dinámicamente durante las pruebas.

### Casos de Prueba Incluidos
- SSID cortos y largos
- Nombres con caracteres especiales
- Nombres con espacios
- Validación de texto en imágenes generadas

## Notas Adicionales y Futuras Mejoras

### Características Técnicas
- **Formato QR**: Estándar WiFi QR oficial
- **Corrección de Errores**: Nivel L (7%)
- **Tamaño QR**: Auto-ajustable
- **Formato Imagen**: PNG con texto superpuesto
- **Compatibilidad**: Android 10+, iOS 11+

### Limitaciones Actuales
- Interfaz disponible solo en español
- Requiere permisos de escritura para guardar imágenes
- Dependiente de fuentes del sistema para texto

### Mejoras Futuradas
- Soporte multiidioma
- Exportación a formatos adicionales (PDF, SVG)
- Integración con gestores de Wi-Fi del sistema
- Modo batch para múltiples redes
- API REST para integración web
- Temas oscuros/claros para la interfaz

### Contribución
Para contribuir:
1. Fork del repositorio
2. Crear rama feature
3. Implementar cambios con pruebas
4. Enviar pull request

### Licencia
Este proyecto está bajo licencia MIT. Consulta el archivo LICENSE para detalles.

### Soporte
Para issues, preguntas o sugerencias:
- Abrir issue en el repositorio
- Revisar documentación en `LINUX.md` para problemas específicos de Linux
- Verificar `instrucciones_actualizacion.md` para compilación

---

**¡Simplifica la conexión Wi-Fi con códigos QR! 📱🔗**
