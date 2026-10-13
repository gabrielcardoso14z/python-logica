segredo = 7
palpite = 0
tentativas = 0
while palpite != segredo:
    palpite = int(input("Adivinhe o número: "))
    tentativas += 1
    if palpite < segredo:
        print("Muito baixo!")
    elif palpite > segredo:
        print("Muito alto!")

print("Você acertou!")
print(f"Você acertou em {tentativas} tentativas.")