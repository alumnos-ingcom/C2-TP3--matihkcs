################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 8
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def ordenar_mayor_a_menor(uno, dos, tres):
    
    if uno > dos and uno > tres:
       return (uno)
    if dos > tres and dos < uno:
        return (dos)
    if tres < dos and tres < uno:
        return (tres)  
  
def ordenar_menor_a_mayor(uno, dos, tres):
    
    
    
    
def prueba():
    
    
    uno = int(input("Ingrese un numero: "))
    dos = int(input("Ingrese el segundo numero: "))
    tres = int(input("Ingrese el tercer numero: "))
    print (f" los numeros de menor a mayor: {ordenar_mayor_a_menor}")




if __name__ == "__main__":
    prueba()