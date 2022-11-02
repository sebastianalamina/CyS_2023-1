from rsa.RSA import *
ENCODING = 'latin_1'

class Interfaz(object):
	"""Interfaz gráfica."""

	def __init__(self):
		"""Instanciación."""
		self.menu_principal()

	def menu_principal(self):
		"""Primera pantalla que ve el usuario."""

		# Menú principal.
		print("--------------------- ¡Hola! ---------------------")
		print("-- Proyecto 2 - Criptografía y Seguridad 2023-1 --")
		print("--------------- Criptosistema RSA ----------------");
		print("--------------------------------------------------");
		print("------------------ Integrantes -------------------");
		print("Sebastián Alamina Ramírez");
		print("Carlos Alberto Desiderio Castillo");
		print("Camila Alexandra Cruz Miranda");
		print("--------------------------------------------------");
		print("1) Generación de claves.");
		print("2) Cifrado.");
		print("3) Descifrado.");
		print("4) Salir.");
		print("--------------------------------------------------");

		# Solicitamos la opción deseada del usuario.
		x = input("Escoge una opción: ")
		print("--------------------------------------------------");

		# Procedemos según el input del usuario.
		if (x == "1"):
			self.clave()
		elif (x == "2"):
			self.cifrar_descifrar(True)
		elif (x == "3"):
			self.cifrar_descifrar(False)
		elif (x != "4"):
			input("Introduce una opción válida. ")
			self.menu_principal()

	def clave(self):
		"""Generación de claves."""

		# Generamos una clave aleatoria (n, e, d).
		key = RSA.generar_clave()

		# Imprimimos la clave generada.
		print("Se han generado las siguientes claves aleatoriamente:\n")
		print(f"n = {key[0]}\n")
		print(f"Clave pública:\n(n, e={key[1]})\n")
		print(f"Clave privada:\n(n, d={key[2]})\n")

		# Regresamos al menú principal después de que
		# el usuario presione "enter".
		input("Presiona 'enter' para continuar. ")
		self.menu_principal()

	def cifrar_descifrar(self, cifrar, m=None, n=None, exp=None):
		"""
		Cifrado y descifrado RSA.
		:param bool cifrar: ¿Se cifra (True) o se descifra (False)?
		:param str m: Mensaje a cifrar o descifrar.
		:param int n: Módulo de las claves.
		:param int exp: Exponente de la clave pública o privada.
		"""

		# Verificación de tipado.
		assert type(cifrar) == bool

		# Cadenas a imprimir.
		des = "" if cifrar else "des"
		not_des = "des" if cifrar else ""
		pub_pri = "pública" if cifrar else "privada"
		e_d = "e" if cifrar else "d"

		# Si al método no se le pasó el mensaje a (des)cifrar,
		# se lo solicitamos al usuario.
		if (m == None):
			m = input(f"Introduce el texto a {des}cifrar:\n")

		# Si no se pasaron los parámetros de
		# módulo y exponente, se solicitan.
		if (n == None or exp == None):
			print(f"\nIntroduce la clave {pub_pri}...")
		if (n == None):
			n = input("n: ")
		if (exp == None):
			exp = input(f"{e_d}: ")

		# El input es una cadena, por lo que intentamos
		# convertir estos valores (n y exp) a enteros.
		try:
			n = int(n)
			exp = int(exp)
		except:
			print(f"\nLos valores 'n' y '{e_d}' deben ser números enteros.")
			input("Presiona 'enter' para continuar.")
			return self.menu_principal()

		# La variable "t" contendrá el texto (des)cifrado.
		t = []

		# Si el mensaje viene en formato de cadena,
		# convertimos cada caracter en byte dentro de una
		# lista. Si ya viene en formato de lista, sólo
		# la asignamos a "t".
		if (type(m) == str):
			for c in m:
				t.append(ord(c))
		else:
			assert type(t) == list
			t = m

		# Imprimimos el texto a (des)cifrar en formato de bytes.
		print(f"\nEl texto a {des}cifrar, en bytes, es:")
		print(*t)

		# (Des)ciframos cada caracter.
		for i,b in enumerate(t):
			if cifrar:
				t[i] = RSA.cifrar(b, n, exp)
			else:
				t[i] = RSA.descifrar(b, n, exp)

		# Imprimimos el texto ya (!des)cifrado en
		# formato de bytes, e intentamos imprimirlo
		# en formato de cadena.
		print(f"\nEl texto {des}cifrado, en bytes, es:")
		print(*t)
		try:
			s = bytes(t).decode(ENCODING)
			print(f"\nEl texto {des}cifrado, en cadena, es:")
			print(s)
		except:
			print(f"\nNo es posible imprimir el texto {des}cifrado en\nformato de cadena; ¡los bytes resultantes son muy\ngrandes!")

		# Si el usuario desea (!des)cifrar el mismo mensaje,
		# le pasamos a la función correspondiente el
		# bytearray directamente. Si no, continuamos
		# al menú principal.
		print(f"\n¿Quieres {not_des}cifrar este mensaje?")
		x = input(f"Ingresa '1', 's' o 'y' para {not_des}cifrarlo: ")
		if (x == "1" or x == "s" or x == "y"):
			print("\n¡Se utilizará el mismo módulo 'n'!")
			self.cifrar_descifrar(not cifrar, t, n)
		else:
			self.menu_principal()
