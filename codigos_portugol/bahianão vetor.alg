algoritmo "semnome"
var
i,c:inteiro
time:vetor [1..3] de caractere
inicio
escreval("---------------------")
escreval("CAMPEONATO DE FUTEBOL")
escreval("---------------------")
para c<- 1 ate 3 faca
   escreval("digite o",c,"o. time:")
   leia(time[c])
fimpara
limpatela
escreval("---------------------")
escreval("   TABELA DE JOGOS   ")
escreval("---------------------")
para i <- 1 ate 3 faca
   para c <- 1 ate 3 faca
      se (i <> c) entao
         escreval(time[i]:12,"[] X []",time[c]:12)
      fimse
   fimpara
fimpara
fimalgoritmo
