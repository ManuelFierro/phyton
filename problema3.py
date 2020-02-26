plA = float(input("Precio por libra paquete A: "))
pmA = float(input("Porcentaje magro paquete A: "))
plB = float(input("Precio por libra paquete B: "))
pmB = float(input("Porcentaje magro paquete B: "))
costoA =(plA/pmA)
costoB =(plB/pmB)
print("Costo por libra de carne magra en Paquete A: " ,costoA)
print("Costo por libra de carne magra en Paquete B: " ,costoB)

if costoA > costoB:
    print("El paquete B es mejor")
else:
    print("El paquete A es mejor")
               
