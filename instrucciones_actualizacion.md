# Instrucciones para Actualizar el Ejecutable

Para generar una nueva versión del ejecutable con todas las mejoras implementadas, sigue estos pasos:

## 1. Generar el Ejecutable

Abre PowerShell o Símbolo del Sistema (cmd) y ejecuta los siguientes comandos:

```powershell
# Navegar a la carpeta del proyecto
cd "c:\Users\tu usuario\Generador de QR Wifi"

# Ejecutar el script de generación de ejecutable
python build_exe.py
```

Alternativamente, si el script no funciona, puedes usar directamente PyInstaller:

```powershell
# Instalar PyInstaller (si no está instalado)
python -m pip install pyinstaller

# Generar el ejecutable sin mostrar la ventana de consola e incluir ícono
python -m PyInstaller --onefile --noconsole --icon=icons/icono.ico --name GeneradorQR-WiFi --clean --noconfirm QR.py
```

## 2. Verificar el Ejecutable

El ejecutable generado debería estar en la carpeta `dist`. Para verificar que funciona correctamente:

1. Navega a la carpeta `dist`
2. Ejecuta el archivo `GeneradorQR-WiFi.exe` 
3. Prueba la generación de un código QR con un SSID largo como "Internet Movil Claro_C2B4"
4. Verifica que el texto aparece correctamente dividido y visible en la imagen

## 3. Notas Importantes

- El ejecutable generado no requiere tener Python instalado para funcionar
- Incluye ícono personalizado para mejor presentación
- Contiene todas las mejoras implementadas:
  - División inteligente de texto respetando palabras completas
  - Posicionamiento mejorado del texto para mejor visibilidad
  - Interfaz gráfica con opciones para mostrar/ocultar contraseña
  - Ocultamiento automático de campos para redes abiertas
  - Mayor espacio para el texto del SSID
