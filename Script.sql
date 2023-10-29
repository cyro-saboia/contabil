-- Criando banco de dados
-- CREATE DATABASE contabil;

-- ################
-- #    SCHEMA    #
-- ################

CREATE SCHEMA comum;

-- ################
-- #  SEQUENCES   #
-- ################

CREATE SEQUENCE comum.usuario_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

  -- ################
-- #    TABLES    #
-- ################

CREATE TABLE comum.tb_usuario_usu (
	id_usuario_usu integer NOT NULL DEFAULT nextval('comum.usuario_seq'::regclass),
	txt_nome_usu varchar(200) NOT NULL,
	txt_email_usu varchar(200) NOT NULL,
  txt_cpf_usu varchar(11) NOT NULL,
  txt_password_usu varchar(128) NOT NULL,
	CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario_usu)
);