import requests

ips = [
    "10.10.110.249",
    "10.10.110.234"
]

def menu(titulo, opciones, salir):
    print("\n")
    opciones = list(opciones)
    print(f"##### {titulo} #####")
    for a in range(len(opciones)):
        print(f"[{a}] - {opciones[a]}")
    if salir:
        print("[999] - Salir")

    opcion = input("Escoge una opción")

    return opcion

def encender(tele):
    if tele:
        for ip in ips:
            requests.get(f"http://{ip}:5000/on")
    else:
        requests.get(f"http://{tele}:5000/on")

def apagar(tele):
    if tele:
        for ip in ips:
            requests.get(f"http://{ip}:5000/off")
    else:
        requests.get(f"http://{tele}:5000/off")

def url(ip, link):
    requests.get(f"http://{ip}:5000/web?url={link}")

def update(ips):
    for ip in ips:
        requests.get(f"http://{ip}:5000/update")

while True:
    opcion = menu("Menú Principal", ["Encender todas las TV", "Apagar todas las TV", "Encender una TV", "Apagar una TV", "Cambiar Enlace", "Actualizar todas las TV"], False)
    if opcion == 0:
        encender(True)
    elif opcion == 1:
        apagar(True)
    elif opcion == 2:
        encender(ips[(menu(("Selecciona una dirección"), ips, False))])
    elif opcion == 3:
        apagar(ips[(menu(("Selecciona una dirección"), ips, False))])
    elif opcion == 4:
        link = input("Introduce un enlace \n")
        url(ips[(menu(("Selecciona una dirección"), ips, False))], link)
    elif opcion == 5:
        update(ips)