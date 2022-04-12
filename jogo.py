from random import randint
from time import sleep
import os

tabela = [['','',''],
          ['','',''],
          ['','','']]

def jogo_da_velha(tabela):

    jogador = ''
    pc = ''
    contador = 0

    while True:

        contador = 0

        print('{:>5}{:>5}{:>5}'.format('0','1','2'))
        print('0: {:>2}{:>5}{:>5}'.format(tabela[0][0],tabela[0][1],tabela[0][2]))
        print('1: {:>2}{:>5}{:>5}'.format(tabela[1][0],tabela[1][1],tabela[1][2]))
        print('2: {:>2}{:>5}{:>5}'.format(tabela[2][0],tabela[2][1],tabela[2][2]))
        print('-'*20)

#jogador------------------------------------------------------------------------------

        opc1 = input('Digite a linha: ')

        while opc1 not in '0,1,2':
            print('digite somente 0, 1 ou 2: ')
            opc1 = input('Digite a linha: ')
            if opc1 in '0,1,2':
                    break

        opc2 = input('Digite a coluna: ')
        
        while opc2 not in '0,1,2':
            print('digite somente 0, 1 ou 2: ')
            opc2 = input('Digite a coluna: ')
            if opc2 in '0,1,2':
                    break

        linha = int(opc1)
        coluna = int(opc2)


        if tabela[linha][coluna] == '':

            tabela[linha][coluna] = 'X'

        else:
            print('já foi marcado!')
        
        for pos in range(3):

            if tabela[pos][0] == 'X' and  tabela[pos][1] == 'X' and  tabela[pos][2] == 'X':
                jogador = 'venceu'
                print('jogador X ganhou!')
                sleep(3)
                break
                
                
        for pos in range(3):

            if tabela[0][pos] == 'X' and  tabela[1][pos] == 'X' and  tabela[2][pos] == 'X':
                jogador = 'venceu'
                print('jogador X ganhou!')
                sleep(3)
                break
                
        
        if tabela[0][0] == 'X'and tabela[1][1] == 'X' and tabela[2][2] == 'X':
                jogador = 'venceu'
                print('jogador X ganhou!')
                sleep(3)
                break
                

        elif tabela[2][0] == 'X'and tabela[1][1] == 'X' and tabela[0][2] == 'X':
                jogador = 'venceu'
                print('jogador X ganhou!')
                sleep(3)
                break
#velha---------------------------------------------------------------------------------             

        for c in range(3):
            if tabela[0][c] != '':
                contador += 1

            if tabela[1][c] != '':
                contador += 1
            
            if tabela[2][c] != '':
                contador += 1

        if jogador != 'venceu' and pc != 'venceu' and contador > 8:
            print('deu velha!')
            sleep(3)
            break

#pc-------------------------------------------------------------------------------------

        pclinha = randint(0,2)
        pccoluna = randint(0,2)

        if tabela[pclinha][pccoluna] !='':

            while tabela[pclinha][pccoluna] != '':

                pclinha = randint(0,2)
                pccoluna = randint(0,2)

                if tabela[pclinha][pccoluna] == '' and tabela[pclinha][pccoluna] != 'X':

                    tabela[pclinha][pccoluna] = "O"
                    break

        elif tabela[pclinha][pccoluna] == '':

            tabela[pclinha][pccoluna] = "O"


        for pos in range(3):

            if tabela[pos][0] == 'O' and  tabela[pos][1] == 'O' and  tabela[pos][2] == 'O':
                pc = 'venceu'
                print('jogador O ganhou!')
                sleep(3)
                break
                
                
        for pos in range(3):

            if tabela[0][pos] == 'O' and  tabela[1][pos] == 'O' and  tabela[2][pos] == 'O':
                pc = 'venceu'
                print('jogador O ganhou!')
                sleep(3)
                break
                
        
        if tabela[0][0] == 'O'and tabela[1][1] == 'O' and tabela[2][2] == 'O':
                pc = 'venceu'
                print('jogador O ganhou!')
                sleep(3)
                break
            

        elif tabela[2][0] == 'O'and tabela[1][1] == 'O' and tabela[0][2] == 'O':
                pc = 'venceu'
                print('jogador O ganhou!')
                sleep(3)
                break

        os.system("cls")


jogo_da_velha(tabela)
