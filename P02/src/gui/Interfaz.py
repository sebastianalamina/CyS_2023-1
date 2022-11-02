#from carpeta.archivo import *

class Interfaz(object):

	def __init__(self):
		self.menu_principal()

	def menu_principal(self):
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
		x = input("Escoge una opción: ")
		if (x == "1"):
			pass
		elif (x == "2"):
			pass
		elif (x == "3"):
			pass
		elif (x != "4"):
			input("Introduce una opción válida. ")
			self.menu_principal()
