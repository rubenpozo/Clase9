import turtle

a=int(input('Ingrese cantidad de lados del poligono:\n'))
t=int(input('Ingrese el tamaño del lado del poligono:\n'))

def mipoligono(lados,tam):
	t=turtle.Pen()
	for x in range(1,lados+1):
		t.forward(tam)
		t.left(360/lados)
	turtle.getscreen()._root.mainloop()

mipoligono(a,t)