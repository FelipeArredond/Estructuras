def main(n):
    
    if(n==4):
        print("6 to -1")
        print("3 to 6")
        print("0 to 3")
        print("7 to 0")
        return n
    
    if(n == 5):
        print("8 to -1")
        print("3 to 8")
        print("6 to 3")
        print("0 to 6")
        print("9 to 0")
        return n

    if(n == 6):
        print("10 to -1")
        print("7 to 10")
        print("2 to 7")
        print("2 to 7")
        print("6 to 2")
        print("0 to 6")
        print("11 to 0")
        return n 

    if(n == 7):
        print("8 to -1")
        print("5 to 8")
        print("12 to 5")
        print("3 to 12")
        print("9 to 3")
        print("0 to 9")
        print("13 to 0")
        return n

    else:
        print("From " + str(((2*n)-2)) + " to -1")
        print("3 to " + str((2*n)-2))
        main(n-4)
        print("0 to " + str(((2*n)-5)))
        print(str(((2*n)-1)) + " to 0")
        
            
        

main(10)    