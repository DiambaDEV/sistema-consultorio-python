class Agendamento:

    def __init__(self, cpf_paciente, data, hora, motivo):
        self.cpf_paciente = cpf_paciente
        self.data = data
        self.hora = hora
        self.motivo = motivo

    def __str__(self):
        return (
            f"CPF: {self.cpf_paciente} | "
            f"Data: {self.data} | "
            f"Hora: {self.hora} | "
            f"Motivo: {self.motivo}"
        )