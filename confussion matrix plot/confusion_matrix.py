#Donde la matriz de confusión es:

C = confusion_matrix(y_true,y_pred)

# Sklearn nos saca en la primera columna los
# predichos como cero(indoor), en vez de los predichos
# como uno(outdoor), así que cambiamos el orden de las
# columnas y filas. 

matriz_confusion_bis = np.array([(C[1]),
                              C[0]])[:,::-1]
print(C)
print(matriz_confusion_bis)

# true negative, false positive, etc...

tn = C[0,0]; fp = C[0,1]; fn = C[1,0]; tp = C[1,1]
NP = fn+tp # Num positive examples
NN = tn+fp # Num negative examples
N  = NP+NN

fpr = fp / (fp+tn+0.)
tpr = tp / (tp+fn+0.)