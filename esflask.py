from flask import Flask, render_template
app = Flask(__name__)
import datetime

@app.route('/')
def img():
  return render_template('index_esflask.html')

 

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
