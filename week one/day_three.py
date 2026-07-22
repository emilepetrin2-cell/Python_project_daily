jour 3 les boucle for (script de déclaration d'appareil avec detection pour savoir si le ping est prêt et si il a des port dangereux d'ouvert[23])

switch1 ={"hostname": "switch1",
        "username": "elpetrino",
        "password": "kali",
        "status": True,
        "port ouvert": [25, 22, 43],
        "ip address": "192.168.20.1"
         }
switch2 ={"hostname": "switch2",
        "username": "elpetrino2",
        "password": "kali",
        "status": True,
        "port ouvert": [23, 22, 53],
        "ip address": "192.168.30.1"
         }
switch3 ={"hostname": "switch3",
        "username": "elpetrino3",
        "password": "kali",
        "status": True,
        "port ouvert": [24, 22, 76],
        "ip address": "192.168.40.1"
         }


switchs =  [switch1, switch2, switch3]
for ip in switchs:
    print(f"""
           ==============================================
            config {ip["hostname"]}
           ==============================================
            username {ip["username"]} privilege 15 password {ip["password"]}
            interface vlan 1
            ip address {ip["ip address"]}
            no shutdown""")
for switch in switchs:
    for port in switch ["port ouvert"]:
        if port == 23:
            print(f"port non sécuriser trouver(23) dans {switch["hostname"]}")
        elif port == 22:
            print(f"port sécuriser trouver(22) dans {switch["hostname"]}")

liste_ip = ["192.168.20.1", "192.168.30.1", "192.168.40.1", "192.168.50.1", "192.168.60.1"]
ips_active = []
for ip in liste_ip:
    ip_active = input(f"Est-ce que l'IP {ip} répond au ping?")
    if ip_active == "oui":
        ips_active.append(ip)
for ip in ips_active:
    print(f"l'ip {ip} est prêt à recevoir le ssh")