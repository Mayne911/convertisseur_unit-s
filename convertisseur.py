import customtkinter as ctk

#Définitions des fonctions 
def cm_to_inches(cm):
    return cm * 0.394

def inches_to_cm(inches):
    return inches * 2.54

def button_callback():
    print("Button clicked")
    if cm_inches.get():
        cm = float(var.get())
        affichage.configure(text="pipi")
        affichage.configure(text=f"{cm} cm = {cm_to_inches(cm)} pouces")
        
    elif inches_cm.get():
        inches = float(var.get())
        affichage.configure(text=f"{inches} pouces = {inches_to_cm(inches)} cm") #Affichage du résultat
    print(var.get())


#Création de la fenêtre
conv = ctk.CTk()
conv.title("Convertisseur d'unités")
conv.geometry("400x400")
conv.grid_columnconfigure(0, weight=1)
conv.grid_columnconfigure((0, 1), weight=1)

#Checkbox
cm_inches = ctk.CTkCheckBox(conv, text="cm en pouces")
cm_inches.grid(row=1, column=0, padx=10, pady=(20, 10), sticky="w")

inches_cm = ctk.CTkCheckBox(conv, text="pouces en cm")
inches_cm.grid(row=1, column=1, padx=10, pady=(20, 10), sticky="e")

#User entry
var = ctk.CTkEntry(conv)
var.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

#Print result
affichage = ctk.CTkLabel(conv, text="Résultat")
affichage.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

#Button
button = ctk.CTkButton(conv, text="Convertir", command=button_callback)
button.grid(row=2, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

if cm_inches.get():
        cm = float(var.get())
        print(f"{cm} cm = {cm_to_inches(cm)} pouces")

conv.mainloop()


#Choix utilisateur
#convert = input("souahiitez-vous convertir des cm en pouces ou des pouces en cm ? : ")
#plsrs_conv = input("Souhaitez-vous convertir plusieurs valeurs ? : ")

# if plsrs_conv == "Non":

#     if convert == "cm en pouces":
#         cm = float(input("Entrez la longueur en cm : ")) 
#         print(f"{cm} cm = {cm_to_inches(cm)} pouces")

#     elif convert == "pouces en cm":
#         pouces = float(input("Entrez la longueur en pouces : "))
#         print(f"{pouces} pouces = {inches_to_cm(pouces)} cm")

# elif plsrs_conv == "Oui":
#      if convert == "cm en pouces":
#         liste_longueurs = []
#         nb_longueurs = int(input("Combien de valeurs voulez-vous convertir ? : ")) 
#         for i in range(nb_longueurs):
#             liste_longueurs.append(float(input(f"Valeur {i + 1} : ")))
#             print(f"{liste_longueurs[i]} cm = {cm_to_inches(liste_longueurs[i])} pouces")
    
#      elif convert == "pouces en cm":
#         liste_longueurs = []
#         nb_longueurs = int(input("Combien de valeurs voulez-vous convertir ? : ")) 
#         for i in range(nb_longueurs):
#             liste_longueurs.append(float(input(f"Valeur {i + 1} : ")))
#             print(f"{liste_longueurs[i]} pouces = {inches_to_cm(liste_longueurs[i])} cm")


