#realizzare un server web che permetta di conoscere capoluoghi di regione.
#l'utente inserisce il nome della regione e il programma restituisce il capoluogo di regione.
#caricare i capoluoghi di regione e le regioni in un'opportuna struttura dati.

#modificare poi l'esercizio precedente per permettere all'utente di inserire un capoluogo e di avere la regione in cui si trova
#l'utente sceglie se avere la regione o il capoluogo selezionando un radio botton.

from flask import Flask,render_template, request
app = Flask(__name__)


dizionario = {'Abruzzo': 'LAquila', 'Basilicata': 'Potenza', 'Calabria': 'Catanzaro', 'Campania': 'Napoli', 'Emilia-Romagna': 'Bologna', 'Friuli-Venezia Giulia': 'Trieste', 'Lazio': 'Roma', 'Liguria': 'Genova',
                     'Lombardia': 'Milano', 'Marche': 'Ancona', 'Molise': 'Campobasso', 'Piemonte': 'Torino', 'Puglia': 'Bari', 'Sardegna': 'Cagliari', 'Sicilia': 'Palermo', 'Toscana': 'Firenze', 'Trentino-Alto Adige': 'Trento',
                     'Umbria': 'Perugia', 'Valle d Aosta': 'Aosta', 'Veneto': 'Venezia'}


@app.route('/', methods=['GET'])       #home page
def home():
    return render_template('homeEs3.html')


    
@app.route('/home', methods=['GET'])
def es():
    scelta = request.args["Scelta"]
    if scelta == "R":
        regione = request.args["RegCap"]
        for key, value in dizionario.items():
            if regione == key:
                capoluogo = value
                return render_template("risultatoes3.html", risposta = capoluogo)
        return "<h1>Errore</h1>"              
    else:
        capoluogo = request.args["RegCap"]
        for key, value in dizionario.items():
            if capoluogo == value:
                regione = key
                return render_template("risultatoes3.html", risposta = regione)
        return "<h1>Errore</h1>"

    
    
      



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)