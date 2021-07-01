import pymysql

connection  = pymysql.connect(host='localhost', user='root',password='1',db='sensores')
cursor = connection .cursor()
query ="LOAD DATA INFILE '/tmp/tem.txt' into table sensores FIELDS TERMINATED BY ','  LINES TERMINATED BY '\n' (t0,TA,fv);"
cursor.execute( query )
connection.commit()
