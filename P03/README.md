# Proyecto 3 - ECIES y ataques de vulnerabilidad :heavy_check_mark:

Consultar el archivo `docs/Especificación.pdf` para más detalles sobre el proyecto.

## Autores :busts_in_silhouette:

- [sebastianalamina](https://github.com/sebastianalamina) (Sebastián Alamina Ramírez)
- [Carlos-Desiderio](https://github.com/Carlos-Desiderio) (Carlos Alberto Desiderio Castillo)
- [caams](https://github.com/caams) (Camila Alexandra Cruz Miranda)

## Estructura :open_file_folder:

- La primera parte del proyecto (criptosistema *ECIES*) se incluye dentro de la carpeta `src`, con las instrucciones de ejecución detalladas a continuación.
- La segunda parte del proyecto (técnicas *XXS* y *SQLi*) se incluye en el archivo `docs/Reporte.pdf`.
- La carpeta `docs/` contiene documentos relevantes al proyecto y al programa.
- La entrega final (100/100) consistió en un comprimido cuyo contenido son los archivos y las carpetas de este subdirectorio.

## Ejecución :gear:

Mediante una terminal con acceso a un compilador de *Python 3*, ejecutar el archivo `Main.py` dentro de la carpeta `src`...

```sh
python3 Main.py
```

Además, es necesario contar con la biblioteca `sympy`, que puede ser instalada con ayuda de `pip`...

```sh
pip install sympy
```

## Notas :clipboard:

- Este criptosistema trabaja sólo con caracteres entre A y Z, sin considerar minúsculas, espacios, la Ñ, acentos, ni ningún otro símbolo o caracter.
- Se ha de considerar un desfase del alfabeto definido por `char_begin` y por el módulo 26, de tal manera que A=`char_begin`, B=`char_begin`+1, ..., Y=`char_begin`+24, Z=`char_begin`+25 (aplicando módulo 26 en cada caso).
- Este programa trabaja con archivos, los cuales deben seguir el siguiente formato:
	```
	a b P m Q n char_begin
	msj
	```
	En donde:
	- La primera línea representa los argumentos del criptosistema ECIES: K = (E, P, m, Q, n) y `char_begin` para definir el alfabeto.
	- En cuestiones de tipado, `P` y `Q` son tuplas de longitud 2 cuyos elementos son enteros, mientras que `a`, `b`, `m`, `n` y `char_begin` son enteros.
	- Entre cada par de argumentos, debe existir un único espacio.
	- No debe haber espacios al final de la línea, ni al principio de la misma.
	- No debe haber espacios dentro de las tuplas `P` y `Q`.
	- `a` y `b` vienen dados por la curva elíptica E: y² = x³ + **a**x + **b**.
	- `P`, `Q` y `n` son la llave pública, mientras que `m` es la llave pública.
		- Se debe cumplir `P` = `mQ`.
		- `n` suele ser el módulo de la curva elíptica.
	- `char_begin` es un argumento <ins>opcional</ins> que representa el desfase del alfabeto. Su valor por defecto, si no se proporciona, es 0.
	- De la segunda línea en adelante, se tiene que `msj` representa el mensaje encriptado o en claro con el que se desea trabajar.
		- Si `msj` está encriptado, entonces cada línea de `msj` sigue el formato `(y1,y2)`, en donde `y1` es una tupla cuyos ambos elementos son enteros, y `y2` también es un entero.
		- Si `msj` está en claro, entonces `msj` consta de líneas con caracteres únicamente entre A y Z sin espacios y sin la Ñ.
- Los archivos se manejan, por defecto, dentro de la carpeta `src/files/`, a menos que se especifique una ruta absoluta.

## Ejemplos :paperclip:

Se incluyen algunos archivos con ejemplos concretos dentro de la carpeta `src/files/`.

- Los archivos `ej0-cifrado.ecies` y `ej0-claro.ecies` contienen el ejemplo presentado al final de las [notas vistas en clase el 7 de noviembre del 2022](https://github.com/sebastianalamina/CyS_2023-1/blob/main/P03/docs/CurvasEl%C3%ADpticas.pdf).
	- Para este ejemplo, A = 1, B = 2, ..., Z = 26. Por ello, `char_begin` = 1.
- El archivo `ej1-cifrado.ecies` contiene el ejemplo presentado al final de las [notas vistas en clase el 23 de noviembre del 2022](https://github.com/sebastianalamina/CyS_2023-1/blob/main/P03/docs/ECIES.pdf).
	- Para este ejemplo, A = 0, B = 1, ..., **J = 9**, ..., Z = 25. Por ello, `char_begin` = 0.
- Los archivos `ej2-cifrado.ecies` y `ej2-claro.ecies` contienen el cuarto ejercicio de la [tarea 3 del curso](https://github.com/sebastianalamina/CyS_2023-1/blob/main/T03/CyS-T03.pdf).
	- Para este ejemplo, A = 0, B = 1, ..., Z = 25. Por ello, `char_begin` = 0.
	- Este archivo ejemplifica cómo el argumento `char_begin` es opcional.
