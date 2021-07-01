import pymysql

try:
	conn = pymysql.connect(host='localhost', user='root',password='1',db='sensores')
	print("Conexión correcta")

	try:
            with conexion.cursor() as cursor:
                adjuntar ="LOAD DATA INFILE '/tmp/tem.txt'  into table sensores  FIELLOAD DATA INFILE '/tmp/tem.txt'  into table sensores  FIELDS TERMINATED BY ','  LINES TERMINATED BY '\n' (t0,TA,fv);"
                cursor.execute(adjuntar, (t0,TA,fv))
                conexion.commit()
           
            finally:
		conexion.close()




except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)

 





#cursor= conn.cursor()
# Recuperar registros de la tabla 'sensores'
#registros = "SELECT * FROM sensores;"

# Mostrar registros
#cursor.execute(registros)
#filas = cursor.fetchall()
#for fila in filas:
#   print(fila)

# Definir comandos para insertar registros

#registro1 = "INSERT INTO sensores (ejemplo) VALUES (%s);"
#val = input("agrega un numero")
# Ejecutar comandos
#cursor.execute(registro1,val)


# Finalizar
#conn.commit()
#conn.close()
