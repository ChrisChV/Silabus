f = open ('u2.data','r')
salida= open('u3.data','w')
for x in f:
	x=x.replace(",","\t")
	x=x.rstrip('\n')
	y=x+"\t2\n"
	print(y)
	salida.write(y)	