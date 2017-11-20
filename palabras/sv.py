
import os
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


## Se recibe el archivo.txt a analizar
##@app.route('/', methods=['POST']) 
##def start():
  ##  file = request.files['file']
    
    ##filename = file.filename
    ##  print(filename)
    ##return jsonify("Archivo recibido")
    
@app.route('/')
def showv():
    return render_template('Principal.html')
    
    
app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

