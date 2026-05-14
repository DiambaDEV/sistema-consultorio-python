class PacienteRepository:

    def __init__(self, db):
        self.db = db

    def salvar(self, paciente):
        query = """
        INSERT INTO pacientes (nome, cpf, telefone, data_nascimento)
        VALUES (%s, %s, %s, %s)
        """
        self.db.cursor.execute(query, (
            paciente.nome,
            paciente.cpf,
            paciente.telefone,
            paciente.data_nascimento
        ))
        self.db.conexao.commit()

    def listar_pacientes(self):
        query = "SELECT * FROM pacientes"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()

    def buscar_por_cpf(self, cpf):
        query = "SELECT * FROM pacientes WHERE cpf = %s"
        self.db.cursor.execute(query, (cpf,))
        return self.db.cursor.fetchone()

    def buscar_por_data_nascimento(self, data):
        query = """
        SELECT nome, cpf, telefone, data_nascimento
        FROM pacientes
        WHERE data_nascimento = %s
        """
        self.db.cursor.execute(query, (data,))
        return self.db.cursor.fetchall()

    def atualizar_telefone(self, cpf, novo_telefone):
        query = """
        UPDATE pacientes
        SET telefone = %s
        WHERE cpf = %s
        """
        self.db.cursor.execute(query, (novo_telefone, cpf))
        self.db.conexao.commit()

    def remover_paciente(self, cpf):
        query = "DELETE FROM pacientes WHERE cpf = %s"
        self.db.cursor.execute(query, (cpf,))
        self.db.conexao.commit()