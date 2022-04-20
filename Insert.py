import mysql.connector
import datetime

# A conexão é feita conforme a instalação do MySql, portanto, é variável.
connection=mysql.connector.connect(
host="localhost",
user = "admin",
password= "root",
database = "teste"
)

cursor = connection.cursor()
sql = "INSERT INTO users (name, email, created) VALUES (%s, %s, %s)"
data = (
  'Willian',
  'email@email.com',
  datetime.datetime.today()
)

cursor.execute(sql, data)
connection.commit()

userid = cursor.lastrowid

cursor.close()
connection.close()

print ('Foi cadastrado o usuário de ID: ', userid)
