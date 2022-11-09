def criptoanalisis_ElGamal(llave_publica, mensaje_cifrado, debug=False):
	"""
	Criptoanálisis al criptosistema ElGamal. Imprime la llave
	privada "a" (o las llaves privadas, en caso de encontrar más
	de una) y devuelve el mensaje ya descrifrado.

	:param tuple llave_publica: Llave pública con la que se cifró
	el mensaje. Se espera la tupla (p, alpha, alpha^a mod p).
	:param list mensaje_cifrado: Mensaje cifrado. Se espera una
	lista con tuplas de la forma (gamma, delta).
	:param bool debug: ¿Imprimir resultados en consola?
	"""

	# Verificaciones de tipado.
	assert isinstance(llave_publica, tuple)
	assert len(llave_publica) == 3
	assert isinstance(mensaje_cifrado, list)
	for t in mensaje_cifrado:
		assert isinstance(t, tuple)
		assert len(t) == 2
	assert isinstance(debug, bool)

	# Imprimiendo en consola.
	if debug: print(f"Descifrando un mensaje de longitud {len(mensaje_cifrado)} que fue cifrado mediante ElGamal con llave pública {llave_publica}...")

	# Extracción de parámetros de la llave pública.
	p = llave_publica[0]
	alpha = llave_publica[1]
	alpha_a_mod_p = llave_publica[2]

	# Búsqueda de la llave privada "a".
	a = None
	for x in range(1,p-1): # Se debe cumplir 1 <= a <= p-2.

		# Buscamos a la "a" que encaje con el valor
		# correspondiente de la llave pública.
		if (((alpha ** x) % p) == alpha_a_mod_p):
			if a == None:
				a = x
				if debug: print(f"Se encontró la llave privada a={a}.")
			else:
				if debug: print(f"¡Además de a={a}, también a={x} cumple {alpha}^a mod {p} = {alpha_a_mod_p}!")

	# Ya contando con la llave privada "a",
	# podemos descifrar el mensaje.
	mensaje_en_claro = ""
	for t in mensaje_cifrado:

		# Cada tupla del mensaje cifrado
		# viene de la forma (gamma, delta).
		gamma = t[0]
		delta = t[1]

		# Necesitamos el valor gamma^(p-1-a), que
		# es multiplicado por delta módulo p para
		# obtener el caracter en claro correspondiente.
		gamma_p_1_a = (gamma ** (p-1-a)) % p
		c = (gamma_p_1_a * delta) % p

		# Pegamos el caracter descifrado al mensaje en claro.
		mensaje_en_claro += chr(c)

	# Finalmente, devolvemos el mensaje ya descifrado.
	return mensaje_en_claro

if __name__ == '__main__':
	""" Función principal. """

	# Criptografía y Seguridad (2023-1)
	# Sebastián Alamina Ramírez
	# Tarea 2 - Ejercicio 4.
	# 09/noviembre/2022
	llave_publica = (2011, 17, 19)
	mensaje_cifrado = [
		(891, 260),
		(1070, 1838),
		(91, 934),
		(1547, 1835),
		(156, 761),
		(641, 1542),
		(842, 1820),
		(237, 1757),
		(7, 1215),
		(119, 1898),
	]
	mensaje_en_claro = criptoanalisis_ElGamal(llave_publica, mensaje_cifrado, debug=True)
	print(f"El mensaje descifrado es:\n{mensaje_en_claro}")
