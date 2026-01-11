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

## 🚀 Inicio Rápido

### Opción 1: Ejecutable Pre-compilado (Recomendado)
1. Ve a [**Releases**](https://github.com/Reyes-1718/Generador-de-QR-Wifi/releases) en GitHub
2. Descarga `GeneradorQR-WiFi.exe` para Windows
3. Ejecuta directamente (sin instalación)

### Opción 2: Desde Código Fuente
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python QR.py
```

## 📚 Documentación

Esta documentación sigue el marco **Diátaxis** para una experiencia de usuario óptima:

### 🛠️ **How-to Guides** (Guías Prácticas)
- [**Construcción y Despliegue**](docs/how-to/building-and-deployment.md) - Instalación, compilación y distribución paso a paso

### 📖 **Referencia Técnica**
- [**API Reference**](docs/reference/api-reference.md) - Documentación completa de funciones y módulos
- [**Proceso de Compilación**](docs/reference/build-process.md) - Detalles técnicos de PyInstaller y empaquetado

### 💡 **Explicación** (Understanding)
- [**Arquitectura del Sistema**](docs/explanation/architecture.md) - Diseño, decisiones técnicas y principios
- [**Formato QR WiFi**](docs/explanation/wifi-qr-format.md) - Estándar, algoritmos y decisiones de diseño

## Requisitos del Sistema

### Software Necesario
- **Python 3.7+** (para código fuente)
- **Sistema Operativo**: Windows 10/11, macOS 10.15+, Linux
- **Pip** (gestor de paquetes Python)

### Dependencias
```
qrcode[pil]>=7.0.0
```

### Verificación
```bash
# Verificar instalación
python -c "import qrcode; from PIL import Image; print('✅ Listo')"
```

## 📁 Estructura del Proyecto

```
Generador de QR Wifi/
├── 📁 docs/                    # 📚 Documentación estructurada
│   ├── 📁 how-to/             # 🛠️ Guías prácticas
│   ├── 📁 reference/          # 📖 Referencia técnica
│   └── 📁 explanation/        # 💡 Explicación conceptual
├── 📁 icons/                  # Íconos de la aplicación
├── 🔧 QR.py                   # Script principal con GUI
├── 🔧 build_exe.py            # Automatización de compilación
├── 🧪 test_qr.py              # Suite de pruebas
├── 📋 requirements.txt        # Dependencias Python
├── 📋 .gitignore             # Configuración Git
└── 📖 README.md              # Este archivo (router principal)
```

## 🎯 Uso Básico

1. **Ejecuta** la aplicación (desde código o ejecutable)
2. **Ingresa** el nombre de la red (SSID)
3. **Selecciona** el tipo de seguridad
4. **Ingresa** la contraseña (si aplica)
5. **Marca** si la red está oculta (opcional)
6. **Genera** el código QR
7. **Guarda** la imagen automáticamente

## 🔧 Desarrollo

### Configuración del Entorno
```bash
# Clonar repositorio
git clone https://github.com/Reyes-1718/Generador-de-QR-Wifi.git
cd "Generador de QR Wifi"

# Crear entorno virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# o
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar Pruebas
```bash
python test_qr.py
```

### Compilar Ejecutable
```bash
python build_exe.py
```

## 📦 Releases y Distribución

Los ejecutables pre-compilados están disponibles en [**GitHub Releases**](https://github.com/Reyes-1718/Generador-de-QR-Wifi/releases):

- ✅ **Windows**: `GeneradorQR-WiFi.exe`
- 🔄 **Linux/macOS**: Compilación desde fuente (ver [guía de despliegue](docs/how-to/building-and-deployment.md))

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Consulta nuestras guías:

1. Revisa la [arquitectura](docs/explanation/architecture.md) para entender el diseño
2. Lee la [referencia API](docs/reference/api-reference.md) para desarrollo
3. Sigue la [guía de construcción](docs/how-to/building-and-deployment.md) para setup

### Proceso
1. Fork el repositorio
2. Crea una rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Implementa cambios con pruebas
4. Envía Pull Request

## 📄 Licencia

Este proyecto está bajo **licencia MIT**. Consulta el archivo LICENSE para detalles completos.

## 🆘 Soporte

- 📋 [**Issues**](https://github.com/Reyes-1718/Generador-de-QR-Wifi/issues) - Reporta bugs o solicita features
- 📚 **Documentación** - Explora `/docs` para guías detalladas
- 🧪 **Pruebas** - Ejecuta `python test_qr.py` para validar funcionalidad

---

**¡Simplifica la conexión Wi-Fi con códigos QR!** 📱🔗

*Para documentación técnica detallada, explora la carpeta [`docs/`](docs/) que contiene guías especializadas siguiendo las mejores prácticas de Diátaxis.*
