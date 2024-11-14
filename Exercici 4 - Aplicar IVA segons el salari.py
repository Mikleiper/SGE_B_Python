salari = 45000
if salari < 15000:
    salari_total = salari
elif salari < 30000:
    salari_total = salari - (salari * 0.10)
elif salari < 60000:
    salari_total = salari - (salari * 0.21)
print(f"El salari total és {salari_total:.0f}")