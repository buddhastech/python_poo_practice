a = 5
b = 10
c = 3

def ecuaciones(a, b, c):
    sumatoria = 0
    while True:
        x = int(input("Ingrese el valor de x: "))
        if x == 0:
            print(sumatoria)
            break
        else:
            y = a * x + b * x + c
            sumatoria += y


ecuaciones(a,b,c)
