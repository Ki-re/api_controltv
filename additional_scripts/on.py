from ip import ip_list
import requests
import time

for ip in ip_list:
    print(f"- IP {ip}")
    iteration = 0
    while True:
        iteration += 1
        requests.get(f"http://{ip}:5000/on")
        print("request encender")
        time.sleep(5)
        requests.get(f"http://{ip}:5000/as")
        print("request seteado el active source")
        time.sleep(5)
        status = requests.get(f"http://{ip}:5000/status").text
        print(f"status: {status}")
        status = status.split()
        if "on" in status or iteration >= 3:
            print("saliendo")
            break
        else:
            print("volvemos a intentarlo")
            time.sleep(5)