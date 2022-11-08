import requests

ips = [
    "10.10.110.249",    # VM
    "10.10.110.234"     # Raspi Test
]

def menu(titulo, opciones):
    print("\n")
    opciones = list(opciones)
    print(f"##### {titulo} #####\n")
    for a in range(len(opciones)):
        print(f"[{a}] - {opciones[a]}")

    opcion = input("\nEscoge una opción\n")

    return opcion

def encender(todas, ip_dir):
    if todas:
        for ip in ips:
            requests.get(f"http://{ip}:5000/on")
    else:
        requests.get(f"http://{ip_dir}:5000/on")

def apagar(todas, ip_dir):
    if todas:
        for ip in ips:
            requests.get(f"http://{ip}:5000/off")
    else:
        requests.get(f"http://{ip_dir}:5000/off")

def url(ip, link):
    requests.get(f"http://{ip}:5000/web?url={link}")

def update(ips):
    for ip in ips:
        requests.get(f"http://{ip}:5000/update")

while True:
    opcion = int(menu("Menú Principal", ["Encender todas las TV", "Apagar todas las TV", "Encender una TV", "Apagar una TV", "Cambiar Enlace", "Actualizar todas las TV"]))
    if opcion == 0:
        encender(True, "")
    elif opcion == 1:
        apagar(True, "")
    elif opcion == 2:
        encender(ips[(menu(("Selecciona una dirección"), ips))])
    elif opcion == 3:
        apagar(ips[(menu(("Selecciona una dirección"), ips))])
    elif opcion == 4:
        link = input("Introduce un enlace \n")
        url(ips[(menu(("Selecciona una dirección"), ips))], link)
    elif opcion == 5:
        update(ips)