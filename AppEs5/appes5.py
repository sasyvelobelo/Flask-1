# si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta. L'utente deve poter inserire il nome della squadra 
# e la data di fondazione e la cità. Deve inoltre poter effettuare delle ricerche inserendo uno dei valori delle colonne e 
# ottenendo i dati presenti.



from flask import Flask, render_template,request
app = Flask(__name__)
import pandas as pd

@app.route('/', methods=['GET'])
def home():
    return render_template('squadraHome.html')

@app.route('/inserisci', methods=['GET'])
def inserisci():
    return render_template('inserisci.html')

@app.route('/dati', methods=['GET'])
def dati():
    # inserimento dei dati nel file csv
    # lettura dei dati dal form html 
    squadra = request.args['Squadra']
    anno = request.args['Anno']
    citta = request.args['Citta']
    # lettura dei dati daal file nel dataframe
    df1 = pd.read_csv('/workspace/Flask/AppEs5/dati.csv')
    # aggiungiamo i nuovi dati nel dataframe 
    nuovi_dati = {'squadra':squadra,'anno':anno,'citta':citta}
    
    df1 = df1.append(nuovi_dati,ignore_index=True)
    # salviamo il dataframe sul file dati.csv
    df1.to_csv('/workspace/Flask/AppEs5/dati.csv', index=False)
    return df1.to_html()   #lo converte in codice html


@app.route('/ricerca', methods=['GET'])
def ricerca():
    return render_template('ricerca.html')



@app.route('/ric', methods=['GET'])
def ric():

df2 = pd.read_csv('/workspace/Flask/AppEs5/dati.csv')
gia_inseriti = {'squadra':squadra,'anno':anno,'citta':citta}

    squadra = request.args['Squadra']
    anno = request.args['Anno']
    citta = request.args['Citta']

    for elemento in nuovi_dati:
        if elemento['squadra'] == squadra:
            if utente['sex'] == 'M':
                return render_template('welcome.html', nome=utente['name'])
            else:
                return render_template('welcomeW.html', nome=utente['name'])

    return render_template('error.html')

    


    # inserimento dei dati nel file csv
    # lettura dei dati dal form html 
    #squadra = request.args['Squadra']
    #anno = request.args['Anno']
    #citta = request.args['Citta']
    # lettura dei dati daal file nel dataframe
    #df1 = pd.read_csv('/workspace/Flask/AppEs5/dati.csv')
    # aggiungiamo i nuovi dati nel dataframe 
    #nuovi_dati = {'squadra':squadra,'anno':anno,'citta':citta}
    
    #df1 = df1.append(nuovi_dati,ignore_index=True)
    # salviamo il dataframe sul file dati.csv
    #df1.to_csv('/workspace/Flask/AppEs5/dati.csv', index=False)
    #return df1.to_html()   #lo converte in codice html






if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3246, debug=True)







