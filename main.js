import express from "express"
import rotas from "./roteador/rotas.js"
import cors from "cors"

const app=express();
app.use(express.json())
app.use(cors())

app.use("/",rotas)
app.listen(9000)
