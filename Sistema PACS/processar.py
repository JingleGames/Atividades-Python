import time
from exames import exames
from listar import listar_exames

# Essa função é responsável por emular um processamento real de exames, utilizando as informações fornecidas anteriormente pelo usuário
def processar_exame():
    if not exames:
        print("Nenhum exame para processar.\n")
        return

    listar_exames()
    escolha = int(input("Digite o número do exame para processar: ")) - 1

    if 0 <= escolha < len(exames):
        print("Processando exame...")
        time.sleep(2)  # Simula o processamento
        exames[escolha]["Status"] = "Pronto"
        print(f"Exame de {exames[escolha]['Paciente']} está pronto!\n")
    else:
        print("Escolha inválida.\n")
