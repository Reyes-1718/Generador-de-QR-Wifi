# Referencia de API

Esta referencia técnica documenta todas las funciones públicas y componentes del Generador de QR WiFi. Está organizada por módulos y proporciona detalles de implementación para desarrolladores.

## Módulo QR.py

### Funciones de Utilidad

#### `limpiar_consola()`
```python
def limpiar_consola() -> None
```
Limpia la pantalla de la consola para una mejor visualización.

**Parámetros:** Ninguno
**Retorno:** Ninguno
**Dependencias:** `os.system()`

#### `escapar_caracteres_wifi(texto: str) -> str`
```python
def escapar_caracteres_wifi(texto: str) -> str
```
Escapa caracteres especiales para el formato WiFi QR según el estándar.

**Parámetros:**
- `texto` (str): Texto a escapar

**Retorno:** Texto con caracteres especiales escapados
**Caracteres escapados:** `;` `,` `:` `"` `\`

#### `limpiar_nombre_archivo(nombre: str) -> str`
```python
def limpiar_nombre_archivo(nombre: str) -> str
```
Limpia el nombre del archivo removiendo caracteres no válidos.

**Parámetros:**
- `nombre` (str): Nombre original del archivo

**Retorno:** Nombre limpio válido para archivos
**Límite:** 50 caracteres máximo
**Caracteres removidos:** `< > : " / \ | ? *`

#### `verificar_dependencias() -> bool`
```python
def verificar_dependencias() -> bool
```
Verifica que las dependencias necesarias estén instaladas.

**Parámetros:** Ninguno
**Retorno:** `True` si todas las dependencias están disponibles, `False` en caso contrario
**Dependencias verificadas:** `qrcode`, `PIL.Image`, `PIL.ImageDraw`, `PIL.ImageFont`

### Funciones de Generación QR

#### `generar_qr_wifi(ssid: str, tipo_seguridad: str, password: str, oculta: bool) -> None`
```python
def generar_qr_wifi(ssid: str, tipo_seguridad: str, password: str, oculta: bool) -> None
```
Genera un código QR para una red Wi-Fi con los parámetros proporcionados.

**Parámetros:**
- `ssid` (str): Nombre de la red Wi-Fi
- `tipo_seguridad` (str): Tipo de seguridad ("WPA", "WEP", "nopass")
- `password` (str): Contraseña de la red (vacía para redes abiertas)
- `oculta` (bool): `True` si la red está oculta

**Proceso:**
1. Escapa caracteres especiales en SSID y contraseña
2. Construye cadena de texto QR en formato estándar
3. Configura QR con corrección de errores L
4. Genera imagen QR
5. Añade texto con nombre de red debajo del QR
6. Guarda imagen como PNG

**Formato QR generado:** `WIFI:S:{ssid};T:{tipo};P:{password};H:{hidden};;`

#### `generar_qr_wifi_interfaz(ssid: tk.StringVar, tipo_seguridad: tk.StringVar, password: tk.StringVar, oculta: tk.BooleanVar) -> None`
```python
def generar_qr_wifi_interfaz(ssid: tk.StringVar, tipo_seguridad: tk.StringVar, password: tk.StringVar, oculta: tk.BooleanVar) -> None
```
Versión adaptada para interfaz gráfica de `generar_qr_wifi`.

**Parámetros:** Variables de Tkinter con los valores de entrada
**Validaciones:**
- SSID no puede estar vacío
- Contraseña requerida para WPA/WEP
**Mensajes:** Usa `messagebox` para errores y confirmaciones

### Interfaz Gráfica

#### `interfaz_grafica() -> None`
```python
def interfaz_grafica() -> None
```
Crea y ejecuta la interfaz gráfica completa del programa.

**Componentes principales:**
- Campo de entrada para SSID
- Radio buttons para tipo de seguridad (WPA, WEP, nopass)
- Campo de contraseña (oculto por defecto)
- Checkbox para red oculta
- Botones: Generar QR, Limpiar campos, Mostrar/Ocultar contraseña

**Funciones auxiliares:**
- `generar_qr_desde_gui()`: Manejador del botón generar
- `mostrar_contraseña()`: Toggle visibilidad contraseña
- `actualizar_campos()`: Actualiza visibilidad campos según tipo seguridad
- `limpiar_campos()`: Resetea todos los campos

**Características:**
- Ícono de ventana (si existe `icons/icono.ico`)
- Campos dinámicos (contraseña oculta para redes abiertas)
- Validación de entrada
- Mensajes de error/éxito

## Módulo build_exe.py

### Función Principal

#### `crear_ejecutable() -> None`
```python
def crear_ejecutable() -> None
```
Crea un ejecutable del programa usando PyInstaller.

**Proceso:**
1. Verifica e instala PyInstaller si es necesario
2. Configura parámetros de compilación
3. Ejecuta PyInstaller con configuración específica
4. Verifica creación exitosa y muestra información

**Parámetros de PyInstaller:**
- `--onefile`: Ejecutable único
- `--noconsole`: Sin ventana de consola
- `--icon icons/icono.ico`: Ícono personalizado
- `--name GeneradorQR-WiFi`: Nombre del ejecutable
- `--clean`: Limpia archivos temporales
- `--noconfirm`: Sin confirmaciones

**Archivos generados:**
- `dist/GeneradorQR-WiFi.exe`: Ejecutable final
- `build/`: Archivos temporales
- `GeneradorQR-WiFi.spec`: Configuración PyInstaller

## Dependencias Externas

### Requeridas
- **qrcode** (>= 7.0): Generación de códigos QR
- **Pillow** (>= 9.0): Manipulación de imágenes
- **tkinter**: Interfaz gráfica (incluido en Python estándar)

### Opcionales para Compilación
- **PyInstaller** (>= 5.0): Creación de ejecutables

## Constantes y Configuraciones

### Configuración QR
```python
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
```

### Configuración de Texto
- **Fuente:** Arial 20pt (fallback: fuente por defecto)
- **Máximo caracteres por línea:** 16
- **Espaciado entre líneas:** 30px
- **Margen inferior:** 10px

### Formatos de Archivo
- **Extensión QR:** `.png`
- **Prefijo nombre:** `qr_wifi_`
- **Nombre base:** SSID limpiado (máx. 50 caracteres)

## Manejo de Errores

### Validaciones de Entrada
- SSID vacío → Error
- Contraseña faltante para WPA/WEP → Error
- Caracteres especiales → Auto-escape

### Manejo de Archivos
- Nombres inválidos → Limpieza automática
- Error de guardado → Mensaje de error con detalles

### Dependencias Faltantes
- Verificación automática al inicio
- Instrucciones de instalación en mensaje de error

## Arquitectura del Sistema

### Patrón de Diseño
- **Separación de responsabilidades:** Lógica QR separada de interfaz
- **Funciones puras:** `generar_qr_wifi()` independiente de UI
- **Adaptadores:** `generar_qr_wifi_interfaz()` para compatibilidad GUI

### Flujo de Datos
1. **Entrada:** Parámetros de red Wi-Fi
2. **Procesamiento:** Escape de caracteres + construcción cadena QR
3. **Generación:** Creación imagen QR + texto
4. **Salida:** Archivo PNG guardado

### Gestión de Estado
- **Interfaz gráfica:** Estado mantenido en variables Tkinter
- **Validación:** Chequeos en tiempo real
- **Feedback:** Mensajes inmediatos al usuario