def loop():
    print("Ingrese un numero")
    i = 0
    n = int(input())
    while(i <= n):
        print(i)
        i = i + 1  


#Suma Pares

def sumpar(nums):
   suma = 0
   for i in range(len(nums)):
       if(nums[i]%2 == 0):
           suma += nums[i]
   print(suma)

sumpar([1,2,3,4,5,6,7,8])          