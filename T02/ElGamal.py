import sympy, numpy, random, math
random.seed("CyS_T02") # Semilla para generar lo mismo que en la tarea.

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
	:return: Mensaje ya descifrado.
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
	assert a != None
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

def generar_relacion_valida(S, p, n, alpha, beta=None):
	"""
	Genera una relación válida.

	Una relación válida, sin utilizar beta, es:
	alpha^k mod p = núm = p_1^c1 * ... * p_j^cj
	en donde k es aleatoria, 0 <= k <= n-1, y p_i está en S.

	Una relación válida, utilizando beta, es:
	beta*alpha^k mod p = núm = p_1^c1 * ... * p_j^cj
	en donde k es aleatoria, 0 <= k <= n-1, y p_i está en S.

	:param list S: Base de factorización.
	:param list p: Valor p.
	:param int n: Valor n.
	:param int alpha: Valor alpha.
	:param int beta: Valor beta.
	:return: La tupla (k, núm, vector) en donde "vector"
	representa el número de ocurrencias de los elementos
	en S dentro de la secuencia p_1^c1 * ... * p_j^cj.
	"""

	# Verificaciones de tipado.
	assert isinstance(S, list)
	assert isinstance(p, int)
	assert isinstance(n, int)
	assert isinstance(alpha, int)
	if beta != None: assert isinstance(beta, int)

	# Busquemos a la "k" tal que la relación sea válida.
	buscar_k = True
	while buscar_k:

		# Actualización de la condición del while.
		# Si no hemos encontrado la "k", esta condición cambiará.
		buscar_k = False

		# Escogemos una k en el rango [0, n-1].
		k = random.randint(0, n-1)

		# El número cuyos factores primos deseamos encontrar es
		# alpha^k mod p.
		a_factorizar = pow(alpha, k, p)

		# Pero si nos dan "beta", este número es
		# beta*alpha^k mod p.
		if beta != None:
			a_factorizar = (a_factorizar * beta) % p

		# Obtenemos los factores primos del número obtenido.
		# Es decir, obtenemos p_1^c1 * ... * p_j^cj.
		factores_primos = sympy.factorint(a_factorizar)

		# Si no hay factores, buscamos otra factorización.
		# (caso conocido: cuando a_factorizar==1)
		if not factores_primos:
			buscar_k = True

		# Comprobamos que cada p_i esté en S. Si alguna
		# no lo está, buscamos otra factorización.
		for fp in factores_primos:
			if fp not in S:
				buscar_k = True
				break
	
	# Creamos un vector cuya i-ésima entrada contiene
	# el número ci del i-ésimo primo en S.
	vector = []
	for s in S:

		# Si el i-ésimo primo en S no es parte de la factorización,
		# la correspondiente entrada del vector tiene un cero.
		if s not in factores_primos:
			vector.append(0)

		# Si el i-ésimo primo en S sí es parte de la factorización,
		# la correspondiente entrada del vector incluye su exponente.
		else:
			vector.append(factores_primos[s])

	# Devolvemos el valor k, el valor alpha^k mod p
	# (o beta*alpha^k mod p), y el vector creado.
	return k, a_factorizar, vector

def generar_sistema_independiente(size, S, p, n, alpha):
	"""
	Genera un sistema linealmente independiente de ecuaciones
	generadas a partir de relaciones válidas aleatorias.

	:param int size: Número de ecuaciones a intentar crear.
	:param list S: Base de factorización.
	:param list p: Valor p.
	:param int n: Valor n.
	:param int alpha: Valor alpha.
	:return: Una lista cuyos elementos son tuplas
	asociadas a relaciones válidas.
	"""

	# Verificaciones de tipado.
	assert isinstance(size, int)
	assert isinstance(S, list)
	assert isinstance(p, int)
	assert isinstance(n, int)
	assert isinstance(alpha, int)

	# Creamos el sistema linealmente independiente.
	linealmente_independiente = False
	while not linealmente_independiente:

		# Agregamos "size" ecuaciones (sin considerar "beta").
		ecuaciones = []
		for i in range(size):
			ecuaciones.append(generar_relacion_valida(S,p,n,alpha,None))

		# Para determinar (con ayuda de numpy y sympy) si el sistema
		# es linealmente independiente, separamos los vectores de las
		# relaciones válidas para crear el sistema a testear, convertimos
		# este sistema en un arreglo de numpy, y testeamos con sympy.
		sistema = [e[2] for e in ecuaciones]
		sistema = numpy.array(sistema)
		_,ec_lin_ind = sympy.Matrix(sistema).T.rref()

		# Comprobamos tener tantas ecuaciones linealmente
		# independientes como se especifica en "size".
		# Comprobamos, además, que el sistema sea
		# soluble con el módulo correspondiente.
		lado_derecho = [[tupla[0]] for tupla in ecuaciones]
		if len(ec_lin_ind) != size or solucionar_sistema_modular(list(sistema), lado_derecho, n) == None:
			linealmente_independiente = False
		else:
			linealmente_independiente = True

	# Regresamos las ecuaciones (es decir, la lista
	# con las tuplas representando relaciones válidas).
	return ecuaciones

