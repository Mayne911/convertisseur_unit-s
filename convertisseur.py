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
    if radio_var.get() == 1:
        cm = float(var.get())
        affichage.configure(text=f"{cm} cm = {cm_to_inches(cm)} pouces")
    elif radio_var.get() == 2:
        inches = float(var.get())
        affichage.configure(text=f"{inches} pouces = {inches_to_cm(inches)} cm")
    elif radio_var.get() == 3:
        m = float(var.get())
        affichage.configure(text=f"{m} m = {m_to_miles(m)} miles")
    elif radio_var.get() == 4:
        miles = float(var.get())
        affichage.configure(text=f"{miles} miles = {miles_to_m(miles)} m")
    elif radio_var.get() == 5:
        kg = float(var.get())
        affichage.configure(text=f"{kg} kg = {kg_to_lbs(kg)} lbs")
    elif radio_var.get() == 6:
        lbs = float(var.get())
        affichage.configure(text=f"{lbs} lbs = {lbs_to_kg(lbs)} kg")
    elif radio_var.get() == 7:
        cm = float(var.get())
        affichage.configure(text=f"{cm} cm = {cm_to_feet(cm)} feet")
    elif radio_var.get() == 8:
        feet = float(var.get())
        affichage.configure(text=f"{feet} feet = {feet_to_cm(feet)} cm")
    elif radio_var.get() == 9:
        cm = float(var.get())
        affichage.configure(text=f"{cm} cm = {cm_to_yards(cm)} yards")
    elif radio_var.get() == 10:
        yards = float(var.get())
        affichage.configure(text=f"{yards} yards = {yards_to_cm(yards)} cm")    


#Création de la fenêtre
conv = ctk.CTk()
conv.title("Convertisseur d'unités")
conv.geometry("400x400")
conv.grid_columnconfigure(0, weight=1)
conv.grid_columnconfigure((0, 1), weight=1)

#Radiobutton
radio_var = ctk.IntVar()
cm_inches = ctk.CTkRadioButton(conv, text="cm en pouces", variable=radio_var, value=1)
cm_inches.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

inches_cm = ctk.CTkRadioButton(conv, text="pouces en cm", variable=radio_var, value=2)
inches_cm.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

m_miles = ctk.CTkRadioButton(conv, text="m en miles", variable=radio_var, value=3)
m_miles.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

miles_m = ctk.CTkRadioButton(conv, text="miles en m", variable=radio_var, value=4)
miles_m.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

kg_lbs = ctk.CTkRadioButton(conv, text="kg en lbs", variable=radio_var, value=5)
kg_lbs.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

lbs_kg = ctk.CTkRadioButton(conv, text="lbs en kg", variable=radio_var, value=6)
lbs_kg.grid(row=3, column=1, padx=10, pady=10, sticky="ew")

cm_feet = ctk.CTkRadioButton(conv, text="cm en feet", variable=radio_var, value=7)
cm_feet.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

feet_cm = ctk.CTkRadioButton(conv, text="feet en cm", variable=radio_var, value=8)
feet_cm.grid(row=4, column=1, padx=10, pady=10, sticky="ew")

cm_yards = ctk.CTkRadioButton(conv, text="cm en yards", variable=radio_var, value=9)
cm_yards.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

yards_cm = ctk.CTkRadioButton(conv, text="yards en cm", variable=radio_var, value=10)
yards_cm.grid(row=5, column=1, padx=10, pady=10, sticky="ew")

#User entry
var = ctk.CTkEntry(conv)
var.grid(row=0, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

#Print result
affichage = ctk.CTkLabel(conv, text="Résultat")
affichage.grid(row=7, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

#Button
button = ctk.CTkButton(conv, text="Convertir", command=button_callback)
button.grid(row=6, column=0, padx=10, pady=10, sticky="ew", columnspan=2)


conv.mainloop()
