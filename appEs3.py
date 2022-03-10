#realizzare un server web che permetta di conoscere capoluoghi di regione.
#l'utente inserisce il nome della regione e il programma restituisce il capoluogo di regione.
#caricare i capoluoghi di regione e le regioni in un'opportuna struttura dati.

#modificare poi l'esercizio precedente per permettere all'utente di inserire un capoluogo e di avere la regione in cui si trova
#l'utente sceglie se avere la regione o il capoluogo selezionando un radio botton.

from flask import Flask,render_template, request
app = Flask(__name__)
lst= []

@app.route('/', methods=['GET'])       #home page
def home():
    return render_template('homeEs3.html')


    
@app.route('/home', methods=['GET'])
def es():
    input = request.args['input']
    radioButton = request.args['CR']

    lst.append({'input':input, 'radioButton': radioButton})

    for elemento in lst:

    if input == capoluoghiRegione.keys() and radioButton == 'C':
           return capoluoghiRegione.values()
    else:
           return render_template('errorRes3.html')

    if input == capoluoghiRegione.values() and radioButton == 'R':
           return capoluoghiRegione.keys()
    else:
           return render_template('errorCes3.html')
    



capoluoghiRegione = {'Abruzzo': 'LAquila', 'Basilicata': 'Potenza', 'Calabria': 'Catanzaro', 'Campania': 'Napoli', 'Emilia-Romagna': 'Bologna', 'Friuli-Venezia Giulia': 'Trieste', 'Lazio': 'Roma', 'Liguria': 'Genova',
                     'Lombardia': 'Milano', 'Marche': 'Ancona', 'Molise': 'Campobasso', 'Piemonte': 'Torino', 'Puglia': 'Bari', 'Sardegna': 'Cagliari', 'Sicilia': 'Palermo', 'Toscana': 'Firenze', 'Trentino-Alto Adige': 'Trento',
                     'Umbria': 'Perugia', 'Valle d Aosta': 'Aosta', 'Veneto': 'Venezia'}















if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)