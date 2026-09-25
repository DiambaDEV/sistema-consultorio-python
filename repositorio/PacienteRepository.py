class PacienteRepository:

    def __init__(self, db):
        self.db = db

    def salvar(self, paciente):
        query = """
        INSERT INTO pacientes (nome, cpf, telefone, data_nascimento)
        VALUES (%s, %s, %s, %s)
        """
        try:
            self.db.cursor.execute(query, (
                paciente.nome,
                paciente.cpf,
                paciente.telefone,
                paciente.data_nascimento
            ))
            self.db.conexao.commit()
        except Exception as e:
            self.db.conexao.rollback()
            print(f"Erro ao salvar paciente: {e}")

    def listar_pacientes(self):
        query = "SELECT * FROM pacientes"
        try:
            self.db.cursor.execute(query)
            return self.db.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao listar pacientes: {e}")
            return []

    def buscar_por_cpf(self, cpf):
        query = "SELECT * FROM pacientes WHERE cpf = %s"
        try:
            self.db.cursor.execute(query, (cpf,))
            return self.db.cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar paciente por CPF: {e}")
            return None

    def buscar_por_data_nascimento(self, data):
        query = """
        SELECT nome, cpf, telefone, data_nascimento
        FROM pacientes
        WHERE data_nascimento = %s
        """
        try:
            self.db.cursor.execute(query, (data,))
            return self.db.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar paciente por data de nascimento: {e}")
            return []

    def atualizar_telefone(self, cpf, novo_telefone):
        query = """
        UPDATE pacientes
        SET telefone = %s
        WHERE cpf = %s
        """
        try:
            self.db.cursor.execute(query, (novo_telefone, cpf))
            self.db.conexao.commit()
        except Exception as e:
            self.db.conexao.rollback()
            print(f"Erro ao atualizar telefone: {e}")

    def remover_paciente(self, cpf):
        query = "DELETE FROM pacientes WHERE cpf = %s"
        try:
            self.db.cursor.execute(query, (cpf,))
            self.db.conexao.commit()
        except Exception as e:
            self.db.conexao.rollback()
            print(f"Erro ao remover paciente: {e}")