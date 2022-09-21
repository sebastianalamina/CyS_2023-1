package auxiliar;
import java.util.Arrays;

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

		// Minúsculas a mayúsculas.
		s = s.toUpperCase();

		// Signos de puntuación.
		// s = s.replaceAll("\\W","");
		// Esta función elimina a las Ñ's.

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

		// Si la matriz es de 1x1...
		if (a.length == 1) {
			assert a[0].length == 1;
			return a[0][0];
		}

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
		throw new Exception("Para el cálculo del determinante, sólo se está trabajando con matrices de dimensiones 1, 2 y 3.");
	}

	/**
	 * Calcula y devuelve la matriz inversa de la matriz dada.
	 * @param a Matriz cuya inversa desea calcularse.
	 * @return Inversa de la matriz dada.
	 * @throws Exception Error si la matriz no tiene inversa.
	 */
	public static int[][] inversa(int[][] a) throws Exception {

		// Primero, calculamos la inversa de la matriz.
		int det = determinante(a);// % 27;

		// Si el determinante es cero, esta matriz no tiene inversa.
		if (det == 0)
			throw new Exception("Esta matriz no tiene inversa.");

		// La inversa de una matriz es la transpuesta de su adjunta...
		int[][] inversa = transpuesta(adjunta(a));

		// entre su determinante.
		for (int x = 0; x < inversa.length; x++)
			for (int y = 0; y < inversa[0].length; y++)
				inversa[x][y] /= det; // AQUÍ SE HACE CERO SI EL DETERMINANTE ES MÁS GRANDE QUE EL NUMERADOR.

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

			return adjuntaAux(a, 2);
		}

		// Si la matriz es de 3x3...
		if (a.length == 3) {
			assert a[0].length == 3;

			return adjuntaAux(a, 3);
		}

		// Si la matriz no es 2x2 ni 3x3, se lanza un error.
		throw new Exception("Para el cálculo de la matriz adjunta, sólo se está trabajando con matrices de dimensiones 2 y 3.");

	}

	// Función auxiliar para calcular la matriz adjunta.
	private static int[][] adjuntaAux(int[][] a, int dim) throws Exception {

		// Creamos la matriz adjunta.
		int[][] adjunta = new int[dim][dim];

		// Llenamos la matriz adjunta, según su definición.
		for (int x = 0; x < dim; x++)
			for (int y = 0; y < dim; y++) {
				int primerTermino = (int) Math.pow(-1, x+y);
				int segundoTermino = determinante(matriz_ij(a, x, y));// % 27;
				adjunta[x][y] = (primerTermino*segundoTermino);// % 27;
			}

		// Devolvemos la matriz adjunta.
		return adjunta;
	}

	/**
	 * Matriz resultante de eliminar el renglón 
	 * dado y la columna dada de la matriz dada.
	 * @param a Matriz de la cual se desea eliminar renglón y columna.
	 * @param i Renglón que se desea eliminar de la matriz.
	 * @param j Columna que se desea eliminar de la matriz.
	 * @return Matriz que resulta de eliminar la fila i
	 * y la columna j de la matriz dada.
	 */
	public static int[][] matriz_ij(int[][] a, int i, int j) {

		// La matriz resultante tendrá un renglón menos y
		// una columna menos que la original.
		int[][] a_ij = new int[a.length-1][a[0].length-1];

		// Recorremos la matriz resultante,
		// llenándola según los valores de i y de j.
		for (int x = 0; x < a_ij.length; x++)
			for (int y = 0; y < a_ij.length; y++) {
				int xPrima = x >= i ? x+1 : x;
				int yPrima = y >= j ? y+1 : y;
				a_ij[x][y] = a[xPrima][yPrima];
			}

		// Devolvemos la matriz resultante.
		return a_ij;

	}

}