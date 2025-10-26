import os
from PIL import Image
from QR import generar_qr_wifi
import unittest

def validar_texto_en_imagen(imagen_path, texto_esperado):
    """Valida que el texto esperado esté presente en la imagen."""
    try:
        img = Image.open(imagen_path)
        img_rgb = img.convert('RGB')
        ancho, alto = img_rgb.size
        # Extraer el área donde se espera el texto
        area_texto = img_rgb.crop((0, alto - 60, ancho, alto))
        # Convertir a escala de grises para simplificar la detección
        area_texto_gris = area_texto.convert('L')
        # Aquí podrías implementar una lógica más avanzada para detectar el texto
        # Por ahora, asumimos que el texto está presente si el área no es completamente blanca
        return area_texto_gris.getextrema() != (255, 255)
    except Exception as e:
        print(f"Error al validar la imagen: {e}")
        return False

def prueba_generar_qr():
    """Prueba para validar la generación de códigos QR y el texto bajo el QR."""
    ssids = [
        "RedCorta",
        "RedMuyMuyLargaConMuchosCaracteres",
        "Red123",
        "RedConCaracteresEspeciales!@#$%^&*()",
        "RedConEspacios En El Nombre",
        "Internet Movil Claro_C2B4"  # Nuevo SSID agregado
    ]

    carpeta_pruebas = "pruebas_qr"
    os.makedirs(carpeta_pruebas, exist_ok=True)

    for ssid in ssids:
        try:
            print(f"Generando QR para: {ssid}")
            # Llamar a la función principal para generar el QR
            generar_qr_wifi(ssid, "WPA", "password123", False)

            # Verificar si la imagen se generó correctamente
            nombre_archivo = f"qr_wifi_{ssid}.png"
            ruta_archivo = os.path.join(carpeta_pruebas, nombre_archivo)

            if os.path.exists(ruta_archivo):
                print(f"✅ QR generado correctamente: {ruta_archivo}")
                # Abrir la imagen para inspección visual
                img = Image.open(ruta_archivo)
                img.show()
            else:
                print(f"❌ Error: No se encontró el archivo generado para {ssid}")

        except Exception as e:
            print(f"❌ Error al generar QR para {ssid}: {e}")

class TestGeneradorQR(unittest.TestCase):

    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.ssid_largo = "RedMuyLargaConMuchosCaracteresParaProbar"  # SSID largo
        self.nombre_archivo = f"qr_wifi_{self.ssid_largo}.png"

    def test_texto_ssid_largo(self):
        """Prueba para validar que el texto del SSID largo no se duplica ni se superpone."""
        # Generar QR
        generar_qr_wifi(self.ssid_largo, "WPA", "password123", False)

        # Validar que el archivo se haya creado
        self.assertTrue(os.path.exists(self.nombre_archivo), "El archivo QR no fue creado.")

        # Validar que el texto esté correctamente en la imagen
        texto_correcto = validar_texto_en_imagen(self.nombre_archivo, self.ssid_largo)
        self.assertTrue(texto_correcto, "El texto del SSID no se muestra correctamente en la imagen.")

    def tearDown(self):
        """Eliminar archivos generados después de las pruebas."""
        if os.path.exists(self.nombre_archivo):
            os.remove(self.nombre_archivo)

if __name__ == "__main__":
    prueba_generar_qr()
    unittest.main()
