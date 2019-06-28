# work_reportlab.py


from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, letter

'''
pip3 install reportlab --user

https://www.reportlab.com/documentation/

https://recursospython.com/guias-y-manuales/crear-documentos-pdf-en-python-con-reportlab/

'''


'''
# 1-hola mundo

ancho, alto=A4                                  # ancho y alto de la pagina, en dinA4, es una tupla en puntos (un punto=1/72 pulgadas)

print (A4)
print (letter)

c=canvas.Canvas("hola mundo.pdf", pagesize=A4)  # genera el archivo pdf vacio, con tamaño dinA4

c.drawString(ancho, alto, "¡Hola, mundo!")      # escribe con margen de 50 puntos
 
c.showPage()                                    # fin o cambio de pagina (se pierden los estilos)

c.save()                                        # guardado de archivo
'''



'''
# 2- figuras geometricas

ancho, alto=A4 
c=canvas.Canvas("figuras geometricas.pdf", pagesize=A4)  # genera el pdf

                       
x=120
y=alto-45

c.drawString(30, alto-50, "Linea")
c.line(x, y, x+100, y)                                # pinta una linea

c.drawString(30, alto-140, "Rectangulo")
c.rect(x, alto-160, 100, 50)                          # pinta un rectangulo

c.drawString(30, alto-300, "Rectangulo Curvo")
c.roundRect(x, alto-500, 300, 200, 10)                # pinta un rectangulo con esquinas curvas

c.showPage()                                          # cambia de pagina

c.drawString(30, alto-170, "Circulo")
c.circle(170, alto-165, 20)                           # pinta circulo

c.drawString(30, alto-240, "Elipse")
c.ellipse(x, y-170, x+100, y-220)                     # pinta elipse

# bezier(), arc(), wedge()

c.showPage()
c.save()
'''


'''
# 3-estilos

ancho, alto=A4 
c=canvas.Canvas("figuras geometricas rellenas.pdf", pagesize=A4)  # genera el pdf

c.setFillColorRGB(1, 0, 0)                                        # valores RGB entre 0.0 y 1.0

c.drawString(50, alto-50, "¡Hola, mundo!")                        # escribe

c.rect(50, alto-150, 50, 50, fill=True)                           # rellena el rectangulo

c.setStrokeColorRGB(0.7, 0, 0.7)                                  # pon color, entre 0 y 1

c.showPage()
c.save()
'''


'''
# 4-texto

ancho, alto=A4 
c=canvas.Canvas("texto.pdf", pagesize=A4)  # genera el pdf

text=c.beginText(50, alto-50)              # empieza el texto

text.setFont("Times-Roman", 12)            # selecciona fuente
 

text.textLine("¡Hola, mundo!")
text.textLine("¡Bienvenido a IronHack!")  # las dos frases aparecen en dos lineas diferentes

text.textLines("Aqui estamos\nConectados a la wifi")  # o alternativo

c.drawText(text)                          # escribe

c.showPage()                 
c.save()
'''


'''
# 5-imagenes

ancho, alto=A4 
c=canvas.Canvas("imagen.pdf", pagesize=A4)                        # genera el pdf

c.drawImage("binning.png", 0, 0, width=600, height=350)   # pinta la imagen

c.showPage()                 
c.save()
'''

'''
# 6-grid

ancho, alto=A4 
c=canvas.Canvas("grid.pdf", pagesize=A4)       # genera el pdf


xlist=[10, 60, 110, 160]                       # puntos de la malla
ylist=[alto-10, alto-60, alto-110, alto-160]
c.grid(xlist, ylist)

c.showPage()                 
c.save()
'''




# 7-ejemplo


import itertools
from random import randint
from statistics import mean
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def grouper(iterable, n):
	args=[iter(iterable)]*n
	return itertools.zip_longest(*args)
	
def export_to_pdf(data):
	c=canvas.Canvas("grilla-alumnos.pdf", pagesize=A4)
	w, h=A4
	max_rows_per_page=45
	
	x_offset=50    # margen
	y_offset=50
	
	padding=15   # espacio entre filas
	
	xlist=[x+x_offset for x in [0, 200, 250, 300, 350, 400, 480]]
	ylist=[h-y_offset-i*padding for i in range(max_rows_per_page+1)]
	
	for rows in grouper(data, max_rows_per_page):
		rows=tuple(filter(bool, rows))
		c.grid(xlist, ylist[:len(rows)+1])
		for y, row in zip(ylist[:-1], rows):
			for x, cell in zip(xlist, row):
				c.drawString(x+2, y-padding+3, str(cell))
		c.showPage()
	
	c.save()
	
data=[("NOMBRE", "NOTA 1", "NOTA 2", "NOTA 3", "PROM.", "ESTADO")]

for i in range(1, 101):
	exams=[randint(0, 10) for _ in range(3)]
	avg=round(mean(exams), 2)
	state="Aprobado" if avg >= 4 else "Desaprobado"
	data.append((f"Alumno {i}", *exams, avg, state))
export_to_pdf(data)
























