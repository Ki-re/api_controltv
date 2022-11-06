import os
import time

repository = "https://github.com/Ki-re/api_controltv.git"

os.system(f"cd /Desktop/api_controltv | git pull {repository} main") # Clonamos el repositorio
time.sleep(5) # Tiempo de gracia
os.system(f"python3 /Desktop/api_controltv/app_raspb.py")
