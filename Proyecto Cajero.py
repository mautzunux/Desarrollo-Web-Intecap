saldo= 3000
intentos= 0

while saldo > 0:
    print("Saldo Q:", saldo)
    retiro= input("Ingrese la cantidad que desea retirar o 0 para salir: ")
    if retiro == "0": 
        print("Adiós")
        break
    if not retiro.isdigit():
        print("Ingrese una cantidad valida")
        continue
    monto= int(retiro)
    if monto > saldo:
        intentos += 1 
        print("Saldo insuficiente.", intentos, "de 3")
        if intentos == 3:
            print("Cajero bloqueado")
            break 
    elif monto == saldo:
        print("Has retirado todo tu dinero, Adios")
        break
    else: 
        saldo -= monto
        print("Retiro exitoso")
        if saldo == 0:
            print("Tu saldo es 0")        