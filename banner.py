#!/usr/bin/python

import commands
import string
import pepito

c = 0
r = 0

while r != 99:

	unidades = commands.getoutput('ls /media/desdes/')

	unidades = unidades.split("\n")
	print "Unidades actuales"
	c = 1
	for i in unidades:
		print str(c)+")",i
		c=c+1
	print "98) Actualizar unidades"
	print "99) Salir\n"
	r = int(raw_input("Ingrese a la opcion: "))

	if (r < c):
		print "\nUnidad seleccionada:", unidades[r-1]
		break
	else:
		if r != 99 and r != 98:
			print "\nElija una opcion valida\n"

pepito.obtenerfile(str(unidades[r-1]))