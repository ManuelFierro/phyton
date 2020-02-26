tanque = float(input("Capacidad del tanque : "))
medidor = float(input("Cuanto marca el medidor? : "))
millas = float(input("Millas por galon?: "))

recorrido = tanque*medidor*millas
if recorrido > 200:
    print("seguro, proceder")
else:
    print("Solo puedes recorrer: ", recorrido, " millas, Consigue gas")
               
