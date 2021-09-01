def main(n):
    PosA = 2*n
    tamaño_arreglo = PosA*2
    i = 0
    j = PosA
    h = PosA + 1
    lista = []
    while(i < tamaño_arreglo):
        if(i <= tamaño_arreglo/2 ):
            lista.append(" ")
        elif(i > tamaño_arreglo/2 ):
           lista.insert(j,"B")
           lista.insert(h,"A")
           j = j + 2
           h = h + 2
        i = 0 + 1       
    print(lista)    

main(4)   