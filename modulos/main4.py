import conversor
print("----------CONVERSOR RPX 50-----------")
print("bem vindo ao conversor rpx 50, aqui você pode converter as unidades de medida,pes,metro,kg,libras,celsius ou fahrenheit")
print("para sair do programa digite 0")
print("para converter de metros para pes digite 1")
print("para converter de pes para metros digite -1")
print("para converter de kg para libra digite 2")
print("para converter de libras para kg digite -2")
print("para converter de celsius para fahrenheit digite 3")
print("para converter de fahrenheit para celsius digite -3")
valor=float(input("digite o valor:"))
while(True):
    print("para sair do programa digite 0")
    print("para converter de metros para pes digite 1")
    print("para converter de pes para metros digite -1")
    print("para converter de kg para libra digite 2")
    print("para converter de libras para kg digite -2")
    print("para converter de celsius para fahrenheit digite 3")
    print("para converter de fahrenheit para celsius digite -3")
    variavel=int(input("digite um entre -3,-2,-1,0,1,2 ou 3 para prosseguir"))
    match variavel:
        case 0:
            print("até mais...")
            break
        case 1:
            print(conversor.me_pe(valor))
        case 2:
            print(conversor.kli(valor))
        case 3:
            print(conversor.cel_fah(valor))
        case -1:
               print(conversor.pe_me(valor))
        case -2:
              print(conversor.lik(valor))
        case -3:
              print(conversor.fah_cel(valor))
