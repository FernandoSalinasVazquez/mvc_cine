#comentario
CREATE DATABASE IF NOT EXISTS cine;

USE cine;

#tablas
CREATE TABLE IF NOT EXISTS peliculas(
	id_pelicula INT NOT NULL AUTO_INCREMENT,
    titulo VARCHAR(40) NOT NULL,
    nacionalidad VARCHAR(20) NOT NULL, 
    director varchar(50) NOT NULL,
    clasificacion VARCHAR(3) NOT NULL,
    sinopsis VARCHAR(400) NOT NULL,
    duracion TIME NOT NULL,
    f_estreno date NOT NULL,
    genero VARCHAR(25) NOT NULL,
    PRIMARY KEY(id_pelicula)

)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS salas(
	id_sala INT NOT NULL AUTO_INCREMENT,
    tipo VARCHAR(15) NOT NULL,
    no_asientos INT NOT NULL,
    PRIMARY KEY(id_sala)
)ENGINE=INNODB;

CREATE TABLE IF NOT EXISTS asientos(
	id_asiento INT NOT NULL AUTO_INCREMENT,
    disponible BOOLEAN NOT NULL,
    id_sala INT NOT NULL,
    PRIMARY KEY(id_asiento),
    CONSTRAINT fk_sala_asiento FOREIGN KEY(id_sala)
		REFERENCES salas(id_sala)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE= INNODB;

CREATE TABLE IF NOT EXISTS proyecciones(
	id_proyeccion INT NOT NULL AUTO_INCREMENT,
    hora TIME NOT NULL,
    lenguaje VARCHAR (25) NOT NULL,
    costo FLOAT NOT NULL,
    f_proyeccion DATE NOT NULL,
    id_pelicula INT NOT NULL,
    id_sala INT NOT NULL,
    PRIMARY KEY(id_proyeccion),
    CONSTRAINT fk_pelicula_proyeccion FOREIGN KEY(id_pelicula)
		REFERENCES peliculas(id_pelicula)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fk_sala_proyeccion FOREIGN KEY(id_sala)
		REFERENCES salas(id_sala)
        ON DELETE CASCADE
        ON UPDATE CASCADE
    
)ENGINE= INNODB;

CREATE TABLE IF NOT EXISTS boletos(
	id_boleto INT NOT NULL AUTO_INCREMENT,
    id_proyeccion INT NOT NULL,
    id_asiento INT NOT NULL,
    PRIMARY KEY(id_boleto),
    CONSTRAINT fk_proyeccion_boleto FOREIGN KEY(id_proyeccion)
		REFERENCES proyecciones(id_proyeccion)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fk_asiento_boleto FOREIGN KEY(id_asiento)
		REFERENCES asientos(id_asiento)
        ON DELETE CASCADE,
	CONSTRAINT fk_sala_boleto FOREIGN KEY(id_sala)
		REFERENCES salas(id_sala)
        ON DELETE CASCADE
        ON UPDATE CASCADE    
)ENGINE= INNODB;


CREATE TABLE IF NOT EXISTS users(
	id_user INT NOT NULL AUTO_INCREMENT,
    username VARCHAR(25) NOT NULL,
    contraseña VARCHAR(25) NOT NULL,
    PRIMARY KEY(id_user)
)ENGINE=INNODB;