import sympy, numpy, itertools
from math import sqrt, floor, gcd

def descifrado_RSA(n, p, q, mensaje_cifrado, debug=False):
	"""
	Descifra el mensaje que fue cifrado mediante RSA y lo devuelve.

	:param int n: Módulo de las llaves pública y privada.
	:param int p: Primer número primo que generó a "n".
	:param int q: Segundo número primo que generó a "n".
	:param list mensaje_cifrado: Lista con el mensaje cifrado. Se
	esperan tuplas de la forma (e, m), en donde "e" es el exponente
	de la llave pública con la que se llegó al mensaje cifrado "m".
	:param bool debug: ¿Imprimir resultados en consola?
	:return: Mensaje ya descifrado.
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

def criba_cuadratica(n, base_size, debug=False):
	"""
	Descompone el número dado mediante Criba Cuadrática.
	:param int n: Número a descomponer.
	:param int base_size: Tamaño que tendrá la base de factores.
	:param bool debug: ¿Imprimir resultados en consola?
	:return: None si no fue posible encontrar un resultado
	para "n" con el tamaño de la base dado, o dos factores
	no triviales para "n".
	"""

	# Verificaciones de tipado.
	assert isinstance(n, int)
	assert isinstance(base_size, int)
	assert isinstance(debug, bool)

	# Construimos la base de factorización S.
	S = [-1,2] # -1 y 2 siempre están incluidos.
	p = 3 # Seguimos con los demás primos.
	for i in range(base_size-2):

		# Sólo introducimos primos para los cuales
		# n es un residuo cuadrático módulo p.
		while sympy.legendre_symbol(n, p) != 1:
			p = sympy.nextprime(p)
		S.append(p)
		p = sympy.nextprime(p)

	# Imprimimos la base.
	if debug: print(f"\nLa base encontrada fue S = {S}.")

	# Calculamos "m".
	m = floor(sqrt(n))
	if debug: print(f"Calculamos m = ⌊√n⌋ = {m}.\n")
	
	# Variables relevantes.
	i = 1 # Fijamos i = 1.
	x = 0 # Vienen en el orden 0, +-1, +-2, ...
	A = [] # Valores a_i.
	F = [] # Factorizaciones.
	V = [] # Vectores v_i.

	# Mientras i <= t+1...
	if debug: print("Iteraciones...")
	while i <= base_size+1:

		# Creamos una cadena, que representa la tabla con
		# i | x | q(x)=b | factorización q(x) | a_i | v_i
		cadena = f"i={i} "

		# Buscaremos una "b" que sea homogénea con la base.
		buscar_b = True
		while buscar_b:
			b = (x+m)**2 - n
			b_homogeneo = S_homogeneo(b, S)

			# Si sí es homogénea, actualizamos la cadena
			# con la "x" correspondiente, y almacenamos
			# la "a" y la factorización correspondientes.
			if b_homogeneo:
				cadena += f"x={x} "
				a = (x+m)
				A.append(a)
				F.append(b_homogeneo)

			# Actualización de "x", que recorre 0, +-1, +-2, ...
			if x <= 0:
				x *= -1
				x += 1
			else:
				x *= -1

			# Si "b" sí es homogénea, podemos dejar de buscarla.
			if b_homogeneo:
				buscar_b = False

		# Guardamos la factorización en formato amigable de cadena.
		factorizacion = "".join( [f"{x}^{y} + " for x,y in b_homogeneo.items()] )[:-3]

		# Creamos los vectores v_i, y los almacenamos en V.
		v = list()
		for s in S:
			e = b_homogeneo.get(s)
			if e == None: e = 0
			v.append(e % 2)
		V.append(v)

		# Actualizamos la cadena, y la imprimimos.
		cadena += f"b={b} a={a} factorizacion={factorizacion} v={v}"
		if debug: print(cadena)

		# Actualización de la i-ésima iteración.
		i += 1

	# Espacio estético.
	if debug: print()

	# Buscaremos los vectores que puedan ser sumados/restados para dar cero...

	# Empezamos separando los vectores independientes de los dependientes.
	_,vectores_independientes = sympy.Matrix(V).T.rref()
	vectores_independientes = [V[x] for x in vectores_independientes]
	vectores_dependientes = [v for v in V if v not in vectores_independientes]

	# Obtenemos todas las combinaciones de todos los tamaños de los vectores dependientes.
	combinaciones_dependientes = []
	elementos = 1
	while elementos <= len(vectores_dependientes):
		combinaciones_dependientes.extend(list(itertools.combinations(vectores_dependientes, elementos)))
		elementos += 1

	# Obtenemos todas las combinaciones de todos los tamaños de los vectores independientes.
	combinaciones_independientes = []
	elementos = 1
	while elementos <= len(vectores_independientes):
		combinaciones_independientes.extend(list(itertools.combinations(vectores_independientes, elementos)))
		elementos += 1

	# Realizamos el producto cartesiano para obtener todas las formas de
	# juntar los vectores independientes con los vectores dependientes.
	combinaciones = list(itertools.product(combinaciones_independientes, combinaciones_dependientes))
	combinaciones = [tupla[0] + tupla[1] for tupla in combinaciones]

	# Por cada combinación posible de vectores dependientes + vectores independientes...
	for combinacion in combinaciones:

		# Sumamos los vectores, quitando cualquier cero para
		# ignorar las entradas que no hacen colisión.
		c = numpy.array(combinacion)
		c = sum(c)
		c = [x for x in c if x != 0]

		# Si el vector resultante tiene todas sus entradas
		# iguales, distintas de 1, entonces los vectores
		# de la combinación pueden ser sumados/restados
		# para dar como resultado cero.
		if c.count(c[0]) == len(c):
			if c[0] == 1:
				continue

			# Imprimimos dichos vectores.
			if debug: print("Los siguientes vectores cumplen Σ_{i∊T} V_{i} = 0:")
			if debug: print(combinacion)

			# Obtenemos T (los índices de los vectores obtenidos).
			T = [i+1 for i,v in enumerate(V) if v in combinacion]
			if debug: print("Por lo que T =", T)

			# Obtenemos los términos a multiplicar para obtener "x",
			# y su representación amigable en cadena.
			a = [A[i-1] for i in T]
			prod = "".join( [f"{str(y)} * " for y in a] )[:-3]

			# Obtenemos la "x".
			x = numpy.prod(a) % n
			if debug: print(f"Así, x = ({prod}) mod {n} = {x}")

			# Calculamos las l_j.
			e_i_j = [F[i-1] for i in T] # Buscamos las factorizaciones correspondientes a los vectores obtenidos.
			e_i_j = [[l[s] if s in l else 0 for s in S] for l in e_i_j] # Obtenemos los exponentes asociados a cada factorización con cada primo de la base S.
			L = list(map(sum, zip(*e_i_j))) # La i-ésima entrada de L será la suma de los i-ésimos exponentes de cada lista de e_i_j.
			L = list(map(lambda f: f//2, L)) # Dividimos cada una de esas sumas entre dos.
			l = "".join( [f"l_{i}={j}   " for i,j in enumerate(L)] )[:-3] # Obtenemos la representación amigable en cadena de estas l's.
			if debug: print("De donde:  ", l)

			# Obtenemos los términos a multiplicar para obtener "y".
			a = dict(zip(S, L)) # Hacemos un diccionario p^l para cada p en S y l en L.
			a_string = "".join( [f"{k}^{v} * " for k,v in a.items()] )[:-3] # Representación amigable de estos términos a multiplicar.
			y = list(map(lambda f: f**(a[f]), a)) # Elevamos cada llave del diccionario a su valor y lo convertimos en lista.
			y = numpy.prod(y) % n # Calculamos "y" al multiplicar estos valores elevados y aplicamos módulo.
			if debug: print(f"Así, y = ({a_string}) mod {n} = {y}")

			# Comprobación de terminación.
			if debug: print(f"\nComprobamos si x ≡ ±y mod n...")

			# Continuamos buscando con otros vectores si hay congruencia.
			if (x % n == y % n or x % n == -y % n):
				if debug: print(f"¡x ≡ ±y mod n!")
				if debug: print("Entonces buscamos otros vectores...\n")
				continue

			# Si no hay congruencia, calculamos el mcd correspondiente y terminamos.
			if debug: print(f"¡x ≢ ±y mod n!\n")
			mcd = gcd(x-y, n)
			if debug: print(f"Entonces mcd(x-y, n) = mcd({x-y}, {n}) = {mcd}")

			# Devolvemos dos factores no triviales de n.
			return mcd, n//mcd

	# Si no hemos logrado resolver para "n" con
	# el tamaño de la base dado, regresamos None.
	return None

def S_homogeneo(b, S):
	"""
	Determina si el número "b" es factorizable
	únicamente con números en S.
	:param int b: Número a factorizar.
	:param list S: Base de factorización.
	:return: False si no es posible factorizar "b"
	únicamente con números en S, o la factorización
	en formato de diccionario, en donde la llave representa
	valores de S y los valores son los exponentes.
	"""

	# Verificaciones de tipado.
	assert isinstance(b, int)
	assert isinstance(S, list)

	# Obtenemos la factorización por primos de "b".
	factorizacion = sympy.factorint(b)

	# Por cada factor primo de la factorización...
	for fp in factorizacion:

		# ...si este factor primo no es
		# parte de S, devolvemos falso.
		if fp not in S:
			return False

	# Devolvemos la factorización si todos los
	# factores primos se encuentran en la base.
	return factorizacion

if __name__ == '__main__':
	""" Función principal. """

	# Criptografía y Seguridad (2023-1)
	# Sebastián Alamina Ramírez
	# Tarea 2 - Ejercicios 3a y 3b.
	# 09/noviembre/2022
	n = 4245221
	p,q = criba_cuadratica(n, 7, debug=True)
	print(f"\nDos factores no triviales para n={n} son {p} y {q}.")

	# Criptografía y Seguridad (2023-1)
	# Sebastián Alamina Ramírez
	# Tarea 2 - Ejercicio 3c.
	# 09/noviembre/2022
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
