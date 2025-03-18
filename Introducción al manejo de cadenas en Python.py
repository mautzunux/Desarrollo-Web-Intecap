# 1.	Escribe un programa que extraiga la primera y la última palabra de una oración. Split()
print("Escribe un programa que extraiga la primera y la última palabra de una oración. Split")

texto="Python es un lenguaje poderoso y versátil"
print(texto)
palabras= texto.split()
primera= palabras[0]
ultima= palabras[6]
print("Primera palabra: ", primera)
print("Ultima palabra: ", ultima)

print("2.	Crea un programa que elimine los espacios repetidos en una cadena")
texto="Hola     mundo     en Python"
print(texto)
palabras=texto.split()
corregido=" ".join(palabras)
print(corregido)

print("3.	Dado un correo electrónico, extrae solo el dominio.")

correo="usuario@gmail.com"
print(correo)
partes= correo.split("@")
dominio= partes[1]
print("El dominio del correo es: ", dominio)

print("4.	Dado un nombre de archivo, verifica si tiene la extensión correcta (ej. .pdf).")

archivo= "documento.pdf"
print(archivo)
if archivo.endswith(".pdf"): 
    print("Si termina en .pdf")
else: 
    print("No termina en .pdf")