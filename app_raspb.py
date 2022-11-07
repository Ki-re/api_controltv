import os
from re import T
from flask import Flask, request
from waitress import serve
import subprocess
import werkzeug.serving

app = Flask(__name__)
repository = "https://github.com/Ki-re/api_controltv.git"
user = subprocess.check_output("echo $USER", shell=True)
ip = ((str(((subprocess.check_output("hostname -i", shell=True)).split())[-1])).replace("b", "")).replace("'", "")
run_port = 5000

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

@app.route('/update') # Permite la actualización mediante github
def update():
        os.system(f"cd /home/{user}/Desktop/api_controltv | git pull {repository} main") # Clonamos el repositorio    
        return "Actualización Realizada Correctamente"

os.system("clear")

print(f"Iniciado Correctamente en la dirección: {ip}:{run_port}")

@werkzeug.serving.run_with_reloader
def run_server(): # Contempla la actualización de los archivos para el correcto funcionamiento del /update
        app.debug = True
        serve(app, host=ip, port=run_port) # Ejecuta por medio de waitress

# serve(app, host=ip, port=run_port) # Ejecuta por medio de waitress

## Test