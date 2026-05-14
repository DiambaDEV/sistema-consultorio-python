class PacienteService:

    def __init__(self, repository):
        self.repository = repository

    def cadastrar_paciente(self, paciente):
        
        paciente_existente = self.repository.buscar_por_cpf(paciente.cpf)

        if paciente_existente:
            print("Paciente já cadastrado.")
            return

        self.repository.salvar(paciente)
        print("Paciente cadastrado com sucesso.")

    def listar_pacientes(self):
        return self.repository.listar_pacientes()

    def buscar_por_cpf(self, cpf):
        return self.repository.buscar_por_cpf(cpf)

    def buscar_por_data_nascimento(self, data):
        return self.repository.buscar_por_data_nascimento(data)

    def atualizar_telefone(self, cpf, telefone):
        self.repository.atualizar_telefone(cpf, telefone)

    def remover_paciente(self, cpf):
        self.repository.remover_paciente(cpf)
