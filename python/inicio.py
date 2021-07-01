arc=open("p.txt","a")
i=1
while i < 100:
      i = i + 1
      print (i)
      arc.write(str(i) + '\n' + '\t')

arc.close()
