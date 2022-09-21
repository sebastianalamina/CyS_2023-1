package auxiliar;

/**
 *  El producto de matrices.
 */
public class Matrices{

    /**
     * Imprime en consola una matriz con un número arbitrario
     * de filas y columnas. Los elementos de la matriz deben ser 
     * números de tipo int.
     */
    public void print(int[][] M) {
        for(int i = 0; i < M.length; i++){
            for(int j = 0; j < M[0].length; j++)
                System.out.print(" " + M[i][j] + " ");
            System.out.println();
        }
    }
   
    /**
     * Nos devuelve el producto punto de dos vectores. Utilizamos este
     * método para crear las entradas (i,j) del resultado
     * de multiplicar dos matrices.
     */
    public static int productoPunto(int[] R1, int[] R2) {
        int pp = 0;
        for(int i = 0; i < R1.length; i++) {
            pp += R1[i]*R2[i];
        }
        return pp;
    }

    /**
     * Método que se encarga de multiplicar dos matrices A y B. 
     * Como sabemos, para que A y B puedan ser multiplicadas, el número de columnas
     * de A debe ser igual al número de filas de B.
     */
    public int[][] multiplicaMatrices(int[][] A, int[][] B) throws IllegalArgumentException {
        int filasA, colsA, filasB, colsB;
        filasA = A.length; colsA = A[0].length;
        filasB = B.length; colsB = B[0].length; 
        
        if(colsA != filasB) {
            System.out.println("\nEl número de columnas de la primer matriz debe ser igual número de renglones de la segunda.\n");
            throw new IllegalArgumentException();
        }

        int[][] C = new int[filasA][colsB];

        for(int i = 0; i < filasA; i++) {
            for(int j = 0; j < colsB; j += 4) {

                // Es recomendado que en un programa se utilice a lo más un hilo
                // por cada núcleo del CPU de la computadora. En mi caso, mi computadora
                // tiene 4 núcleos, por eso tenemos a lo más 4 hilos ejecutándose a la vez.
                int num = colsB-j >= 4 ? 4 : colsB;

                Multiplier[] m = new Multiplier[num];

                for(int h = 0; h < num; h++) {
                    int[] columna = new int[B.length];

                    // Lo que hacemos aquí es crear un vector que contenga los elementos 
                    // a los que se les hará el producto punto para encontar C[i][j],
                    // es decir, la fila i de A y la columna B de j.

                    for(int k = 0; k < B.length; k++)
                        columna[k] = B[k][j+h];
                    
                    m[h] = new Multiplier(A[i], columna);
                    // Lanzamos los hilos. Cada uno se encarga de encontrar el valor de alguna
                    // entrada de C, utilizando el método productoPunto.
                    m[h].multiplica();

                    C[i][j+h] = m[h].pp;
                }
            }
        }

        return C;
    }

}
