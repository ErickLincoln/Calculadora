from turtle import ycor
from funções import*



while True:
    print('\nIniciando...')
    print('\nSelecione a Operação')
    print('1.Somar?')
    print('2.Subtrair?')
    print('3.Multiplicar?')
    print('4.Dividir?')
    print('5.N ao Cubo?')
    print('6.Raiz?')

    escolha = (input('Insira sua escolha:'))
    if escolha in ('1', '2', '3', '4'):
        x = float(input("insira o primeiro numero: "))
        y = float(input("Insira o segundo numero: "))

        if escolha == '1':
            print('Somando ', x, 'mais', y)
            print(x, "+", y, "=", add(x, y))

        elif escolha == '2':
            print('Subtraindo ', x, 'e', y)
            print(x, "-", y, "=", subst(x, y))

        elif escolha == '3':
            print('Multiplicando ', x, 'e', y)
            print(x, "*", y, "=", multpl(x, y))

        elif escolha == '4':
            try:
                print('Dividindo ', x, 'e', y)
                print(x, "/", y, "=", divid(x, y))
            except ZeroDivisionError:
                print("Não pode dividir por zero")

    elif escolha in ('5', '6'):
        x = float(input("insira o numero: "))
        
        if escolha == '5':
            print('Elevando ', x, 'ao Cubo')
            print(x, "*", x, "=", cubo(x))

        elif escolha == '6':
            print("A raiz de ", x, "é", sqrt(x))
        
        Calcular_de_novo = input("Outro cálculo? (S/N): ")
        if Calcular_de_novo == "N":
          break
    
    else:
        print("Tente novamente...")

if __name__ == '__calculator__':
        app.run(debug= True)