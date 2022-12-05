from ecies.ECIES import *
import os

# Carpeta en la cual se guardarán y de la cual se leerán
# los archivos cuando no se especifique una ruta absoluta.
CARPETA_DE_ARCHIVOS = "files/"

class Interfaz(object):
	"""Interfaz gráfica."""

	def __init__(self):
		"""Instanciación."""
		while self.menu_principal() != "exit":
			print("--------------------------------------------------");
			input("Presiona 'enter' para continuar.")
		print("¡Nos vemos!")
		print("--------------------------------------------------");

	def menu_principal(self):
		"""Primera pantalla que ve el usuario."""

		# Menú principal.
		print("--------------------- ¡Hola! ---------------------");
		print("-- Proyecto 3 - Criptografía y Seguridad 2023-1 --");
		print("-------------- Criptosistema ECIES ---------------");
		print("--------------------------------------------------");
		print("------------------ Integrantes -------------------");
		print("Sebastián Alamina Ramírez");
		print("Carlos Alberto Desiderio Castillo");
		print("Camila Alexandra Cruz Miranda");
		print("--------------------------------------------------");
		print("1) Cifrado.");
		print("2) Descifrado.");
		print("3) Salir.");
		print("--------------------------------------------------");

		# Solicitamos la opción deseada del usuario.
		x = input("Escoge una opción: ")
		print("--------------------------------------------------");

		# Procedemos según el input del usuario.
		if (x == "1"):
			self.cifrar_descifrar(True)
		elif (x == "2"):
			self.cifrar_descifrar(False)
		elif (x == "3"):
			return "exit"
		else:
			print("Introduce una opción válida. ")

	def cifrar_descifrar(self, cifrar):
		"""
		Cifrado y descifrado ECIES.
		:param bool cifrar: ¿Se cifra (True) o se descifra (False)?
		"""

		# Verificación de tipado.
		assert type(cifrar) == bool

		# Cadenas a imprimir.
		des = "" if cifrar else "des"
		not_des = "des" if cifrar else ""
		pub_pri = "pública" if cifrar else "privada"

		# Solicitamos al usuario el nombre del archivo que se leerá.
		print(f"Introduce el nombre del archivo del cual se leerá\nel texto {not_des}cifrado.")
		print(f"• Si no proporcionas una ruta absoluta, los\narchivos se leerán de la carpeta {CARPETA_DE_ARCHIVOS}")
		print(f"• El archivo no será sobrescrito; se abrirá para\nsólo lectura.")
		file_to_read = input()
		file_to_read = file_to_read if os.path.isabs(file_to_read) else CARPETA_DE_ARCHIVOS+file_to_read
		print("--------------------------------------------------");

		# Intentamos obtener los argumentos K = (E, P, m, Q, n) del archivo a leer.
		# Si algo falla, imprimimos las consideraciones que debe llevar el archivo, y terminamos.
		try:
			K = get_parametros_ECIES(file_to_read)
			assert K != None
		except Exception as e:
			print("ERROR DE LECTURA:", e)
			print("\nConsideraciones:")
			print("• La primera línea del archivo debería llevar el\nsiguiente formato:")
			print("a b P m Q n char_begin")
			print("Tal que K = (y²=x³+ax+b, P, m, Q, n).")
			print("• No debe haber un espacio al final de la línea.")
			print("• Debe haber sólo un espacio entre cada argumento.")
			print("• El formato de P y Q es (x,y) sin espacios.")
			print("• a,b,m,n,x,y deben ser enteros.")
			return

		# Intentamos obtener el mensaje a (des)cifrar del archivo a leer.
		# Si algo falla, imprimimos las consideraciones que debe llevar el archivo, y terminamos.
		try:
			msj = get_mensaje_ECIES(file_to_read, cifrar)
			assert msj != None
		except Exception as e:
			print("ERROR DE LECTURA:", e)
			print("\nConsideraciones:")
			if cifrar:
				print("• Cada línea del mensaje debe consistir de sólo\ncaracteres entre A y Z, sin espacios y sin contar\na la Ñ.")
			else:
				print("• Cada línea del mensaje debe consistir de una\ntupla (y₁,y₂), donde y₁ es otra tupla (y₁ₓ,y₁ᵧ).")
				print("• y₂,y₁ₓ,y₁ᵧ deben ser enteros.")
			print("• No debe haber espacios al final de las líneas.")
			return

		# Una vez que hemos obtenido los argumentos y el mensaje del archivo a leer,
		# extraemos los argumentos en sus respectivas variables.
		E,P,m,Q,char_begin = K

		# Intentamos (des)cifrar y guardamos el "resultado".
		# Si algo falla, sólo imprimimos el error y terminamos.
		try:
			if cifrar:
				resultado = ECIES.cifrar(E,P,m,Q,msj,char_begin)
			else:
				resultado = ECIES.descifrar(E,P,m,Q,msj,char_begin)
		except Exception as e:
			print(f"ERROR AL {des.upper()}CIFRAR:", e)
			print(e)
			return

		# Solicitamos al usuario el nombre del archivo sobre el cual se escribirá el "resultado".
		print(f"Introduce el nombre del archivo sobre el cual se\nguardará el texto {des}cifrado.")
		print(f"• Si no proporcionas una ruta absoluta, los\narchivos se leerán de la carpeta {CARPETA_DE_ARCHIVOS}")
		print(f"• ¡Si el archivo ya existe, será sobrescrito!")
		file_to_write = input()
		file_to_write = file_to_write if os.path.isabs(file_to_write) else CARPETA_DE_ARCHIVOS+file_to_write
		print("--------------------------------------------------");

		# Intentamos escribir el resultado sobre el archivo de escritura.
		try:

			# Abrimos el archivo dado en modo escritura.
			with open(file_to_write, "w") as f:

				# La primera línea del archivo lleva los argumentos del criptosistema en el formato
				# a b P m Q n char_begin
				f.write(f"{E.a} {E.b} {str(P).replace(' ', '')} {m} {str(Q).replace(' ', '')} {E.p} {char_begin}\n")

				# Si estamos cifrando, la variable "resultado" contiene tuplas.
				if cifrar:

					# Convertimos cada tupla en cadena, lo cual resulta en una cadena con espacios,
					# por lo que a cada cadena le quitamos este espacio. Luego, escribimos dicha
					# tupla (ya sin espacios) sobre el archivo con un salto de línea.
					for t in resultado:
						t = str(t).replace(' ', '')
						f.write(t)
						f.write("\n")

				# Si estamos descifrando, la variable "resultado" contiene una cadena.
				else:

					# Sólo escribimos la cadena sobre el archivo, junto con un salto de línea.
					# No importa qué tan larga sea esta línea, pues todo el proceso ya está automatizado.
					f.write(resultado)
					f.write("\n")

		# Si algo falla al intentar esta escritura, sólo imprimimos el error y terminamos.
		except Exception as e:
			print(f"ERROR AL {des.upper()}CIFRAR:", e)
			print(e)
			return

		# Si se llega a este punto, todo el proceso fue éxitoso.
		print(f"Resultado escrito exitosamente sobre el archivo\n{file_to_write}")


