import mysql.connector
import datetime

# A conexão é feita conforme a instalação do MySql, portanto, é variável.
connection = mysql.connector.connect(
  host='localhost',
  user='admin',
  password='root',
  database='teste'
)

cursor = connection.cursor()
sql = 'UPDATE users SET name = %s, email = %s WHERE id = %s'
data=(
  'terceiro usuario',
  'email.alterado@email.com',
  9
)
#O ID alterado será considerado conforme informado na linha 17. 


cursor.execute(sql, data)
connection.commit()

recordsaffected = cursor.rowcount

cursor.close()
connection.close()

print (recordsaffected, 'Registros alterados')
