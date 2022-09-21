package auxiliar;

/**
 * Clase Auxiliar.
 * Auxilia en el manejo de cadenas y arreglos.
 * Simula una clase estática, por lo que todos
 * sus métodos han de ser estáticos (similar al
 * funcionamiento de la clase Math).
 */
public final class Auxiliar extends Object {


	/**
	 * Constructor de la clase Auxiliar.
	 * Es privado para evitar instanciación, y no hace nada.
	 */
	private Auxiliar() {}

	/**
	 * Toma una cadena y la normaliza. Es decir, le quita signos
	 * de puntuación, acentos, espacios en blanco, y convierte
	 * las minúsculas en mayúsculas.
	 * @param texto Texto que será normalizado.
	 * @return Texto ya normalizado.
	 */
	public static String normalizarTexto(String texto) {

		// Copiamos el texto a normalizar.
		String s = texto;

		// Acentos.
		s = s.replaceAll("Á","A");
		s = s.replaceAll("É","E");
		s = s.replaceAll("Í","I");
		s = s.replaceAll("Ó","O");
		s = s.replaceAll("Ú","I");
		s = s.replaceAll("á","a");
		s = s.replaceAll("é","e");
		s = s.replaceAll("í","i");
		s = s.replaceAll("ó","o");
		s = s.replaceAll("ú","u");

		// Espacios.
		s = s.replaceAll("\\s","");

		// Signos de puntuación.
		s = s.replaceAll("\\W","");

		// Minúsculas a mayúsculas.
		s = s.toUpperCase();

		// Devolvemos el texto ya normalizado.
		return s;
	}

	/**
	 * Toma dos matrices (de enteros) y las multiplica.
	 * @param a1 Arreglo izquierdo a multiplicar.
	 * @param a2 Arreglo derecho a multiplicar.
	 * @return La matriz que resulta de multiplicar los
	 * arreglos de los parámetros.
	 */
	public static int[][] multiplicarArreglos(int[][] a1, int[][] a2) {

		Matrices m = new Matrices();

		return m.multiplicaMatrices(a1, a2);
		
	}

	/**
	 * Calcula y devuelve el determinante de una matriz.
	 * @param a Arreglo del cual se desea calcular el determinante.
	 * @return Determinante de la matriz.
	 * @throws Exception Error si la matriz no es 2x2 o 3x3.
	 */
	public static int determinante(int[][] a) throws Exception {

		// Si la matriz es de 2x2...
		if (a.length == 2) {
			assert a[0].length == 2;
			return (a[0][0]*a[1][1]) - (a[0][1]*a[1][0]);
		}

		// Si la matriz es de 3x3...
		if (a.length == 3) {
			assert a[0].length == 3;
			return (a[0][0]*a[1][1]*a[2][2])
			+ a[0][1]*a[1][2]*a[2][0]
			+ a[0][2]*a[1][0]*a[2][1]
			- a[0][2]*a[1][1]*a[2][0]
			- a[0][0]*a[1][2]*a[2][1]
			- a[0][1]*a[1][0]*a[2][2];
		}

		// Si la matriz no es 2x2 ni 3x3, se lanza un error.
		throw new Exception("Sólo se está trabajando con matrices de dimensiones 2 y 3.");
	}

	/**
	 * Calcula y devuelve la matriz inversa de la matriz dada.
	 * @param a Matriz cuya inversa desea calcularse.
	 * @return Inversa de la matriz dada.
	 * @throws Exception Error si la matriz no tiene inversa.
	 */
	public static int[][] inversa(int[][] a) throws Exception {

		// Primero, calculamos la inversa de la matriz.
		int det = determinante(a);

		// Si el determinante es cero, esta matriz no tiene inversa.
		if (det == 0)
			throw new Exception("Esta matriz no tiene inversa.");

		// La inversa de una matriz es la transpuesta de su adjunta...
		int[][] inversa = transpuesta(adjunta(a));

		// entre su determinante.
		for (int x = 0; x < inversa.length; x++)
			for (int y = 0; y < inversa[0].length; y++)
				inversa[x][y] /= det;

		// Devolvemos la matriz inversa.
		return inversa;
	}

	/**
	 * Calcula y devuelve la matriz transpuesta de la matriz dada.
	 * @param a Matriz cuya transpuesta desea calcularse.
	 * @return Transpuesta de la matriz dada.
	 */
	public static int[][] transpuesta(int[][] a){

		// Si la matriz original es de mxn,
		// la transpuesta es de nxm
		int m = a.length;
		int n = a[0].length;
		int[][] transpuesta = new int[n][m];

		// Calculamos la transpuesta.
		for(int x = 0; x < n; x++)
			for(int y = 0; y < m; y++)
				transpuesta[x][y] = a[y][x];

		// La devolvemos.
	    return transpuesta;
	}


	/**
	 * Calcula y devuelve la matriz adjunta de la matriz dada.
	 * @param a Matriz cuya matriz adjunta desea calcularse.
	 * @return Matriz adjunta de la matriz dada.
	 */
	private static int[][] adjunta(int[][] a) throws Exception {

		// Si la matriz es de 2x2...
		if (a.length == 2) {
			assert a[0].length == 2;

			adjuntaAux(a, 2);
		}

		// Si la matriz es de 3x3...
		if (a.length == 3) {
			assert a[0].length == 3;

			adjuntaAux(a, 3);
		}

		// Si la matriz no es 2x2 ni 3x3, se lanza un error.
		throw new Exception("Sólo se está trabajando con matrices de dimensiones 2 y 3.");

	}

	// Función auxiliar para sacar la adjunta de A[N][N] en adj[N][N].
	static int[][] adjuntaAux(int A[][], int dim) {

		// temp son los cofactores de A[][]

		int [][]temp = new int[dim][dim];
	
		for (int i = 0; i < dim; i++)
		{
			for (int j = 0; j < dim; j++)
			{
				// Sacamos los cofactores de A[i][j]
				cofactor(A, temp, i, j, dim);
	
				// Intercambiamos las filas y columnas para conseguir la
				// transpuesta de la matriz de cofactores = la matriz adjunta
				//adj[j][i] = (sign)*determinante(temp);

				transpuesta(temp);
			}
		}
		return temp;
	}

	// Función de los cofactores de A[p][q] en temp[][]. n es la
	// dimension de A[][]
	static int[][] cofactor(int A[][], int temp[][], int p, int q, int n) {
		int i = 0, j = 0;
	
		// Bucle para cada elemento de la matriz
		for (int row = 0; row < n; row++) {
			for (int col = 0; col < n; col++) {
				// Copiamos en una matriz temporal solo aquellos elementos
				// que no están en sus filas y columnas
				if (row != p && col != q) {
					temp[i][j++] = A[row][col];
	
					// La fila se llena así que aumentamos el índice de la fila y 
					// resetamos el índice de las columnas
					if (j == n - 1)	{
						j = 0;
						i++;
					}
				}
			}
		}
		return temp;
	}

}
