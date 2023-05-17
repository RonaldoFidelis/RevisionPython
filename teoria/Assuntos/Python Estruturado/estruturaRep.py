print('Bem-vindo ao app de aluguel!')
avancar = input('Vamos começar? (s/n) ')
if avancar == 's':
    question = input('Você quer alugar um carro ou estar procurando uma casa? ')
    if question == 'uma casa':
        questCasa = input('Ok, casa ou apartamento? ')
        if questCasa == 'casa':
            print('Infelizmente não temos nenhuma casa disponível no momento :(')
        elif questCasa == 'apartamento':
            print('Opa, deixa eu te mostrar algumas maravilhas que temos!')
        else:
            print('Não entendi :/')
    elif question == 'um carro':
        questCarro = input('Ok, pode digitar a marca: ')
        if questCarro == 'BMW' or 'Audi':
            print('Vou te mostrar nossas naves!')
        else:
            print('No momento só temos BMW e AUDI')
    else:
        print('Não entendi, escolha entre "um carro" ou "uma casa"')
else:
    print('Tudo bem, até a próxima!')

#

