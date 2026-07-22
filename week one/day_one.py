jour 1:
appareils=[]  #créer la liste
while True:          #créer une boucle while pour pouvoir demander des info a l'infinie
    appareil=input("quelle est l'addresse ip de votre appareil?")             #demander l'ip de l,appareil
    appareil.count(".")                                     #compte le nombre de . dans l'ip obtenue
    if appareil.count(".") < 3 or appareil.count(".") > 3:                          #dit que l'addresse doit avec 3 points
        print("votre appareil n'est pas valide")
        continue                                               # retourne en haut avec message d'erreur
    no=appareil.split(".")                                        #créer une variable qui emporte tout les split entre les .
    address_valide=True                                         #créer une variable pour les addresse valide
    for x in no:                                               #dire les x dans la variable no
        if not x.isdigit() or int(x) < 0 or int(x) > 255:                 #dit que chaque segment doit etre entre 0 et 255
            address_valide=False                                             #aussinon l,addresse n'est plus valide
            break                                                          #brise
    if not address_valide:                                                 #quand l'ip devien invalide
        print("veuillez entrer une addresse valide")
        continue                                                            #message d'erreur et retour en haut
    appareils.append(appareil)                                                #ajouter l'addresse retenu dans la liste
    choice = input("avez-vous un autre appareil?")                           #créer variable selon choix
    if choice == "n":                                              #si non la boucle brise et on passe a la prochaine étape
        break

appareils.sort()                                         #trier les ip en ordre de numéraux
for appareil in appareils:                                 #pour chaque appareil dans la liste appareille:
    print(appareil)                                      #imprimer les appareilles
inventaire=appareils                                    #renommer l'inventaire
machine_up=[]                                           #création de 2 listes pour trier
machine_down=[]						#création de 2 listes pour trier
for ip in inventaire:                                   #pour chaque ip dans notre inventaire on fait les actions suivante:
    while True:                                          #tant que l'action est vraie
        etat=input("est ce que cette machine reçoit les ping?:" + ip + " (y/n)")   #demande si l'ip recoit les ping pour chaque appareil
        if etat=="y":                                                  #tri entre oui et non et le met dans la bonne liste et ferme la boucle ensuite
            machine_up.append(ip)
            break
        elif etat=="n":
          machine_down.append(ip)
          break
        else:
            print("veuiller répondre avec y/n")                  #si ce n'est pas y ou n affiche l'erreur et retourne en haut de la boucle
up = len(machine_up)                                            # création de 2 nouvelles variable qui compte le nombre de machine ouverte et fermer et ensuite affiche a l'aide d'un message les résultat
down = len(machine_down)
print("il a " + str(up) + " de fonctionnelle")
print (machine_up)
print("il a " + str(down) + " de non fonctionnelle")
print (machine_down)
