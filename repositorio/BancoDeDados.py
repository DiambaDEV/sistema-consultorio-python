import mysql.connector

class BancoDeDados:

    def __init__(self):
        self.conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1010",
            database="consultorio"
        )

        self.cursor = self.conexao.cursor()
    
    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()

    def buscar_por_data_nascimento(self, data):
        query = """
        SELECT nome, cpf, telefone, data_nascimento
        FROM pacientes
        WHERE data_nascimento = %s
        """

        self.db.cursor.execute(query, (data,))
        return self.db.cursor.fetchall()
    
    def listar_pacientes(self):
        query = "SELECT * FROM pacientes"
        self.db.cursor.execute(query)
        return self.db.cursor.fetchall()
    
    
