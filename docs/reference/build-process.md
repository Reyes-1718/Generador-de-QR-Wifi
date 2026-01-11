# Referencia del Proceso de Compilación

Esta referencia técnica documenta el proceso de compilación, empaquetado y distribución del Generador de QR WiFi. Incluye detalles de PyInstaller, configuración de builds y estrategias de distribución.

## Configuración de PyInstaller

### Archivo .spec

El archivo `GeneradorQR-WiFi.spec` se genera automáticamente con la siguiente configuración:

```python
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

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
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='GeneradorQR-WiFi',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulator=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icons/icono.ico',
    version_file=None,
)
```

### Parámetros de Compilación

#### Parámetros Esenciales
- **`--onefile`**: Genera un único archivo ejecutable
- **`--noconsole`**: Oculta la ventana de terminal (aplicación GUI pura)
- **`--icon icons/icono.ico`**: Incluye ícono personalizado en el ejecutable

#### Parámetros de Optimización
- **`--clean`**: Elimina archivos temporales de compilaciones anteriores
- **`--noconfirm`**: Evita prompts de confirmación durante la compilación
- **`upx=True`**: Habilita compresión UPX para reducir tamaño del ejecutable

#### Parámetros de Depuración (no usados en producción)
- **`debug=False`**: Deshabilita información de depuración
- **`strip=False`**: Mantiene símbolos de depuración (útil para troubleshooting)

## Estructura de Archivos Generados

### Directorio `build/`
Contiene archivos temporales generados durante la compilación:

```
build/
├── GeneradorQR-WiFi/
│   ├── Analysis-00.toc      # Análisis de dependencias
│   ├── EXE-00.toc          # Información del ejecutable
│   ├── PKG-00.toc          # Información del paquete
│   ├── PYZ-00.pyz          # Archivo Python comprimido
│   ├── PYZ-00.toc          # Tabla de contenidos PYZ
│   ├── warn-GeneradorQR-WiFi.txt  # Advertencias de compilación
│   ├── xref-GeneradorQR-WiFi.html # Referencias cruzadas
│   └── localpycs/          # Archivos Python compilados
```

### Directorio `dist/`
Contiene el ejecutable final y archivos de distribución:

```
dist/
└── GeneradorQR-WiFi.exe    # Ejecutable final (único archivo)
```

### Archivo .spec
Archivo de configuración de PyInstaller que puede ser modificado para compilaciones personalizadas.

## Dependencias Incluidas

### Automáticamente Incluidas
PyInstaller detecta automáticamente la mayoría de las dependencias:

- **qrcode**: Biblioteca principal para generación QR
- **PIL/Pillow**: Manipulación de imágenes
- **tkinter**: Framework de interfaz gráfica (incluido en Python)

### Dependencias Ocultas
En casos complejos, puede requerir `hiddenimports`:

```python
hiddenimports=[
    'PIL.Image',           # Para manipulación de imágenes
    'PIL.ImageDraw',       # Para dibujo de texto
    'PIL.ImageFont',       # Para fuentes de texto
    'qrcode.constants',    # Constantes de qrcode
]
```

## Optimizaciones de Rendimiento

### Compresión
- **UPX**: Reducción de tamaño del ejecutable (~30-50% menor)
- **Onefile**: Distribución simplificada (un solo archivo)

### Memoria
- **Strip**: Eliminación de símbolos de depuración en producción
- **Excludes**: Exclusión de módulos no utilizados

### Velocidad de Inicio
- **Noarchive**: Desactiva archivado para inicio más rápido
- **Runtime_tmpdir**: Directorio temporal optimizado

## Estrategias de Distribución

### Distribución Directa
```bash
# Archivo único listo para distribución
dist/GeneradorQR-WiFi.exe
```

### Empaquetado con Instaladores
- **Inno Setup** (Windows): Crea instaladores .exe con opciones avanzadas
- **NSIS**: Sistema de instalación scriptable
- **Advanced Installer**: Interfaz gráfica para creación de instaladores

