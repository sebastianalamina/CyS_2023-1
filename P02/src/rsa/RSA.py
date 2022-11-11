import sympy
import math

class RSA(object):
	"""Criptosistema RSA."""
	
	def generar_clave():
		"""
		Función que genera una clave pública y otra privada para el criptosistema RSA.
		:return: Tupla (n, e, d) que representa una clave aleatoria. "n" es el módulo,
		"e" el exponente de la clave pública, y "d" el exponente de la clave privada.
		"""

		# Debugeo.
		debug = False

		# Rango para creación de números primos.
		cien_digitos = 10**99
		muchos_digitos = cien_digitos**4

		# Números primos distintos aleatorios.
		p = sympy.randprime(cien_digitos, muchos_digitos)
		if debug: print(f"p = {p}")
		q = sympy.randprime(cien_digitos, muchos_digitos)
		if debug: print(f"q = {q}")
		
		# La probabilidad de que sean iguales es muy baja,
		# pero hacemos la comprobación de todas maneras.
		while p == q:
			q = sympy.randprime(cien_digitos, muchos_digitos)

		# Se calcula "n" que se usará como módulo
		# para la clave pública y privada.
		n = p * q
		if debug: print(f"n = {n}")

		# Función de Euler.
		phi = (p-1) * (q-1)
		if debug: print(f"φ = {phi}")

		# Entero "e" positivo menor que phi y coprimo con
		# phi, que será el exponente de la clave pública.
		e = sympy.randprime(cien_digitos/2, cien_digitos)
		if debug: print(f"e = {e}")
		assert (e < phi) and (math.gcd(e, phi) == 1)

		# Se calcula "d" que satisfaga la congruencia
		# e*d ≡ 1 (mod phi). Es decir, "d" es el
		# multiplicativo modular inverso de: e mod phi.
		# Esto es equivalente a d ≡ e mod^-1 (phi).
		# "d" será el exponente de la clave privada.
		d = pow(e, -1, phi)
		if debug: print(f"d = {d}")

		# Regresamos la tupla que incluye
		# las claves pública y privada.
		return (n, e, d)

	def cifrar(m, n, e):
		"""
		Función que cifra según el criptosistema RSA.
		El texto cifrado "c" se calcula con la función:
			c ≡ m^e ⟮mod n)
		:param int m: Entero que representa el
		caracter a cifrar.
		:param int n: Módulo de la clave.
		:param int e: Exponente de la clave pública.
		:return: El texto ya cifrado "c".
		"""
		return pow(m, e, n)

	def descifrar(c, n, d):
		"""
		Función que descifra según el criptosistema RSA.
		El texto descifrado "m" se calcula con la función:
			m ≡ c^d ⟮mod n)
		:param int c: Entero que representa el
		caracter cifrado a descifrar.
		:param int n: Módulo de la clave.
		:param int d: Exponente de la clave privada.
		:return: El texto ya descifrado "m".
		"""
		return pow(c, d, n)