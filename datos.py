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

    while(i <= n):
        #Movimiento 1
        if(i == 0):
            pos_uno = lista[tamaño_arreglo-2]
            pos_dos = lista[tamaño_arreglo-1]
            #to
            lista[tamaño_arreglo-3]= " "
            lista[tamaño_arreglo-2]= " "
            lista[(PosA-2)] = pos_dos
            lista[(PosA-1)] = pos_uno  
        #Movimiento 2
        if(i==1):
            pos_uno = lista[12]
            pos_dos = lista[13]
            #to
            lista[12] = " "
            lista[13] = " "
            lista[17] = pos_uno
            lista[18] = pos_dos
        #Movimiento 3 
        if(i==3):
            pos_uno =  lista[15]
            pos_dos = lista[16]
            #to
            lista[15] = " "
            lista[16] = " "
            lista[12] = pos_uno   
            lista[13] = pos_dos
        #Movimiento 4
        if(i == 4):
            pos_uno = lista[9]
            pos_dos = lista[10]
            #to
            lista[9] = " "
            lista[10] = " "
            lista[15] = pos_uno
            lista[16] = pos_dos

        #Movimiento 5
        if(i == 5):
            pos_uno = lista[18]
            pos_dos = lista[19]
            #to
            lista[18] = " "
            lista[19] = " "
            lista[9] = pos_uno
            lista[10] = pos_dos    


        #INCREMENTO
        i  = i + 1    

    print(lista)        

main()    