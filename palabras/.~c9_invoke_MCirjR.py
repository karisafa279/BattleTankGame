import os
from flask import Flask

app = Flask(__name__)

verbos = 0
adjetivos = 0
sufijos = 0
prefijos = 0

@app.route('/start', methods=['POST']) 
def start():
    if not request.content:
        abort(400)
    print request.content

app.run(host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

