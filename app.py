from flask import Flask, render_template
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return render_template("index.html")

@app.route('/it', methods=['GET'])
def Ciao_Mondo():
    return ('<h1>Ciapo, Mondo!</h1>')

@app.route('/fr', methods=['GET'])
def Bonjour():
    return ('<h1>Bonjour, Monde!</h1>')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

