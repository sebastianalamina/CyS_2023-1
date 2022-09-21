package interfaz;
import java.util.Scanner;
import vigenère.*;
import hill.*;

/**
 * Clase Interfaz.
 * Se encarga de la salida que se imprime al usuario,
 * así como de manejar el "input" que éste introduzca.
 */
public class Interfaz extends Object {

	private Scanner sc;	/* Scanner para leer input. */
	private String texto; /* Texto a encriptar o desencriptar. */
	private String clave; /* Clave para encriptar o desenctriptar. */

	/**
	 * Constructor de la clase Interfaz.
	 * Termina su ejecución hasta que el usuario decide terminar
	 * la ejecución del programa.
	 */
	public Interfaz() {

		// Inicializamos y guardamos un Scanner, para
		// leer "input" del usuario.
		sc = new Scanner(System.in);

		// Redirigimos al menú principal.
		menuPrincipal();
	}

	/**
	 * Menú principal de la interfaz. Imprime las opciones que
	 * tiene el usuario dentro del programa, y redirige al
	 * programa según el "input" que introduzca.
	 */
	private void menuPrincipal() {

		// Imprimimos el menú principal.
		System.out.println("--------------------- ¡Hola! ---------------------");
		System.out.println("--------------------------------------------------");
		System.out.println("-- Proyecto 1 - Criptografía y Seguridad 2023-1 --");
		System.out.println("--------- Cripsosistemas Vigenère y Hill ---------");
		System.out.println("--------------------------------------------------");
		System.out.println("------------------ Integrantes -------------------");
		System.out.println("");
		System.out.println("");
		System.out.println("");
		System.out.println("--------------------------------------------------");
		System.out.println("1) Ejecutar Vigenère.");
		System.out.println("2) Ejecutar Hill.");
		System.out.println("3) Salir.");
		System.out.println("--------------------------------------------------");

		// Obtenemos el "input" del usuario, y redirigimos.
		String x = getOpcion("Escoge una opción:");
		if ( !x.equals("3") ) {
			if ( x.equals("1") )
				vigenère();
			else if ( x.equals("2") )
				hill();
			else if (x != "3") {
				getOpcion("Introduce una opción válida.");
				menuPrincipal();
			}
		}
	}

	/**
	 * Obtiene un "input" del usuario.
	 * @param msj_para_usuario Mensaje a imprimir para el usuario
	 * como "prompt" para que introduzca algún input.
	 * @return Cadena con el "input" del usuario. Si no
	 * introduce nada, se devuelve la cadena vacía.
	 */
	private String getOpcion(String msj_para_usuario) {

		// Imprimimos el "prompt".
		System.out.println(msj_para_usuario);

		// Obtenemos y devolvemos el "input", si hay.
		if (sc.hasNextLine())
			return sc.nextLine();

		// Si no hay "input", devolvemos la cadena vacía.
		return "";
	}

	/**
	 * Ejecución de Vigenère.
	 */
	private void vigenère() {

		// Imprimimos para saber si se desea encriptar o desencriptar.
		System.out.println("-------------------- VIGENÈRE --------------------");
		System.out.println("1) Encriptar.");
		System.out.println("2) Desencriptar.");
		System.out.println("--------------------------------------------------");

		// Obtenemos la opción deseada.
		String x = getOpcion("Escoge una opción:");
		if ( !(x.equals("1")||x.equals("2")) ) {
			getOpcion("Introduce una opción válida.");
			vigenère();
			return;
		}

		// Obtenemos el texto a (des)encriptar y la clave para (des)encriptar.
		obtenciónTextoClave(x);

		// Imprimimos el resultado.
		if (x.equals("1"))
			System.out.println(Vigenère.encripta(texto, clave));
		else if (x.equals("2"))
			System.out.println(Vigenère.decifra(texto, clave));

		// Simulamos una interacción antes de continuar.
		getOpcion("Presiona 'Enter' para continuar.");

		// Redigirimos al menú principal.
		menuPrincipal();
	}

	/**
	 * Ejecución de Hill
	 */
	private void hill() {

		// Imprimimos para saber si se desea encriptar o desencriptar.
		System.out.println("---------------------- HILL ----------------------");
		System.out.println("1) Encriptar.");
		System.out.println("2) Desencriptar.");
		System.out.println("--------------------------------------------------");

		// Obtenemos la opción deseada.
		String x = getOpcion("Escoge una opción:");
		if ( !(x.equals("1")||x.equals("2")) ) {
			getOpcion("Introduce una opción válida.");
			hill();
			return;
		}

		// Obtenemos el texto a (des)encriptar y la clave para (des)encriptar.
		obtenciónTextoClave(x);

		// Imprimimos el resultado.
		if (x.equals("1"))
			System.out.println(Hill.encripta(texto, clave));
		else if (x.equals("2"))
			System.out.println(Hill.desencripta(texto, clave));

		// Simulamos una interacción antes de continuar.
		getOpcion("Presiona 'Enter' para continuar.");

		// Redigirimos al menú principal.
		menuPrincipal();
	}

	/**
	 * Almacena, en las variables globales, el texto para encriptar
	 * o desencriptar, y la clave con la cual hacerlo.
	 * @param opcion Cadena "1" para el encriptado. Cadena "2" para
	 * el desencriptado.
	 */
	private void obtenciónTextoClave(String opcion) {

		// Obteniendo el texto.
		System.out.println("--------------------------------------------------");
		System.out.print("Introduce el texto a ");
		if (opcion.equals("2"))
			System.out.print("des");
		System.out.println("encriptar...");
		texto = getOpcion("");

		// Obteniendo la clave.
		System.out.println("--------------------------------------------------");
		System.out.print("Ahora, introduce la clave para ");
		if (opcion.equals("2"))
			System.out.print("des");
		System.out.println("encriptar...");
		clave = getOpcion("");

		// Imprimiendo parte del resultado.
		System.out.println("--------------------------------------------------");
		System.out.print("El texto ");
		if (opcion.equals("2"))
			System.out.print("des");
		System.out.println("encriptado es el siguiente:");
	}

}