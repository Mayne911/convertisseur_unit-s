liste = [1, 2, 3, 4]
print(liste)
liste2 = []

test = int(input("combien de valeurs à convertir ? : "))

for i in range(test):
    print(i)
    liste2.append(liste[i] * 2)

print(liste2)