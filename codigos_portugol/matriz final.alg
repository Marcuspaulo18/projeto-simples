algoritmo "semnome"
var
m:vetor [1..4,1..4] de inteiro
c,l,SDP,p2l,MM3:inteiro
inicio
SDP<-0
P2L<-1
para c<- 1 ate 4 faca
para l<- 1 ate 4 faca
escreval("digite o valor desejado na posição [",c,"],[",l,"]:")
leia(m[c,l])
se(l = c) entao
SDP<- SDP+ m[c,l]
fimse
fimpara
fimpara

para c<- 1 ate 4 faca
para l<- 1 ate 4 faca
escreva(m[c,l]:3)
fimpara
escreval()
fimpara

para c<- 1 ate 4 faca
p2l<- p2l * m[2,c]
fimpara
para L<- 1 ate 4 faca
se (m[3,l] > MM3) entao
mm3<- m[3,l]
fimse
fimpara
escreval("a soma da diagonal principal é",SDP)
escreval("o produto da segunda linha é",p2l)
escreval("o maior valor da terceira linha é",mm3)
fimalgoritmo
