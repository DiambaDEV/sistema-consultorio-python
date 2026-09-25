class AgendamentoService:

    def __init__(self, repository):
        self.repository = repository

    def criar_agendamento(self, agendamento):
        
        agendamento_existente = self.repository.buscar_por_data_hora(
            agendamento.data,
            agendamento.hora
        )

        if agendamento_existente:
            print("Já existe um agendamento nesse horário.")

        else:
            self.repository.salvar(agendamento)
            print("Agendamento criado com sucesso.")
            
    def listar_agendamentos(self):
        return self.repository.listar()
    
    # Não agendar em fins de semana

    def buscar_por_cpf(self, cpf):
        return self.repository.buscar_por_cpf(cpf)
    
    def buscar_por_data(self, data):
        return self.repository.buscar_por_data(data)
    
    def cancelar(self, id):
        agendamento = self.repository.buscar_por_id(id)

        if not agendamento:
            print("Agendamento não encontrado.")
            return
        
        self.repository.cancelar(id)
        print("Agendamento cancelado com sucesso.")


