import os
from re import T
from flask import Flask, request
from waitress import serve
import subprocess
import werkzeug.serving
import time

app = Flask(__name__)
repository = "https://github.com/Ki-re/api_controltv.git"
user = subprocess.check_output("echo $USER", shell=True) # Obtenemos el username
ip = ((str(((subprocess.check_output("hostname -I", shell=True)).split())[-1])).replace("b", "")).replace("'", "") # Obtenemos la IP y limpiamos el output 
run_port = 5000

url = ""

try:
        path = f"/home/{user}/Desktop/defaultip.txt"
        file = open(path, "r")
        url = file.read()
except:
        pass

if url == "":
        url = "google.com"

os.system(f'sensible-browser {url}')
# if int(subprocess.check_output("uptime | awk '{print $3}'"), shell=True) <= 3:
#         os.system('sensible-browser --start-fullscreen')
#         time.sleep(5)
#         try:
#                 path = f"/home/{user}/Desktop/defaultip.txt"
#                 file = open(path, "r")
#                 url = file.read()
#         except:
#                 url = 'google.com'
#         os.system(f'sensible-browser {url}')

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

# Uso: X.X.X.X:5000/update
@app.route('/update') # Permite la actualización mediante github
def update():
        os.system(f"git pull {repository} main") # Clonamos el repositorio    
        return "Actualización Realizada Correctamente"

@app.route('/defaultweb') # Abre una página web en la RaspB
def web():
        url = request.args['url']
        path = f"/home/{user}/Desktop/defaultip.txt"
        file = open(path, "w")
        file.write(url)
        file.close()
        return "Nueva dirección predeterminada establecida"

# @app.route('/pip') # Instala un nuevo modulo
# def update():
#         modulo = request.args['module']
#         os.system(f"python3 -m pip install {modulo}") # Clonamos el repositorio    
#         return "Actualización Realizada Correctamente"

########################################################################################################################################

os.system("clear")
print(f"Iniciado Correctamente en la dirección: {ip}:{run_port}")

@werkzeug.serving.run_with_reloader
def run_server(): # Contempla la actualización de los archivos para el correcto funcionamiento del /update
        app.debug = True
        serve(app, host=ip, port=run_port) # Ejecuta por medio de waitress