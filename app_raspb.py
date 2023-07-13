import os
from re import T
from flask import Flask, request
from waitress import serve
import subprocess
import werkzeug.serving

# Para que se encienda chromium con la raspi hay que poner lo siguiente
# @sensible-browser IP --start-fullscreen 
# En la ruta: /etc/xdg/lxsession/LXDE-pi/autostart

app = Flask(__name__)
user = subprocess.check_output("echo $USER", shell=True) # Obtenemos el username
ip = ((str(((subprocess.check_output("hostname -I", shell=True)).split())[-1])).replace("b", "")).replace("'", "") # Obtenemos la IP y limpiamos el output 
run_port = 5000

# Uso: X.X.X.X:5000/on
@app.route('/on') # Enciende el televisor por medio del cec
def on():
        os.system('echo "on 0" | cec-client -s -d 1')
        return "Encendiendo televisor..."

# Uso: X.X.X.X:5000/off
@app.route('/off') # Apaga el televisor por medio del cec
def off():
        os.system('echo "standby 0" | cec-client -s -d 1')
        return "Apagando televisor..."

# Uso: X.X.X.X:5000/web?url=*enlace*
@app.route('/web') # Abre una página web en la RaspB
def web():
        url = request.args['url']
        os.system(f'sensible-browser {url} --start-fullscreen')
        return "Abriendo Web..."

# Uso: X.X.X.X:5000/update
@app.route('/update') # Permite la actualización mediante github
def update():
        os.system(f"git pull https://github.com/Ki-re/api_controltv.git main") # Clonamos el repositorio    
        return "Actualización Realizada Correctamente"

# Uso: X.X.X.X:5000/as
@app.route('/as') # Marca la Raspb como source activo
def active_source():
        os.system('echo "as" | cec-client -s -d 1')   
        return "Active Source correcto"

# Uso: X.X.X.X:5000/status
@app.route('/status') # Marca la Raspb como source activo
def status():
        status = os.system('echo "pow 0.0.0.0" | cec-client -s -d 1 | grep "power status"')   
        return status

########################################################################################################################################

os.system("clear")
print(f"Iniciado Correctamente en la dirección: {ip}:{run_port}")

@werkzeug.serving.run_with_reloader
def run_server(): # Contempla la actualización de los archivos para el correcto funcionamiento del /update
        app.debug = True
        serve(app, host=ip, port=run_port) # Ejecuta por medio de waitress
