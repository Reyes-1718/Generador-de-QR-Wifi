import qrcode
import os
import re
import sys
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import messagebox, filedialog

def limpiar_consola():
    """Limpia la pantalla de la consola para una mejor visualización."""
    os.system('cls' if os.name == 'nt' else 'clear')

def escapar_caracteres_wifi(texto):
    """Escapa caracteres especiales para el formato WiFi QR según el estándar."""
    if not texto:
        return ""
    # Escapar caracteres especiales: ; , : " \
    caracteres_especiales = {';': '\\;', ',': '\\,', ':': '\\:', '"': '\\"', '\\': '\\\\'}
    for char, escaped in caracteres_especiales.items():
        texto = texto.replace(char, escaped)
    return texto

def limpiar_nombre_archivo(nombre):
    """Limpia el nombre del archivo removiendo caracteres no válidos."""
    # Remover caracteres no válidos para nombres de archivo
    nombre_limpio = re.sub(r'[<>:"/\\|?*]', '_', nombre)
    # Limitar longitud y remover espacios al inicio/final
    nombre_limpio = nombre_limpio.strip()[:50]
    return nombre_limpio if nombre_limpio else "wifi_qr"

def verificar_dependencias():
    """Verifica que las dependencias necesarias estén instaladas."""
    try:
        import qrcode
        from PIL import Image, ImageDraw, ImageFont
        return True
    except ImportError:
        print("❌ Error: Los módulos 'qrcode' y 'PIL' no están instalados.")
        print("   Instálalos ejecutando: pip install qrcode[pil]")
        return False

