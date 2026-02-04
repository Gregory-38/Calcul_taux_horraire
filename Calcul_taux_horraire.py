while True:

    def calcule_mensuel(paye_annuelle): 
        return paye_annuelle / 12

    def calcule_hebdo(paye_mensuel):
        return paye_mensuel / 4

    def calcule_heure(paye_hebdo, horaire_fait):
        return paye_hebdo / horaire_fait

    paye_annuel = input("veuillez saisir votre salaire annuel uniquement en chiffre : ")
    paye_annuel = float(paye_annuel)

    heure_travailler = input("Veuillez entrée vos heures effectuée de la semaine : ")
    heure_travailler = int(heure_travailler)

    paye_mensuel = calcule_mensuel(paye_annuel)

    paye_hebdo = calcule_hebdo(paye_mensuel)

    paye_heure = calcule_heure(paye_hebdo, heure_travailler)

    print(f"Le taux horaire est de {round(paye_heure, 2)} euros")

    again = input("vouslez refaire un calcul ? OUI / NON : ")
    if again != "oui":
        print(f"fin du programme")
        break

