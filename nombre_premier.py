# fonction qui retourne la liste des nombres premiers entre deux nombres donnés
def liste_nombres_premiers(debut, fin):
    nombres_premiers = []
    for num in range(debut, fin + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                nombres_premiers.append(num)
    return nombres_premiers


# Importation de la fonction depuis le fichier si nécessaire
# from nombre_premier import liste_nombres_premiers

# Appel de la fonction
resultat = liste_nombres_premiers(1, 20)
print("Nombres premiers entre 10 et 50:", resultat)
