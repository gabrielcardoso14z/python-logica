nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
ano_nascimento = 2026 - idade
print(nome, "você nasceu por volta de", ano_nascimento, "e tem", idade, "anos")

if int (idade) <=18:
    print(nome, "você não pode comparecer a esse evento")
else:
    print(nome, "você pode comparecer a esse evento")