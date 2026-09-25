class Paciente:

    def __init__(self, nome, cpf, telefone, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.data_nascimento = data_nascimento

    def __str__(self):
        return (
            f"Nome: {self.nome} | "
            f"CPF: {self.cpf} | "
            f"Telefone: {self.telefone} | "
            f"Data de nascimento: {self.data_nascimento}"
        )