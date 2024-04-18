# Script de Python para Extracción de Texto de Documentos PDF mediante OCR

## Descripción del Proyecto
Este proyecto ofrece un script de Python que facilita la extracción de texto de documentos PDF utilizando la tecnología de Reconocimiento Óptico de Caracteres (OCR). Está diseñado para convertir documentos escaneados o imágenes en texto editable y buscable, lo cual es esencial para la digitalización y el análisis documental.

## Trasfondo
El manejo eficiente de documentos en formato PDF que solo existen en forma impresa o escaneada puede ser un desafío. Este script utiliza la tecnología OCR para transformar estos documentos en texto editable, superando los obstáculos que implica el manejo de grandes volúmenes de información no accesible digitalmente.

## Características Principales
- **Extracción de Texto con OCR**: Utiliza `EasyOCR`, un módulo de Python eficiente para la extracción de texto desde imágenes y documentos escaneados.
- **Soporte para Diversos Formatos de PDF**: Gracias a `Fitz`, el script puede manipular y extraer texto de varios formatos de documentos PDF, incluidos los más complejos como los que contienen imágenes o capas múltiples.
- **Preprocesamiento de Imágenes**: Implementa la biblioteca `Pillow` para optimizar imágenes antes de la extracción de texto, mejorando la precisión del OCR.
- **Interfaz de Línea de Comandos**: Ofrece una interfaz simple para usuarios, permitiendo la ejecución eficiente del script y facilitando la automatización de tareas de extracción de texto.

## Tecnologías Utilizadas
- **Python**: Lenguaje de programación principal del proyecto.
- **EasyOCR**: Modulo de python para extraer texto desde imagenes.
- **Pillow**: Utilizada para la manipulación de imágenes en Python, facilitando el preprocesamiento necesario para la extracción efectiva del texto.
- **Fitz**: Manipulacion de archivos a nivel código.

## Instalación y Uso
1. Clona el repositorio desde [GitHub](https://github.com/RicardoJGM/ocrReadPDF.git) con el comando `git clone`.
2. Asegurarse de tener instalado pip con el siguiente comando `python -m ensurepip --upgrade`
3. (Opcional) Crear un ambiente virtualizado en `python python -m venv <nombre_env>/env` y activarlo, en windows (`<ruta_env_creado>/env/Scripts/activate`); en linux (`source <ruta_env_creado>/env/bin/activate`)
4. Dirigirse al directorio clonado e instalar las dependencias necesarias con `pip install -r requirements.txt`.
5. Ejecutar el script de python `python readPDFwithOCR.py`.
6. Desde un API Client, POSTMAN de preferencia, por método POST mandamos el archivo pdf a extraer el texto al endpoint siguiente: `http://localhost:5000/subir`.
![image](https://github.com/RicardoJGM/ocrReadPDF/assets/112904134/602032a2-e237-4c77-9e12-d0a576badf3b)
![image](https://github.com/RicardoJGM/ocrReadPDF/assets/112904134/2e6fdbb9-f1f4-415b-a6f8-32c438e82e3f)
8. Los resultados se mostrarán en la consola o se guardarán en un archivo de salida especificado.
![image](https://github.com/RicardoJGM/ocrReadPDF/assets/112904134/17bcb990-9c48-425d-9f72-a3300c9add5b)

## Funcionamiento
![OCR](https://github.com/RicardoJGM/ocrReadPDF/assets/112904134/99465e7f-36c2-4c40-aa38-e21215547946)

## Contribuciones
Si estás interesado en mejorar este proyecto, tus contribuciones son bienvenidas. Sigue estos pasos para contribuir:
1. Realiza un fork del repositorio.
2. Crea una nueva rama para tus cambios (`git checkout -b mejora-nueva`).
3. Compromete tus cambios (`git commit -am 'Añade alguna mejora'`).
4. Empuja la rama (`git push origin mejora-nueva`).
5. Solicita un pull request.

## Autores
- Carlos Santamaría Solano
- Ricardo De Jesus Garcia Mejía
- Jose Adolfo Jimenez Solís
- Diego Azpe Carmona
