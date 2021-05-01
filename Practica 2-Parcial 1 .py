'''Practica de como calcular si paga renta'''

cliente = input("Ingrese el nombre del cliente: ")
totalIngresos = int(input("Ingrese el monto total de ingresos: "))
deducibleImpuestos = int(input("Ingrese el monto total de gastos deducibles de impuesto: "))
rentaGravable = totalIngresos - deducibleImpuestos
if rentaGravable <= 31043000:
    impuesto10 = rentaGravable * 0.10
    ingresos = rentaGravable - impuesto10
    print("El cliente ",cliente," con monto de renta gravable: ",rentaGravable," deberá pagar un total de impuestos: ", impuesto10," dejando así un ingreso de: ",ingresos)
elif rentaGravable > 31043000 and rentaGravable <= 62444000:
    impuesto10 = 31043000 * 0.10
    residuoRentaGravable = rentaGravable - 31043000
    impuesto20 = residuoRentaGravable * 0.20
    impuestoCombinado = impuesto10 + impuesto20
    ingresos = rentaGravable - impuestoCombinado
    print("El cliente ",cliente," con monto de renta gravable: ",rentaGravable," deberá pagar un total de impuestos: ", impuestoCombinado," dejando así un ingreso de: ",ingresos)
else:
    residuoRentaGravable30 = rentaGravable - 62444000
    residuoRentaGravable20 = rentaGravable - residuoRentaGravable30
    impuesto10 = 31043000 * 0.10
    impuesto20 = residuoRentaGravable20 * 0.20
    impuesto30 = residuoRentaGravable30 * 0.30
    impuestoCombinado = impuesto10 + impuesto20 + impuesto30
    ingresos = rentaGravable - impuestoCombinado
    print("El cliente ",cliente," con monto de renta gravable: ",rentaGravable," deberá pagar un total de impuestos: ", impuestoCombinado," dejando así un ingreso de: ",ingresos)
