create database SGRUB;
use SGRUB;

create table registro(
ideregistro bigint primary key not null,
nome varchar(60) not null,
email varchar(60) not null,
senha varchar(60) not null
);

create table registro_empresa(
ideregistro_empresa bigint primary key not null,
nome varchar(60) not null,
numero_cnpj bigint not null,
numero_cep bigint not null
);

create table relatorio(
iderelatorio bigint primary key auto_increment key not null,
categoria varchar(60) not null,
probabilidades varchar(60) not null,
resultado varchar(60) not null

);
alter table registro_empresa drop column numero_cep;
alter table registro modify column ideregistro bigint auto_increment not null;
alter table registro_empresa modify column ideregistro_empresa bigint auto_increment;
alter table relatorio modify column iderelatorio bigint auto_increment;
drop table relatorio;
alter table relatorio add column ideregistro_empresa bigint auto_increment not null;
select distinct registro_empresa.nome,categoria,probabilidades,resultado from relatorio join registro_empresa on registro_empresa.ideregistro_empresa=relatorio.iderelatorio;