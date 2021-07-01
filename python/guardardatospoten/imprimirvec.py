arc=open("while.txt","w")
def prueba():
    s="hola"
    a = 1
    b=[]
    while a <100:
         print(a)
         a = a + 1
	 b.append(a)
    return b,s

arc.write(str(prueba()))
arc.close()
