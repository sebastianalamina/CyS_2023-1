package hill;
import auxiliar.*;
import vigenère.*;
import java.util.Arrays;

/**
 * Clase Hill.
 * Se encarga del encriptado y desencriptado
 * de textos mediante el criptosistema Hill.
 */
public class Hill {

	/* Alfabeto a utilizar. */
	private static String enie = "\u00f1";
	private static String nm = enie.toUpperCase();
	private static String[] alfabeto = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z"};

	/** Método que encripta usando Hill.
	* @param msg Mensaje a cifrar.
	* @param key Clave para cifrar. 
	*/
	public static String encripta(String msg, String key) throws Exception {

		// Normalizamos la llave y comprobamos que sea de longitud 2^2 o 3^2.
		String llave = Auxiliar.normalizarTexto(key);
		if (llave.length() != 4 && llave.length() != 9)
			throw new Exception("La longitud de la clave debe ser de 4 o 9 caracteres.");

		// Calculamos N.
		int n = (int) Math.sqrt(llave.length());

		// Creamos la matriz asociada a la llave.
		int[][] llaveM = new int[n][n];
		for (int x = 0; x < n; x++)
			for (int y = 0; y < n; y++)
				llaveM[x][y] = Vigenère.LetterToNumber(""+llave.charAt(x*n+y));

		// Error si la matriz de la llave no es invertible.
		if (Auxiliar.determinante(llaveM) == 0)
			throw new Exception("La matriz que genera la clave no es invertible.");

		// Normalizamos el texto a encriptar y lanzamos error si éste no puede dividirse en N-gramas.
		String texto = Auxiliar.normalizarTexto(msg);
		if (texto.length() % n != 0)
			throw new Exception("El texto debería poder dividirse en diagramas o trigramas.");

		// Creamos una variable para ir almacenando los N-gramas
		// y otra variable para ir almacenando el texto encriptado.
		int[][] nGrama = new int[n][1];
		String textoEncriptado = "";

		// Recorremos el texto original.
		for (int i = 0; i < texto.length(); i++) {

			// Vamos creando el N-grama.
			nGrama[i%n][0] = Vigenère.LetterToNumber(""+texto.charAt(i));

			// Si el N-grama ya se llenó...
			if ((i+1)%n == 0) {

				// ...creamos el criptograma...
				int[][] criptograma = Auxiliar.multiplicarArreglos(llaveM, nGrama);

				// ...le aplicamos módulo...
				for (int j = 0; j < criptograma.length; j++)
					criptograma[j][0] %= 27;

				// ...y pegamos los caracteres correspondientes al texto encriptado...
				for (int j = 0; j < criptograma.length; j++)
					textoEncriptado += alfabeto[criptograma[j][0]];
			}
		}

		// Finalmente, devolvemos el texto encriptado.
		return textoEncriptado;
	}

	/** Método que desencripta usando Hill.
	* @param msg Mensaje a descifrar.
	* @param key Clave para descifrar. 
	*/
	public static String desencripta(String secret, String key) throws Exception {
		return "";
	}

}