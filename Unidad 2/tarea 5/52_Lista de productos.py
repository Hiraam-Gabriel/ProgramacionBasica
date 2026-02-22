print('******reporte de venta******')
lista=[
    ["chocolate",15.0,30], 
    ["Coca Cola", 20.0, 10], 
    ["papas fritas",26.0,13],
    ["chcles",10.0,6],
    ["leche",30.0,20]
    ]

print(f"{'producto':<15} {'precio ($)':<12} {'cantidad':<10}")
print("-"*40)
for fila in lista:   
    print (f"{fila[0]:<15} {fila[1]:<12} {fila[2]:<10}")