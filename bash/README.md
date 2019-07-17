# Bash exercices

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
* Encuentra al usuario activo en el sistema
* Encuentra dónde estás en tu sistema de ficheros
* Lista los ficheros que terminan por txt en la carpeta lorem
* Muestra el contenido de los ficheros `at.txt` y `lorem.txt`
* contar el número de **archivos** que empiezan por `lorem` que están en este directorio y en directorios internos

```console
find . -name 'lorem*' -type f | wc -l
```
