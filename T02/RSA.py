def descifrado_RSA(n, p, q, mensaje_cifrado, debug=False):
	"""
	Descifra el mensaje que fue cifrado mediante RSA y lo devuelve.

	:param int n: Módulo de las llaves pública y privada.
	:param int p: Primer número primo que generó a "n".
	:param int q: Segundo número primo que generó a "n".
	:param list mensaje_cifrado: Lista con el mensaje cifrado. Se
	esperan tuplas de la forma (e, m), en donde "e" es el exponente
	de la llave pública con la que se llegó al mensaje cifrado "m".
	"""

	# Verificaciones de tipado.
	assert isinstance(n, int) and isinstance(p, int) and isinstance(q, int)
	assert isinstance(mensaje_cifrado, list)
	for t in mensaje_cifrado:
		assert isinstance(t, tuple)
		assert len(t) == 2
	assert isinstance(debug, bool)

	# Imprimiendo en consola.
	if debug: print(f"\nDescifrando un mensaje de longitud {len(mensaje_cifrado)} que fue cifrado mediante RSA con parámetros n={n}, p={p}, q={q}...\n")

	# Desciframos el mensaje en claro, considerando que
	# la llave privada depende de cada llave pública.
	mensaje_en_claro = ""
	for t in mensaje_cifrado:

		# Cada tupla del mensaje cifrado
		# viene de la forma (e, m).
		e = t[0]
		m = t[1]

		# Calculamos la función de Euler.
		phi = (p-1) * (q-1)

		# Calculamos "d", que es el exponente
		# de la clave privada.
		d = pow(e, -1, phi)

		# Desciframos el caracter en curso.
		c = pow(m, d, n)

		# Imprimimos en consola.
		if debug: print(f"Al mensaje {m} cifrado con llave pública RSA ({n}, {e}) le corresponde la llave privada ({n}, {d}) y corresponde al caracter en claro {c}.")

		# Pegamos el caracter descifrado al mensaje en claro.
		mensaje_en_claro += chr(c)

	# Finalmente, devolvemos el mensaje ya descifrado.
	return mensaje_en_claro

if __name__ == '__main__':
	""" Función principal. """

	# Criptografía y Seguridad (2023-1)
	# Sebastián Alamina Ramírez
	# Tarea 2 - Ejercicio 3.
	# 09/noviembre/2022
	n = 4245221
	p,q = 2011,2111
	mensaje_cifrado = [
		(7, 2787825),
		(11, 2055284),
		(13, 2061537),
		(17, 4003203),
		(19, 3833015),
		(23, 504464),
		(29, 1181333),
		(31, 3063352),
		(37, 1145481),
		(41, 899155),
		(43, 1046164),
		(47, 1315170),
		(49, 1878863),
		(53, 2088416),
		(59, 2571920),
		(61, 2621019),
		(71, 1550905),
	]
	mensaje_en_claro = descifrado_RSA(n, p, q, mensaje_cifrado, debug=True)
	print(f"\nEl mensaje descifrado es:\n{mensaje_en_claro}\n")
