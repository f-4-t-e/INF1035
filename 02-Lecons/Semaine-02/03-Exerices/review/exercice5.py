
'''
Écrire « Entrer ancien salaire : »
ancien_salaire = Lire entrée

salaire_annuel = 1.03 * ancien_salaire
salaire_mensuel = salaire_annuel / 12
montant_retroactif = 9 * 0.03 * ancien_salaire / 12

Écrire « Le nouveau salaire annuel est », salaire_annuel
Écrire ...
'''

ancien_salaire = float(input("Entrer ancien salaire : "))

salaire_annuel = 1.03 * ancien_salaire
salaire_mensuel = salaire_annuel / 12
montant_retroactif = 9 * 0.03 * ancien_salaire / 12

print("Le nouveau salaire annuel est ", salaire_annuel)
print("Le nouveau salaire mensuel est ", salaire_mensuel)
print("Le montant rétro actif est ", montant_retroactif)
