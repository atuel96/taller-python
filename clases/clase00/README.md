# Preliminares

## Usando Jupyter Lab


Para ejecutar Jupyter Lab desde anaconda partimos abriendo `Anaconda Prompt` en Windows o abriendo la terminal y escribiendo `conda activate base` en Linux o MacOs.

Deberiamos ver que la línea actual de la terminal empieza con `(base)`. Luego podemos ejectuar Jypter Lab con el siguiente comando (sin el `$`):

```
$jupyter lab
```

### Prompt 
Al símbolo `$` se le llama prompt, y es un caracter que nos indica que podemos escribir y ejecutar comandos (ver [Wikipedia](https://es.wikipedia.org/wiki/Prompt)). El prompt varía según el sistema o el lenguaje, por ejemplo en Windows verán un `>`, en Linux/Unix un `$` y en MacOS un `%`.

### Abrir Jupyter Lab en cualquier carpeta

Cuando abrimos Jupyter Lab, lo abrimos en el directorio que nos muestra la terminal.

En el caso de Linux o MacOS dependerá del directorio en el cual hayamos abierto la terminal.

En el caso de Windows **Anaconda Prompt** se abre por defecto en el directorio de nuestro usuario `C:/Users/<nombre-de-usuario>`. Para abrir Jupyter Lab en otro directorio, tenemos que empezar por cambiar el directorio con el comando `cd` seguido del nuevo directorio:

```
cd <nuevo-directorio>
```

Por ejemplo si partimos desde el directorio `C:\Users\MiUsuario>` y queremos llegar al directorio `C:\MiCarpeta\TallerDePython` haremos lo siguiente:

```
(base) C:\Users\MiUsuario>
(base) C:\Users\MiUsuario>cd C:\MiCarpeta\TallerDePython
(base) C:\MiCarpeta\TallerDePython>
```

Una vez que hayamos cambiado el directorio podemos ejecutar `jupyter lab`:

```
(base) C:\MiCarpeta\TallerDePython>jupyer lab
```

### Video Demostración en Windows

[Link Video YouTube](https://www.youtube.com/watch?v=0LtAamZTtmc)

## Entornos de Desarrollo Integrado y Editores de Texto

*En Construcción...*

* [Visual Studio Code](https://code.visualstudio.com/) (Nuestra Recomendación)
* [Spyder](https://www.spyder-ide.org/) (Instalado Con Anaconda)