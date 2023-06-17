-- Creacion de la base de datos
CREATE DATABASE fast_api_rest;

\c fast_api_rest

CREATE TABLE usuarios (
	usuario_id SERIAL,
	nombre CHARACTER VARYING(30),
	usuario CHARACTER VARYING(30),
	password CHARACTER VARYING(100),
	telefono CHARACTER VARYING(30),


	CONSTRAINT pk_usuario_id PRIMARY KEY(usuario_id)
);


CREATE VIEW vista_usuarios AS
SELECT 
	usuario_id, 
	nombre, 
	usuario, 
	password, 
	telefono
FROM usuarios;


CREATE OR REPLACE FUNCTION usuarios (
	_usuario_id INT,
	_nombre CHARACTER VARYING,
	_usuario CHARACTER VARYING,
	_password CHARACTER VARYING,
	_telefono CHARACTER VARYING
) RETURNS VOID AS
$BODY$
	BEGIN
		INSERT INTO usuarios (usuario_id, nombre, usuario, password, telefono)
		VALUES (_usuario_id, _nombre, _usuario, _password, _telefono);
	END;
$BODY$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION obtener_usuario (
	_usuario_id INT
) RETURNS SETOF usuarios AS
$BODY$
	BEGIN
		RETURN QUERY SELECT * FROM usuarios WHERE usuarios.usuario_id=_usuario_id;
	END;
$BODY$
LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION eliminar_usuario(
	_usuario_id INT
) RETURNS VOID AS
$BODY$

	BEGIN
		DELETE FROM usuarios WHERE usuarios.usuario_id=_usuario_id;
	END;
$BODY$
LANGUAGE plpgsql
