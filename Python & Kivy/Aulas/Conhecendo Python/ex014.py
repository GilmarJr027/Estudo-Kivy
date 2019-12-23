"""
14) Faça um algoritmo que solicite ao usuário informar
o valor de uma compra. Em seguida, aplique 10% de desconto
e imprima na tela tanto
o valor total e também o valor com o desconto aplicado.

"""


compra_bruta = float(input('Informe o valor total da compra R$:'))

desconto = 10 / 100

desconto_text = 10

desconto_compra = (compra_bruta * desconto) 

compra_liquida = (compra_bruta - desconto_compra)

print('Compra valor Bruto R${}\nDesconto concedido {}%\nValor do Desconto'
' R${}\nTotal da Compra R$ {}'.format(compra_bruta, desconto_text, desconto_compra, compra_liquida))




