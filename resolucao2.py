palavra = str(input('Digite uma palavra: '))

quantidade_a = palavra.count("a")
quantidade_A = palavra.count("A")

def verificar_palavra(palavra):

    if "a" in palavra:
        
        print('A letra "a" está presente na string!')

        if "a" .islower():
            print(f'A letra "a" minúscula aparece {quantidade_a} vezes!')
        else:
            print('A string não possui letras "a" minúsculas')

    if "A" in palavra:

        if "A" .isupper():
            print(f'A letra "a" maiúscula aparece {quantidade_A} vezes!')
        
        else:
            print('A string não possui letras "a" maiúsculas!')

    else:
        print('A letra "a" não está presente na string!')

if palavra != None:
    verificar_palavra(palavra)
      
else:
    print('não foi possível verificar a string')
