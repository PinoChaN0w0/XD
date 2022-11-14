"""def sumar(): #Sin parametro
    n1 =1 
    n2 =2
    res = n1+n2
    print(f"el resultado es{res}")"""
"""def operar(n1,n2,operar):   #con parametro y sin retorno
    if(operar =="+"):
        res = n1+n2
    elif(operar =="-"):
        res = n1+n2
    return res 
    
    

n1=int(input("Ingrese valor 1: "))
n2=int(input("Ingrese valor 2: "))
operadoor =input("Ingrese operacion: ")

print(operar(n1,n2,operar)*2)"""


def resta (a, b):
    return a-b
resta(30, 10)

def calculo(precio, desc):
    return precio - (precio + desc/100)
datos =[10000,10]
print("el monto dinal a pagar:", calculo(*datos))

#Calculo del IVA

print("Bienvenido al programa mas raro de la historia.")
print("1. Calculo  del IVA")
print("2. Descuento el program")
print("3. Calculo  del IMC")
opc=int()


      