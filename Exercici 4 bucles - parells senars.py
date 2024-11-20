
num = [1,4,5,67,34,55,78,90,2,44,65,33,35,50]
parells = "Números parells: "
senars =  "Números senars: "

print(f"{parells}")
for i in num:
    if i % 2 == 0:
        print(f"{i}", end="-")
print (f"\n{senars}")    
for i in num:
    if i % 2 != 0:  
        print(f"{i}", end="-")
