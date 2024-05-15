create database if not exists test_inf;
use test_inf;

create table usuario(
    id int auto_increment primary key,
    nome varchar(60) not null,
    email varchar(60) not null
);

create table endereco(
    id int auto_increment primary key,
    cep varchar(60) not null,
    endereco varchar(60) not null,
    usuario_id int not null,
    foreign key (usuario_id) references usuario(id)
);

create table entrega(
    id int auto_increment primary key,
    endereco_entrega varchar(60) not null,
    usuario_id int not null,
    foreign key (usuario_id) references usuario(id)
);