def get_parametros_ECIES(file_to_read):
	"""
	Obtiene los parámetros K = (E, P, m, Q, n), correspondientes
	al criptosistema ECIES, de la primera línea del archivo dado.
	:param str file_to_read: Cadena que representa el nombre o la
	ruta del archivo a leer. La primera línea debe llevar el formato
	a b P m Q n char_begin
	donde K = (y²=x³+ax+b, P, m, Q, n).
	:return: La tupla (E, P, m, Q, char_begin), o None si la lectura de
	la primera línea del archivo contiene más argumentos de lo esperado.
	"""
	
	# Abrimos el archivo dado en modo sólo lectura.
	with open(file_to_read, "r") as f:

		# Extraemos la primera línea del archivo y extraemos,
		# dentro de una lista, los trozos separados por espacio.
		primera_linea = f.readline()
		argumentos = primera_linea.split(' ')

		# 'char_begin' es un argumento opcional. Si no se agrega, es 0.
		if len(argumentos) == 6:
			argumentos.append(0)

		# Si la cantidad de argumentos es errónea, no devolvemos
		# nada (None). Esto también se pueda dar cuando hay espacios
		# de sobra (más de un espacio seguido, un espacio al final
		# de la línea, etc.).
		if len(argumentos) < 6 or len(argumentos) > 7:
			return

	# Contando desde 0, P es el elemento 2 de la lista, y Q
	# es el 4. Pero Q se vuelve el 3 al sacar a P de la lista.
	puntos = argumentos.pop(2), argumentos.pop(3)

	# Obtenemos las tuplas P y Q.
	P,Q = map(str_to_inttuple, puntos)

	# Obtenemos los enteros correspondientes
	# del resto de los argumentos.
	a,b,m,n,char_begin = map(int, argumentos)

	# Creamos la curva elíptica asociada a los argumentos.
	E = CurvaEliptica(a, b, n)

	# Devolvemos la tupla (E, P, m, Q, char_begin).
	return E,P,m,Q,char_begin

