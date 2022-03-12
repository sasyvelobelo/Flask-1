# Realizzare un server web che permetta di effettuare il login 
# L'utente inserisce lo username e la password
# Se l'username è admin e se la password è xxx123## il sito ci saluta con un messaggio di benvenuto 
# Altrimenti ci da un messaggio di errore 

from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def es():
    return render_template('es.html')


@app.route('/date', methods=['GET'])
def date():
    Name = request.args['Name']
    
    Pass = request.args['Pass']

    if Name==('admin') and Pass==('xxx123#'):
       return render_template('welcome.html', nome=Name)
    else:
        return render_template('error.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)