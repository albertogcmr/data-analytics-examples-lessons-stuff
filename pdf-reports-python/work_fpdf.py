# work_fpdf.py


from fpdf import FPDF                  # para crear pdf


'''
pip3 install fpdf --user

https://pypi.org/project/fpdf/

http://www.fpdf.org

https://github.com/reingart/pyfpdf

https://pyfpdf.readthedocs.io/en/latest/Tutorial/index.html
'''

'''
# 1-hola mundo

pdf=FPDF()                             # por defecto se crea en formato dinA4, explicitamente FPDF('P', 'mm', 'A4')

pdf.add_page()                         # se añade una pagina, origen arriba a la izq a 1cm

#pdf.set_margins()                     # se pueden ajustar los margenes , set_top_margin, set_left_margin, set_right_margin, set_auto_page_break

pdf.set_font('Arial', 'B', 16)         # se define la fuente de letra (Arial, negrita, tamaño 16)

pdf.cell(40, 10, '¡Hola Mundo!')       # se crea la celda del texto, (ancho(mm), alto(mm), texto)

#pdf.cell(w=0, h=0, txt='a', border=0, ln=0, align='', fill=False, link='')
# (ancho, alto, texto, borde, salto de linea, alineado, relleno, url)

pdf.output('hola mundo.pdf', 'F')      # guardado del pdf, en la misma carpeta que el archivo (nombre, destino)
# destino

#   I: envia el archivo al buscador
#   D: envia el archivo al buscador y fuerza la descarga
#   F: guarda el archivo en local, puede incluir el path
#   S: devuelve el documento como string
'''







'''
# 2-imagenes

pdf=FPDF()                                                          # formato dinA4

pdf.add_page()                                                      # añade pagina

pdf.set_xy(0, 0)                                                    # define abscisa y ordinate, posicion actual. Si el valor es nagativo empieza por abajo

pdf.set_font('arial', 'B', 12)                                      # arial 12 en negrita

pdf.cell(60)                                                        # posicion texto

pdf.cell(90, 10, "Solar Flares vs Sunspots", 0, 2, 'C')             # titulo

pdf.cell(90, 10, " ", 0, 2, 'C')                                    # celda vacia, como salto de linea

pdf.image('sol.jpg', x=8, y=20, w=20, h=60, type = '', link = '') # imagen 

pdf.output('sol.pdf', 'F')                                          # guardado del pdf
'''






'''
# 3-clase pdf

class PDF(FPDF):
	
    def header(self):                          # cabecera
        self.image('binning.png', 10, 8, 33)   # imagen
        self.set_font('Arial', 'B', 15)        # Arial negrita 15        
        self.cell(80)                          # mueve a la derecha        
        self.cell(30, 10, 'Title', 1, 0, 'C')  # titulo
        self.ln(20)                            # salto de linea

    def footer(self):                                                           # pie de pagina
        self.set_y(-15)                                                         # posicion a 1.5 cm desde abajo
        self.set_font('Arial', 'I', 8)                                          # Arial italica 8
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')    # numero de pagina


# inicio de la clase
pdf=PDF()                                               # inicia clase PDF, crea pdf
pdf.alias_nb_pages()                                    # define un alias para el numero total de paginas 
pdf.add_page()                                          # añade pagina
pdf.set_font('Times', '', 12)                           # selecciona la fuente de letra
for i in range(1, 41):                                  # bucle para crear lineas de texto
    pdf.cell(0, 10, 'Numero de linea ' + str(i), 0, 1)  # añade celdas de texto
pdf.output('clase pdf.pdf', 'F')                        # guarda pdf
'''





'''
# 4-clase completo


titulo='Python Data Science Handbook'

class PDF(FPDF):
    def header(self):                              # cabecera
        self.set_font('Arial', 'B', 15)            # fuente Arial negrita 15  
        ancho=self.get_string_width(titulo)+6      # calcula el ancho del titulo y su posicion
        self.set_x((210-ancho)/2)
        self.set_draw_color(0, 80, 180)            # colores del marco, fondo y texto
        self.set_fill_color(230, 230, 0)
        self.set_text_color(220, 50, 50)
        self.set_line_width(1)                     # ancho del marco (1 mm)
        self.cell(ancho, 9, titulo, 1, 1, 'C', 1)  # titulo
        self.ln(10)                                # salto de linea


    def footer(self):                                                # pie de pagina
        self.set_y(-15)                                              # posicion a 1.5 cm desde abajo
        self.set_font('Arial', 'I', 8)                               # fuente Arial italica 8
        self.set_text_color(128)                                     # color texto en gray
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')   # numero de pagina


    def chapter_title(self, numero, etiqueta):                                 # titulo del capitulo
        self.set_font('Arial', '', 12)                                         # fuente Arial 12
        self.set_fill_color(200, 220, 255)                                     # color del fondo
        self.cell(0, 6, 'Chapter %d : %s' % (numero, etiqueta), 0, 1, 'L', 1)  # titulo
        self.ln(4)                                                             # salto de linea


    def chapter_body(self, nombre, numero):                      # cuerpo del capitulo
        with open(nombre, 'rb') as f:                            # se lee el archivo de texto
            txt=f.read().decode('latin-1')
        self.set_font('Times', '', 12)                           # fuente Times 12
        self.multi_cell(0, 5, txt)                               # texto con saltos de linea (multicelda)
        self.ln()                                                # salto de linea
        self.set_font('', 'I')                                   # alusion en fuente italica
        self.cell(0, 5, '(fin del capitulo {})'.format(numero))


    def print_chapter(self, numero, titulo, nombre):     # imprime el capitulo
        self.add_page()                                  # añade pagina
        self.chapter_title(numero, titulo)               # numero y titulo de capitulo
        self.chapter_body(nombre, numero)                # cuerpo del capitulo



pdf=PDF()                                                             # inicia clase PDF
pdf.set_title(titulo)                                                 # titulo
pdf.set_author('Jake VanderPlas')                                     # autor
pdf.print_chapter(1, 'IPython: Beyond Normal Python', 'c1.txt')       # capitulo 1
pdf.print_chapter(2, 'Introduction to NumPy', 'c2.txt')               # capitulo 2
pdf.output('libro.pdf', 'F')                                          # guarda pdf
'''


























