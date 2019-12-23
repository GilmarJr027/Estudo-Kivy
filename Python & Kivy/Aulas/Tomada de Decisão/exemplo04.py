num1 = input('Digite um número:')
num1 = int(num1)

num2 = input('Digite outro número:')
num2 = int(num2)

if(num1 == num2):
    print('o número {} é igual ao número {} '.format(num1, num2))
if(num1 != num2):
    print('O número {} é diferente do número {}'.format(num1, num2))
if(num1 < num2):
    print('O número {} é menor que o número {}'.format(num1, num2))
if(num1 > num2):
    print('O número {} é maior que o número {}'.format(num1, num2))
if(num1 >= num2):
    print('O número {} é maior ou igual ao número {}'.format(num1,num2))
if(num1 <= num2):
    print('O número {} é menor ou igual ao número {}'.format(num1, num2))
