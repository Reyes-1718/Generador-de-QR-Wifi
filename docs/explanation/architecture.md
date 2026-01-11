# Arquitectura del Sistema

Esta sección explica la arquitectura del Generador de QR WiFi, sus decisiones de diseño, patrones implementados y consideraciones técnicas que guían su desarrollo.

## Visión General de la Arquitectura

El Generador de QR WiFi es una aplicación de escritorio que combina generación de códigos QR con interfaz gráfica intuitiva. Su arquitectura sigue principios de simplicidad, modularidad y mantenibilidad.

### Componentes Principales

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Interfaz      │    │   Lógica de     │    │   Generación    │
│   Gráfica       │◄──►│   Negocio       │◄──►│   QR + Imagen   │
│   (Tkinter)     │    │   (Validación)  │    │   (qrcode)      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 ▼
                    ┌─────────────────┐
                    │   Persistencia  │
                    │   (Sistema de   │
                    │   Archivos)     │
                    └─────────────────┘
```

## Principios de Diseño

### 1. Separación de Responsabilidades

Cada función tiene una responsabilidad única y bien definida:

- **Generación QR**: `generar_qr_wifi()` - Lógica pura de creación de códigos
- **Interfaz**: `interfaz_grafica()` - Gestión de UI y eventos
- **Utilidades**: Funciones helper para validación y formateo
- **Compilación**: `build_exe.py` - Automatización de empaquetado

### 2. Simplicidad sobre Complejidad

- **Lenguaje**: Python nativo sin frameworks complejos
- **Dependencias**: Mínimas y ampliamente utilizadas
- **Arquitectura**: Monolítica intencional para facilidad de mantenimiento

### 3. Experiencia de Usuario Primero

- **Interfaz intuitiva**: Campos claramente etiquetados
- **Validación en tiempo real**: Feedback inmediato
- **Manejo de errores**: Mensajes claros y accionables

## Patrón Arquitectónico

### Adaptador para Interfaz Gráfica

El sistema utiliza un patrón adaptador para conectar la lógica de negocio con la interfaz gráfica:

```python
# Función pura (lógica de negocio)
def generar_qr_wifi(ssid, tipo_seguridad, password, oculta):
    # Lógica independiente de UI
    pass

# Adaptador para Tkinter
def generar_qr_wifi_interfaz(ssid_var, tipo_var, password_var, oculta_var):
    # Extrae valores de widgets Tkinter
    # Llama a función pura
    # Maneja mensajes de UI
    pass
