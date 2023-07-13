from ip import ip_list
import requests
import time

for ip in ip_list:
    iteration = 0
    while True:
        iteration += 1
        requests.get(f"http://{ip}:5000/off")
        time.sleep(3)
        status = requests.get(f"http://{ip}:5000/status").text
        status = status.split()
        if "standby" in status or iteration >= 3:
            break
        else:
            time.sleep(5)