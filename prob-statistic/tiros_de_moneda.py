# tiros_de_moneda.py  (modelo beta-binomial)


import sys
print(sys.version[:100])              # version del sistema (actual 3.7.2)
import numpy as np                    # numerical python, algebra lineal
from scipy import stats               # libreria estadistica de scipy
from matplotlib import pyplot as plt  # para plots


tiradas=[0,2,10,20,50,500]    # lista del numero de intentos (experimentos de Bernoulli)
  
datos=stats.bernoulli.rvs(0.5,size=tiradas[-1])   # se tiran 500 veces la moneda, 0-cruz, 1-cara (B(p,n))

x=np.linspace(0,1,100)  # espaciado lineal entre 0 y 1, 100 puntos, se discretiza el eje x


for i,N in enumerate(tiradas):  # se actualiza la informacion respecto al nº de tiradas, modelo beta-binomial (i actualizaciones , N tiradas)
	
	caras=datos[:N].sum()        # suma las caras que van saliendo
	
	ax=plt.subplot(len(tiradas)/2, 2, i+1)             # se crea un plot cada vez que se actualiza
	ax.set_title("%s tiradas, %s caras" % (N, caras))  # titulo  
	plt.xlabel("$P(x)$, Probabilidad de Cara")         # etiqueta x
	plt.ylabel("Densidad")                             # etiqueta y
	if i == 0:                                         # limite del eje y en el primer plot (0 tiradas)
		plt.ylim([0.0, 2.0])
	plt.setp(ax.get_yticklabels(), visible=False)      # quita los numeros del eje y
	y=stats.beta.pdf(x, 1+caras, 1+N-caras)            # se crea y se dibuja la distribucion beta que representa... (Beta(x,a,b))
	plt.plot(x,y)                                      # ... la creencia a posteriori de la perfeccion de la moneda (beta-binomial, bayesiano)
	plt.fill_between(x, 0, y, color='b', alpha=0.5)    # se rellena de color la distribucion 
	
	
plt.tight_layout()  # se expande el plot
plt.show()          # se plotea
