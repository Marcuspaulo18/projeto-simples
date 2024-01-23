algoritmo "matrix3x3"
var
valores:vetor [1..3,1..3] de inteiro
l,c,totpar:inteiro
inicio
para l <- 1 ate 3 faca
para c<- 1 ate 3 faca
escreval("digite um valor na posição [",l,"],[",c,"]:")
leia(valores[l,c])
fimpara
fimpara
totpar<-0
para l<- 1 ate 3 faca
para c<-  1 ate 3 faca
se ( valores [l,c] % 2=0) entao
escreva ("{",valores [l,c] : 2,"}")
totpar<- totpar + 1
senao
fimse
escreva(valores [l,c]:4)
fimpara
escreval()
fimpara
escreval("ao todo foram", totpar ,"valores pares")
fimalgoritmo
