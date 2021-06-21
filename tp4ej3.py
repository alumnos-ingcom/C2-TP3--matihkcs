################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 3 
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrenheit(centigrados):
    """Esta funcion convierte de centigrados a fahrenheit"""
    return ( centigrados * (9/5  + 32))
    
def convertir_a_centigrados(fahrenheit):
    """Esta funcion funcion, calcula de fahrenheit a centigrados
"""
    return ((fahrenheit -32) * 5/9)



def prueba():
    ingreso_centigrados = float(input("Ingrese Grados Centigrados a convertir: "))
    ingreso_fahrenheit = float(input("Ingrese grados fahrenheit a convertir: "))
    
    fahrenheit = convertir_a_fahrenheit(ingreso_centigrados)
    print (f"Los grados fahrenheit son {fahrenheit}: ")
   
   
    centigrados = convertir_a_centigrados(ingreso_fahrenheit)
    print(f"Los grados centrigrados son {centigrados}: ")
    




if __name__ == "__main__":
    prueba()