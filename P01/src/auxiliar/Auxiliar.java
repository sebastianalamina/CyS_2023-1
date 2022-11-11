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

	/** Método para obtener el inverso multiplicativo
    * @param n el número al que se le calculara el inverso multiplicativo en Z_27.
    * @return el inverso multiplicativo de n.
    */
    public static int inverso(int n)throws Exception{  // únicos elementos que to tienen inverso son: 3 y 9, factores de 27. 
        for (int i=1; i<27; i++) {  // recorremos multiplicando n a cada elemento de Z_27
            int m = (n*i)%27;       // lo pasamos a modulo 27
            // System.out.println(m);
            if (m == 1) {       // si enconramos algún elemento que al multiplicarlo sea 1
                return i;     // regresamos dicho elemento, pues es su inverso.
            }
        }
        String nl = Integer.toString(n);   // si no encontramos inverso lanzamos la excepción.
        throw new Exception("No existe inverso para "+ nl); // esto sirve para el determinante, si es cero, o su determinante no tiene inverso
    } 


    /** Método para obtener el inverso aditivo
    * @param n el número al que se le calculara el inverso aditivo en Z_27.
    * @return el inverso aditivo de n.
    */
    public static int inversoad(int n){  // calcula el inverso aditivo en Z_27 de n
        return (27 - n)%27;
    }

    /**
     * Calcula y devuelve la matriz inversa de la matriz dada.
     * @param m Matriz cuya inversa desea calcularse.
     * @return Inversa de la matriz dada.
     * @throws Exception Error si la matriz no tiene inversa, o la matriz es de otra dimension.
     */
    public static int[][] matrizInv(int[][] m)throws Exception{
        int da = determinante(m)%27;   // determinante
            if (da<0) {
                da = inversoad(-da);  // si el determinante resulta ser negativo, lo pasamos a su valor en Z27
            }
            da = inverso(da);  // inverso del determinante.
            // System.out.println(da);

        if (m.length == 2) {   // si la matriz es de 2x2, se aplica la formula del inverso del determinante por la adjunta.
            for (int i=0; i<m.length; i++) {  // si hay entradas negativas, se pasan a Z27, para trabajar con ellas
                for (int j=0; j<m[i].length; j++) {
                    if (m[i][j] < 0) {  // se colocan los valores de la matriz a Z27
                        m[i][j] = inversoad(-(m[i][j]%27)) ; 
                    }
                    m[i][j] = m[i][j]%27;
                }
            }
            // print(m);
            int[][] adjm = {{m[1][1], inversoad(m[1][0])},{inversoad(m[0][1]), m[0][0]}};  // adjunta de la matriz
            // System.out.println(adjm.length);
            adjm[0][0] = (adjm[0][0] * da) % 27;   // multiplicamos cada entrada por el inverdo del determinante mod 27
            adjm[0][1] = (adjm[0][1] * da) % 27;
            adjm[1][0] = (adjm[1][0] * da) % 27;
            adjm[1][1] = (adjm[1][1] * da) % 27; 
            return transpuesta(adjm); /// regresamos la matriz traspuesta que es la inversa
        }
        if (m.length == 3) {
            // calculamos la adjunta traspuesta de la matriz

            int[][] adt = transpuesta(adjTras(m));
            // print(adt);
            for (int i=0; i<adt.length; i++) {  // si hay entradas negativas, se pasan a Z27, para trabajar con ellas
                for (int j=0; j<adt[i].length; j++) {
                    if (adt[i][j] < 0) {  // se colocan los valores de la matriz a Z27
                        // System.out.println(-adt[i][j]);
                        // System.out.println(inversoad(-m[i][j]));
                        adt[i][j] = inversoad(-(adt[i][j])) ; 
                        adt[i][j] = (adt[i][j]*da) %27; //  multiplicamos cada entrada por el inverso del determinante.

                    }else{
                        adt[i][j] = adt[i][j];
                        adt[i][j] = (adt[i][j]*da) %27;
                    }
                    
                }
            }
            return adt;
        }else{
            throw new Exception("Solo se trabaja con matrices de 2x2 o 3x3.");
        }
    }

     /**
     * Calcula y devuelve la matriz adjunta traspuesta de la matriz dada.
     * @param m Matriz cuya adjunta desea calcularse.
     * @return Adjunta de la matriz dada.
     * @throws Exception Si la matriz no es de dimension 3.
     */
    public static int[][] adjTras(int[][] m) throws Exception {
        if (m.length == 3) {
            int[][] ad = new int[3][3];
            int u = 1;
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    ad[i][j] = (u*determinante(matriz_ij(m,i,j)))%27;
                    u = -1*u;
                }
            }
            return ad;
        }
        throw new Exception("Para el cálculo de la matriz adjunta, sólo se está trabajando con matrices de dimensiones 2 y 3.");
    }


}