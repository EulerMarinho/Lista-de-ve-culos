# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 09:28:29 2021

@author: Euler
"""

import numpy 

df=[]

titulo=[]
titulo.append('Marca')
titulo.append('Modelo')
titulo.append('Ano')
titulo.append('Valor')

df.append(titulo)
continuar='1'
while continuar=='1':
    a=input('*****************************''\n''*Sistema autocarros EulerRCM*''\n''*****************************''\n'
            'MENU PRINCIPAL''\n''1 - Ler os veiculos''\n''2 - Adicionar veiculo''\n''3 - Exibir carros por grupo''\n')
    while a!='2' and a!='1' and a!='3':
        print('a=',a,'   .   ')
        print('Valor invalido, digite novamente')
        a=input('MENU PRINCIPAL''\n''1 - Ler os veiculos''\n''2 - Adicionar veiculo''\n''3 - Exibir carros por grupo')
    
    
    if a=='1':
        print(df)
    if a=='2':
        carro=[]
        carro.append(input('Digite a marca:'))
        carro.append(input('Digite o modelo:'))
        carro.append(input('Digite o ano:'))
        carro.append(input('Digite o valor:'))
        df.append(carro)
        print('Veículo inserido no sistema!')
        
        
    if a=='3':
        b=input('FILTRAR POR:''\n''1 - Valor''\n''2 - Montadora''\n''3 - Modelo''\n''4 - Valor ')
        while b!='2' and b!='1' and b!='3' and b!='4':
            print('b=',a,'   .   ')
            print('Valor invalido, digite novamente')
            b=input('FILTRAR POR:''\n''1 - Valor''\n''2 - Montadora''\n''3 - Modelo''\n''4 - Ano ''\n')
       
        if b=='1':
            valorsup=input('Insira o valor maximo: ')
            valorinf=input('Insira o valor mínimo: ')
            cont=0
            for b in range(1,len(df)):
            
                if df[b][3]<=valorsup and df[b][3]>=valorinf:
                    cont=1
                    break
                
            if cont ==0:
                print('\n''Não foram encontrads carros nesta faixa de preço')
            
            if cont==1:
                print('\n''Os carros encontrados nessa faixa de preço são:')  
                for b in range(1,len(df)):
                
                    if df[b][3]<=valorsup and df[b][3]>=valorinf:
                    
                        print (df[b])
                    
                    
        if b=='2':
            montadora=input('Insira a montadora: ')
            
            print('ok, b=2')
        if b=='3':
            print('ok, b=3')
        if b=='4':
            print('ok, b=4')
                       
    continuar=input('Deseja realizar nova operação?''\n''1 - sim''\n''Outro valor - Não''\n')
    
    
    