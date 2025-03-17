# Esse é o arquivo principal responsável por mostrar as opções ao usuário

# Aqui, importamos os outros arquivos que contém as funções para cada opção apresentada
from adicionar import adicionar_exame
from listar import listar_exames
from processar import processar_exame

medico = False
paciente = False

# Isso é apenas para melhorar a experiência do usuário, com uma mensagem de boas vindas amigável e convidativa
print("***************************************")
print("*BEM-VINDO AO TERMINAL DO SISTEMA PACS*")
print("***************************************")

print("1. Área do médico\n2. Área do paciente\n")

area = int(input("Escolha uma opção: "))

# Esse loop é responsável por fazer o usuário escolher uma das opções e retornar ao "menu" assim que concluir o processo da opção escolhida
while True:
    if area == 1:
        medico = True
    elif area == 2:
        paciente = True
    else:
        print("Opção inválida. Tente novamente.\n")
        break

    while medico:
        print("1. Adicionar exame")
        print("2. Acessar lista de exames")
        print("3. Processar exame")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_exame()
        elif opcao == "2":
            listar_exames()
        elif opcao == "3":
            processar_exame()
        else:
            print("Opção inválida. Tente novamente.\n")
            break
    
    while paciente:
        exame_paciente = input("Digite seu nome: ")
        
