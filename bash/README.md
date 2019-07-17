# Bash exercices

## Links to remove
https://linuxhint.com/30_bash_script_examples/
https://www.tutorialspoint.com/unix/

## Intro

Vamos a practicar con `bash`, un lenguaje de programación que se ejecuta en la línea de comandos!

## Setup
1. Ubícate en la carpeta en la que ejecutando en el terminal. Al ejecutar `ls` 
```console
$ ls
```

2. Deberías ver: 
```console
exercices  inputs  lorem  lorem-copy  modules  outputs  README.md
```
## Ejercicios
* Imprime en consola "Hello World".
* Almacena en una variable `name` tu nombre mediante el comando `read`.
* Imprime esa variable.
* Crea un directorio nuevo llamado `new_dir`.
* Elimina ese directorio.
* Crea un directorio nuevo que se llame como el contenido de la variable `name`.
* Elimina ese directorio. 
* Copia el archivo `sed.txt` dentro de la carpeta lorem a la carpeta lorem-copy. 
* Copia los otros dos archivos de la carpeta lorem a la carpeta lorem-copy en una sola linea mediante el pipe `|`. 
* 
* Visualiza las primeras 3 linas del archivo `sed.txt` dentro de la carpeta lorem-copy 
* Visualiza las ultimas 3 linas del archivo `sed.txt` dentro de la carpeta lorem-copy 
* Añade `Homo homini lupus.` al final de archivo `sed.txt` dentro de la carpeta lorem-copy. 
* Visualiza las últimas 3 linas del archivo `sed.txt` dentro de la carpeta lorem-copy. Deberías ver ahora `Homo homini lupus.`
* Encuentra al usuario activo en el sistema.
* Encuentra dónde estás en tu sistema de ficheros.
* Lista los archivos que terminan por `txt` en la carpeta lorem.
* Muestra el contenido del archivo `sed.txt` dentro de la carpeta lorem.
* Muestra el contenido de los archivos `at.txt` y `lorem.txt` dentro de la carpeta lorem. 
* Cuenta el número de lineas que tiene el archivo `sed.txt` dentro de la carpeta lorem. Tendrás que usar `cat` y `wc`. 
* Cuenta el número de **archivos** que empiezan por `lorem` que están en este directorio y en directorios internos

```console
find . -name 'lorem*' -type f | wc -l
```




## Ficheros bash

Cualquier comandos o comandos de bash se pueden almacenar en un fichero. Creamos el fichero: 
```console
$ nano list_files.sh
```
E incluimos el contenido que queramos. 
```python
#!/bin/bash
ls
```

Una vez con los permisos adecuados podemos ejecutar el script `$ chmod a+x list_files.sh`
```console
$ bash list_files.sh
```
Y veremos por consola el siguiente output. 
```console
exercices  inputs  lorem  lorem-copy  modules  outputs  README.md
```

## Bonus

