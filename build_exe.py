"""
Script para crear ejecutable del generador de QR WiFi
Ejecutar: py build_exe.py
"""

import os
import subprocess
import sys

def crear_ejecutable():
    """Crea un ejecutable del programa QR.py usando PyInstaller."""
    
    print("===========================================")
    print("  Creando ejecutable del Generador QR WiFi  ")
    print("===========================================")
    
    # Verificar si PyInstaller está instalado
    try:
        import PyInstaller
        print("✅ PyInstaller encontrado.")
    except ImportError:
        print("❌ PyInstaller no está instalado.")
        print("   Instalando PyInstaller...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"], check=True)
        print("✅ PyInstaller instalado correctamente.")
    
    # Configuración del ejecutable
    nombre_ejecutable = "GeneradorQR-WiFi"
    
    # Comando para crear el ejecutable
    comando = [
        "pyinstaller",
        "--onefile",                    # Un solo archivo ejecutable
        "--noconsole",                  # Sin mostrar ventana de consola
        "--name", nombre_ejecutable,    # Nombre del ejecutable
        "--clean",                      # Limpiar archivos temporales
        "--noconfirm",                  # No pedir confirmación
        "QR.py"                         # Archivo fuente
    ]
    
    print(f"\n🔄 Creando ejecutable '{nombre_ejecutable}.exe'...")
    print("   Esto puede tomar unos minutos...")
    
    try:
        # Ejecutar PyInstaller
        resultado = subprocess.run(comando, capture_output=True, text=True, check=True)
        
        print("\n✅ ¡Ejecutable creado exitosamente!")
        print(f"📁 Ubicación: dist/{nombre_ejecutable}.exe")
        print("\n📋 Archivos generados:")
        print(f"   - dist/{nombre_ejecutable}.exe  (ejecutable final)")
        print(f"   - build/  (archivos temporales)")
        print(f"   - {nombre_ejecutable}.spec  (archivo de configuración)")
        
        # Verificar si el ejecutable existe
        ruta_ejecutable = f"dist/{nombre_ejecutable}.exe"
        if os.path.exists(ruta_ejecutable):
            tamaño = os.path.getsize(ruta_ejecutable) / (1024 * 1024)  # MB
            print(f"\n📊 Tamaño del ejecutable: {tamaño:.1f} MB")
            
            print("\n🚀 Para usar el ejecutable:")
            print(f"   1. Navega a la carpeta 'dist'")
            print(f"   2. Ejecuta '{nombre_ejecutable}.exe'")
            print(f"   3. ¡Listo! El programa funcionará sin Python instalado")
            
        else:
            print("❌ Error: El ejecutable no se creó correctamente.")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error al crear el ejecutable: {e}")
        print("   Salida del error:")
        print(e.stderr)
        
    except Exception as e:
        print(f"❌ Error inesperado: {e}")

if __name__ == "__main__":
    crear_ejecutable()
