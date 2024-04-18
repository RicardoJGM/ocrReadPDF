#Creado por: 
# Ricardo de Jesús García Mejía - 200820130 - Ing. En Sistemas Computacionales
# Carlos Santamaría Solano - 200820130 - Ing. En Sistemas Computacionales
# Diego Azpe Carmano - 200820130 - Ing. En Sistemas Computacionales
# José Adolfo Jimenez Solis - 200820130 - Ing. En Sistemas Computacionales

from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
import cv2
import easyocr
import fitz
from PIL import Image

app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in 'pdf'

def pdf2png(nombre_archivo):
    ruta_directorio = "./Output_files/"
    nombre_raiz = os.path.splitext(os.path.basename(nombre_archivo))[0]
    archivos_generados = []

    if not os.path.exists(ruta_directorio):
        os.makedirs(ruta_directorio)
        print(f"Directorio '{ruta_directorio}' creado exitosamente.")

    existing_files = [f for f in os.listdir(ruta_directorio) if f.startswith(nombre_raiz) and f.endswith('.png')]
    if existing_files:
        archivos_generados = [os.path.join(ruta_directorio, f) for f in existing_files]

    archivo_pdf = fitz.open(nombre_archivo)
    for numero_pagina in range(archivo_pdf.page_count):
        page = archivo_pdf.load_page(numero_pagina)
        img = page.get_pixmap(matrix=fitz.Matrix(600/300, 600/300))
        img_pillow = Image.frombytes("RGB", [img.width, img.height], img.samples)
        nuevo_nombre_archivo = f"{ruta_directorio}{nombre_raiz}_{numero_pagina + 1}.png"
        if os.path.exists(nuevo_nombre_archivo):
            print(f"El archivo '{nuevo_nombre_archivo}' ya existe. Saltando...")
        else:
            img_pillow.save(nuevo_nombre_archivo, "PNG")
            archivos_generados.append(nuevo_nombre_archivo)
            print(f"El archivo '{nuevo_nombre_archivo}' guardado exitosamente.")
    
    archivo_pdf.close()
    return archivos_generados

class Reader():
    @staticmethod
    def leer_imagen(ruta_imagen):
        img = cv2.imread(ruta_imagen)
        return img
    
    def __init__(self):
        idiomas = ['en','es','fr','de','it','pt']
        self.reader = easyocr.Reader(idiomas, model_storage_directory=os.path.join('models'), download_enabled=True)
    
    def __call__(self, img):
        return self.extract_texto(img)
    
    def extract_texto(self, img):
        resultado = self.reader.readtext(img)
        texto_extraido = []
        for texto in filter(lambda x: x[-1] > .45, resultado):
            box, acc_texto, confidence = texto
            img = cv2.rectangle(img, [int(i) for i in box[0]], [int(i) for i in box[2]], (0, 255, 0), 2)
            texto_extraido.append(acc_texto)
        return texto_extraido, img

def create_texto(nombre_salida_archivo, texto):
    output_file_path = f"./Output_files/{nombre_salida_archivo[:-4]}.txt"
    text_joined = ','.join(texto)
    text_completion = text_joined[:-1]
    with open(output_file_path, 'w') as file2write:
        file2write.write(text_completion)
    print(f"Archivo txt para {nombre_salida_archivo} generado con exito")
    return text_completion 

@app.route('/subir', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No se ha proporcionado ningún archivo'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No se ha seleccionado ningún archivo'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join('./', filename)
        file.save(filepath)
        
        archivos_generados = pdf2png(filepath)
        reader = Reader()
        todo_texto_extraido = []
        for archivo_generado in archivos_generados:
            imagen = reader.leer_imagen(archivo_generado)
            texto_extraido, _ = reader(imagen)
            todo_texto_extraido.extend(texto_extraido)

        output_text = create_texto(filename, todo_texto_extraido)

        return jsonify({'texto_extraido': output_text})

    else:
        return jsonify({'error': 'Extensión de archivo no permitida'})

if __name__ == '__main__':
    app.run()
