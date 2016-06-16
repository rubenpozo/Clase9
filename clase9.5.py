import turtle

#a=int(input('Ingrese el numero de puntas para dibujar la estrella:\n'))
t=turtle.Pen()
t.speed(1)
for x in range(1,6):
	t.forward(100)
	t.left(144)
turtle.getscreen()._root.mainloop()