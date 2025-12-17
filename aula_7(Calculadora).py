# calculadora com funções básicas  + - / * 

def somar(a,b):
    print(a + b)

def div(a , b):
    print(a/b)

def sub(a, b):
    print(a - b)

def mult(a, b):
    print(a*b)       


def calculadora():

    while True: 
        n1 =  float(input('='))
        op =  input('escolha a operação')

        if op  == '+':
            n2 = float(input('='))
            somar(n1, n2)
        elif  op =='-':
            n2 = float(input('='))
            sub(n1, n2)
        elif op == '*':
            n2 = float(input('='))
            mult(n1, n2)
        elif op == '/':
            n2 = float(input('='))
            div(n1, n2)
        else:
            print('Digite algo válido')    

calculadora() 