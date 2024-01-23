algoritmo "tabuada"
var
contador,N,R:inteiro
inicio
contador<-1
escreva("quer ver a tabuada de qual numero? ")
leia(N)
repita
R<- N * contador
escreval(N," x", contador ," =", R)
contador<-contador+1
ate(contador>10)
fimalgoritmo
