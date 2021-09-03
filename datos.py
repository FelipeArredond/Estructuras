def main():
    print("Ingrese un Numero entre 3 y 100")
    n = int(input())
    i = 0
    PosA = 2 * n
    tamaño_arreglo = PosA*2
    lista = []
    while(i < tamaño_arreglo):
        if(i < PosA):
            lista.insert(i, " ")
        elif(i >= PosA):
            if(i%2!=0):
                lista.insert(i, "A")
            elif(i%2==0):
                lista.insert(i, "B")
        i = i + 1
    #Print para verificar que el orden inicial sea el correcto
    print(lista)

    print("Ordenado")

    #Inicia el ordenamiento
    
    i = 0

    while(i <= 0):
        if(i == 0):
            pos_uno = lista[(tamaño_arreglo-2)]
            pos_dos = lista[(tamaño_arreglo-1)]
            #to
            lista[(tamaño_arreglo-1)-1]= " "
            lista[(tamaño_arreglo-1)-2]= " "
            lista[(PosA-2)] = pos_dos
            lista[(PosA-1)] = pos_uno
        i = i + 1
    print(lista)        

main()    