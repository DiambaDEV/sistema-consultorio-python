class AgendamentoRepository:

    def __init__(self, db):
        self.db = db

    def salvar(self, agendamento):
        query = """
        INSERT INTO agendamentos (cpf_paciente, data, hora, motivo)
        VALUES (%s, %s, %s, %s)
        """

        valores = (
            agendamento.cpf_paciente,
            agendamento.data,
            agendamento.hora,
            agendamento.motivo
        )
        try: 
            self.db.cursor.execute(query, valores)
            self.db.conexao.commit()
        except Exception as e:
            self.db.conexao.rollback()
            print(f"Erro ao salvar agendamento: {e}")

    def listar(self):
        query = "SELECT * FROM agendamentos"
        try:
            self.db.cursor.execute(query)
            return self.db.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao listar agendamentos: {e}")
            return []

    def buscar_por_data_hora(self, data, hora):

        query = """
        SELECT * FROM agendamentos
        WHERE data = %s AND hora = %s
        """
        try:
            self.db.cursor.execute(query, (data, hora))
            return self.db.cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar agendamento por data e hora: {e}")
            return None

    def buscar_por_cpf(self, cpf):
        query = """
        SELECT * FROM agendamentos
        WHERE cpf_paciente = %s
        """
        try:
            self.db.cursor.execute(query, (cpf,))
            return self.db.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar agendamento por CPF: {e}")
            return []
    
    def buscar_por_data(self, data):
        query = """
        SELECT * FROM agendamentos
        WHERE data = %s
        """
        try:
            self.db.cursor.execute(query, (data,))
            return self.db.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar agendamento por data: {e}")
            return []
    
    def buscar_por_data(self, data):
        query = """
        SELECT * FROM agendamentos
        WHERE data = %s
        """
        try:
            self.db.cursor.execute(query, (data,))
            return self.db.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao buscar agendamento por data: {e}")
            return []
        
    def cancelar(self, id):
        query = "DELETE FROM agendamentos WHERE id = %s"
        try:
            self.db.cursor.execute(query, (id,))
            self.db.conexao.commit()
        except Exception as e:
            self.db.conexao.rollback()
            print(f"Erro ao cancelar agendamento: {e}")

    def buscar_por_id(self, id):
        query = "SELECT * FROM agendamentos WHERE id = %s"
        try:
            self.db.cursor.execute(query, (id,))
            return self.db.cursor.fetchone()
        except Exception as e:
            print(f"Erro ao buscar agendamento por ID: {e}")
            return None