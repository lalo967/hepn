import time

ahora = time.strftime("%c")
## representacion de fecha y hora

arc=open("fechay.txt","a")

print "Fecha y hora " + time.strftime("%c")
arc.write(str(ahora) + '\n' + '\t')
arc.close
