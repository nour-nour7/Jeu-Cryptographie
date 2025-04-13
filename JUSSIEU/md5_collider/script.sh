#!/bin/bash

#créer le préfixe avec "nour" + padding
python3 -c "
nom = \"nour\"
# Ajouter du padding pour avoir une taille multiple de 64 octets
while len(nom.encode('utf-8')) % 64 != 0:
    nom += \"0\"
# Enregistrer le préfixe dans un fichier
with open(\"prefixe.txt\", \"w\") as f:
    f.write(nom)
print(f'Préfixe créé: {nom}')
print(f'Longueur: {len(nom)} caractères')
"

echo "génération de la première collision..."
./coll_finder prefixe.txt A.bin B.bin

cat prefixe.txt A.bin > prefixe_A.txt

echo "génération de la seconde collision..."
./coll_finder prefixe_A.txt C.bin D.bin

echo -n "h4ckm0d3" > suffixe.txt

cat prefixe.txt A.bin C.bin suffixe.txt > file1.bin
cat prefixe.txt A.bin D.bin suffixe.txt > file2.bin
cat prefixe.txt B.bin C.bin suffixe.txt > file3.bin
cat prefixe.txt B.bin D.bin suffixe.txt > file4.bin

md5sum file1.bin file2.bin file3.bin file4.bin

xxd -p file1.bin | tr -d '\n' > key1.txt
xxd -p file2.bin | tr -d '\n' > key2.txt
xxd -p file3.bin | tr -d '\n' > key3.txt
xxd -p file4.bin | tr -d '\n' > key4.txt

echo "Voici les 4 clés à soumettre au jeu:"
echo "Clé 1: $(cat key1.txt)"
echo "Clé 2: $(cat key2.txt)"
echo "Clé 3: $(cat key3.txt)"
echo "Clé 4: $(cat key4.txt)"

# nour en hexadécimal est 6e6f7572
# h4ckm0d3 6834636b6d306433
echo "Vérification des conditions:"
for i in {1..4}; do
  key=$(cat key$i.txt)
  if [[ $key == 6e6f7572* ]]; then
    echo "Clé $i commence bien par 'nour'"
  else
    echo "ERREUR: Clé $i ne commence pas par 'nour'"
  fi
  
  if [[ $key == *6834636b6d306433 ]]; then
    echo "Clé $i se termine bien par 'h4ckm0d3'"
  else
    echo "ERREUR: Clé $i ne se termine pas par 'h4ckm0d3'"
  fi
done