# funciones

def mensaje_2(name, clase, age, survived): 
    if survived == 1 or survived: 
        survived = 'vivo'
    else: 
        survived = 'fallecido'
    try: 
        age = int(age)
    except: 
        age = 'edad desconocida'
    try: 
        clase = str(int(clase)) + "ª"
    except: 
        clase = 'desconocida'
    name = namesplit(name)

    return "{}, pasajero de clase {}, de {} años:  {}.".format(name, clase, age, survived)


def namesplit(name): 
    res = name
    if ',' in name: 
        res = ' '.join(name.split(',')[::-1])
        
    return res