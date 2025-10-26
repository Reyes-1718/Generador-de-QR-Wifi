# Generador de Códigos QR para Conexión Wi-Fi - Guía para Linux

Esta guía está diseñada específicamente para usuarios de sistemas Linux que desean utilizar o compilar el Generador de Códigos QR para conexiones Wi-Fi.

## Índice
1. [Requisitos](#requisitos)
2. [Instalación desde código fuente](#instalación-desde-código-fuente)
3. [Generación de ejecutable para Linux](#generación-de-ejecutable-para-linux)
4. [Ejecución del programa](#ejecución-del-programa)
5. [Solución de problemas comunes](#solución-de-problemas-comunes)

## Requisitos

### Software necesario
- **Python 3.7 o superior**
- **Pip** (gestor de paquetes de Python)
- **Tkinter** (para la interfaz gráfica)

### Verificación de requisitos

```bash
# Verificar la versión de Python
python3 --version

# Verificar que pip está instalado
python3 -m pip --version

# Verificar que Tkinter está instalado
python3 -c "import tkinter; print('Tkinter está instalado')"
```

Si Tkinter no está instalado, puedes instalarlo según tu distribución:

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S tk
```

## Instalación desde código fuente

1. **Clonar o descargar el repositorio:**

```bash
# Si tienes Git instalado:
git clone [URL-DEL-REPOSITORIO]

# O descarga y descomprime el archivo ZIP del proyecto
```

2. **Navegar al directorio del proyecto:**

```bash
cd Mis_Apps  # O el nombre que hayas dado a la carpeta
```

3. **Instalar las dependencias:**

```bash
python3 -m pip install -r requirements.txt
```

## Generación de ejecutable para Linux

Para crear un ejecutable independiente que funcione en sistemas Linux sin necesidad de tener Python instalado:

### Instalación de PyInstaller

```bash
python3 -m pip install pyinstaller
```

### Creación del ejecutable

```bash
python3 -m PyInstaller --onefile --noconsole --name GeneradorQR-WiFi QR.py
```

Opciones explicadas:
- `--onefile`: Genera un único archivo ejecutable
- `--noconsole`: No muestra la ventana de terminal, solo la interfaz gráfica
- `--name GeneradorQR-WiFi`: Nombre del archivo ejecutable resultante

### Ubicación del ejecutable

El ejecutable se encontrará en la carpeta `dist` dentro del directorio del proyecto.

### Hacer el ejecutable ejecutable (si es necesario)

```bash
chmod +x dist/GeneradorQR-WiFi
```

## Ejecución del programa

### Desde el código fuente

```bash
python3 QR.py
```

### Desde el ejecutable

```bash
# Navegar al directorio dist
cd dist

# Ejecutar el programa
./GeneradorQR-WiFi
```

O simplemente haciendo doble clic en el archivo ejecutable en tu gestor de archivos (asegúrate de que tenga permisos de ejecución).

## Solución de problemas comunes

### Error: "Tkinter no está disponible"

Si aparece un error sobre Tkinter al iniciar el programa, asegúrate de tener instalado el paquete python3-tk:

```bash
sudo apt-get install python3-tk  # Para sistemas basados en Debian
```

### El ejecutable no se inicia

Verifica que tiene permisos de ejecución:

```bash
chmod +x dist/GeneradorQR-WiFi
```

### Error de dependencias en el ejecutable

Si el ejecutable generado muestra errores relacionados con bibliotecas faltantes, puede ser necesario incluir paquetes adicionales:

```bash
python3 -m PyInstaller --onefile --noconsole --name GeneradorQR-WiFi --add-data "recursos:recursos" QR.py
```

### Problemas de visualización de fuentes

Si las fuentes no se visualizan correctamente, prueba a usar la fuente del sistema:

```bash
# Instalar fuentes comunes
sudo apt-get install fonts-liberation  # En Ubuntu/Debian
```

---

## Notas para distribuciones específicas

### Ubuntu/Debian
El programa debería funcionar sin problemas siguiendo las instrucciones anteriores.

### Fedora/RHEL
Asegúrate de tener instalados los siguientes paquetes:
```bash
sudo dnf install python3-tkinter python3-pillow
```

### Arch Linux
Instala los siguientes paquetes:
```bash
sudo pacman -S tk python-pillow
```

---

Para cualquier problema o sugerencia específica de Linux, por favor abre un issue en el repositorio del proyecto.
