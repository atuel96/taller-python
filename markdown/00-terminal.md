# Comandos Básicos para moverse con la Terminal

### 1. Listar el contenido de un directorio: ls
El comando `ls` se utiliza para listar el contenido del directorio actual. Esto te muestra los archivos y carpetas dentro de la carpeta en la que te encuentras.

``` bash
ls
```
### 2. Crear un nuevo directorio: mkdir
El comando `mkdir` seguido del nombre de la carpeta crea una carpeta con ese nombre. Por ejemplo, para crear una carpeta llamada mi_carpeta:

``` bash
mkdir mi_carpeta
```
### 3. Cambiar de directorio: cd
Para entrar en un directorio, se usa el comando `cd` (que significa "cambiar directorio"). Para entrar en la carpeta mi_carpeta recién creada:

``` bash
cd mi_carpeta
```
Ahora estás dentro de mi_carpeta.

### 4. Volver al directorio anterior: cd ..
Para volver al directorio anterior (el que estaba antes de entrar en el directorio actual), se usa:

``` bash
cd ..
```
Esto te llevará un nivel arriba en la estructura de directorios. Si quiero volver arriba dos niveles puedo usar:

``` bash
cd ../..
```

### 5. Eliminar un archivo o directorio: rm
El comando rm se utiliza para eliminar archivos o directorios. Es importante tener cuidado, ya que rm no envía los archivos a la papelera de reciclaje, ¡los elimina permanentemente!

Para eliminar un archivo llamado archivo.txt, usa:

``` bash
rm archivo.txt
```
Y si deseas eliminar un directorio junto con su contenido, puedes usar la opción `-r` (recursivo):

``` bash
rm -r mi_carpeta
```
Importante: rm elimina los archivos y directorios de forma permanente. No va a la papelera.

### Resumen:
`ls`: Lista los archivos y carpetas del directorio actual.
`mkdir nombre_carpeta`: Crea una nueva carpeta.
`cd nombre_carpeta`: Entra en una carpeta.
`cd ..`: Vuelve al directorio anterior.
`rm archivo`: Elimina un archivo. ¡Cuidado, no va a la papelera!