'''
Sistema onde o usuário escolhe a resposta correta
'''
perguntas = {
    'pergunta1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'respostas_certa': 'b',
    },
    'pergunta2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '2', 'b': '10', 'c': '6'},
        'respostas_certa': 'c',
    },
}

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas')
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Digite sua resposta: ')
    print(pv['respostas_certa'])
    if resposta_usuario == pv['respostas_certa']:
        print('Parabéns')
    else:
        print('Deu ruim')
    print()
