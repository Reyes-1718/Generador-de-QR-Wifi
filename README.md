# Generador de Códigos QR para Conexión Wi-Fi

## Descripción
Este programa genera códigos QR que permiten conectarse automáticamente a redes Wi-Fi simplemente escaneando el código con un smartphone. El código QR generado incluye el nombre de la red y todos los parámetros necesarios para la conexión automática.

## Características
- ✅ Generación de códigos QR compatibles con el estándar WiFi QR
- ✅ Soporte para redes WPA/WPA2, WEP y redes abiertas
- ✅ Manejo de redes ocultas
- ✅ Escape automático de caracteres especiales
- ✅ Nombre de la red incluido en la imagen de forma clara y legible
- ✅ División inteligente de nombres largos respetando palabras completas
- ✅ Interfaz de usuario amigable con opción para mostrar/ocultar contraseña
- ✅ Validación de entrada de datos
- ✅ Manejo de errores robusto

## Requisitos del Sistema

### Software Necesario
- **Python 3.7 o superior**
- **Sistema Operativo**: Windows, macOS, Linux

### Dependencias de Python
El programa utiliza las siguientes librerías:
- `qrcode[pil]` - Para generar códigos QR
- `PIL (Pillow)` - Para manipulación de imágenes (incluido en qrcode[pil])

Las dependencias estándar de Python incluidas:
- `os` - Para operaciones del sistema
- `re` - Para expresiones regulares
- `sys` - Para funciones del sistema

## Instalación

### Opción 1: Usar el ejecutable (recomendado)
Si dispones del ejecutable `GeneradorQR-WiFi.exe`, no necesitas instalar nada. Simplemente:
1. Haz doble clic en el ejecutable
2. La aplicación se iniciará directamente con la interfaz gráfica

### Opción 2: Ejecución desde código fuente

#### Paso 1: Verificar Python
Asegúrate de tener Python instalado:
```powershell
py --version
```

#### Paso 2: Instalar Dependencias
Ejecuta el siguiente comando para instalar las dependencias:
```powershell
py -m pip install qrcode[pil]
```

O usando el archivo requirements.txt:
```powershell
py -m pip install -r requirements.txt
```

### Paso 3: Verificar la Instalación
Puedes verificar que las dependencias están instaladas correctamente:
```powershell
py -c "import qrcode; from PIL import Image; print('Dependencias instaladas correctamente')"
```

## Uso del Programa

### Ejecución
Para ejecutar el programa:
```powershell
py QR.py
```
O si has generado el ejecutable, simplemente haz doble clic en `GeneradorQR-WiFi.exe` (se abrirá directamente la interfaz gráfica sin mostrar ninguna ventana de terminal).

### Interfaz Gráfica
El programa ahora incluye una interfaz gráfica amigable donde podrás:

1. **Nombre de la Red (SSID)**
   - Introduce el nombre exacto de tu red Wi-Fi
   - No puede estar vacío
   - Los nombres largos se dividirán automáticamente respetando palabras completas

2. **Tipo de Seguridad**
   - WPA/WPA2 (la más común)
   - WEP (menos segura, obsoleta)
   - Ninguna (red abierta)

3. **Contraseña**
   - Solo requerida para redes WPA/WPA2 y WEP
   - Puedes mostrar/ocultar la contraseña usando el botón correspondiente

4. **Red Oculta**
   - Marca la casilla si tu red está oculta

5. **Botones de Acción**
   - "Generar Código QR": Crea y guarda el código QR
   - "Limpiar Campos": Reinicia todos los valores

### Ejemplo de Uso
```
==============================================
  Generador de Código QR para Conexión Wi-Fi  
==============================================

[1] Introduce el nombre de tu red Wi-Fi (SSID): MiRedWiFi

[2] Selecciona el tipo de seguridad de la red:
    1: WPA/WPA2 (la más común)
    2: WEP
    3: Ninguna (red abierta)
    Elige una opción (1, 2, 3): 1

[3] Introduce la contraseña de la red: MiContraseña123

[4] ¿La red está oculta? (s/n): n

Generando código QR...

==============================================
¡Éxito! El código QR se ha guardado como: 'qr_wifi_MiRedWiFi.png'
Escanea este archivo con tu teléfono para conectarte a la red.
==============================================
```

## Estructura del Proyecto

```
Mis_Apps/
├── QR.py                    # Programa principal
├── requirements.txt         # Lista de dependencias
├── README.md               # Documentación (este archivo)
├── qr_wifi_[nombre].png    # Códigos QR generados
└── __pycache__/            # Archivos de caché de Python
    └── QR.cpython-313.pyc
```

