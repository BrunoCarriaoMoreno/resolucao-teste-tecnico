numero = int(input('Insira um número: '))

fibonacci =[0, 1]

while True:

    proximo_numero = fibonacci[-1] + fibonacci [-2]
    if proximo_numero > numero:
        break

    fibonacci.append(proximo_numero)
    

if numero in fibonacci:
    print('o número pertence a sequência!')

else: 
    print('o número não pertence a sequência!')
        




