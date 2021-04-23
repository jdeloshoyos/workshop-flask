#! /usr/bin/python3
# Encoding: UTF-8

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():

    if request.method == "POST":
        contenido = {
            "nombre": request.form.get("nombre", type=str, default=""),
            "mision": request.form.get("mision", type=str, default=""),
            "color": request.form.get("color", type=str, default=""),
            "caballeros": [
                "Lancelot",
                "Gawain",
                "Geraint",
                "Percival",
                "Bors the Younger",
                "Lamorak",
                "Kay",
                "Gareth",
                "Bedivere",
                "Gaheris",
                "Galahad",
                "Tristan"
            ]
        }
    else:
        contenido = ""

    return render_template(
        "home.html",
        contenido=contenido
    )