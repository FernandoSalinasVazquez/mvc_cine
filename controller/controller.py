from model.model import Model
from view.view import View
from datetime import date
from datetime import time
import getpass


class Controller:

	def __init__(self):
		self.model = Model()
		self.view = View()

	def start(self):
		self.view.start()
		self.menu_inicio()

	def menu_inicio(self):
		o = '0'
		while o != '3':
			self.view.menu_inicio()
			self.view.option('3')
			o = input()
			if o == '1':
				c = self.comprobacion_creeciales()
				if c:
					self.main_menu()
				else:
					self.start()
			elif o == '2':
				self.main_menu_not_admin()
			elif o == '3':
				self.view.end()
			else: 
				self.view.not_valid_option()
		return

	def main_menu(self):
		o = '0'
		while o != '7':
			self.view.main_menu()
			self.view.option('7')
			o = input()
			if o == '1':
				self.menu_peliculas()
			elif o == '2':
				self.menu_salas()
			elif o == '3':
				self.menu_proyecciones()
			elif o == '4':
				self.menu_asientos()
			elif o == '5':
				self.menu_boletos()
			elif o == '6':
				self.menu_usuarios()
			elif o == '7':
				self.view.end()
			else: 
				self.view.not_valid_option()
		return

	def main_menu_not_admin(self):
		o = '0'
		while o != '5':
			self.view.menu_not_admin()
			self.view.option('5')
			o = input()
			if o == '1':
				self.menu_peliculas_not_admin()
			elif o == '2':
				self.menu_salas_not_admin()
			elif o == '3':
				self.menu_proyecciones_not_amin()
			elif o == '4':
				self.menu_asientos_not_admin()			
			elif o == '5':
				self.view.end()
			else: 
				self.view.not_valid_option()
		return

	def update_lists(self, fs, vs):
		fields = []
		vals = []
		for f,v in zip(fs, vs):
			if v !='':
				fields.append(f+' = %s')
				vals.append(v)
		return fields, vals

