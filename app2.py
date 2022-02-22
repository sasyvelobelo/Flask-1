#realizzare un server web che visualizzi l'ora e colori lo sfondo in base all'orario: un colore per la mattina, uno per il pomeriggio, uno per la sera e uno per la notte.

from flask import Flask, request, render_template
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index1.html")

@app.route("/getTime", methods=['GET'])
def getTime():
    print("browser time: ", request.args.get("time"))
    print("server time : ", time.strftime('%A %B, %d %Y %H:%M:%S'));
    return "Done"