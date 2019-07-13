# virtual Environments

## 1. Documentation

Link: https://realpython.com/python-virtual-environments-a-primer/ 

## 2. Installation

```
sudo apt-get install python3-venv
pip3 install virtualenv
```

## 3. Create virtual environment

Create a new virtual environment inside the directory. 

``` 
$ python3 -m venv env
```

Activate virtual environment

```
$ source env/bin/activate
```
Now you see: 

```
(env) $
```

## 4. Requirements
Crea tu proyecto y ve instalando únicamente las librerías que necesitas. Así no se incluyen ni pisan las que ya tienes en tu sistema. 

Para ver las librerías instaladas en el entorno actual: 

```
(env) $ pip3 freeze
```

Now you see nothing but:  

```
pkg-resources==0.0.0
(env) $
```

Instalamos numpy para nuestro `main.py`

```
(env) $ pip3 install numpy
```

Now you see numpy installed:  

```
numpy==1.16.4
pkg-resources==0.0.0
(env) $
```

Vamos a crear un archivo `requirements.txt` que contiene todas las dependencias que necesita nuestro programa con la versión adecuada, así en un futuro podremos saber qué versión de cada librería se usaba. Puede que versiones futuras de numpy funcionen de otra forma a la deseada en nuestro programa actual. 

```
(env) $ pip3 freeze > requirements.txt
```

Esto crea el archivo `requirements.txt` con el contenido del output del comando `pip3 freeze`. 

Ahora puedes trabajar en tu código sin miedo a que desconfigure tu PC. 

## 5. Deactivate venv

Una vez hayas terminado de trabajar simplemente deja cerrado el entorno hasta la siguiente vez que tengas que activarlo. 

```
(env) $ deactivate
```

Now you see:  

```
$
```

## 5. Exporting code

Cuando queramos exportar este proyecto a otro PC, simplemente habrá que instalar virtualenv en ese otro equipo y seguir los pasos del apartado `3. Create virtual environment` y activarlo. Una vez activo hay que instalar todo lo que diga `requirements.txt` mediante el siguiente comando. 

```
(env) $ pip3 install -r requirements.txt
```

Y cuando vuelvas a ejecutar dentro del entorno virtual el comando `pip3 freeze` obtendrás el siguiente output: 

```
(env) $ pip3 freeze
numpy==1.16.4
pkg-resources==0.0.0
```