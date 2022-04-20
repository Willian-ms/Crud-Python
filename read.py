import mysql.connector
import datetime

# A conexão é feita conforme a instalação do MySql, portanto, é variável.
connection = mysql.connector.connect(
  host='localhost',
  user='admin',
  password='root',
  database='teste'
)

cursor =connection.cursor()

sql='SELECT *FROM users'

cursor.execute(sql)
results = cursor.fetchall()

cursor.close()
connection.close()

for result in results:
    print (result)