# si vuole realizzare un sito web per memorizzare le squadre di uno sport a scelta. L'utente deve poter inserire il nome della squadra 
# e la data di fondazione e la cità. Deve inoltre poter effettuare delle ricerche inserendo uno dei valori delle colonne e 
# ottenendo i dati presenti.



from flask import Flask, render_template, request
app = Flask(__name__)
lst = []

@app.route('/', methods=['GET'])
def form():
        
    return render_template('form.html')



@app.route('/dates', methods=['GET'])
def es():

    Nome = request.args['Nome']
    Anno = request.args['Anno']
    Citta = request.args['Citta']

    lst.append({'Nome':Nome,'Anno':Anno,'Citta':Citta})
    
    
    return 









if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)