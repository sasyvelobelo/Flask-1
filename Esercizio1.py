from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def html():
    return render_template("Esercizio1.html")

@app.route("/meteo")
def meteo():
    nRandom = random.randint(0,8)
    if nRandom <= 2:
        immagine = "/static/images/pioggia.png"
    elif nRandom <= 5:
        immagine = "/static/images/nuvole.png"
    else:
        immagine = "/static/images/sole.jpg"
    return render_template("meteo.html", meteo=immagine)





if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3248, debug=True)





