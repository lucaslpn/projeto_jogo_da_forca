from time import sleep


def tela_inicial():
    print('''
=========================================
'            JOGO                       '
'                 DA                    '
'                    FORCA              '
=========================================
''')

    
def main():
    
    tela_inicial() # tela inical do game

    letras_user = []
    palavra = 'TECLADO'
    tentativas = 5
    ganhou = False

    while tentativas != 0:
       
        for letra in palavra:
            if letra in letras_user:
                print(letra, end=' ')
            else:
                print('_', end=' ')
        
        print()
        print()
        
        escolha = str(input('Insira uma letra : ')).upper() 
        letras_user.append(escolha)
        
        
        if escolha.upper() not in palavra.upper():
            tentativas -= 1
        
        print(f'Você ainda tem {tentativas} chances.')

    
main()





