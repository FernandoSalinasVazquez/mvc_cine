class View:
    #Vista 

    def start(self):
        print('======================')
        print('Bienvenido')
        print('======================')

    def end(self):
        print('======================')
        print('Gracias por su Visita')
        print('======================')


    def main_menu(self):
        print('======================')
        print('-- Menu Principal Admin --')
        print('======================')
        print('1. Peliculas')
        print('2. Salas')
        print('3. Proyecciones')
        print('4. Asientos')
        print('5. Boletos')
        print('6. Usuarios')
        print('7. Salir')
    
    def menu_not_admin(self):
        print('======================')
        print('-- Menu Principal --')
        print('======================')
        print('1. Peliculas')
        print('2. Salas')
        print('3. Proyecciones')
        print('4. Asientos')
        print('5. Salir')
        

    def option(self, last):
        print('Selcciona una opcion (1-'+last+'): ', end ='')


    def not_valid_option(self):
        print('¡Opcion no valida!\nIntenta de nuevo')
    
    def ask(self, output):
        print(output, end='')

    def msg(self, output):
        print(output)

    def ok(self, id, op): 
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err): 
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
    
    def menu_inicio(self):
        print('Eres Admin?')
        print('1.Si ')
        print('2.No ')
        print('3.Salir ')
        
        #Views of peliculas
    def peliculas_menu_not_admin(self):
        print('======================')
        print('-- Submenu Peliculas --')
        print('======================')
        print('1. Mostrar Pelicula')
        print('2. Mostrar todas las peliculas')
        print('3. Mostrar peliculas por genero')
        print('4. Mostrar peliculas por director')
        print('5. Regresar')
        
    def peliculas_menu(self):
        print('======================')
        print('-- Submenu Peliculas --')
        print('======================')
        print('1. Agregar pelicula')
        print('2. Mostrar Pelicula')
        print('3. Mostrar todas las peliculas')
        print('4. Mostrar peliculas por genero')
        print('5. Mostrar peliculas por director')
        print('6. Actualizar pelicula')
        print('7. Borrar pelicula')
        print('8. Regresar')
    
    def show_a_pelicula(self, record):
        print('ID: ', record[0])
        print('Titulo: ', record[1])
        print('Nacionalidad: ', record[2])
        print('Director: ', record[3])
        print('Clasificacion: ', record[4])
        print('Sinopsis: ', record[5])
        print('Duracion: ', record[6], 'hrs')
        print('Fecha de Estreno: ', record[7])
        print('Genero: ', record[8])

    def show_pelicula_header(self, header):
        print(header.center(70, '*'))
        print('-'*70)
    
    def show_peliculas_midder(self):
        print('-'*70)

    def show_peliculas_footer(self):
        print('*'*70)
    

        #Views of Salas
    def salas_menu(self):
        print('======================')
        print('-- Submenu Salas --')
        print('======================')
        print('1. Agregar Sala')
        print('2. Mostrar Sala')
        print('3. Mostrar todas las Salas')
        print('4. Actualizar pelicula')
        print('5. Borrar pelicula')
        print('6. Regresar')

    def salas_menu_not_admin(self):
        print('======================')
        print('-- Submenu Salas --')
        print('======================')
        print('1. Mostrar Sala')
        print('2. Mostrar todas las Salas')
        print('3. Regresar')
        
    def show_a_sala(self, record):
        print('ID: ', record[0])
        print('Tipo: ', record[1])
        print('Numero de asientos: ', record[2])

    def show_salas_header(self, header):
        print(header.center(20, '*'))
        print('-'*20)
    
    def show_salas_midder(self):
        print('-'*20)

    def show_salas_footer(self):
        print('*'*20)

            #Views of proyecciones
    def proyecciones_menu(self):
        print('======================')
        print('-- Submenu Proyecciones --')
        print('======================')
        print('1. Agregar Proyeccion')
        print('2. Mostrar Proyeccion')
        print('3. Mostrar todas las Proyecciones')
        print('4. Actualizar Proyeccion')
        print('5. Borrar Proyeccion')
        print('6. Regresar')
        
    def proyecciones_menu_not_admin(self):
        print('======================')
        print('-- Submenu Proyecciones --')
        print('======================')
        print('1. Mostrar Proyeccion')
        print('2. Mostrar todas las Proyecciones')
        print('3. Regresar')
    
    def show_a_proyeccion(self, record):
        print('Pelicula: ', record[0])
        print('Clasificacion: ', record[1])
        print('Hora: ', record[2])
        print('Lenguaje: ', record[3])
        print('Costo: ', record[4])
        print('Fecha: ', record[5])


    def show_proyecciones_header(self, header):
        print(header.center(20, '*'))
        print('-'*20)
    
    def show_proyecciones_midder(self):
        print('-'*20)

    def show_proyecciones_footer(self):
        print('*'*20)

     #Views of boletos
    def boletos_menu(self):
        print('======================')
        print('-- Submenu Boletos --')
        print('======================')
        print('1. Agregar Boleto')
        print('2. Mostrar Boleto')
        print('3. Mostrar todas los boletos')
        print('4. Actualizar boleto')
        print('5. Borrar boleto')
        print('6. Regresar')
        
    def show_a_boleto(self, record):
        print('ID boleto: ', record[0])
        print('ID Proyeccion: ', record[1])
        print('ID asiento: ', record[2])
        print('ID Sala: ', record[3])


    def show_boleto_header(self, header):
        print(header.center(10, '*'))
        print('-'*10)
    
    def show_boleto_midder(self):
        print('-'*10)

    def show_boleto_footer(self):
        print('*'*10)

        #Views of Asientos
    def asientos_menu(self):
        print('======================')
        print('-- Submenu Asientos --')
        print('======================')
        print('1. Agregar Asiento')
        print('2. Mostrar Asiento')
        print('3. Mostrar todas los Asientos')
        print('4. Actualizar asiento')
        print('5. Borrar asiento')
        print('6. Regresar')

    def asientos_menu_not_admin(self):
        print('======================')
        print('-- Submenu Asientos --')
        print('======================')
        print('2. Mostrar Asiento')
        print('3. Mostrar todas los Asientos')
        print('6. Regresar')
        
        
    def show_a_asiento(self, record):
        print('ID Asiento: ', record[0])
        print('Disponible: ', record[1])
        print('ID Sala: ', record[2])


    def show_asiento_header(self, header):
        print(header.center(10, '*'))
        print('-'*10)
    
    def show_asiento_midder(self):
        print('-'*10)

    def show_asiento_footer(self):
        print('*'*10)

       #Views of Usuarios
    def usuarios_menu(self):
        print('======================')
        print('-- Submenu Usuarios --')
        print('======================')
        print('1. Agregar Usuario')
        print('2. Mostrar Usuario')
        print('3. Mostrar todas los Usuarios')
        print('4. Actualizar Usuario')
        print('5. Borrar Usuario')
        print('6. Regresar')
        
    def show_a_usuario(self, record):
        print('ID usuario: ', record[0])
        print('Username: ', record[1])
        print('Contraseña: ', record[2])

    def show_usuario_header(self, header):
        print(header.center(10, '*'))
        print('-'*10)
    
    def show_usuario_midder(self):
        print('-'*10)

    def show_usuario_footer(self):
        print('*'*10)
