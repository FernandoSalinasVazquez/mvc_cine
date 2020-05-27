from mysql import connector

class Model:
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db =self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d={}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx= connector.connect(**self.config_db)
        self.cursor =self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    def create_salas(self, tipo, no_asientos):
        try:
            sql = 'INSERT INTO salas (`tipo`,`no_asientos`) VALUES (%s, %s)'
            vals =(tipo, no_asientos)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_sala(self, id_sala):
        try:
            sql = 'SELECT * FROM salas WHERE id_sala = %s'
            vals = (id_sala, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_salas(self):
        try:
            sql = 'SELECT * FROM salas'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def update_sala(self, fields, vals):
        try:
            sql = 'UPDATE salas SET '+','.join(fields)+' WHERE id_sala= %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_sala(self, id_sala):
        try:
            sql = 'DELETE FROM salas WHERE id_sala=%s'
            vals = (id_sala,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    ##Metodos de Peliculas

    def create_pelicula(self, titulo, nacionalidad, director, clasificacion, sinopsis, duracion, f_estreno, genero):
        try:
            sql = 'INSERT INTO peliculas (`titulo`,`nacionalidad`,`director`, `clasificacion`, `sinopsis`, `duracion`, `f_estreno`,`genero`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            vals =(titulo, nacionalidad, director, clasificacion, sinopsis, duracion, f_estreno, genero)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_pelicula(self, id_pelicula):
        try:
            sql = 'SELECT * FROM peliculas WHERE id_pelicula = %s'
            vals = (id_pelicula, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_peliculas(self):
        try:
            sql = 'SELECT * FROM peliculas'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def read_peliculas_genero(self, genero):
        try:
            sql = 'SELECT * FROM peliculas WHERE genero = %s'
            vals = (genero, )
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def read_peliculas_director(self, director):
        try:
            sql = 'SELECT * FROM peliculas WHERE director = %s'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err
    
    def update_pelicula(self, fields, vals):
        try:
            sql = 'UPDATE peliculas SET '+','.join(fields)+' WHERE id_pelicula= %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_pelicula(self, id_pelicula):
        try:
            sql = 'DELETE FROM peliculas WHERE id_pelicula=%s'
            vals = (id_pelicula,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    

    #Metodos para Asientos

    def create_asiento(self, disponible, id_sala):
        try:
            sql = 'INSERT INTO asientos (`disponible`,`id_sala`) VALUES (%s, %s)'
            vals =(disponible, id_sala)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_asiento(self, id_asiento):
        try:
            sql = 'SELECT asientos.*, id_sala FROM asientos JOIN salas ON salas.id_sala =asientos.id_sala AND asientos.id_asiento=%s'
            vals = (id_asiento, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err

    def read_asientos(self):
        try:
            sql = 'SELECT asientos.*, id_sala FROM asientos JOIN salas ON salas.id_sala =asientos.id_sala'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_asiento(self, fields, vals):
        try:
            sql = 'UPDATE asientos SET '+','.join(fields)+' WHERE id_asiento= %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_asiento(self, id_asiento):
        try:
            sql = 'DELETE FROM asientos WHERE id_asiento=%s'
            vals = (id_asiento,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodos Proyeccion

    def create_proyeccion(self, hora, lenguaje, costo, f_proyeccion, id_pelicula, id_sala):
        try:
            sql = 'INSERT INTO proyecciones (`hora`,`lenguaje`, `costo`, `f_proyeccion`, `id_pelicula`, `id_sala`) VALUES (%s, %s, %s, %s, %s, %s)'
            vals =(hora, lenguaje, costo, f_proyeccion, id_pelicula, id_sala)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_proyeccion(self, id_proyeccion):
        try:
            sql = 'SELECT peliculas.titulo, peliculas.clasificacion, proyecciones.hora, proyecciones.lenguaje, proyecciones.costo, proyecciones.f_proyeccion, salas.id_sala FROM proyecciones JOIN peliculas JOIN salas ON salas.id_sala=proyecciones.id_sala AND proyecciones.id_pelicula=peliculas.id_pelicula AND proyecciones.id_proyeccion=%s'
            vals = (id_proyeccion, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err
 
    def read_proyecciones(self):
        try:
            sql = 'SELECT peliculas.titulo, peliculas.clasificacion, proyecciones.hora, proyecciones.lenguaje, proyecciones.costo, proyecciones.f_proyeccion, salas.id_sala FROM proyecciones JOIN peliculas JOIN salas ON salas.id_sala=proyecciones.id_sala AND proyecciones.id_pelicula=peliculas.id_pelicula'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_proyeccion(self, fields, vals):
        try:
            sql = 'UPDATE proyecciones SET '+','.join(fields)+' WHERE id_proyeccion= %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_proyeccion(self, id_proyeccion):
        try:
            sql = 'DELETE FROM proyecciones WHERE id_proyeccion=%s'
            vals = (id_proyeccion,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Metodos boleto

    def create_boleto(self, id_proyeccion, id_asiento, id_sala):
        try:
            sql = 'INSERT INTO boletos ( `id_proyeccion`, `id_asiento`, `id_sala`) VALUES (%s, %s, %s)'
            vals =(id_proyeccion, id_asiento, id_sala)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_boleto(self, id_boleto):
        try:
            sql = 'SELECT peliculas.titulo, salas.id_sala, asientos.id_asiento, boletos.id_boleto FROM boletos JOIN proyecciones JOIN salas JOIN asientos ON salas.id_sala=boletos.id_sala AND proyecciones.id_proyeccion= boletos.id_proyeccion AND asientos.id_asiento= boletos.id_asiento AND boletos.id_boleto=%s'
            vals = (id_boleto, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err
 
    def read_boletos(self):
        try:
            sql = 'SELECT peliculas.titulo, salas.id_sala, asientos.id_asiento, boletos.id_boleto FROM boletos JOIN proyecciones JOIN salas JOIN asientos ON salas.id_sala=boletos.id_sala AND proyecciones.id_proyeccion= boletos.id_proyeccion AND asientos.id_asiento= boletos.id_asiento'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_boleto(self, fields, vals):
        try:
            sql = 'UPDATE boletos SET '+','.join(fields)+' WHERE id_boleto= %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_boleto(self, id_boleto):
        try:
            sql = 'DELETE FROM boletos WHERE id_boleto=%s'
            vals = (id_boleto,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

        
    #Metodos Usuarios

    def create_user(self, username, contraseña):
        try:
            sql = 'INSERT INTO users (`username`,`contraseña`) VALUES (%s, %s)'
            vals =(username, contraseña)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_user(self, id_user):
        try:
            sql = 'SELECT * FROM users WHERE id_user = %s'
            vals = (id_user, )
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchone()
            return records
        except connector.Error as err:
            return err
        
    def comprobacion_usuario(self, usuario, contraseña):
        try:
            sql = 'SELECT * FROM users WHERE username = %s AND contraseña = %s'
            vals = (usuario, contraseña)
            self.cursor.execute(sql, vals)
            if self.cursor.fetchall():
                print('Usuario Correcto')
                return True
            else:
                print('Usuario/contraseña incorrecto')
                return False
        except connector.Error as err:
            return err


    def read_users(self):
        try:
            sql = 'SELECT * FROM users'
            self.cursor.execute(sql)
            record = self.cursor.fetchall()
            return record
        except connector.Error as err:
            return err

    def update_user(self, fields, vals):
        try:
            sql = 'UPDATE users SET '+','.join(fields)+' WHERE id_user= %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_user(self, id_user):
        try:
            sql = 'DELETE FROM users WHERE id_user=%s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