### Distribución vía GitHub Releases
```yaml
# Ejemplo de release assets
- GeneradorQR-WiFi.exe          # Ejecutable principal
- GeneradorQR-WiFi-portable.zip # Versión portable
- setup.exe                     # Instalador completo
```

## Solución de Problemas de Compilación

### Errores Comunes

#### "ModuleNotFoundError"
**Síntoma:** PyInstaller no encuentra un módulo
**Solución:** Agregar a `hiddenimports` en .spec

#### "Icon not found"
**Síntoma:** Error al incluir ícono
**Solución:** Verificar ruta `icons/icono.ico` existe

#### "tkinter not found" (Linux)
**Síntoma:** Error en sistemas Linux sin tkinter
**Solución:** Instalar `python3-tk`

### Optimizaciones de Troubleshooting

#### Compilación Verbose
```bash
pyinstaller --debug=all --onefile --noconsole QR.py
```

#### Análisis de Dependencias
```bash
pyinstaller --debug=imports QR.py
```

#### Verificación de Ejecutable
```bash
# Verificar dependencias del ejecutable
objdump -p dist/GeneradorQR-WiFi.exe | grep "DLL Name"
```

## Métricas de Compilación

### Tamaño Típico
- **Sin compresión:** ~15-20 MB
- **Con UPX:** ~8-12 MB
- **Variación:** Dependiente de versión de Python y dependencias

### Tiempo de Compilación
- **Primera vez:** 2-5 minutos
- **Compilaciones posteriores:** 30-60 segundos (con --clean)

### Requisitos del Sistema
- **RAM:** Mínimo 2GB, recomendado 4GB+
- **Disco:** 500MB espacio libre temporal
- **Python:** Misma versión que el target

## Compatibilidad Multiplataforma

### Windows
- **Arquitectura:** x86_64 (64-bit)
- **Dependencias:** Incluye VCRUNTIME si necesario
- **Manifest:** Auto-generado para UAC

### Linux
- **Distribuciones:** Ubuntu, Fedora, Arch, etc.
- **Dependencias:** tkinter debe estar disponible
- **Ejecutable:** Requiere permisos de ejecución (`chmod +x`)

### macOS
- **Arquitectura:** x86_64/ARM64 (Apple Silicon)
- **Code Signing:** Recomendado para distribución
- **Bundle:** Estructura de aplicación .app

## Variables de Entorno

### PyInstaller
```bash
# Directorio de trabajo
PYINSTALLER_WORKDIR=/tmp/pyinstaller

# Configuración de caché
PYINSTALLER_CACHE_DIR=~/.pyinstaller

# Nivel de verbosidad
PYINSTALLER_VERBOSE=1
```

### Python
```bash
# Asegurar codificación UTF-8
PYTHONUTF8=1

# Optimizar bytecode
PYTHONOPTIMIZE=1
```

## Scripts de Automatización

### build_exe.py
Script principal que automatiza todo el proceso:

```python
def crear_ejecutable():
    # Verificación de dependencias
    # Configuración de comando
    # Ejecución de PyInstaller
    # Verificación de resultado
    # Reporte de métricas
```

### Scripts Adicionales (Futuros)
- **build_all.py**: Compilación para múltiples plataformas
- **test_build.py**: Verificación de ejecutable generado
- **package_release.py**: Preparación de assets de release

## Mejores Prácticas

### Versionado
- Incluir número de versión en nombre del ejecutable
- Mantener historial de .spec files
- Documentar cambios entre versiones

### Seguridad
- Firmar ejecutables (especialmente Windows/macOS)
- Verificar integridad de dependencias
- Evitar inclusión de datos sensibles

### Mantenimiento
- Limpiar directorios build/ regularmente
- Archivar .spec files importantes
- Documentar dependencias específicas de plataforma