```

**Beneficios:**
- **Testabilidad**: Lógica pura fácilmente testeable
- **Reutilización**: Función core usable desde CLI o API
- **Mantenibilidad**: Cambios en UI no afectan lógica de negocio

## Componentes Técnicos

### Generación de Códigos QR

#### Estándar WiFi QR

El sistema implementa el estándar definido en la especificación QR Code:

```
WIFI:S:<SSID>;T:<TYPE>;P:<PASSWORD>;H:<HIDDEN>;;
```

**Campos:**
- **S (SSID)**: Nombre de la red
- **T (Type)**: WPA, WEP, nopass
- **P (Password)**: Contraseña (opcional)
- **H (Hidden)**: true/false para redes ocultas

#### Manejo de Caracteres Especiales

Implementa escaping según estándar:
- `;` → `\;`
- `,` → `\,`
- `:` → `\:`
- `"` → `\"`
- `\` → `\\`

### Procesamiento de Imágenes

#### Composición de Imagen Final

```
┌─────────────────┐
│       QR        │ ← Código QR generado
│     Code        │
├─────────────────┤
│   Network Name  │ ← Texto del SSID
│   (Multi-line)  │
└─────────────────┘
```

**Especificaciones:**
- **Tamaño QR**: Configurable via qrcode.QRCode
- **Texto**: Arial 20pt, centrado, multi-línea
- **Formato**: PNG con transparencia

#### Algoritmo de Ajuste de Texto

1. **División por palabras**: Respeta límites de palabras completas
2. **Límite de caracteres**: Máximo 16 por línea
3. **Centrado dinámico**: Ajusta posición según número de líneas
4. **Espaciado fijo**: 30px entre líneas para consistencia

## Gestión de Estado

### Estado de la Aplicación

La aplicación mantiene estado mínimo y efímero:

- **Campos de entrada**: Valores actuales del formulario
- **Preferencias**: Tipo de seguridad seleccionado
- **Estado de validación**: Resultado de últimas validaciones

### Persistencia

- **Archivos generados**: QR codes guardados como PNG
- **Configuración**: No persistente (reinicia con aplicación)
- **Historial**: No mantenido (por simplicidad)

## Manejo de Errores

### Estrategias Implementadas

#### Validación de Entrada
- **Campos requeridos**: SSID obligatorio
- **Dependencias condicionales**: Contraseña requerida para WPA/WEP
- **Formato de archivo**: Limpieza automática de nombres

#### Recuperación de Errores
- **Dependencias faltantes**: Instalación automática cuando posible
- **Archivos no encontrados**: Mensajes informativos
- **Errores de sistema**: Captura y presentación amigable

#### Logging y Debugging
- **Consola**: Información detallada durante desarrollo
- **Mensajes de usuario**: Feedback claro y conciso
- **Códigos de error**: Identificables para troubleshooting

## Consideraciones de Rendimiento

### Optimizaciones Implementadas

#### Generación QR
- **Configuración óptima**: Parámetros balanceados para velocidad/calidad
- **Procesamiento por lotes**: No aplicable (generación individual)
- **Caché**: No implementado (operaciones simples)

#### Interfaz Gráfica
- **Actualización selectiva**: Solo campos afectados por cambios
- **Validación lazy**: Solo cuando necesario
- **Recursos mínimos**: Tkinter nativo sin overhead

### Limitaciones Conocidas

#### Memoria
- **Imágenes grandes**: QR codes consumen memoria proporcional al tamaño
- **Múltiples generaciones**: No optimizado para batch processing

#### CPU
- **Generación síncrona**: UI bloquea durante creación de QR
- **Procesamiento de texto**: Algoritmo simple, efectivo para casos típicos

## Seguridad

### Consideraciones Implementadas

#### Validación de Entrada
- **Sanitización**: Escape de caracteres especiales
- **Longitud limitada**: Prevención de ataques de buffer
- **Tipo de datos**: Validación estricta de tipos

#### Manejo de Archivos
- **Nombres seguros**: Eliminación de caracteres peligrosos
- **Rutas controladas**: Escritura solo en directorio actual
- **Permisos**: No requiere elevación de privilegios

### Limitaciones de Seguridad

#### Contraseñas en Memoria
- **Almacenamiento temporal**: Contraseñas permanecen en memoria
- **No encriptadas**: Texto plano durante procesamiento
- **Limpieza**: No implementada (depende del GC de Python)

#### Distribución
- **Ejecutables**: No firmados digitalmente
- **Dependencias**: No verificadas por integridad

## Escalabilidad y Mantenibilidad

### Modularidad

El código está organizado en funciones cohesivas:

- **Utilidades**: `limpiar_consola()`, `escapar_caracteres_wifi()`
- **Generación**: `generar_qr_wifi()` y variantes
- **Interfaz**: `interfaz_grafica()` y handlers
- **Compilación**: `build_exe.py` separado

### Extensibilidad

Puntos de extensión identificados:

- **Nuevos tipos de seguridad**: Fácil agregar a radio buttons
- **Formatos de salida**: Arquitectura preparada para PDF, SVG
- **Validaciones personalizadas**: Framework extensible
- **Internacionalización**: Separación de strings del código

### Testing

Estrategia de testing recomendada:

- **Unit tests**: Funciones puras (`generar_qr_wifi`)
- **Integration tests**: Flujo completo GUI
- **Visual tests**: Verificación de QR codes generados
- **Cross-platform**: Testing en Windows/Linux/macOS

## Decisiones de Tecnología

### Python como Lenguaje Principal

**Razones:**
- **Simplicidad**: Sintaxis clara, aprendizaje rápido
- **Ecosistema**: Amplia disponibilidad de bibliotecas
- **Portabilidad**: Ejecutable en múltiples plataformas
- **Mantenibilidad**: Comunidad activa y documentación extensa

### Tkinter para Interfaz Gráfica

**Razones:**
- **Incluido**: Parte del estándar de Python
- **Suficiente**: Completo para necesidades de la aplicación
- **Portabilidad**: Funciona en Windows, Linux, macOS
- **Liviano**: Sin dependencias adicionales complejas

### qrcode + Pillow para Generación

**Razones:**
- **Especializadas**: Diseñadas específicamente para el propósito
- **Estables**: Mantenidas activamente
- **Flexibles**: API rica para personalización
- **Integradas**: Funcionan bien juntas

### PyInstaller para Distribución

**Razones:**
- **Maduro**: Herramienta estable y ampliamente usada
- **Multiplataforma**: Soporte para Windows, Linux, macOS
- **Configurable**: Gran control sobre el proceso de empaquetado
- **Comunidad**: Amplio soporte y documentación

## Evolución Futura

### Mejoras Arquitectónicas Consideradas

#### Separación en Módulos
```
qr_generator/
├── __init__.py
├── core.py          # Lógica de generación
├── ui.py            # Interfaz gráfica
├── utils.py         # Utilidades
└── cli.py           # Interfaz de línea de comandos
```

#### Arquitectura MVC
```
├── models/          # Datos y validación
├── views/           # Interfaz de usuario
├── controllers/     # Lógica de control
└── services/        # Servicios externos
```

#### API REST
- **Servidor web**: Exposición como servicio web
- **Formatos múltiples**: JSON, PNG, SVG
- **Autenticación**: Para uso empresarial

### Escalabilidad Horizontal

#### Procesamiento Paralelo
- **Workers**: Generación concurrente de múltiples QR
- **Queue**: Sistema de colas para procesamiento batch
- **Load balancing**: Distribución de carga

#### Almacenamiento Distribuido
- **Cloud storage**: AWS S3, Google Cloud Storage
- **CDN**: Distribución global de assets
- **Cache**: Redis para QR codes frecuentes

### Monitoreo y Observabilidad

#### Métricas
- **Performance**: Tiempo de generación, tamaño de archivos
- **Usage**: Número de QR generados, tipos de red
- **Errors**: Tasa de fallos, tipos de error

#### Logging
- **Estructurado**: JSON logs para análisis
- **Niveles**: DEBUG, INFO, WARN, ERROR
- **Rotación**: Gestión automática de archivos de log

Esta arquitectura proporciona una base sólida para el crecimiento futuro mientras mantiene la simplicidad que caracteriza al proyecto.