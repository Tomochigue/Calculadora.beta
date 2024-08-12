def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x / y

def menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    

def calculadora():
    while True:
        menu()
        escolha = input("Digite sua escolha (1/2/3/4) ou 'q' para sair: ")

        if escolha == 'q':
            print("Saindo...")
            break

        if escolha in ['1', '2','3','4']:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == '1':
                print(f"Resultado: {num1} + {num2} = {adicao(num1, num2)}")
            elif escolha == '2':
                print(f"Resultado: {num1} - {num2} = {subtracao(num1, num2)}")
            elif escolha == '3':
                print(f"Resultado: {num1} * {num2} = {multiplicacao(num1, num2)}")
            elif escolha == '4':
                print(f"Resultado: {num1} / {num2} = {divisao(num1, num2)}")
        else:
            print("Entrada invalida, por favor tente novamente.")

# Executar a calculadora
calculadora()