import turtle
a=int(input('Ingrese el numero de lados para dibujar:\n'))

t=turtle.Pen()
t.speed(1)
for x in range(1,a+1):
	t.forward(100)
	t.left(360/a)
turtle.getscreen()._root.mainloop()