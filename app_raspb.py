import os
from re import T
from flask import Flask, request
from waitress import serve
import subprocess
import werkzeug.serving
import time

# To launch Chromium on the Raspberry Pi, add the following:
# @sensible-browser IP --start-fullscreen  
# In the path: /etc/xdg/lxsession/LXDE-pi/autostart  

time.sleep(30)
                
app = Flask(__name__)
user = subprocess.check_output("echo $USER", shell=True) # Get the username  
ip = ((str(((subprocess.check_output("hostname -I", shell=True)).split())[-1])).replace("b", "")).replace("'", "") # Get the IP and clean the output  
run_port = 5000

# Usage: X.X.X.X:5000/on
@app.route('/on') # Turns on the TV using CEC  
def on():
        os.system('echo "on 0" | cec-client -s -d 1')
        return "Turning on TV..."

# Usage: X.X.X.X:5000/off
@app.route('/off') # Turns off the TV using CEC  
def off():
        os.system('echo "standby 0" | cec-client -s -d 1')
        return "Turning off TV..."

# Usage: X.X.X.X:5000/web?url=*link*
@app.route('/web') # Opens a web page on the Raspberry Pi  
def web():
        url = request.args['url']
        os.system(f'sensible-browser {url} --start-fullscreen')
        return "Opening Web..."

# Usage: X.X.X.X:5000/update
@app.route('/update') # Allows updating via GitHub  
def update():
        os.system(f"git pull https://github.com/Ki-re/api_controltv.git main") # Clone the repository    
        return "Update Successfully Completed"

# Usage: X.X.X.X:5000/as
@app.route('/as') # Marks the Raspberry Pi as an active source  
def active_source():
        os.system('echo "as" | cec-client -s -d 1')   
        return "Active Source set successfully"

# Usage: X.X.X.X:5000/status
@app.route('/status') # Checks the power status of the TV  
def status():
        status = os.popen('echo "pow 0.0.0.0" | cec-client -s -d 1 | grep "power status"').read()  
        return status

########################################################################################################################################

os.system("clear")
print(f"Successfully started at address: {ip}:{run_port}")

@werkzeug.serving.run_with_reloader
def run_server(): # Handles file updates for proper /update functionality  
        app.debug = True
        serve(app, host=ip, port=run_port) # Runs via Waitress
