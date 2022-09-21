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

		return new int[0][0];
	}

	/**
	 * Calcula y devuelve el determinante de una matriz.
	 * @param a Arreglo del cual se desea calcular el determinante.
	 * @return Determinante de la matriz.
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

}