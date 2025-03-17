from exames import exames

# Essa é a função responsável por adicionar exames à lista de exames
def adicionar_exame():
    paciente = input("Digite o nome do paciente: ")
    tipo = input("Digite o tipo de exame: ")
    exame = {"Paciente": paciente, "Tipo": tipo, "Status": "Em análise"}
    exames.append(exame)
    print(f'Exame de {paciente} adicionado!\n')