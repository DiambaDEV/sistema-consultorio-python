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

        self.db.cursor.execute(query, valores)
        self.db.conexao.commit()

    def listar(self):
        query = "SELECT * FROM agendamentos"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    def buscar_por_data_hora(self, data, hora):

        query = """
        SELECT * FROM agendamentos
        WHERE data = %s AND hora = %s
        """

        self.db.cursor.execute(query, (data, hora))

        return self.db.cursor.fetchone()