# Controllers for Peliculas

	def menu_peliculas(self):
		o = '0'
		while o != '8':
			self.view.peliculas_menu()
			self.view.option('8')
			o = input()
			if o == '1':
				self.create_pelicula()
			elif o == '2':
				self.read_a_pelicula()
			elif o == '3':
				self.read_peliculas()
			elif o == '4':
				self.read_peliculas_genero()
			elif o == '5':
				self.read_peliculas_director()
			elif o == '6':
			    self.update_pelicula()
			elif o == '7':
			    self.delete_pelicula()
			elif o == '8':
				return
			else: 
			    self.view.not_valid_option()
		return
	
	def menu_peliculas_not_admin(self):
		o = '0'
		while o != '5':
			self.view.peliculas_menu_not_admin()
			self.view.option('5')
			o = input()
			if o == '1':
				self.read_a_pelicula()
			elif o == '2':
				self.read_peliculas()
			elif o == '3':
				self.read_peliculas_genero()
			elif o == '4':
				self.read_peliculas_director()
			elif o == '5':
				return
			else: 
			    self.view.not_valid_option()
		return

	def ask_pelicula(self):
		self.view.ask('Titulo: ')
		titulo = input()
		self.view.ask('Nacionalidad: ')
		nacionalidad = input()
		self.view.ask('Director: ')
		director = input()
		self.view.ask('Clasificacion: ')
		clasificacion = input()
		self.view.ask('Sinopsis: ')
		sinopsis = input()
		self.view.ask('Duracion: ')
		duracion = input()
		self.view.ask('Fecha Estreno: ')
		f_estreno = input()
		self.view.ask('Genero: ')
		genero = input()
		return[titulo, nacionalidad, director, clasificacion, sinopsis, duracion, f_estreno, genero]

	def create_pelicula(self):
		titulo, nacionalidad, director, clasificacion, sinopsis, duracion, f_estreno, genero = self.ask_pelicula()
		out = self.model.create_pelicula(titulo, nacionalidad, director, clasificacion, sinopsis, duracion, f_estreno, genero)
		if out == True:
			self.view.ok(titulo+' '+f_estreno, 'agrego')
		else:
			self.view.error('No se pudo agregar la pelicula. REVISA')
		return

	def read_a_pelicula(self):
		self.view.ask('ID Pelicula: ')
		id_pelicula = input()
		pelicula = self.model.read_a_pelicula(id_pelicula)
		if type(pelicula) == tuple:
			self.view.show_pelicula_header('  Datos de la Pelicula '+id_pelicula+' ')
			self.view.show_a_pelicula(pelicula)
			self.view.show_peliculas_midder()
			self.view.show_peliculas_footer()
		else:
			if pelicula == None:
				self.view.error('LA PELICULA NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
		return

	def read_peliculas(self):
		peliculas = self.model.read_peliculas()
		if type(peliculas) == list:
			self.view.show_pelicula_header('Todas las peliculas')
			for pelicula in peliculas:
				self.view.show_a_pelicula(pelicula)
			self.view.show_peliculas_midder()
			self.view.show_peliculas_footer()
		else:
			self.view.error('PROBLEMA AL LEER  LAS PELICULAS. REVISA')
		return
	
	def read_peliculas_director(self):
		self.view.ask('Director: ')
		director = input()
		peliculas = self.model.read_peliculas_director(director)
		if type(peliculas) == list:
			self.view.show_pelicula_header('  Peliculas de '+director+' ')
			for pelicula in peliculas:
				self.view.show_a_pelicula(pelicula)
			self.view.show_peliculas_midder()
			self.view.show_peliculas_footer()
		else:
			self.view.error('PROBLEMA AL LEER  LAS PELICULAS. REVISA')
		return

	def read_peliculas_genero(self):
		self.view.ask('Genero: ')
		genero = input()
		peliculas = self.model.read_peliculas_genero(genero)
		if type(peliculas) == list:
			self.view.show_pelicula_header('  Peliculas de '+genero+' ')
			for pelicula in peliculas:
				self.view.show_a_pelicula(pelicula)
			self.view.show_peliculas_midder()
			self.view.show_peliculas_footer()
		else:
			self.view.error('PROBLEMA AL LEER  LAS PELICULAS. REVISA')
		return
	
	def update_pelicula(self):
		self.view.ask('ID de la pelucula a modificar: ')
		id_pelicula = input()
		pelicula = self.model.read_a_pelicula(id_pelicula)
		if type(pelicula) == tuple:
			self.view.show_pelicula_header('  Datos de la Pelicula '+id_pelicula+' ')
			self.view.show_a_pelicula(pelicula)
			self.view.show_peliculas_midder()
			self.view.show_peliculas_footer()
		else:
			if pelicula == None:
				self.view.error('La pelicula no existe')
			else:
				self.view.error('Problemas al leer la pelicula, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_pelicula()
		fields, vals = self.update_lists(['titulo','nacionalidad','director', 'clasificacion', 'sinopsis', 'duracion', 'f_estreno','genero'], whole_vals)
		vals.append(id_pelicula)
		vals = tuple(vals)
		out = self.model.update_pelicula(fields, vals)
		if out == True:
			self.view.ok(id_pelicula, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la pelucula. REVISA')
		return

	def delete_pelicula(self):
		self.view.ask('ID Pelicula a borrar: ')
		id_pelicula = input()
		count = self.model.delete_pelicula(id_pelicula)
		if count !=0:
			self.view.ok(id_pelicula, 'borro')
		else:
			if count == 0:
				self.view.error('La pelicula no existe')
			else:
				self.view.error('Problemas al leer la pelicula. REVISA')
		return

#Controllers for salas

	def menu_salas(self):
		o = '0'
		while o != '6':
			self.view.salas_menu()
			self.view.option('6')
			o = input()
			if o == '1':
				self.create_sala()
			elif o == '2':
				self.read_a_sala()
			elif o == '3':
				self.read_salas()
			elif o == '4':
			    self.update_sala()
			elif o == '5':
			    self.delete_sala()
			elif o == '6':
				return
			else: 
			    self.view.not_valid_option()
		return

	def menu_salas_not_admin(self):
		o = '0'
		while o != '3':
			self.view.salas_menu_not_admin()
			self.view.option('3')
			o = input()
			if o == '1':
				self.read_a_sala()
			elif o == '2':
				self.read_salas()
			elif o == '3':
				return
			else: 
			    self.view.not_valid_option()
		return

	def ask_sala(self):
		self.view.ask('Tipo: ')
		tipo = input()
		self.view.ask('Numero Asientos: ')
		no_asientos = input()
		return[tipo, no_asientos]

	def create_sala(self):
		tipo, no_asientos = self.ask_sala()
		out = self.model.create_salas(tipo, no_asientos)
		if out == True:
			self.view.ok(tipo+' con asientos: '+no_asientos, '  agrego')
		else:
			self.view.error('No se pudo agregar la sala. REVISA')
		return

	def read_a_sala(self):
		self.view.ask('ID Sala: ')
		id_sala = input()
		sala = self.model.read_a_sala(id_sala)
		if type(sala) == tuple:
			self.view.show_salas_header('  Datos de la sala '+id_sala+' ')
			self.view.show_a_sala(sala)
			self.view.show_salas_midder()
			self.view.show_salas_footer()
		else:
			if sala == None:
				self.view.error('LA SALA NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
		return

	def read_salas(self):
		salas = self.model.read_salas()
		if type(salas) == list:
			self.view.show_salas_header('Todas las Salas')
			for sala in salas:
				self.view.show_a_sala(sala)
			self.view.show_salas_midder()
			self.view.show_salas_footer()
		else:
			self.view.error('PROBLEMA AL LEER  LAS SALAS. REVISA')
		return

	def update_sala(self):
		self.view.ask('ID de la sala a modificar: ')
		id_sala = input()
		sala = self.model.read_a_sala(id_sala)
		if type(sala) == tuple:
			self.view.show_salas_header('  Datos de la sala '+id_sala+' ')
			self.view.show_a_sala(sala)
			self.view.show_salas_midder()
			self.view.show_salas_footer()
		else:
			if sala == None:
				self.view.error('La sala no existe')
			else:
				self.view.error('Problemas al leer la sala, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_sala()
		fields, vals = self.update_lists(['tipo','no_asientos'], whole_vals)
		vals.append(id_sala)
		vals = tuple(vals)
		out = self.model.update_sala(fields, vals)
		if out == True:
			self.view.ok(id_sala, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la sala. REVISA')
		return

	def delete_sala(self):
		self.view.ask('ID sala a borrar: ')
		id_sala = input()
		count = self.model.delete_sala(id_sala)
		if count !=0:
			self.view.ok(id_sala, 'borro')
		else:
			if count == 0:
				self.view.error('La sala no existe')
			else:
				self.view.error('Problemas al leer la sala. REVISA')
		return

	#Controllers for proyecciones
	def menu_proyecciones(self):
		o = '0'
		while o != '6':
			self.view.proyecciones_menu()
			self.view.option('6')
			o = input()
			if o == '1':
				self.create_proyeccion()
			elif o == '2':
				self.read_a_proyeccion()
			elif o == '3':
				self.read_proyecciones()
			elif o == '4':
			    self.update_proyeccion()
			elif o == '5':
			    self.delete_proyeccion()
			elif o == '6':
				return
			else: 
			    self.view.not_valid_option()
		return


	def menu_proyecciones_not_amin(self):
		o = '0'
		while o != '3':
			self.view.proyecciones_menu_not_admin()
			self.view.option('3')
			o = input()
			if o == '1':
				self.read_a_proyeccion()
			elif o == '2':
				self.read_proyecciones()
			elif o == '3':
				return
			else: 
			    self.view.not_valid_option()
		return

	def ask_proyeccion(self):
		self.view.ask('Hora: ')
		hora = input()
		self.view.ask('Lenguaje: ')
		lenguaje = input()
		self.view.ask('Costo: ')
		costo = input()
		self.view.ask('Fecha Proyeccion: ')
		f_proyeccion = input()
		self.view.ask('ID pelicula: ')
		id_pelicula = input()
		self.view.ask('ID sala: ')
		id_sala = input()
		return[hora, lenguaje, costo, f_proyeccion, id_pelicula, id_sala]

	def create_proyeccion(self):
		hora, lenguaje, costo, f_proyeccion, id_pelicula, id_sala = self.ask_proyeccion()
		out = self.model.create_proyeccion(hora, lenguaje, costo, f_proyeccion, id_pelicula, id_sala)
		if out == True:
			self.view.ok(hora+' '+f_proyeccion, ' agrego')
		else:
			self.view.error('No se pudo agregar la proyeccion. REVISA')
		return

	def read_a_proyeccion(self):
		self.view.ask('ID Proyeccion: ')
		id_proyeccion = input()
		proyeccion = self.model.read_a_proyeccion(id_proyeccion)
		if type(proyeccion) == tuple:
			self.view.show_proyecciones_header('  Datos de la proyeccion '+id_proyeccion+' ')
			self.view.show_a_proyeccion(proyeccion)
			self.view.show_proyecciones_midder()
			self.view.show_proyecciones_footer()
		else:
			if proyeccion == None:
				self.view.error('LA PROYECCION NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER LA proyeccion. REVISA.')
		return

	def read_proyecciones(self):
		proyecciones = self.model.read_proyecciones()
		if type(proyecciones) == list:
			self.view.show_proyecciones_header('Todas las Proyecciones')
			for proyeccion in proyecciones:
				self.view.show_a_proyeccion(proyeccion)
			self.view.show_proyecciones_midder()
			self.view.show_proyecciones_footer()
		else:
			self.view.error('PROBLEMA AL LEER  LAS PROYECCIONES. REVISA')
		return

	def update_proyeccion(self):
		self.view.ask('ID de la proyeccion a modificar: ')
		id_proyeccion = input()
		proyeccion = self.model.read_a_proyeccion(id_proyeccion)
		if type(proyeccion) == tuple:
			self.view.show_proyecciones_header('  Datos de la proyeccion '+id_proyeccion+' ')
			self.view.show_a_proyeccion(proyeccion)
			self.view.show_proyecciones_midder()
			self.view.show_proyecciones_footer()
		else:
			if proyeccion == None:
				self.view.error('La proyeccion no existe')
			else:
				self.view.error('Problemas al leer la proyeccion, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_proyeccion()
		fields, vals = self.update_lists(['hora', 'lenguaje', 'costo', 'f_proyeccion', 'id_pelicula', 'id_sala'], whole_vals)
		vals.append(id_proyeccion)
		vals = tuple(vals)
		out = self.model.update_proyeccion(fields, vals)
		if out == True:
			self.view.ok(id_proyeccion, 'actualizo')
		else:
			self.view.error('No se pudo actualizar la proyeccion. REVISA')
		return

	def delete_proyeccion(self):
		self.view.ask('ID proyeccion a borrar: ')
		id_proyeccion = input()
		count = self.model.delete_proyeccion(id_proyeccion)
		if count !=0:
			self.view.ok(id_proyeccion, 'borro')
		else:
			if count == 0:
				self.view.error('La proyeccion no existe')
			else:
				self.view.error('Problemas al leer la proyeccion. REVISA')
		return

	
	#Controllers for asientos
	def menu_asientos(self):
		o = '0'
		while o != '6':
			self.view.asientos_menu()
			self.view.option('6')
			o = input()
			if o == '1':
				self.create_asiento()
			elif o == '2':
				self.read_a_asiento()
			elif o == '3':
				self.read_asientos()
			elif o == '4':
			    self.update_asiento()
			elif o == '5':
			    self.delete_asiento()
			elif o == '6':
				return
			else: 
			    self.view.not_valid_option()
		return

	def menu_asientos_not_admin(self):
		o = '0'
		while o != '3':
			self.view.asientos_menu_not_admin()
			self.view.option('3')
			o = input()
			if o == '1':
				self.read_a_asiento()
			elif o == '2':
				self.read_asientos()
			elif o == '3':
				return
			else: 
			    self.view.not_valid_option()
		return


	def ask_asiento(self):
		self.view.ask('Disponible: ')
		disponible = input()
		self.view.ask('ID Sala: ')
		id_sala = input()
		return[disponible, id_sala]

	def create_asiento(self):
		disponible, id_sala = self.ask_asiento()
		out = self.model.create_asiento(disponible, id_sala)
		if out == True:
			self.view.ok(id_sala+' '+disponible, ' agrego')
		else:
			self.view.error('No se pudo agregar el asiento. REVISA')
		return

	def read_a_asiento(self):
		self.view.ask('ID Asiento: ')
		id_asiento = input()
		asiento = self.model.read_a_asiento(id_asiento)
		if type(asiento) == tuple:
			self.view.show_asiento_header('  Datos de el asieneto '+id_asiento+' ')
			self.view.show_a_asiento(asiento)
			self.view.show_asiento_midder()
			self.view.show_asiento_footer()
		else:
			if asiento == None:
				self.view.error('EL ASIENTO NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER EL ASIENTO. REVISA.')
		return

	def read_asientos(self):
		asientos = self.model.read_asientos()
		if type(asientos) == list:
			self.view.show_salas_header('Todas los Asientos')
			for asiento in asientos:
				self.view.show_a_asiento(asiento)
			self.view.show_asiento_midder()
			self.view.show_asiento_footer()
		else:
			self.view.error('PROBLEMA AL LEER  LAOS ASIENTOS. REVISA')
		return

	def update_asiento(self):
		self.view.ask('ID de el asiento a modificar: ')
		id_asiento = input()
		asiento = self.model.read_a_asiento(id_asiento)
		if type(asiento) == tuple:
			self.view.show_asiento_header('  Datos de el asiento '+id_asiento+' ')
			self.view.show_a_asiento(asiento)
			self.view.show_asiento_midder()
			self.view.show_asiento_footer()
		else:
			if asiento == None:
				self.view.error('El asiento no existe')
			else:
				self.view.error('Problemas al leer el asiento, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_asiento()
		fields, vals = self.update_lists(['disponible', 'id_sala'], whole_vals)
		vals.append(id_asiento)
		vals = tuple(vals)
		out = self.model.update_asiento(fields, vals)
		if out == True:
			self.view.ok(id_asiento, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el asiento. REVISA')
		return

	def delete_asiento(self):
		self.view.ask('ID asiento a borrar: ')
		id_asiento = input()
		count = self.model.delete_asiento(id_asiento)
		if count !=0:
			self.view.ok(id_asiento, 'borro')
		else:
			if count == 0:
				self.view.error('El asiento no existe')
			else:
				self.view.error('Problemas al leer el asiento. REVISA')
		return

	#Controllers for boletos
	def menu_boletos(self):
		o = '0'
		while o != '6':
			self.view.boletos_menu()
			self.view.option('6')
			o = input()
			if o == '1':
				self.create_boleto()
			elif o == '2':
				self.read_a_boleto()
			elif o == '3':
				self.read_boletos()
			elif o == '4':
			    self.update_boleto()
			elif o == '5':
			    self.delete_boleto()
			elif o == '6':
				return
			else: 
			    self.view.not_valid_option()
		return

	def ask_boleto(self):
		self.view.ask('ID proyeccion: ')
		id_proyeccion = input()
		self.view.ask('ID asiento: ')
		id_asiento = input()
		self.view.ask('ID sala: ')
		id_sala = input()
		return[id_proyeccion, id_asiento, id_sala]

	def create_boleto(self):
		id_proyeccion, id_asiento, id_sala = self.ask_boleto()
		out = self.model.create_boleto(id_proyeccion, id_asiento, id_sala)
		if out == True:
			self.view.ok(id_proyeccion+' '+id_asiento, ' agrego')
		else:
			self.view.error('No se pudo agregar el boleto. REVISA')
		return

	def read_a_boleto(self):
		self.view.ask('ID boleto: ')
		id_boleto = input()
		boleto = self.model.read_a_boleto(id_boleto)
		if type(boleto) == tuple:
			self.view.show_boleto_header('  Datos de el boleto '+id_boleto+' ')
			self.view.show_a_boleto(boleto)
			self.view.show_boleto_midder()
			self.view.show_boleto_footer()
		else:
			if boleto == None:
				self.view.error('EL BOLETO NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA.')
		return

	def read_boletos(self):
		boletos = self.model.read_boletos()
		if type(boletos) == list:
			self.view.show_boleto_header('Todas los Asientos')
			for boleto in boletos:
				self.view.show_a_boleto(boleto)
			self.view.show_boleto_midder()
			self.view.show_boleto_footer()
		else:
			self.view.error('PROBLEMA AL LEER  LOS BOLETOS. REVISA')
		return

	def update_boleto(self):
		self.view.ask('ID de el boleto a modificar: ')
		id_boleto = input()
		boleto = self.model.read_a_boleto(id_boleto)
		if type(boleto) == tuple:
			self.view.show_boleto_header('  Datos de el boleto '+id_boleto+' ')
			self.view.show_a_boleto(boleto)
			self.view.show_boleto_midder()
			self.view.show_boleto_footer()
		else:
			if boleto == None:
				self.view.error('El boleto no existe')
			else:
				self.view.error('Problemas al leer el boleto, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_boleto()
		fields, vals = self.update_lists(['id_proyeccion', 'id_asiento', 'id_sala'], whole_vals)
		vals.append(id_boleto)
		vals = tuple(vals)
		out = self.model.update_boleto(fields, vals)
		if out == True:
			self.view.ok(id_boleto, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el boleto. REVISA')
		return

	def delete_boleto(self):
		self.view.ask('ID boleto a borrar: ')
		id_boleto = input()
		count = self.model.delete_boleto(id_boleto)
		if count !=0:
			self.view.ok(id_boleto, 'borro')
		else:
			if count == 0:
				self.view.error('El boleto no existe')
			else:
				self.view.error('Problemas al leer el boleto. REVISA')
		return

	#Controllers for USuarios
	def menu_usuarios(self):
		o = '0'
		while o != '6':
			self.view.usuarios_menu()
			self.view.option('6')
			o = input()
			if o == '1':
				self.create_usuario()
			elif o == '2':
				self.read_a_usuario()
			elif o == '3':
				self.read_usuarios()
			elif o == '4':
			    self.update_usuario()
			elif o == '5':
			    self.delete_usuario()
			elif o == '6':
				return
			else: 
			    self.view.not_valid_option()
		return

	def ask_usuario(self):
		self.view.ask('Username: ')
		username = input()
		self.view.ask('Contraseña: ')
		contraseña = input()
		return[username, contraseña]
	
	def inicio_sesion(self):
		self.view.ask('Username: ')
		username = input()
		self.view.ask('Contraseña: ')
		contraseña = getpass.getpass("Contraseña: ")
		return[username, contraseña]


	def comprobacion_creeciales(self):
		usuario, contraseña = self.inicio_sesion()
		c = self.model.comprobacion_usuario(usuario, contraseña)
		return c

	def create_usuario(self):
		username, contraseña = self.ask_usuario()
		out = self.model.create_user(username, contraseña)
		if out == True:
			self.view.ok(username+' '+contraseña, ' agrego')
		else:
			self.view.error('No se pudo agregar el usuario. REVISA')
		return

	def read_a_usuario(self):
		self.view.ask('ID usuario: ')
		id_usuario = input()
		usuario = self.model.read_a_user(id_usuario)
		if type(usuario) == tuple:
			self.view.show_usuario_header('  Datos de el usuario '+id_usuario+' ')
			self.view.show_a_usuario(usuario)
			self.view.show_usuario_midder()
			self.view.show_usuario_footer()
		else:
			if usuario == None:
				self.view.error('EL USUARIO NO EXISTE')
			else:
				self.view.error('PROBLEMA AL LEER EL USUSARIO. REVISA.')
		return

	def read_usuarios(self):
		usuarios = self.model.read_users()
		if type(usuarios) == list:
			self.view.show_usuario_header('Todos los Usuarios')
			for usuario in usuarios:
				self.view.show_a_usuario(usuario)
			self.view.show_usuario_midder()
			self.view.show_usuario_footer()
		else:
			self.view.error('PROBLEMA AL LEER  LOS USUARIOS. REVISA')
		return
	
	def update_usuario(self):
		self.view.ask('ID de el usuario a modificar: ')
		id_usuario = input()
		usuario = self.model.read_a_user(id_usuario)
		if type(usuario) == tuple:
			self.view.show_usuario_header('  Datos de el usuario '+id_usuario+' ')
			self.view.show_a_usuario(usuario)
			self.view.show_usuario_midder()
			self.view.show_usuario_footer()
		else:
			if usuario == None:
				self.view.error('El usuario no existe')
			else:
				self.view.error('Problemas al leer el usuario, REVISA')
			return
		self.view.msg('Ingresa los valores a modificar:(vacio para dejarlo igual)')
		whole_vals = self.ask_usuario()
		fields, vals = self.update_lists(['username', 'contraseña'], whole_vals)
		vals.append(id_usuario)
		vals = tuple(vals)
		out = self.model.update_user(fields, vals)
		if out == True:
			self.view.ok(id_usuario, 'actualizo')
		else:
			self.view.error('No se pudo actualizar el usuario. REVISA')
		return

	def delete_usuario(self):
		self.view.ask('ID usuario a borrar: ')
		id_usuario = input()
		count = self.model.delete_user(id_usuario)
		if count !=0:
			self.view.ok(id_usuario, 'borro')
		else:
			if count == 0:
				self.view.error('El usuario no existe')
			else:
				self.view.error('Problemas al leer el usuario. REVISA')
		return