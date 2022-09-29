import random


title= 'coins multiplier'
print(30*'=')
print (title.upper())
print(30*'=')

user= str(input('Nome De Usuario: '))
coins= int(input('Quer quantos Creditos? '))
print(30*'=')

while coins>0:
    n= random.randint(0 , 50)
    bet_value= int(input('Valor Da Sua Aposta: '))
    bet= int(input('Numero Da Sorte (0-50): '))
    if bet>50:
        print(30*'=')
        print('Numero Da Sorte Maior Que o Limite')
        print(30*'=')
    else:
        if coins<bet_value:
            print(30*'=')
            print('Coins Insuficientes')
            print('Seu Saldo é De: ', coins)
            print(30*'=')
        else:
            if n==bet:
                coins= coins+bet_value
                print(30*'-')
                print('O Numero Sorteado Foi: ', n)
                print('Parabéns',user,'Você Ganhou',bet_value,'Coins')
                print('Novo Saldo: ',coins)
                print(30*'-')
            else:
                coins= coins-bet_value
                print(30*'-')
                print('O Numero Sorteado Foi: ', n)
                print('Você Perdeu',bet_value,'Coins')
                print('Novo Saldo: ', coins)
                print(30*'-')
print(30*'=')
print('Seus Coins Acabaram, Volte Outro Dia')
print(30*'=')
print('GAME OVER')
print(30*'=')
