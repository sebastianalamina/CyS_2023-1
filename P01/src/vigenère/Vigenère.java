package vigenère;
import auxiliar.*;

public class Vigenère{
	static String n = "\u00f1";
	static String nm = n.toUpperCase();
	// Tabla de Vigenere:
	static String[][] tabla = {{"A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z"},
                               {"B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A"},
                               {"C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B"},
                               {"D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C"},
                               {"E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D"},
                               {"F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E"},
                               {"G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F"},
                               {"H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G"},
                               {"I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H"},
                               {"J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I"},
                               {"K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J"},
                               {"L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K"},
                               {"M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L"},
                               {"N",nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M"},
                               {nm,"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N"},
                               {"O","P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm},
                               {"P","Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O"},
                               {"Q","R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P"},
                               {"R","S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q"},
                               {"S","T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R"},
                               {"T","U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S"},
                               {"U","V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T"},
                               {"V","W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U"},
                               {"W","X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V"},
                               {"X","Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W"},
                               {"Y","Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X"},
                               {"Z","A","B","C","D","E","F","G","H","I","J","K","L","M","N",nm,"O","P","Q","R","S","T","U","V","W","X","Y"}};


    /**  Método para quitar los espacios y eliminar los caracteres repetidos de una cadena 
    *@param s es la cadena a "limpiar" de caracteres repetidos y espacios.
    *@return La cadena sin caracteres repetidos y sin espacios.
    */
    public static String removeDup(String s){
    	String r = "";
    	String[] ar = s.split(""); // se colocan los carácteres en un arreglo
    	for (int i = ar.length-1; i > -1; i--) { // se itera de atras al inicio del arrelo
    		for (int j=0; j<i; j++) {           // buscando si el caracter ya esta en el arreglo
    			if (ar[i].equals(ar[j]) || ar[i].equals(" ")) {  // si el caracter ya esta, se elimina o se sustituye por cadena vacía
    				ar[i] = "";
    				break;
    			}
    		}
    		r= ar[i] + r;  // se va concatenando la cadena sin elementos repetidos 
    	}
    	return r;
    }

    /** Método que toma una letra y regresa el número de la columna en la tabla de vigenere
    * @param l la letra que buscara como columna en la tabla.
    * @return el número de la posición de la columna en la tabla.
    */
    public static int LetterToNumber(String l){
		for (int i=0; i<27; i++) {  // se busca la letra en el abcedario y regresa su posición en el arreglo
			if(l.equals(tabla[0][i])){
				return i;
			}
		}
		return -1;
    }
    
    /** Método que crea el arreglo emparejando la palabra clave con el mensaje, haciendo que se repita la clave 
    * @param msg el mensaje al que se le enparejara la clave.
    * @param key la palabra clave que se emparejara al mensaje.
    * @return el arreglo con 2 dimensiones, con el mensaje y el arreglo con la palabra clave.
    */
    public static String[][] empareja(String msg, String key){
    	int index = 0;
    	String[] m = msg.split(""); // se crean arreglos separando las letras de la clave y mensaje
    	String[] c = key.split("");
    	String[] cb = new String [msg.length()];  // se crea un arreglo se la longitud del mensaje.
    	for (int i = 0; i < m.length; i++) {  // se itera sobre el último arreglo que se creo.
    		if (m[i].equals(" ")) {   // si se encuentra un espacio, de deja el espacio.
    			cb[i] = " ";
    		}
    		else{  // si no hay espacio se coloca el residuo del indice con la longitud de la clave
    			cb[i] = c[index % c.length];
    			index++;  // se le suma uno al indice para no perder su posición.
    		} 			
    	}
    	String[][] r = {m,cb};  // se crea el arreglo ya emparenjando.
    	return r;
    }

    /** Método que encripta usando Vigenere
    * @param msg el mensaje a cifrar.
    * @param key la palabra clave para cifrar el mensaje. 
    */
    public static String encripta(String msg, String key){
    	String secret = "";  // se crea la cadena que almacenara el mensaje cifrado
    	msg =msg.toUpperCase(); // se pasa el mensaje a mayusculas.
        msg = msg.replaceAll("ñ","n");  // se reemplaza si hay una Ñ o ñ
        msg = msg.replaceAll("Ñ","n");
        msg= msg.replaceAll("[^a-zA-Z\t/} ]", ""); // se quita todo lo que no sea letra.
        msg = msg.replaceAll("n",nm);  // se recuperan las Ñ con el atributo de clase
    	
    	key = key.toUpperCase(); // Lo mismo con la clave
        key = key.replaceAll("ñ","n"); 
        key = key.replaceAll("Ñ","n");
        key = removeDup(key.replaceAll("[^a-zA-Z\t/} ]", "")); 
        key = key.replaceAll("n",nm);  

        // System.out.println(msg);
        // System.out.println(key);

    	String[][] ar = empareja(msg,key);  // se crea el arreglo enparejando el mensaje y la clave ya limpios

    	for (int i=0; i<ar[0].length; i++) {   // se itera sobre cada letra del mensaje
    		if (ar[0][i].equals(" ")) {   // si hay espacios se ignoran 
    			secret += " ";
    			continue;
    		}
    		else{ // si hay letras, se buscan sus posiciones de renglones y columnas, y se concatena la letra que resulta en la tabla.
    			secret += tabla[LetterToNumber(ar[0][i])][LetterToNumber(ar[1][i])];
    		}	
    	}
    	return secret;
    }

    /** Método que desencripta usando Vigenere
    * @param msg el mensaje a descifrar.
    * @param key la palabra clave para descifrar el mensaje. 
    */
    public static String decifra(String secret, String key){
    	String msg = "";

    	secret = secret.replaceAll("Ñ",nm);
        secret = Auxiliar.normalizarTexto(secret);

    	key = key.toUpperCase(); // Lo mismo con la clave
        key = key.replaceAll("ñ","n"); 
        key = key.replaceAll("Ñ","n");
        key = removeDup(key.replaceAll("[^a-zA-Z\t/} ]", "")); 
        key = key.replaceAll("n",nm);   // se le quitan los duplicados y espacios a la clave

    	String[][] ar = empareja(secret,key); // se emparejan la clave con el mensaje a decifrar

    	for (int i=0; i<ar[0].length; i++) {  // se itera sobre el arreglo con indices de la clave
    		if (ar[1][i].equals(" ")) {   // si hay espacios se ignoran 
    			msg += " ";
    			continue;
    		}
    		else{  // se toma la columna de la tabla correspondiente a cada letra de la clave y se itera
    			for (int j=0; j<26; j++) {  // cuando se encuentra la letra del mensaje cifrado, se va a su fila correspondiente
    				if (tabla[LetterToNumber(ar[1][i])][j].equals(ar[0][i])) {  // y se toma el indice en esa fila
    					msg += tabla[j][0];                                // para concatenar la letra del mensaje original
    					break;
    				}
    			}
    		}
    	}
    	return msg;
    }
    
}

 // ( @ _ @ )