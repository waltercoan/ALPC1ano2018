print("Digite o numero base")
base = int(input())
fat = 1
while base  >= 1:
    print(base)
    fat = fat * base
    base = base - 1
print("Resultado", fat)
