import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

class BancoDeDados:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        self.cursor = self.conexao.cursor()

    def fechar_conexao(self):
        self.cursor.close()
        self.conexao.close()