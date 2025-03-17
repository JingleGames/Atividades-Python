from exames import exames

# Essa função é responsável por listar os exames já cadastrados na lista de exames
def listar_exames():
    if not exames:
        print("Nenhum exame cadastrado.\n")
        return

    for i, exame in enumerate(exames, start=1):
        print(f"{i}. Paciente: {exame['Paciente']} | Tipo: {exame['Tipo']} | Status: {exame['Status']}")
    print()
