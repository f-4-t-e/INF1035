'''
Écrire « Entrer nombre d’étudiant »
nb_etudiant = Lire entrée

Écrire « Entrer nombre hot-dogs »
nb_hotdogs = Lire entrée

nb_saucisses = nb_etudiant * nb_hotdogs
nb_supplementaire = nb_saucisses % 12
nb_paquet = nb_saucisses // 12

Écrire « Il faudra », nb_paquet, « paquets et », nb_supplemantaire «saucisses supplementaire »
'''

nb_etudiant = int(input("Entrer nombre d'étudiant : "))
nb_hotdogs = int(input("Entrer nombre hot-dogs : "))

nb_saucisses = nb_etudiant * nb_hotdogs
nb_supplementaire = nb_saucisses % 12
nb_paquet = nb_saucisses // 12

print("Il faudra %s paquets et %s saucisses supplementaires" % (nb_paquet, nb_supplementaire))
