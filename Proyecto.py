unidades = ["", "uno", "d0os", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
decenas = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta", " sesenta", "setenta", "ochenta", "noventa"]
especiales = {11: "once", 12: "doce", 13: "trece", 14: "catorce", 15: "quince",
              16: "dieciséis", 17: "diecisiete", 18: "dieciocho", 19: "diecinueve"}

numero= int(input("Ingrese un numero entre del 1 al 99: "))
if numero < 10: 
    texto = unidades[numero]
elif 10 < numero < 20: 
    texto = especiales[numero]
elif numero % 10 == 0: 
    texto = decenas[numero // 10]
elif 20 < numero < 30: 
    texto = "veinti" + unidades[numero % 10]
else:
    texto = decenas[numero // 10] + " y " + unidades[numero % 10]
print(f"El número {numero} en texto es: {texto}")