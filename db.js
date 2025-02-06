import mysql from "mysql"

export const db= mysql.createConnection({
    host:"localhost",
    user:"root",
    password:"Mpso_7890@",
    database:"contato"
})