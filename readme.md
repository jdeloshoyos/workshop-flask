
# WORKSHOP DEPARTAMENTO DE INFORMÁTICA BIOMÉDICA
## DESARROLLO DE APPS WEB CON PYTHON / FLASK

Este repo contiene el ejemplo completo trabajado en el workshop de desarrollo de apps web con Python y Flask, para futura referencia.

### Algunos recordatorios

- Creación y activación de entorno virtual:

        python -m venv env
        env/scripts/activate[.bat/.ps1]

- Instalación de paquetes/dependencias requeridos:

        pip install flask
        pip install gunicorn

- Guardar dependencias como un archivo:

        pip freeze > requirements.txt

- Variable de entorno para activar modo de desarrollo de servidor integrado Flask:

        FLASK_ENV=development
        python -m flask run

- Construir y ejecutar imagen Docker:

        docker build --tag flask-workshop .
        docker run --name flask-workshop --rm -p 5010:5010 flask-workshop
