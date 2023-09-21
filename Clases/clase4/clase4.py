# CONEXION A BASES DE DATOS

# MySQL <-- mysql-connector-python, PyMySQL, MySQLdb
# PostgreSQL --> psycopg, pg8000
# SQLite <-- sqlite3
# SQL Server --> pymssql, pyodbc
# Oracle --> cx_Oracle

# SQLite

# Browser --> https://sqlitebrowser.org

import sqlite3

# Variable donde guarda la BBDD
dir = "C:\\Users\\AndresGiuffre\\OneDrive - kyndryl\\Documents\\PythonProgramming\\python_programming\\Clases\\clase4\\"

# Crear una conexión con la BBDD
conn = sqlite3.connect(dir + "database.sqlite")

# Crear cursor
cursor = conn.cursor()

# Correr código SQL con el método execute()
cursor.execute("CREATE TABLE personas (nombre TEXT, edad NUMERIC)")

# Realizamos un commit() para confirmar los cambios
conn.commit()

# Finalizamos la conexión
conn.close()