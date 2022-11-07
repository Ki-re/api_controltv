import os
import time
import subprocess

repository = "https://github.com/Ki-re/api_controltv.git"

user = subprocess.check_output("echo $USER", shell=True)

os.system(f"cd /Desktop/api_controltv | git pull {repository} main") # Clonamos el repositorio
time.sleep(5) # Tiempo de gracia
os.system(f"python3 home/{user}/Desktop/api_controltv/app_raspb.py")
