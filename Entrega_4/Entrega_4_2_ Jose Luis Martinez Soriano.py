### JOSE LUIS MARTÍNEZ SORIANO ENTREGA 4.2

lista_paraprimos=[1,3,4,8,5,5,22,13,97,101,244,123,87,22,14,77]

def primos(num):
    contador = 0
    for i in range(2,num):
        if num % i == 0:
            contador += 1
    if contador ==0:
        return num
        

primos_lista=filter(primos,lista_paraprimos)
print(list(primos_lista))
