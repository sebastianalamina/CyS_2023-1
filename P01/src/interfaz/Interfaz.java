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
		menu_principal();
	}

	/**
	 * Menú principal de la interfaz. Imprime las opciones que
	 * tiene el usuario dentro del programa, y redirige al
	 * programa según el "input" que introduzca.
	 */
	private void menu_principal() {

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
		String x = get_opcion("Escoge una opción:");
		if ( !x.equals("3") ) {
			if ( x.equals("1") )
				vigenère();
			else if ( x.equals("2") )
				hill();
			else if (x != "3") {
				get_opcion("Introduce una opción válida.");
				menu_principal();
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
	private String get_opcion(String msj_para_usuario) {

		// Imprimimos el "prompt".
		System.out.println(msj_para_usuario);

		// Obtenemos y devolvemos el "input", si hay.
		if (sc.hasNextLine())
			return sc.nextLine();

		// Si no hay "input", devolvemos la cadena vacía.
		return "";
	}

	/**
	 * uwu
	 */
	private void vigenère() {



		// Simulamos una interacción antes de continuar.
		get_opcion("Presiona 'Enter' para continuar.");

		// Redigirimos al menú principal.
		menu_principal();
	}

	/**
	 * uwu
	 */
	private void hill() {

		

		// Simulamos una interacción antes de continuar.
		get_opcion("Presiona 'Enter' para continuar.");

		// Redigirimos al menú principal.
		menu_principal();
	}

}