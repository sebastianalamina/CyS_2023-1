import sympy, math

class CurvaEliptica(object):
	"""
	Forma reducida de una Curva Elíptica:
	y² = x³ + ax + b donde a,b ∊ Zₚ.
	"""

	def __init__(self, a, b, p):
		"""
		Inicializa una Curva Elíptica en su forma reducida:
		y² = x³ + ax + b donde a,b ∊ Zₚ.
		:param int a: Coeficiente que multiplica a "x".
		:param int b: Término independiente.
		:param int p: Primo asociado a la curva elíptica.
		"""

		# Comprobaciones.
		assert p > 3
		distinto_de_cero = (4*pow(a,3) + 27*pow(b,2)) % p
		if (distinto_de_cero == 0):
			raise Exception("4a³+27b² debería ser distinto de cero.")
		assert distinto_de_cero != 0

		# Asignaciones.
		self.a = a
		self.b = b
		self.p = p

	def sumar(self, P, Q):
		"""
		:param tuple P: Primer punto dentro de la curva elíptica a sumarse.
		:param tuple Q: Segundo punto dentro de la curva elíptica a sumarse.
		:return: P + Q.
		"""

		# Elemento identidad.
		if P == 0:
			return Q
		elif Q == 0:
			return P

		# Comprobaciones.
		assert type(P) == tuple
		assert type(Q) == tuple
		assert len(P) == 2
		assert len(Q) == 2
		for n in P:
			assert n < self.p
		for n in Q:
			assert n < self.p
		assert P in self
		assert Q in self

		# Extracción de los valores de P y de Q.
		x1,y1 = P
		x2,y2 = Q

		# Si x2 = x1 y y2 = -y1 entonces P + Q = O.
		if x2 == x1 and (y2 == -y1 or y2+y1 == self.p):
			return 0

		# λ es la pendiente correspondiente a los puntos P y Q.
		if P == Q:
			try:
				division = pow(2*y1, -1, self.p)
			except Exception as e:
				print(f"Error al sumar P+Q={P}+{Q} pues se intentó la operación (2y₁)⁻¹ mod p = {2*y1}⁻¹ mod {self.p}: {e}.")
				return
			my_lambda = (3*pow(x1,2) + self.a) * division
			my_lambda %= self.p
		else:
			try:
				division = pow(x2-x1, -1, self.p)
			except Exception as e:
				print(f"Error al sumar P+Q={P}+{Q} pues se intentó la operación (x₂-x₁)⁻¹ mod p = {x2-x1}⁻¹ mod {self.p}: {e}.")
				return
			my_lambda = (y2-y1) * division
			my_lambda %= self.p
		assert type(my_lambda) == int

		# Definimos los valores del punto resultante P+Q = (x3,y3).
		x3 = pow(my_lambda, 2) - x1 - x2
		y3 = my_lambda*(x1-x3) - y1

		# Calculamos el punto resultante, módulo p.
		suma = (x3 % self.p, y3 % self.p)

		# Comprobamos que el punto resultante
		# se encuentre dentro de la curva.
		assert suma in self

		# Devolvemos el punto resultante, módulo p.
		return suma

	def multiplicar_escalar(self, m, P):
		"""
		:param int m: Escalar que multiplica al punto.
		:param tuple P: Punto en la curva elíptica.
		:return: La multiplicación mP.
		"""

		# Cualquier escalar multiplicado por el punto
		# en el infinito resulta en el mismo punto.
		if P == 0:
			return P

		# Comprobaciones.
		assert type(m) == int
		assert type(P) == tuple
		assert m >= 0

		# Multiplicación por cero.
		if m == 0:
			return 0

		# Recursión que realiza m-1 veces la suma P + P. 
		while m > 1:
			return self.sumar(P, self.multiplicar_escalar(m-1, P))

		# Comprobamos que el punto resultante
		# se encuentre dentro de la curva.
		assert P in self

		# Cuando m==1, devolvemos el mismo punto P módulo p.
		return P

	def comprimir_punto(self, P):
		"""
		Sea P = (x, y) ∊ E. El punto de compresión de P es (x, y mod 2).
		:param tuple P: Punto a comprimir.
		:return: El punto P comprimido.
		"""

		# Comprobaciones.
		assert type(P) == tuple

		# Devolvemos el punto comprimido.
		return (P[0], P[1] % 2)

	def descomprimir_punto(self, P):
		"""
		Operación inversa al punto de compresión.
		:param tuple P: Punto a descomprimir.
		:return: El punto P descomprimido.
		"""
		
		# Comprobaciones.
		assert type(P) == tuple

		# Extracción de los valores de P.
		x,i = P

		# Cálculo de "z".
		z = pow(x,3) + self.a*x + self.b
		z %= self.p

		# Si "z" no es RC mod p, entonces se toma el otro valor válido para "z".
		if (sympy.legendre_symbol(z, self.p) != 1):
			# print(f"Cambiando z={z} a z={self.p-z} para P={P}.") # DEBUG: Borrar esto.
			z = self.p - z
			assert sympy.legendre_symbol(z, self.p) == 1

		# El valor de √z lo podemos calcular como z^{(p+1)/4} mod p siempre que p ≡ 3 mod 4.
		if not (self.p%4 == 3%4):
			raise Exception("Cálculo de √z no definido para este caso.")

		# Cálculo de la raíz cuadrada de "z".
		exponente_z = (self.p+1) / 4
		assert exponente_z - math.floor(exponente_z) == 0 # Comprobación entera...
		exponente_z = int(exponente_z) # ...antes de convertir en entero.
		y = pow(z, exponente_z, self.p)

		# Si y ≡ i mod 2, el punto descomprimido es (x, y).
		if y%2 == i%2:
			punto_descomprimido = (x, y)

		# De otro modo, el punto descomprimido es (x, p-y).
		else:
			punto_descomprimido = (x, self.p-y)

		# Comprobamos que el punto descomprimido
		# sea parte de la curva.
		assert punto_descomprimido in self

		# Devolvemos el punto descomprimido.
		# print(f"Para {P}, z={z} y y={y}.") # DEBUG: Borrar esto.
		return punto_descomprimido

	def __contains__(self, obj):
		"""
		Sobreescritura de la función. Se usa en casos como "P in E",
		donde P podría representar un punto y E una Curva Elíptica.
		:param ? obj: Objeto a determinar si es parte de la curva.
		:return: Si el objeto dado representa un punto dentro de
		la curva.
		"""

		# El punto O.
		if obj == 0:
			return True

		# El objeto dado debe ser una tupla que represente un punto.
		if (type(obj) != tuple) or (len(obj) != 2):
			return False

		# Extracción de las coordenadas del punto.
		x,y = obj

		# y²
		left = pow(y,2,self.p) # y

		# x³ + ax + b
		right = pow(x,3,self.p) + (self.a*x) + self.b
		right %= self.p

		# Comprobamos que el punto dado pertenezca a la curva.
		if left == right:
			return True

		# En cualquier otro caso, el punto no pertenece a la curva.
		return False
