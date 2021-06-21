################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 4 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara(numero, otro_numero):
    """ Esta funcion compara los 3 numeros ingresados
"""
    if numero<otro_numero:
        return (-1)
    if numero>otro_numero:
        return (1)
    elif numero == otro_numero:
        return (0)
    

def prueba():
    
    numero = int(input("Ingrese un numero a comparar :"))
    otro_numero = int(input("Ingrese otro numero a comparar: "))
    print(f"La comparacion de los numeros es: {compara(numero, otro_numero)}")
    
    
if __name__ == "__main__":
    prueba()