def generar_qr_wifi(ssid, tipo_seguridad, password, oculta):
    """
    Genera un código QR para una red Wi-Fi con los parámetros proporcionados.
    """
    # Escapar caracteres especiales en el SSID y la contraseña
    ssid_escapado = escapar_caracteres_wifi(ssid)
    password_escapado = escapar_caracteres_wifi(password)

    # Construir la cadena de texto para el QR en el formato estándar
    texto_qr = f"WIFI:S:{ssid_escapado};T:{tipo_seguridad};P:{password_escapado};H:{'true' if oculta else 'false'};;"

    # Configuración del QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Añadir los datos y crear la imagen
    qr.add_data(texto_qr)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convertir a RGB para poder añadir texto
    img_rgb = img.convert('RGB')

    # Crear una imagen más grande para incluir el texto
    ancho_original, alto_original = img_rgb.size
    alto_texto = 60  # Espacio para el texto
    img_final = Image.new('RGB', (ancho_original, alto_original + alto_texto), 'white')

    # Pegar el QR en la imagen final
    img_final.paste(img_rgb, (0, 0))

    # Añadir texto con el nombre de la red
    draw = ImageDraw.Draw(img_final)

    # Intentar usar una fuente del sistema, si no está disponible usar la por defecto
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    # Dividir el nombre de la red en líneas si es muy largo, respetando palabras completas
    max_caracteres_por_linea = 16
    texto_red = ssid
    palabras = texto_red.split()
    lineas = []
    linea_actual = ""
    
    for palabra in palabras:
        # Si la palabra es más larga que el máximo de caracteres permitidos, la dividimos
        if len(palabra) > max_caracteres_por_linea:
            if linea_actual:
                lineas.append(linea_actual)
                linea_actual = ""
            # Dividir la palabra larga en fragmentos
            for i in range(0, len(palabra), max_caracteres_por_linea):
                lineas.append(palabra[i:i+max_caracteres_por_linea])
        # Si agregar la palabra no excede el límite
        elif len(linea_actual + " " + palabra if linea_actual else palabra) <= max_caracteres_por_linea:
            if linea_actual:
                linea_actual += " " + palabra
            else:
                linea_actual = palabra
        # Si agregar la palabra excede el límite, empezamos una nueva línea
        else:
            lineas.append(linea_actual)
            linea_actual = palabra
    
    # No olvidamos agregar la última línea si hay contenido
    if linea_actual:
        lineas.append(linea_actual)

    # Ajustar el espaciado entre líneas dinámicamente
    espaciado_entre_lineas = 30  # Espaciado fijo para evitar superposición

    # Calcular posición inicial para centrar todas las líneas y asegurar que sean visibles
    # Ajustamos la posición inicial más arriba 
    posicion_inicial_y = alto_original + 10  # Reducido de 20 a 10 para subir el texto
    
    # Calcular altura total que ocupará el texto (para múltiples líneas)
    altura_total_texto = len(lineas) * espaciado_entre_lineas
    
    # Si hay riesgo de que el texto se salga, ajustar la posición inicial
    if posicion_inicial_y + altura_total_texto > alto_original + alto_texto - 10:  # 10px de margen inferior
        # Ajustar para centrar verticalmente
        posicion_inicial_y = alto_original + ((alto_texto - altura_total_texto) // 2)

    # Dibujar cada línea con el espaciado ajustado
    for idx, linea in enumerate(lineas):
        bbox = draw.textbbox((0, 0), linea, font=font)
        texto_ancho = bbox[2] - bbox[0]
        texto_x = (ancho_original - texto_ancho) // 2
        texto_y = posicion_inicial_y + (idx * espaciado_entre_lineas)
        draw.text((texto_x, texto_y), linea, fill="black", font=font)

    # Guardar la imagen con nombre limpio
    nombre_base = limpiar_nombre_archivo(ssid)
    nombre_archivo = f"qr_wifi_{nombre_base}.png"

    try:
        img_final.save(nombre_archivo)
        print(f"¡Éxito! El código QR se ha guardado como: '{nombre_archivo}'")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def generar_qr_wifi_interfaz(ssid, tipo_seguridad, password, oculta):
    """
    Función adaptada para la interfaz gráfica, genera el código QR y lo guarda como imagen.
    """
    ssid = ssid.get().strip()
    tipo_seguridad = tipo_seguridad.get()
    password = password.get().strip()
    oculta = "true" if oculta.get() else "false"

    if not ssid:
        messagebox.showerror("Error", "El nombre de la red no puede estar vacío.")
        return

    if tipo_seguridad in ["WPA", "WEP"] and not password:
        messagebox.showerror("Error", "La contraseña no puede estar vacía para redes WPA/WEP.")
        return

    ssid_escapado = escapar_caracteres_wifi(ssid)
    password_escapado = escapar_caracteres_wifi(password)

    texto_qr = f"WIFI:S:{ssid_escapado};T:{tipo_seguridad};P:{password_escapado};H:{oculta};;"

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(texto_qr)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    # Convertir a RGB para añadir texto
    img_rgb = img.convert('RGB')
    ancho_original, alto_original = img_rgb.size
    alto_texto = 70  # Aumentado de 60 a 70 para dar más espacio al texto
    img_final = Image.new('RGB', (ancho_original, alto_original + alto_texto), 'white')
    img_final.paste(img_rgb, (0, 0))

    draw = ImageDraw.Draw(img_final)
    try:
        font = ImageFont.truetype("arial.ttf", 20)
    except:
        font = ImageFont.load_default()

    texto_red = ssid

    # Dividir el nombre de la red en líneas si es muy largo, respetando palabras completas
    max_caracteres_por_linea = 16
    palabras = texto_red.split()
    lineas = []
    linea_actual = ""
    
    for palabra in palabras:
        # Si la palabra es más larga que el máximo de caracteres permitidos, la dividimos
        if len(palabra) > max_caracteres_por_linea:
            if linea_actual:
                lineas.append(linea_actual)
                linea_actual = ""
            # Dividir la palabra larga en fragmentos
            for i in range(0, len(palabra), max_caracteres_por_linea):
                lineas.append(palabra[i:i+max_caracteres_por_linea])
        # Si agregar la palabra no excede el límite
        elif len(linea_actual + " " + palabra if linea_actual else palabra) <= max_caracteres_por_linea:
            if linea_actual:
                linea_actual += " " + palabra
            else:
                linea_actual = palabra
        # Si agregar la palabra excede el límite, empezamos una nueva línea
        else:
            lineas.append(linea_actual)
            linea_actual = palabra
    
    # No olvidamos agregar la última línea si hay contenido
    if linea_actual:
        lineas.append(linea_actual)

    # Ajustar el espaciado entre líneas dinámicamente
    espaciado_entre_lineas = 30  # Espaciado fijo para evitar superposición

    # Calcular posición inicial para centrar todas las líneas y asegurar que sean visibles
    # Ajustamos la posición inicial más arriba 
    posicion_inicial_y = alto_original + 10  # Reducido de 20 a 10 para subir el texto
    
    # Calcular altura total que ocupará el texto (para múltiples líneas)
    altura_total_texto = len(lineas) * espaciado_entre_lineas
    
    # Si hay riesgo de que el texto se salga, ajustar la posición inicial
    if posicion_inicial_y + altura_total_texto > alto_original + alto_texto - 10:  # 10px de margen inferior
        # Ajustar para centrar verticalmente
        posicion_inicial_y = alto_original + ((alto_texto - altura_total_texto) // 2)

    # Dibujar cada línea con el espaciado ajustado
    for idx, linea in enumerate(lineas):
        bbox = draw.textbbox((0, 0), linea, font=font)
        texto_ancho = bbox[2] - bbox[0]
        texto_x = (ancho_original - texto_ancho) // 2
        texto_y = posicion_inicial_y + (idx * espaciado_entre_lineas)
        draw.text((texto_x, texto_y), linea, fill="black", font=font)

    nombre_base = limpiar_nombre_archivo(ssid)
    nombre_archivo = f"qr_wifi_{nombre_base}.png"

    try:
        img_final.save(nombre_archivo)
        messagebox.showinfo("Éxito", f"El código QR se ha guardado como: {nombre_archivo}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar el archivo: {e}")

def interfaz_grafica():
    """Crea una interfaz gráfica para el programa."""
    def generar_qr_desde_gui():
        ssid = entrada_ssid.get().strip()
        tipo_seguridad = opcion_seguridad.get()
        password = entrada_password.get().strip()
        oculta = "true" if var_oculta.get() else "false"

        if not ssid:
            messagebox.showerror("Error", "El nombre de la red no puede estar vacío.")
            return

        if tipo_seguridad in ["WPA", "WEP"] and not password:
            messagebox.showerror("Error", "La contraseña no puede estar vacía para redes WPA/WEP.")
            return

        ssid_escapado = escapar_caracteres_wifi(ssid)
        password_escapado = escapar_caracteres_wifi(password)

        texto_qr = f"WIFI:S:{ssid_escapado};T:{tipo_seguridad};P:{password_escapado};H:{oculta};;"

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto_qr)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Convertir a RGB para añadir texto
        img_rgb = img.convert('RGB')
        ancho_original, alto_original = img_rgb.size
        alto_texto = 70  # Aumentado de 60 a 70 para dar más espacio al texto
        img_final = Image.new('RGB', (ancho_original, alto_original + alto_texto), 'white')
        img_final.paste(img_rgb, (0, 0))

        draw = ImageDraw.Draw(img_final)
        try:
            font = ImageFont.truetype("arial.ttf", 20)
        except:
            font = ImageFont.load_default()

        texto_red = ssid

        # Dividir el nombre de la red en líneas si es muy largo, respetando palabras completas
        max_caracteres_por_linea = 16
        palabras = texto_red.split()
        lineas = []
        linea_actual = ""
        
        for palabra in palabras:
            # Si la palabra es más larga que el máximo de caracteres permitidos, la dividimos
            if len(palabra) > max_caracteres_por_linea:
                if linea_actual:
                    lineas.append(linea_actual)
                    linea_actual = ""
                # Dividir la palabra larga en fragmentos
                for i in range(0, len(palabra), max_caracteres_por_linea):
                    lineas.append(palabra[i:i+max_caracteres_por_linea])
            # Si agregar la palabra no excede el límite
            elif len(linea_actual + " " + palabra if linea_actual else palabra) <= max_caracteres_por_linea:
                if linea_actual:
                    linea_actual += " " + palabra
                else:
                    linea_actual = palabra
            # Si agregar la palabra excede el límite, empezamos una nueva línea
            else:
                lineas.append(linea_actual)
                linea_actual = palabra
    
        # No olvidamos agregar la última línea si hay contenido
        if linea_actual:
            lineas.append(linea_actual)

        # Ajustar el espaciado entre líneas dinámicamente
        espaciado_entre_lineas = 30  # Espaciado fijo para evitar superposición

        # Calcular posición inicial para centrar todas las líneas y asegurar que sean visibles
        # Ajustamos la posición inicial más arriba 
        posicion_inicial_y = alto_original + 10  # Reducido de 20 a 10 para subir el texto
        
        # Calcular altura total que ocupará el texto (para múltiples líneas)
        altura_total_texto = len(lineas) * espaciado_entre_lineas
        
        # Si hay riesgo de que el texto se salga, ajustar la posición inicial
        if posicion_inicial_y + altura_total_texto > alto_original + alto_texto - 10:  # 10px de margen inferior
            # Ajustar para centrar verticalmente
            posicion_inicial_y = alto_original + ((alto_texto - altura_total_texto) // 2)

        # Dibujar cada línea con el espaciado ajustado
        for idx, linea in enumerate(lineas):
            bbox = draw.textbbox((0, 0), linea, font=font)
            texto_ancho = bbox[2] - bbox[0]
            texto_x = (ancho_original - texto_ancho) // 2
            texto_y = posicion_inicial_y + (idx * espaciado_entre_lineas)
            draw.text((texto_x, texto_y), linea, fill="black", font=font)

        nombre_base = limpiar_nombre_archivo(ssid)
        nombre_archivo = f"qr_wifi_{nombre_base}.png"

        try:
            img_final.save(nombre_archivo)
            messagebox.showinfo("Éxito", f"El código QR se ha guardado como: {nombre_archivo}")
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar el archivo: {e}")

    def mostrar_contraseña():
        if entrada_password.cget("show") == "*":
            entrada_password.config(show="")
            boton_mostrar_password.config(text="Ocultar Contraseña")
        else:
            entrada_password.config(show="*")
            boton_mostrar_password.config(text="Mostrar Contraseña")

    def limpiar_campos():
        entrada_ssid.delete(0, tk.END)
        entrada_password.delete(0, tk.END)
        var_oculta.set(False)
        opcion_seguridad.set("WPA")

    ventana = tk.Tk()
    ventana.title("Generador de Código QR para Wi-Fi")

    tk.Label(ventana, text="Nombre de la red (SSID):").pack(pady=5)
    entrada_ssid = tk.Entry(ventana, width=30)
    entrada_ssid.pack(pady=5)

    tk.Label(ventana, text="Tipo de seguridad:").pack(pady=5)
    opcion_seguridad = tk.StringVar(value="WPA")
    tk.Radiobutton(ventana, text="WPA/WPA2", variable=opcion_seguridad, value="WPA").pack()
    tk.Radiobutton(ventana, text="WEP", variable=opcion_seguridad, value="WEP").pack()
    tk.Radiobutton(ventana, text="Ninguna (red abierta)", variable=opcion_seguridad, value="nopass").pack()

    tk.Label(ventana, text="Contraseña:").pack(pady=5)
    entrada_password = tk.Entry(ventana, width=30, show="*")
    entrada_password.pack(pady=5)

    boton_mostrar_password = tk.Button(ventana, text="Mostrar Contraseña", command=mostrar_contraseña)
    boton_mostrar_password.pack(pady=5)

    var_oculta = tk.BooleanVar()
    tk.Checkbutton(ventana, text="¿La red está oculta?", variable=var_oculta).pack(pady=5)

    tk.Button(ventana, text="Generar Código QR", command=generar_qr_desde_gui).pack(pady=20)
    tk.Button(ventana, text="Limpiar Campos", command=limpiar_campos).pack(pady=5)

    ventana.mainloop()


if __name__ == "__main__":
    # Si se ejecuta como script principal, mostrar la interfaz gráfica
    interfaz_grafica()
