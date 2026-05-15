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
    
    
