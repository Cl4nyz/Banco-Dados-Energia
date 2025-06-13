import csv
from dotenv import get_key
import psycopg2
import pandas as pd

NAME = get_key('.env', 'PG_NAME')
USER = get_key('.env', 'PG_USER')
PASSWORD = get_key('.env', 'PG_PASSWORD')
HOST = get_key('.env', 'PG_HOST')
PORT = get_key('.env', 'PG_PORT')

# Caminhos para os arquivos CSV utilizados
PROC_ENERGY_CSV = 'bancos/energia_processada.csv'
WORLD_DATA_CSV = 'bancos/WDI_processado.csv'

def create_pg_connection():
	"""Cria uma conexão com o banco de dados PostgreSQL."""
	try:
		conn = psycopg2.connect(
			dbname=NAME,
			user=USER,
			password=PASSWORD,
			host=HOST,
			port=PORT
		)
		print(f'Nome: {NAME}')
		return conn
	except Exception as e:
		print(f"Erro ao conectar ao banco de dados: {e}")
		return None
	
def close_pg_cursor(cursor):
	"""Fecha o cursor."""
	if cursor:
		cursor.close()
		print("Cursor fechado.")

def end_pg_connection(conn):
	"""Faz commit e encerra a conexão com o banco de dados."""
	if conn:
		conn.commit()
		conn.close()
		print("Conexão encerrada.")

def execute_query(conn, query, num=0):
	"""Executa uma consulta SQL e retorna os resultados."""
	cursor = conn.cursor()
	try:
		cursor.execute(query)
		results = cursor.fetchall()
		colnames = [desc[0] for desc in cursor.description]
		df = pd.DataFrame(results, columns=colnames)
		print(df.to_string(index=False))
		if (num != 0):
			df.to_csv(f'resultados/resultado_query_{num}.csv', index=False)
		print("Query executada com sucesso.")
	except Exception as e:
		print(f"Erro ao executar consulta: {e}")
		return None
	finally:
		close_pg_cursor(cursor)

def query_rows(conn, query):
	cursor = conn.cursor()
	cursor.execute(query)
	return cursor.fetchall()