# first we need to put our given data into a suitable data-structure
# in this case we use dictionaries to map human properties to their respective dna-sequence
hair = {"black" : "CCAGCAATCGC", "brown" : "GCCAGTGCCG", "blonde" : "TTAGCTATCGC"}
face = {"square" : "GCCACGG", "round" : "ACCACAA", "oval" : "AGGCCTCA"}
eyes = {"blue" : "TTGTGGTGGC", "green" : "GGGAGGTGGC", "brown" : "AAGTAGTGAC"}
gender = {"female" : "TGAAGGACCTTC", "male" : "TGCAGGAACTTC"}
race = {"white" : "AAAACCTCA", "black" : "CGACTACAG", "asian" : "CGCGGGCCG"}

# map each person to a list of properties describing the person at hand...
# mind that the order of properties in the list is important
people = {"Eva" : ["female", "white", "blonde", "blue", "oval"],
          "Larisa" : ["female", "white", "brown", "brown", "oval"],
          "Matej" : ["male", "white", "black", "blue", "oval"],
          "Miha": ["male", "white", "brown", "green", "square"]}

# preberemo in shranimo osumljenčev DNK
with open("dna.txt", "r") as dna_file:
    dna = dna_file.read()       

# karakteristike osumljenca
suspect = []

for x in gender:
    if gender[x] in dna:
        print(x)
        suspect.append(x)

for x in race:
    if race[x] in dna:
        print(x)
        suspect.append(x)

for x in hair:
    if hair[x] in dna:
        print(x)
        suspect.append(x)

for x in eyes:
    if eyes[x] in dna:
        print(x)
        suspect.append(x)

for x in face:
    if face[x] in dna:
        print(x)
        suspect.append(x)

for p in people:
    if people[p] == suspect:
        print(f"The person who ate the ice-cream is {p}.")
        break