def get_mensaje_ECIES(file_to_read, cifrar):
	"""
	Obtiene un mensaje correspondiente al criptosistema ECIES
	al leer las líneas del archivo dado.
	:param str file_to_read: Cadena que representa el nombre o la
	ruta del archivo a leer. Las líneas deben tener el formato
	((y0,y1),y2)
	donde y0,y1,y2 son enteros, si se quiera descifrar. O, si
	se quiere cifrar, las líneas deben contener únicamente letras
	mayúsculas entre A y Z, sin espacios ni Ñ.
	:param bool cifrar: ¿Se cifra (True) o se descifra (False)?
	:return: Una lista con las tuplas (si se quiere descifrar)
	o una cadena con caracteres entre A y Z (si se quiere cifrar).
	"""

	# Abrimos el archivo dado en modo sólo lectura.
	with open(file_to_read, "r") as f:

		# Procesamos la primera línea del archivo, que contiene
		# los argumentos correspondientes al criptosistema.
		primera_linea = f.readline()
		num_args = len(primera_linea.split(' '))
		if num_args < 6 or num_args > 7:
			return

		# Si estamos cifrando, el mensaje que queremos cifrar
		# consistirá en una cadena. Si estamos descifrando, el
		# mensaje que queremos descifrar consistirá en una lista
		# de tuplas.
		msj = "" if cifrar else []

		# Por cada línea del archivo, sin contar la primera línea
		# (la función readline() ya leyó dicha línea).,,
		for line in f:

			# Si la línea tiene un salto de línea al final, lo quitamos.
			if line.endswith("\n"):
				line = line[0:-1]

			# Si se trata de una línea vacía, la ignoramos.
			if line == '':
				continue

			# Si estamos cifrando, esperamos sólo caracteres.
			if cifrar:

				# Nos aseguramos de que los caracteres se encuentren
				# entre A y Z, sin espacios y sin contar a la Ñ.
				for c in line:
					assert ord(c) >= 65
					assert ord(c) <= 90

				# Agregamos cada línea a la cadena que resultará al final.
				msj += line

			# Si estamos descifrando, esperamos tuplas.
			else:

				# Nos aseguramos de tener tuplas cuyo uno
				# de sus elementos también sea una tupla.
				assert line.startswith("((")
				assert line.endswith(")")
				assert line.count('(') == 2
				assert line.count(')') == 2
				assert line.count(',') == 2

				# Buscamos la posición de las dos comas,
				# para determinar los elementos de la
				# tupla y = (y1,y2).
				coma1 = line.find(',')
				coma2 = line[coma1+1:].find(',')+coma1+1
				# Para encontrar la segunda coma, consideramos la
				# cadena que ya no contiene a la primera coma. Pero
				# este último 'find' devuelve un índice relativo
				# a la cadena que corta el primer cacho de la cadena
				# completa, por lo que hay que sumarle estas posiciones.

				# Convertimos la cadena que representa a la tupla y1.
				# Y convertimos el entero y2.
				y1 = str_to_inttuple(line[1:coma2])
				y2 = int(line[coma2+1:-1])

				# Agregamos la tupla y=(y1,y2) a la lista que resultará al final.
				msj.append((y1,y2))

		# Devolvemos el mensaje (ya sea en claro o
		# cifrado) con el que el criptosistema trabajará.
		return msj

def str_to_inttuple(s):
	"""
	Convierte la cadena dada en una tupla de enteros.
	:param str s: Cadena sin espacios que contiene la
	representación de una tupla de la forma "(x,y)",
	donde x,y son números que serán convertidos a enteros.
	:return: La tupla asociada a la cadena "s"."
	"""

	# Comprobaciones sobre la cadena
	assert s.startswith('(')
	assert s.endswith(')')
	assert ',' in s

	# Quitamos los paréntesis de los extremos.
	s = s.replace('(', "")
	s = s.replace(')', "")

	# Obtenemos los números de la cadena "s",
	# y los guardamos en la ahora lista "s".
	s = s.split(',')
	assert len(s) == 2

	# Obtenemos los enteros de la lista "s"",
	# y los devolvemos.
	x,y = map(int, s)
	return x,y
