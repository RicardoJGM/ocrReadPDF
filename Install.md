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
