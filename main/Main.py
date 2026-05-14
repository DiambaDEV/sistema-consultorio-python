from modelos.Paciente import Paciente
from services.PacienteService import PacienteService
from repositorio.BancoDeDados import BancoDeDados
from repositorio.PacienteRepository import PacienteRepository
from utils.cpf_utils import formatar_cpf
from utils.cpf_utils import validar_cpf

db = BancoDeDados()
repository = PacienteRepository(db)
service = PacienteService(repository)

while True:
    print("\n=== SISTEMA CONSULTÓRIO ===")
    print("1 - Cadastrar paciente")
    print("2 - Buscar pacientes")
    print("3 - Listar pacientes")
    print("4 - Editar paciente")
    print("5 - Remover paciente")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        cpf = input("CPF (somente números): ")

        if not validar_cpf(cpf):
            print("CPF inválido! Deve conter exatamente 11 números.")

        if service.buscar_por_cpf(cpf):
            print("Paciente já cadastrado.")
        else:
            telefone = input("Telefone: ")
            data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")

            paciente = Paciente(
                nome,
                cpf,
                telefone,
                data_nascimento
            )

        service.cadastrar_paciente(paciente)

    elif opcao == "2":
        print("\n1 - Buscar por CPF")
        print("2 - Buscar por Data de nascimento")
        sub_opcao = input("Escolha: ")

        if sub_opcao =="1":
            cpf = input("Digite o CPF: ")
            paciente = service.buscar_por_cpf(cpf)
            
            if paciente:
                print(paciente)
            else:
                print("Paciente não encontrado.")
                
        elif sub_opcao == "2":
            data = input("Digite a data de nascimento (AAAA-MM-DD): ")
            pacientes = service.buscar_por_data_nascimento(data)

            if pacientes:
                for p in pacientes:
                    print(p)

            else:
                print("Nenhum paciente encontrado.")
        else:
            print("Opção inválida.")

    elif opcao == "3":
        pacientes = service.listar_pacientes()
        
        if pacientes:
            for p in pacientes:
                print(f"Nome: {p[1]} | CPF: {formatar_cpf(p[2])} | Telefone: {p[3]} | Data: {p[4]}")
        else:
            print("Nenhum paciente cadastrado.")

    
    elif opcao == "4":
        cpf = input("Digite o CPF do paciente: ")

        paciente = service.buscar_por_cpf(cpf)

        if paciente:
            novo_telefone = input("Novo telefone: ")
            service.atualizar_telefone(cpf, novo_telefone)
            print("Telefone atualizado com sucesso. ")
        else:
            print("Paciente não encontrado")

    
    elif opcao == "5":
        pacientes = service.listar_pacientes()

        if not pacientes:
            print("Nenhum paciente cadastrado.")
        else:
            print("\n--- PACIENTES CADASTRADOS ---")

            for i, p in enumerate(pacientes, start=1):
                print(f"{i} - {p}")
            
            escolha = input("\nDigite o número do paciente que deseja remover: ")

            try:
                indice = int(escolha) - 1
                paciente_escolhido = pacientes[indice]

                print("\nVocê escolheu:")
                print(paciente_escolhido)

                confirmar = input("Confirmar exclusão? (s/n): ")

                if confirmar.lower() == "s":
                    cpf = paciente_escolhido[1]
                    service.remover_paciente(cpf)
                    print("Paciente removido com sucesso.")
                else:
                    print("Operação cancelada.")

            except (IndexError, ValueError):
                print("Escolha inválida.")
