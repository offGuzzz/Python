import random



n= random.randint(0,50)

title= 'coins multiplier'
print(30*'=')
print (title.upper())
print(30*'=')

user= str(input('Nome De Usuario: '))
coins= int(input('Quer quantos Creditos? '))
print(30*'=')

while coins>0:
    bet_value= int(input('Valor Da Sua Aposta: '))
    bet= int(input('Numero Da Sorte: '))
    if coins<bet_value:
        print(30*'=')
        print('Coins Insuficientes')
        print('Seu Saldo é De: ', coins)
        print(30*'=')
    else:
        if n==bet:
            coins= coins+bet_value
            print(30*'-')
            print('Parabéns',user,'Você Ganhou',bet_value,'Coins')
            print('Novo Saldo: ',coins)
            print(30*'-')
        else:
            coins= coins-bet_value
            print(30*'-')
            print('Você Perdeu',bet_value,'Coins')
            print('Novo Saldo: ', coins)
            print(30*'-')
print('Seus Coins Acabaram, Volte Outro Dia')