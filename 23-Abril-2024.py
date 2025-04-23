def conteo(n):
    if n < 0:
        print('Despliegue')
    else:
        print(n)
        conteo(n-1)
conteo(4)