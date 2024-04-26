CREATE DATABASE IF NOT EXISTS School;
USE School;

CREATE TABLE STUDENT(
id INT,
first_name VARCHAR(30),
born VARCHAR(10)
);

INSERT INTO STUDENT (id,first_name,born) VALUES(1234,"Marcus","2004");

CREATE TABLE COURSES(
id_course INT,
course_name VARCHAR(30),
Hours_to VARCHAR(10)
);

INSERT INTO COURSES (id_course,course_name,Hours_to) VALUES(12121,"java_coffe_time","400");

CREATE TABLE REGISTRATION(
id_registration INT,
id_aluno VARCHAR(30),
id_course VARCHAR(30),
registration_date VARCHAR(30)
);

INSERT INTO REGISTRATION(id_registration,id_aluno,id_course,registration_date) VALUES(113223,"12122","122000","21221");


TRUNCATE TABLE COURSES;

SELECT * FROM COURSES;

DROP DATABASE school;