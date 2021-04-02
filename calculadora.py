contador = 0
def menu():
    global contador
    operador = str(input("+, -, *, /, 5(sair): \n"))
    if operador == "5":
        return
    nro = float(input("Digite um numero: \n"))
    if operador == "+":
        contador = contador + nro
        print(contador)
        menu()
    elif operador == "-":
        contador = contador - nro
        print(contador)
        menu()
    elif operador == "*":
        contador = contador * nro
        print(contador)
        menu()
    elif operador == "/":
        contador = contador/nro
        print(contador)
        menu()    
    else:
        print("Formato inválido!")
menu()

print("Até a próxima!")
