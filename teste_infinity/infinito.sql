create database infinito;
use infinito;
create table cadastro(
cadastro_id int auto_increment primary key not null,
cadastro_usuario varchar(60) not null,
cadastro_email varchar(60) not null,
cadastro_senha varchar(60) not null
);

create table login(
login_id int auto_increment primary key not null,
login_usuario varchar(60) not null,
login_senha varchar(60) not null

); 

create table endereco(
endereco_id int auto_increment primary key not null,
endereco_primogenito varchar(60)not null,
endereco_cep varchar(60)not null,
endereco_pedido varchar(60)not null


); 

create table pedido(
pedido_id int auto_increment primary key not null,
pedido_cep varchar(60)not null,
pedido_endereco varchar(60)not null


); 