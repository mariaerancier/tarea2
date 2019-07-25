cadena=input("Escriba un string: ")
diccionario={}
for letra in cadena:
    if letra not in diccionario:
        diccionario[letra]=cadena.count(letra)
print(diccionario)
