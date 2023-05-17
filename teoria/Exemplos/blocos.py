# em Python todos os blocos são iniciados com o símbolo : (dois pontos)

a = 0
y = 30
for i in range(y):#Inicio do bloco
    if a % 2 == 0:
        a += 1
        continue
    else:
        if a % 5 == 0:
            break
        else:
            a += 3
print(a)

""" O primeiro número que vai ser checado é o 0 e o resto da divisão de 0/2 é 0
 Logo a += 1, ou seja o proximo número será o 1, mas 1%2 != de 0, e vai para o Else
 Mas o primeiro if a % 5 == 0, também será falso, pois o resto de 1/5 é 1, logo ele passa para a proxima checagem
 a += 3, ou seja, 1+3 = 4. E ele volta para o inicio da estrutura de condicional
 Dessa vez o resto da divisão de 4/2 é 0, logo a += 1, ou seja, 4 + 1 e ele volta para a mesma checagem
 Dessa vez o resto da divisão de 5/2 não é = 0, passado para o Else
 Agora no if, a=5 % 5 == 0 é verdadeira e a condicional acaba. """