## Funciones del Programa

### `limpiar_consola()`
Limpia la pantalla de la consola para una mejor visualización.

### `escapar_caracteres_wifi(texto)`
Escapa caracteres especiales según el estándar WiFi QR:
- `;` → `\\;`
- `,` → `\\,`
- `:` → `\\:`
- `"` → `\\"`
- `\` → `\\\\`

### `limpiar_nombre_archivo(nombre)`
Limpia el nombre del archivo removiendo caracteres no válidos y limitando la longitud.

### `verificar_dependencias()`
Verifica que las dependencias necesarias (`qrcode` y `PIL`) estén instaladas.

### `generar_qr_wifi()`
Función principal que:
1. Solicita datos de la red Wi-Fi
2. Genera el código QR con formato estándar
3. Añade el nombre de la red como texto
4. Guarda la imagen resultante

## Formato del Código QR

El programa genera códigos QR siguiendo el estándar WiFi QR:
```
WIFI:S:<SSID>;T:<WPA|WEP|nopass>;P:<PASSWORD>;H:<true|false>;;
```

Donde:
- `S`: SSID (nombre de la red)
- `T`: Tipo de seguridad
- `P`: Contraseña
- `H`: Red oculta (true/false)

## Características Técnicas

### Configuración del QR
- **Versión**: 1 (auto-ajustable)
- **Corrección de errores**: L (Low - 7%)
- **Tamaño de caja**: 10 píxeles
- **Borde**: 4 cajas
- **Colores**: Negro sobre blanco

### Imagen Final
- **Formato**: PNG
- **Colores**: RGB
- **Texto**: Nombre de la red centrado debajo del QR
- **División de texto**: Inteligente, respetando palabras completas
- **Distribución**: Ajuste automático de espaciado vertical para visibilidad óptima
- **Fuente**: Arial (Windows) o fuente por defecto
- **Tamaño de fuente**: 20 píxeles

## Manejo de Errores

El programa incluye manejo robusto de errores:

### Dependencias Faltantes
```
❌ Error: Los módulos 'qrcode' y 'PIL' no están instalados.
   Instálalos ejecutando: pip install qrcode[pil]
```

### Datos Inválidos
```
❌ Error: El nombre de la red no puede estar vacío.
❌ Error: La contraseña no puede estar vacía para redes WPA.
```

### Errores de Archivo
```
❌ Error al guardar el archivo: [detalle del error]
   Verifica que tienes permisos para escribir en el directorio actual.
```

### Interrupción del Usuario
```
⚠️  Operación cancelada por el usuario.
```

## Compatibilidad

### Sistemas Operativos
- ✅ Windows 10/11
- ✅ macOS 10.15+
- ✅ Linux (Ubuntu, CentOS, etc.)

### Dispositivos Móviles
Los códigos QR generados son compatibles con:
- ✅ Android 10+
- ✅ iOS 11+
- ✅ Aplicaciones de cámara nativas
- ✅ Aplicaciones de lectura de QR

## Solución de Problemas

### "Python no encontrado"
```powershell
# Instalar Python desde Microsoft Store o python.org
# Verificar instalación:
py --version
```

### "Módulo no encontrado"
```powershell
# Reinstalar dependencias:
py -m pip install --upgrade qrcode[pil]
```

### "Error de permisos"
```powershell
# Ejecutar como administrador o cambiar a directorio con permisos
cd Documents
py QR.py
```

### "Fuente no encontrada"
El programa maneja automáticamente la falta de fuentes, usando la fuente por defecto del sistema.

## Personalización

### Modificar Colores
Cambiar los colores del QR en la línea:
```python
img = qr.make_image(fill_color="black", back_color="white")
```

### Modificar Tamaño
Cambiar el tamaño del QR:
```python
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,  # Cambiar este valor
    border=4,
)
```

### Modificar Fuente
Cambiar la fuente del texto:
```python
font = ImageFont.truetype("fuente_personalizada.ttf", 20)
```

## Contribuciones

Para contribuir al proyecto:
1. Hacer fork del repositorio
2. Crear una rama para tu feature
3. Realizar cambios y pruebas
4. Enviar pull request

## Licencia

Este proyecto está bajo licencia MIT. Puedes usar, modificar y distribuir libremente.

## Contacto

Si tienes preguntas o sugerencias, puedes:
- Abrir un issue en el repositorio
- Enviar un pull request
- Contactar al desarrollador

---

**¡Disfruta generando códigos QR para tus redes WiFi! 📱📶**
