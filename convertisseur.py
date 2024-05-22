import customtkinter as ctk

#Définitions des fonctions 
def cm_to_inches(cm):
    return cm * 0.394

def inches_to_cm(inches):
    return inches * 2.54

def m_to_miles(m):
    return m * 0.000621371

def miles_to_m(miles):
    return miles * 1609.34

def kg_to_lbs(kg):
    return kg * 2.20462

def lbs_to_kg(lbs):
    return lbs * 0.453592

def cm_to_feet(cm):
    return cm * 0.0328084

def feet_to_cm(feet):
    return feet * 30.48

def cm_to_yards(cm):
    return cm * 0.0109361

def yards_to_cm(yards):
    return yards * 91.44

def button_callback():
    print("Button clicked")
    if radio_var_dist.get() == 1:
        cm = float(var.get())
        affichage.configure(text=f"{cm} cm = {cm_to_inches(cm)} pouces")
    
    elif radio_var_dist.get() == 2:
        inches = float(var.get())
        affichage.configure(text=f"{inches} pouces = {inches_to_cm(inches)} cm")
    
    elif radio_var_dist.get() == 3:
        m = float(var.get())
        affichage.configure(text=f"{m} m = {m_to_miles(m)} miles")
    
    elif radio_var_dist.get() == 4:
        miles = float(var.get())
        affichage.configure(text=f"{miles} miles = {miles_to_m(miles)} m")

    elif radio_var_weight.get() == 1:
        kg = float(var.get())
        affichage.configure(text=f"{kg} kg = {kg_to_lbs(kg)} lbs")
    
    elif radio_var_weight.get() == 2:
        lbs = float(var.get())
        affichage.configure(text=f"{lbs} lbs = {lbs_to_kg(lbs)} kg")
    
    elif radio_var_dist.get() == 5:
        cm = float(var.get())
        affichage.configure(text=f"{cm} cm = {cm_to_feet(cm)} feet")
    
    elif radio_var_dist.get() == 6:
        feet = float(var.get())
        affichage.configure(text=f"{feet} feet = {feet_to_cm(feet)} cm")
    
    elif radio_var_dist.get() == 7:
        cm = float(var.get())
        affichage.configure(text=f"{cm} cm = {cm_to_yards(cm)} yards")
    
    elif radio_var_dist.get() == 8:
        yards = float(var.get())
        affichage.configure(text=f"{yards} yards = {yards_to_cm(yards)} cm") 

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

#Print result
affichage = ctk.CTkLabel(conv, text="Résultat")
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


conv.mainloop()
