import os
from re import T
from flask import Flask, request
from waitress import serve

app = Flask(__name__)

# os.system('flask run -h 10.10.110.166')

# Uso: X.X.X.X:5000/on
@app.route('/on') # Enciende el televisor por medio del cec
def on():
        os.system('echo "on 0"|cec-client -s -d 1')
        return "Encendiendo televisor..."

# Uso: X.X.X.X:5000/off
@app.route('/off') # Apaga el televisor por medio del cec
def off():
        os.system('echo "standby 0"|cec-client -s -d 1')
        return "Apagando televisor..."

# Uso: X.X.X.X:5000/web?url=*enlace*
@app.route('/web') # Abre una página web en la RaspB
def web():
        url = request.args['url']
        os.system('sensible-browser '+url)
        return "Abriendo Web..."
        
# app.run(port=5000)

serve(app, host="172.18.4.168", port=5000) # Ejecuta la API por medio de waitress