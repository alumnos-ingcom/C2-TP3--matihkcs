################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 9 Numeros primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def es_primo(numero):
    
    contador = 0
    
    for num in range(numero):
        if numero % (num+1) != 0:
            continue
        else:
            contador +=1
    if contador == 2:
        return True
    else:
        return False
            
def prueba():

    numero = int(input("escribe un numero: "))
    if es_primo(numero):
        print("es primo")
    else:
        print("no es primo")
    
        
if __name__ == "__main__":
    prueba()