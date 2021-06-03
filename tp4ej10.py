################
# Matias Scandizzo - @matihkcs
# Plantilla de ejercicio Numero 10 palindromos
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_palindromo(texto):
    texto = texto.replace(" ", " ")
    texto_invertido = texto[::-1]
    if texto ==texto_invertido:
        return "true"
    else:
        return "false"


texto = input("Escribe una palabra: ")
palindromo = es_palindromo(texto)
if palindromo == "true":
    print("es palindromo")
else:
    print("no es palindromo")


if __name__ == "__main__":
    es_palindromo(texto)