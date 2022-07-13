#!/usr/bin/env python
# coding: utf-8

# In[ ]:


perguntas = {
    'Pergunta 1' : {
        'pergunta': 'Quando é 2+2 ?',
        'respostas': {'a': '1','b': '4','c': '5',},
        'resposta_certa': 'b',
    },
    'Pergunta 2' : {
        'pergunta': 'Quando é 3*2 ?',
        'respostas': {'a': '4','b': '10','c': '6',},
        'resposta_certa': 'c',
    },
    'Pergunta 3' : {
        'pergunta': 'Quando é 5*2 ?',
        'respostas': {'a': '4','b': '10','c': '6',},
        'resposta_certa': 'b',
    },
    'Pergunta 4' : {
        'pergunta': 'Quando é 10*2 ?',
        'respostas': {'a': '20','b': '10','c': '6',},
        'resposta_certa': 'a',
    },
    'Pergunta 5' : {
        'pergunta': 'Quando é 20*2 ?',
        'respostas': {'a': '40','b': '20','c': '24',},
        'resposta_certa': 'a',
    },
}
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha uma das opções abaixo')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')
        
    resposta_usario = input('Sua resposta: ')
    
    if resposta_usario == pv['resposta_certa']:
        print("Você acertou !")
        respostas_certas += 1
    else: 
        print("Você errou")
    
    print()
    
qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas/qtd_perguntas * 100
 
print(f'Você acertou {respostas_certas} respostas.')
print(f'Sua porcentagem de acertoi foi de {porcentagem_acerto} %.')

