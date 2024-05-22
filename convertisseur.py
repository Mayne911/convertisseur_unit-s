import customtkinter as ctk

#Définitions des fonctions 
def conversion(mesure, valeur):
    valeur = valeur * mesure
    return f"{valeur:.2f}"

def button_callback():
    if radio_var_dist.get() == 1:
        valeur = float(var.get())
        mesure = 0.393701
        affichage.configure(text=f"{valeur} cm = {conversion(mesure, valeur)} inches")
    
    elif radio_var_dist.get() == 2:
        valeur = float(var.get())
        mesure = 2.54
        affichage.configure(text=f"{valeur} pouces = {conversion(mesure,valeur)} cm")

    elif radio_var_dist.get() == 3:
        valeur = float(var.get())
        mesure = 0.000621371
        affichage.configure(text=f"{valeur} m = {conversion(mesure, valeur)} miles")
    
    elif radio_var_dist.get() == 4:
        valeur = float(var.get())
        mesure = 1609.34
        affichage.configure(text=f"{valeur} miles = {conversion(mesure, valeur)} m")

    elif radio_var_weight.get() == 1:
        valeur = float(var.get())
        mesure = 2.20462
        affichage.configure(text=f"{valeur} kg = {conversion(mesure, valeur)} lbs")
    
    elif radio_var_weight.get() == 2:
        valeur = float(var.get())
        mesure = 0.453592
        affichage.configure(text=f"{valeur} lbs = {conversion(mesure, valeur)} kg")
    
    elif radio_var_dist.get() == 5:
        valeur = float(var.get())
        mesure = 0.0328084
        affichage.configure(text=f"{valeur} cm = {conversion(mesure, valeur)} feet")
    
    elif radio_var_dist.get() == 6:
        valeur = float(var.get())
        mesure = 30.48
        affichage.configure(text=f"{valeur} feet = {conversion(mesure, valeur)} cm")
    
    elif radio_var_dist.get() == 7:
        valeur = float(var.get())
        mesure = 0.0109361
        affichage.configure(text=f"{valeur} cm = {conversion(mesure, valeur)} yards")
    
    elif radio_var_dist.get() == 8:
        valeur = float(var.get())
        mesure = 91.44
        affichage.configure(text=f"{valeur} yards = {conversion(mesure, valeur)} cm") 

def display_dist():
    cm_inches.grid()
    inches_cm.grid()
    m_miles.grid()
    miles_m.grid()
    cm_feet.grid()
    feet_cm.grid()
    cm_yards.grid()
    yards_cm.grid()
    radio_var_weight.set(0)
    kg_lbs.grid_remove()
    lbs_kg.grid_remove()   

def display_weight():
    cm_inches.grid_remove()
    inches_cm.grid_remove()
    m_miles.grid_remove()
    miles_m.grid_remove()
    cm_feet.grid_remove()
    feet_cm.grid_remove()
    cm_yards.grid_remove()
    yards_cm.grid_remove()
    radio_var_dist.set(0)
    kg_lbs.grid()
    lbs_kg.grid()

#Création de la fenêtre
conv = ctk.CTk()
conv.title("Convertisseur d'unités")
conv.geometry("400x400")
conv.grid_columnconfigure(0, weight=1)
conv.grid_columnconfigure((0, 1), weight=1)

#Radiobutton
radio_var_choix = ctk.IntVar()
radio_var_dist = ctk.IntVar()
radio_var_weight = ctk.IntVar()


choix_dist = ctk.CTkRadioButton(conv, text="Distance", variable=radio_var_choix, value=1, command=display_dist)
choix_dist.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

choix_weight = ctk.CTkRadioButton(conv, text="Poids", variable=radio_var_choix, value=2, command=display_weight)
choix_weight.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

cm_inches = ctk.CTkRadioButton(conv, text="cm en pouces", variable=radio_var_dist, value=1)
cm_inches.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

inches_cm = ctk.CTkRadioButton(conv, text="pouces en cm", variable=radio_var_dist, value=2)
inches_cm.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

m_miles = ctk.CTkRadioButton(conv, text="m en miles", variable=radio_var_dist, value=3)
m_miles.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

miles_m = ctk.CTkRadioButton(conv, text="miles en m", variable=radio_var_dist, value=4)
miles_m.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

cm_feet = ctk.CTkRadioButton(conv, text="cm en feet", variable=radio_var_dist, value=5)
cm_feet.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

feet_cm = ctk.CTkRadioButton(conv, text="feet en cm", variable=radio_var_dist, value=6)
feet_cm.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

cm_yards = ctk.CTkRadioButton(conv, text="cm en yards", variable=radio_var_dist, value=7)
cm_yards.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

yards_cm = ctk.CTkRadioButton(conv, text="yards en cm", variable=radio_var_dist, value=8)
yards_cm.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

kg_lbs = ctk.CTkRadioButton(conv, text="kg en lbs", variable=radio_var_weight, value=1)
kg_lbs.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

lbs_kg = ctk.CTkRadioButton(conv, text="lbs en kg", variable=radio_var_weight, value=2)
lbs_kg.grid(row=6, column=1, padx=10, pady=10, sticky="ew")

#User entry
var = ctk.CTkEntry(conv)
var.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

# Print result
affichage = ctk.CTkLabel(conv, text="Résultat", font=("Arial", 12), bg_color="white", fg_color="black")
affichage.grid(row=8, column=0, padx=10, pady=10, sticky="ew", columnspan=2)


#Button
button = ctk.CTkButton(conv, text="Convertir", command=button_callback)
button.grid(row=7, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

#initialisation de la fenêtre
cm_inches.grid_remove()
inches_cm.grid_remove()
m_miles.grid_remove()
miles_m.grid_remove()
cm_feet.grid_remove()
feet_cm.grid_remove()
cm_yards.grid_remove()
yards_cm.grid_remove()
kg_lbs.grid_remove()
lbs_kg.grid_remove()

valeur = 0


conv.mainloop()
