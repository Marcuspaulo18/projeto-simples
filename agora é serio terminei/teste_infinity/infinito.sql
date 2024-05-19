create database infinito;
use infinito;
create table cadastro(
cadastro_id int auto_increment primary key not null,
cadastro_usuario varchar(60) not null,
cadastro_email varchar(60) not null,
 cadastro_senha varchar(60) not null, 
 cadastro_cep varchar(60) not null,
 cadastro_endereco varchar(60) not null
);
create table logins(
login_id int auto_increment primary key not null,
login_email varchar(60) not null,
login_senha varchar(60) not null

);
create table entrega(
entrega_id int auto_increment primary key not null,
distan varchar(60)not null,
temp varchar(60)not null
);
