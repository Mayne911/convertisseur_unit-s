
#Définitions des fonctions 
def cm_to_inches(cm):
    return cm * 0.394

def inches_to_cm(inches):
    return inches * 2.54

#Choix utilisateur
convert = input("souahiitez-vous convertir des cm en pouces ou des pouces en cm ? : ")
plsrs_conv = input("Souhaitez-vous convertir plusieurs valeurs ? : ")

if plsrs_conv == "Non":

    if convert == "cm en pouces":
        cm = float(input("Entrez la longueur en cm : ")) 
        print(f"{cm} cm = {cm_to_inches(cm)} pouces")

    elif convert == "pouces en cm":
        pouces = float(input("Entrez la longueur en pouces : "))
        print(f"{pouces} pouces = {inches_to_cm(pouces)} cm")

elif plsrs_conv == "Oui":
     if convert == "cm en pouces":
        liste_longueurs = []
        nb_longueurs = int(input("Combien de valeurs voulez-vous convertir ? : ")) 
        for i in range(nb_longueurs):
            liste_longueurs.append(float(input(f"Valeur {i + 1} : ")))
            print(f"{liste_longueurs[i]} cm = {cm_to_inches(liste_longueurs[i])} pouces")
    
     elif convert == "pouces en cm":
        liste_longueurs = []
        nb_longueurs = int(input("Combien de valeurs voulez-vous convertir ? : ")) 
        for i in range(nb_longueurs):
            liste_longueurs.append(float(input(f"Valeur {i + 1} : ")))
            print(f"{liste_longueurs[i]} pouces = {inches_to_cm(liste_longueurs[i])} cm")


        


