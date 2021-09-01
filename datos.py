def main(n):
    tamaño_arreglo = (2*n)*2
    i = 0
    j = 1
    h = 2
    #n = int(input)
    lista = []
    while(i < tamaño_arreglo):
        lista.insert(j,"B")
        lista.insert(h,"A")
        i = i + 1
        j = j + 2
        h = h + 2

    print(lista)    

main(3)    
