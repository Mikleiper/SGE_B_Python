
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
parells = "números parells: "
senars =  "Números senars: "
sumaPar = 0
sumaSen = 0

for i in num:
    if i % 2 == 0:
        sumaPar += i
    else:
        sumaSen += i 

print(f"Suma dels {parells} {sumaPar}", end=" ")
print(f"\nSuma dels {senars} {sumaSen}", end=" ")


