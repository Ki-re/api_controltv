from ip import ip_list
import requests
import time

for ip in ip_list:
    print(f"- IP {ip}")
    iteration = 0
    while True:
        iteration += 1
        requests.get(f"http://{ip}:5000/off")
        print("request apagar")
        time.sleep(3)
        status = requests.get(f"http://{ip}:5000/status").text
        print(f"status: {status}")
        status = status.split()
        if "standby" in status or "unknown" in status or iteration >= 3:
            print("saliendo")
            break
        else:
            print("volvemos a intentarlo")
            time.sleep(5)