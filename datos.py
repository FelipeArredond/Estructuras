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

main()    