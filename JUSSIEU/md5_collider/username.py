nom = "nour"

while len(nom) % 64 != 0:
    nom += "0"

with open("prefixe.txt", "w") as f:
    f.write(nom)