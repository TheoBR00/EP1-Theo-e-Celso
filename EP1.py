# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 15:42:34 2018

@author: Theo B.R
"""
import tkinter as tk
import json

window = tk.Tk()

botão = tk.Button(window)
botão.configure(text="Diga oi!")
botão.grid()

window.mainloop()


cardapio = {'frango a parmegiana': '30.0', 'miojo': '10.0', 'macarrão': '45', 'filé mignon': '40', 'fetuccine com frutos do mar ao creme de trufas brancas': '85.0', 'petit gateau': '20.0', 'suco de maracujá': '12', 'guaraná': '5'}                                      
comanda = {}
comanda_2 = {}
comanda_3 = {}

conta = {}
conta_2 = {}
conta_3 = {}


p = []
lista_quant = []
cont = 0

verifica = True
i = 0
conta = 0

while verifica:
    with open('cardapio.json', 'r') as arquivo:
        conteudo = arquivo.read()
        cardapio = json.loads(conteudo)
    print('Cardapio eletrônico:')
    print('0 - Sair')
    print('1 - Imprimir cardápio')
    print('2 - Adicionar item')
    print('3 - Remover item')
    print('4 - Imprimir comanda')
    escolha = int(input('Faça sua escolha: '))
    
    if escolha < 0:
        print('Escolha inválida! Tente novamente')
        escolha = int(input('Faça sua escolha: '))
    
    if escolha == 1:
        for prato, preço in cardapio.items():
            print('- {0} R$ {1}'.format(prato, preço))

    elif escolha == 2:
        pedido = input('O que você gostaria de pedir?: ')
        
        if pedido not in cardapio.keys():
            print('O item {0} não está no cardápio! Tente novamente'.format(pedido))
            
            pedido = input('O que você gostaria de pedir?: ')
            
        elif pedido in cardapio.keys():
            adicionar = int(input('O item {0} já está incluído no cardápio! Quanto você gostaria de adicionar?: '.format(pedido)))
            conta += float(cardapio[pedido]) * adicionar
            comanda[pedido] = adicionar
            lista_quant.append(comanda)
        
        
    elif escolha == 3:
        remover = input('Qual item você gostaria de remover?: ')
        for r in comanda:
            if remover == r:
                del comanda[remover]
                conta -= float(cardapio[remover]) * adicionar
                print(comanda)
                break
    
    
    elif escolha == 0:
        print('A conta saiu R$ {0}'.format(conta))
        print('Obrigado por utilizar nosso sistema!')
        guardar = json.dumps(comanda, sort_keys=True, indent=4)
        with open('pratos.json', 'w') as arquivo_2:
            arquivo_2.write(guardar)
        verifica = False
        
    elif escolha == 4:
        print(comanda)
    
    