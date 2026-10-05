print("CALCULADORA BASICA")
a = float(input("Primer numero: "))
b = float(input("Segundo numero: "))
op = input("Operacion (+, -, *, /): ")

if op == "+":
    print("Resultado:", a + b)
elif op == "-":
    print("Resultado:", a - b)
elif op == "*":
    print("Resultado:", a * b)
elif op == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("Operacion no valida")
