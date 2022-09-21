# Proyecto 1 - Criptosistemas Vigenère y Hill :heavy_check_mark:

Consultar el archivo `Especificación.pdf` para más información sobre el proyecto.

## Autores :busts_in_silhouette:

- [sebastianalamina](https://github.com/sebastianalamina) (Sebastián Alamina Ramírez)

- [Carlos-Desiderio](https://github.com/Carlos-Desiderio) (Carlos Alberto Desiderio Castillo)

- [caams](https://github.com/caams) (Camila Alexandra Cruz Miranda)

## Ejecución :gear:

### Ejecución con Ant :ant:

Desde esta carpeta, y mediante alguna terminal con acceso a un compilador de Java, ejecutar los siguientes comandos:
- Si se desea correr el programa, ejecutar `ant` o `ant run`.
- Si se desea sólo compilar el programa, ejecutar `ant compile`. El resultado se encontrará en `src/build-ant`.
- Si se desea la documentación del programa, ejecutar `ant docs`. El resultado se encontrará en `src/docs-ant`.
- Si se desea limpiar la compilación y/o la documentación del programa, ejecutar `ant clean`.

### Ejecución con `javac` y `java` :coffee:

*Dentro* de la carpeta `src`, compilar y ejecutar el programa con `javac` y `java`. Se recomienda la siguiente serie de comandos:
1. Compilar con `javac -d ./classes *.java`. El resultado se encontrará en `src/classes`.
2. Ejecutar con `java -ea -cp ./classes Main`.
3. (Opcional) Limpiar la compilación con `rm -r classes`.
