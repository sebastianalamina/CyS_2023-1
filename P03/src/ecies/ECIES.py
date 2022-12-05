from ecies.CurvaEliptica import * 
import random

class ECIES(object):
	"""Criptosistema ECIES."""

	def cifrar(E, P, m, Q, msj, char_begin=0):
		"""
		Cifra según el criptosistema ECIES.
		:param CurvaEliptica E: Curva elíptica reducida.
		:param tuple P: Primer punto P.
		:param int m: Número que multiplica a P para obtener Q.
		:param tuple Q: Segudo punto Q = mP.
		:param str msj: Cadena con únicamente caracteres en mayúsculas,
		sin espacios ni otros símbolos (ABC...MNOP...XYZ).
		:param int char_begin: Desfase del alfabeto. A considerar:
		A=begin B=begin+1 ... Z=begin+25
		:return: Lista con tuplas de la forma y=(y₁,y₂) donde y₁∊Zₚ×Z₂ y y₂∊Z*ₚ.
		"""

		# Comprobaciones.
		assert type(E) == CurvaEliptica
		assert (type(P) == tuple) and (len(P) == 2)
		assert (type(Q) == tuple) and (len(Q) == 2)
		assert (type(m) == int) and (type(char_begin) == int)
		assert type(msj) == str
		assert Q == E.multiplicar_escalar(m, P)
		for c in msj:
			# Comprobamos que se trate de una letra
			# mayúscula entre A y Z (sin considerar Ñ).
			assert ord(c) >= 65
			assert ord(c) <= 90

		# El mensaje cifrado será una lista con tuplas.
		msj_cifrado = []

		# Por cada caracter del mensaje en claro...
		for c in msj:

			# Sea kQ = (x0, y0) con x0 != 0 donde
			# k ∊ Z*ₙ es un número secreto aleatorio.
			x0 = 0
			while x0 == 0:
				k = random.randint(1, E.p) # Rango [a,b).
				if math.gcd(k, E.p) != 1:
					continue
				x0,_ = E.multiplicar_escalar(k, Q)

			# Obtenemos el número "x" que representa al caracter actual.
			x = ECIES.char_to_num(c, char_begin)

			# Primera coordenada del caracter cifrado.
			kP = E.multiplicar_escalar(k, P)
			y1 = E.comprimir_punto(kP)

			# Segunda coordenada del caracter cifrado.
			y2 = (x*x0) % E.p

			# Agregamos el caracter ya cifrado a la
			# lista que contendrá el mensaje cifrado.
			msj_cifrado.append((y1, y2))

		# Finalmente, devolvemos la lista
		# con el mensaje ya cifrado.
		return msj_cifrado

	def descifrar(E, P, m, Q, msj, char_begin=0):
		"""
		Descifra según el criptosistema ECIES.
		:param CurvaEliptica E: Curva elíptica reducida.
		:param tuple P: Primer punto P.
		:param int m: Número que multiplica a P para obtener Q.
		:param tuple Q: Segudo punto Q = mP.
		:param str msj: Lista con tuplas de la forma y=(y₁,y₂)
		donde y₁∊Zₚ×Z₂ y y₂∊Z*ₚ.
		:param int char_begin: Desfase del alfabeto. A considerar:
		A=begin B=begin+1 ... Z=begin+25
		:return: Cadena con únicamente caracteres en mayúsculas,
		sin espacios ni otros símbolos (ABC...MNOP...XYZ).
		"""

		# El mensaje descifrado será una cadena.
		msj_claro = ""

		# Por cada tupla y=(y₁,y₂) del mensaje cifrado...
		for y1,y2 in msj:

			# Descomprimimos el punto y₁.
			y1_descomprimido = E.descomprimir_punto(y1)

			# Definimos (x0,y0) = m * punto_de_descompresión(y₁).
			x0,y0 = E.multiplicar_escalar(m, y1_descomprimido) # DEBUG: Cambiar y0 por _.

			# DEBUG: Borrar esto.
			# print(f"Al descomprimir {y1} resulta {y1_descomprimido} y por m={m} es ({x0},{y0}).")

			# El número que representa al caracter
			# descifrado viene dado por y₂(x0)⁻¹ mod p.
			d = y2 * pow(x0, -1, E.p)
			d %= E.p

			# DEBUG: Borrar esto.
			# print(f"Para y=({y1},{y2}) resulta d={d}.")

			# Convertimos el número que representa al caracter, en el caracter
			# correspondiente, y lo agregamos a la cadena a devolver.
			msj_claro += ECIES.num_to_char(d, char_begin)

		# Finalmente, devolvemos la cadena
		# con el mensaje ya descifrado.
		return msj_claro

	def char_to_num(char, begin=0):
		"""
		Toma un caracter y devuelve a qué número corresponde,
		considerando que A=begin B=begin+1 ... Z=begin+25.
		:param str char: Cadena de longitud 1 a convertir en número.
		:param int begin: Desfase del alfabeto.
		:return: El número asociado al caracter dado, según el
		desfase proporcionado.
		"""
		num = ord(char)
		num -= 65
		assert num >= 0 and num <= 25
		return num+begin

	def num_to_char(num, begin=0):
		"""
		Toma un número y devuelve a qué caracter corresponde,
		considerando que A=begin B=begin+1 ... Z=begin+25.
		:param str num: Número a convertir en caracter.
		:param int begin: Desfase del alfabeto.
		:return: Cadena de longitud 1 asociada al número dado,
		según el desfase proporcionado.
		"""
		num -= begin
		num %= 26
		num += 65
		return chr(num)

# DEBUG: Borrar esto.

# E = CurvaEliptica(1, 1, 71)
# P = (18, 61)
# for x in range(1, 71):
# 	if E.multiplicar_escalar(x, P) == (59, 6):
# 		m = x
# 		print(f"m={m}")
# 		break
# Q = E.multiplicar_escalar(m, P)
# assert Q == (59, 6)
# msj = [
# 	((23,0),21),
# 	((13,1),47),
# 	((9,1),57),
# 	((44,0),25),
# 	((39,1),11),
# 	((64,1),53),
# 	((5,1),26),
# ]
# char_begin = 0
# # for x in range(26):
# # 	char_begin = x
# print(char_begin, ECIES.descifrar(E,P,m,Q,msj,char_begin))

	# ((23,0),52),
	# ((4,0),44),
	# ((58,1),13),
	# ((65,0),11),
	# ((9,1),63),
	# ((41,0),55),
	# ((30,0),21),
