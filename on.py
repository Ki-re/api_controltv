from ip import ip_list
import requests
import time

for ip in ip_list:
    requests.get(f"{ip}:5000/on")
    time.sleep(15)
    requests.get(f"{ip}:5000/as")
    time.sleep(5)
    requests.get(f"{ip}:5000/status")