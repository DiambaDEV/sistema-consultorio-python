from datetime import datetime

from repositorio.BancoDeDados import BancoDeDados
from repositorio.PacienteRepository import PacienteRepository
from repositorio.AgendamentoRepository import AgendamentoRepository
from services.PacienteService import PacienteService
from services.AgendamentoService import AgendamentoService
from modelos.Paciente import Paciente
from modelos.Agendamento import Agendamento
from utils.telefone_utils import validar_telefone, formatar_telefone
from utils.cpf_utils import formatar_cpf, validar_cpf   
from utils.data_utils import formatar_data 

db = BancoDeDados()
repository = PacienteRepository(db)
service = PacienteService(repository)
agendamento_repository = AgendamentoRepository(db)
agendamento_service = AgendamentoService(agendamento_repository)


while True:

    print("\n=== SISTEMA CONSULTÓRIO ===")
    print("1 - Cadastrar paciente")
    print("2 - Buscar pacientes")
    print("3 - Listar pacientes")
    print("4 - Editar paciente")
    print("5 - Remover paciente")
    print("6 - Criar agendamento")
    print("7 - Listar agendamentos")
    print("8 - Buscar agendamento por CPF")
    print("9 - Buscar agendamento por Data")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        
        while True:

            nome = input("Nome: ")

            if nome.replace(" ", "").isalpha():
                break
            else:
                print("Nome inválido. Digite apenas letras.")
        
        cpf = input("CPF (somente números): ")

        cpf = ''.join(filter(str.isdigit, cpf))

        if not validar_cpf(cpf):
            print("CPF inválido.")
            continue 

        while True:

            data_nascimento = input("Data de nascimento (AAAA-MM-DD): ")

            try:
                date = datetime.strptime(data_nascimento, "%Y-%m-%d")

                if date > datetime.now():
                    print("Data de nascimento não pode ser no futuro.")
                    continue    
                break

            except ValueError:
                print("Data inválida. Digite no formato AAAA-MM-DD.")   

        while True:

            telefone = input("Telefone (somente números): ")

            if validar_telefone(telefone):
                telefone = ''.join(filter(str.isdigit, telefone))
                break
            else:
                print("Telefone inválido. Digite um telefone DDD + número, com 10 ou 11 dígitos numéricos.")

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
                print(
                    f"Nome: {p[1]} | "
                    f"CPF: {formatar_cpf(p[2])} | "
                    f"Telefone: {formatar_telefone(p[3])} | "
                    f"Data: {formatar_data(p[4])}"
                )
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

    elif opcao == "6":

        cpf = input("CPF do paciente: ")

        paciente = service.buscar_por_cpf(cpf)

        if not paciente:
            print("Paciente não encontrado.")

        else:

            # 🔹 DATA
            while True:
                data = input("Data de agendamento (AAAA-MM-DD): ")

                try:
                    date = datetime.strptime(data, "%Y-%m-%d")
                    if date.date() < datetime.now().date():
                        print("Não é possível agendar em datas passadas.")
                        continue
                    break
                except ValueError:
                    print("Data inválida. Digite novamente.")

            # 🔹 HORA + CONFLITO
            while True:
                hora = input("Hora de agendamento (HH:MM): ")

                try:
                    datetime.strptime(hora, "%H:%M")
                except ValueError:
                    print("Hora inválida. Digite novamente.")
                    continue

                agendamento_existente = agendamento_repository.buscar_por_data_hora(
                    data,
                    hora
                )

                if agendamento_existente:
                    print("Já existe um agendamento nesse horário. Tente outro.")
                    continue

                break

            # 🔹 MOTIVO
            motivo = input("Motivo da consulta: ")

            agendamento = Agendamento(
                cpf,
                data,
                hora,
                motivo
            )

            agendamento_service.criar_agendamento(agendamento)
    elif opcao == "7":

        agendamentos = agendamento_service.listar_agendamentos()

        if agendamentos:

            print("\n--- AGENDAMENTOS ---")

            for a in agendamentos:
                print(
                    f"ID: {a[0]} | "
                    f"CPF: {formatar_cpf(a[1])} | "
                    f"Data: {a[2]} | "
                    f"Hora: {a[3]} | "
                    f"Motivo: {a[4]}"
                )

        else:
            print("Nenhum agendamento encontrado.")

    elif opcao == "8":

        cpf = input("Digite o CPF: ")
        agendamentos = agendamento_service.buscar_por_cpf(cpf)
        if agendamentos:
            for a in agendamentos:
                print(
                    f"ID: {a[0]} | "
                    f"CPF: {formatar_cpf(a[1])} | "
                    f"Data: {a[2]} | "
                    f"Hora: {a[3]} | "
                    f"Motivo: {a[4]}"
                )
        else:
            print("Nenhum agendamento encontrado para esse CPF.")
    
    elif opcao == "9":

        data = input("Digite a data (AAAA-MM-DD): ")
        agendamentos = agendamento_service.buscar_por_data(data)
        if agendamentos:
            for a in agendamentos:
                print(
                    f"ID: {a[0]} | "
                    f"CPF: {formatar_cpf(a[1])} | "
                    f"Data: {a[2]} | "
                    f"Hora: {a[3]} | "
                    f"Motivo: {a[4]}"
                )
        else:
            print("Nenhum agendamento encontrado para essa data.")

    elif opcao == "10":

        agendamentos = agendamento_service.listar_agendamentos()

        if not agendamentos:
            print("Nenhum agendamento encontrado.") 
        else:
            print("\n--- AGENDAMENTOS ---")

            for a in agendamentos:
                print(
                    f"ID: {a[0]} | "
                    f"CPF: {formatar_cpf(a[1])} | "
                    f"Data: {a[2]} | "
                    f"Hora: {a[3]} | "
                    f"Motivo: {a[4]}"
                )

            escolha = input("\nDigite o ID do agendamento que deseja cancelar: ")

            try:
                id = int(escolha)
                agendamento_escolhido = None

                for a in agendamentos:
                    if a[0] == id:
                        agendamento_escolhido = a
                        break

                if not agendamento_escolhido:
                    print("Agendamento não encontrado.")
                    continue

                print("\nVocê escolheu:")
                print(
                    f"ID: {agendamento_escolhido[0]} | "
                    f"CPF: {formatar_cpf(agendamento_escolhido[1])} | "
                    f"Data: {agendamento_escolhido[2]} | "
                    f"Hora: {agendamento_escolhido[3]} | "
                    f"Motivo: {agendamento_escolhido[4]}"
                )

                confirmar = input("Confirmar cancelamento? (s/n): ")

                if confirmar.lower() == "s":
                    agendamento_service.cancelar(id)
                else:
                    print("Operação cancelada.")

            except ValueError:
                print("ID inválido. Digite um número inteiro.")

    elif opcao == "0":
        print("Encerando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")   
