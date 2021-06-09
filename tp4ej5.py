################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 1
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    """ Esta funcion analiza si el numero es: positivo, negativo o 0.
"""
    
    if numero > 0:
        return ("El numero es positivo")
    
    
    elif numero < 0:
        return ("El numero es negativo")
    
    else:
        return ("El numero ingresado es 0")
    
    
    
def prueba():
    
    numero = int(input("Ingrese un numero: "))
    
    print(f" el resultado es: {signo(numero)}")
    
    




if __name__ == "__main__":
    prueba()