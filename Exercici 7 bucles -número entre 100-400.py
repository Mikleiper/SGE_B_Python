num = int(input((f"introdueix un nou número: ")))

while(num > 100 and num < 400 ):
    print(f"{num} està entre 100 i 400")
    num = int(input((f"introdueix un nou número: ")))
    
print(f"{num} no està entre 100 i 400")
