cadastro = {}
while True:
    nome = input("Digite o nome completo: ")
    if nome == '':
        break 

    idade = int(input("Digite a idade: "))
    cidade = input("Digite a cidade: ")


    cadastro [nome] = {"idade": idade, "cidade": cidade}
    
print("Cadastro: ")
print(cadastro)
for nome, dados in cadastro.items():
    print("- Nome:", nome)
    print(" Idade:", dados ["idade"])
    print("  Cidade", dados["cidade"])