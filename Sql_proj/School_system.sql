create database School_System;
use School_system;

create table aluno(
matricula int,
nome varchar(60),
idade int,
endereço varchar(60)
);

create table turma(
id_turma int,
horario varchar(60),
semana varchar(60)
);

create table professores(
id_matricula int,
nome varchar(60),
especialidade varchar(60),
endereço varchar(60)
);
create table disciplina(
id_disciplina int,
nome varchar(60),
quant int
);
insert into turma values(12,"7:30","ter,qui,sex,sab");
insert into aluno values(140604,"marcus paulo",20,"caminho das arvores");
insert into professores values(12122,"xavier","furacão romeno","para");
insert into disciplina values(12122,"poledance",1);
select * from aluno;