def solucionar_sistema_modular(coeficientes, lado_derecho, m):
	"""
	Soluciona el sistema de ecuaciones lineales con módulo dado.
	:param list coeficientes: Lista con los coeficientes de los
	polinomios del sistema.
	:param list lado_derecho: Lista con los números con los
	cuales cada polinomio está siendo igualado.
	:param int m: Módulo a aplicar.
	:return: Valores de cada variable del sistema.
	"""

	# Verificaciones de tipado.
	assert isinstance(coeficientes, list)
	assert isinstance(lado_derecho, list)
	assert isinstance(m, int)

	# Convertimos en matrices de sympy las listas dadas.
	coeficientes = sympy.Matrix(coeficientes)
	lado_derecho = sympy.Matrix(lado_derecho)

	# Conseguimos la determinante de los coeficientes.
	det = int(coeficientes.det())

	# Si la determinante y el módulo son coprimos, continuamos.
	# Si no lo son, no podemos resolver este sistema.
	if math.gcd(det, m) == 1:
		return pow(det, -1, m) * coeficientes.adjugate() @ lado_derecho % m
	else:
		return None

if __name__ == '__main__':
	""" Función principal. """

	# Criptografía y Seguridad (2023-1)
	# Sebastián Alamina Ramírez
	# Tarea 2 - Ejercicios 4a y 4b.
	# 10/noviembre/2022
	beta = 19 # Índice.
	alpha = 17 # Base.
	p = 2011 # Módulo.
	n = p-1 # Valor n.
	S = [2,3,5,7,11] # Base de factorización dada.
	ecuaciones = len(S) # Se necesitan al menos |S| ecuaciones.
	sistema = generar_sistema_independiente(ecuaciones, S, p, n, alpha)

	# Imprimimos las relaciones válidas generadas aleatoriamente.
	print("\nLas siguientes relaciones involucran elementos de S:")
	for ecuacion in sistema:
		k = ecuacion[0]
		num = ecuacion[1]
		vector = ecuacion[2]
		factorizacion = ""
		for fp,fpn in sympy.factorint(num).items():
			factorizacion += f"{fp}^{fpn} * "
		factorizacion = factorizacion[:-3]
		print(f"{alpha}^{k} mod {p} = {num} = {factorizacion} ---> {vector}")

	# Imprimimos el sistema de ecuaciones generado por las relaciones anteriores.
	print("\nEstas relaciones inducen el siguiente sistema linealmente independiente:")
	for ecuacion in sistema:
		k = ecuacion[0]
		num = ecuacion[1]
		vector = ecuacion[2]
		terminos = ""
		for fp,fpn in sympy.factorint(num).items():
			terminos += f"{fpn}log_{alpha}({fp}) + "
		terminos = terminos[:-3] + f" mod {n}"
		print(f"{k} = {terminos}")

	# Resolvemos el sistema.
	coeficientes = [tupla[2] for tupla in sistema]
	lado_derecho = [[tupla[0]] for tupla in sistema]
	soluciones = solucionar_sistema_modular(coeficientes, lado_derecho, n)
	soluciones = numpy.array(soluciones).astype(numpy.float64)

	# Imprimimos las soluciones del sistema.
	print("\nLas soluciones al sistema son:")
	for i,s in enumerate(S):
		print(f"log_{alpha}({s}) = {int(soluciones[i])}")

	# Generamos y resolvemos la relación válida
	# beta*alpha^k mod p.
	k,beta_alpha_k_mod_p,vector = generar_relacion_valida(S, p, n, alpha, beta)
	factorizacion = ""
	ecuacion = ""
	for fp,fpn in sympy.factorint(beta_alpha_k_mod_p).items():
		factorizacion += f"{fp}^{fpn} * "
		ecuacion += f"{fpn}log_{alpha}({fp}) + "
	factorizacion = factorizacion[:-3]
	ecuacion = ecuacion[:-3]
	log_alpha_beta = int((numpy.sum(soluciones.T * vector) - k) % n)

	# Imprimimos esta última.
	print(f"\nLuego, obtenemos la relación β*α^k mod p...\n{beta}*{alpha}^{k} mod {p} = {beta_alpha_k_mod_p} = {factorizacion}")
	print(f"De donde se obtiene:\nlog_{alpha}({beta}) = ({ecuacion} - {k}) mod {n}")
	print(f"log_{alpha}({beta}) = {log_alpha_beta}")

	# Imprimimos la llave privada.
	a = log_alpha_beta
	print(f"\nAsí, la llave privada es a = {a}.\n")

	# Criptografía y Seguridad (2023-1)
	# Sebastián Alamina Ramírez
	# Tarea 2 - Ejercicio 4c.
	# 10/noviembre/2022
	# NOTA: Si bien ya contamos con la llave privada (obtenida
	# previamente), este paso descifra ElGamal mediante fuerza
	# bruta (sólo por curiosidad sobre cómo lograrlo así).
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
	print(f"\nEl mensaje descifrado es:\n{mensaje_en_claro}\n")
