import random

numero = random.randint(1,2)
chute  =  int(input('Numero chute: '))

if numero == chute:
    print('Acertou em cheio! o numero é', numero)
elif (numero - chute) == 1  or   (numero - chute) == -1:
    print('Quase... o numero é', numero)
else:
    print('Errou feio o numero é' , numero)