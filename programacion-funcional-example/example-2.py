# variables
arr = [1,2,8,5,8,8,2,1,2,3,4,5,4,3,2]

# resta 3
arr = [x-3 for x in arr]

# eleva al cuadrado
arr = [x**2 for x in arr]

# resta 2
arr = [x-2 for x in arr]

# suma 3
arr = [x+3 for x in arr]

# el último pasa a ser el primero
arr = [arr[-1]] + arr[:-1]

# resultado: suma los 5 primeros
suma = sum(arr[:5])

print(suma)


# ahora refactoriza para hacer lo mismo en orden inverso (menos resultado). 
