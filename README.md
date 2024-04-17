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
1. Clona el repositorio desde [GitHub](https://github.com/tuusuario/nombre-proyecto).
2. Instala las dependencias necesarias con `pip install -r requirements.txt`.
3. Ejecuta el script con el comando `python script_ocr.py <ruta_del_archivo_pdf>`.
4. Los resultados se mostrarán en la consola o se guardarán en un archivo de salida especificado.

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
