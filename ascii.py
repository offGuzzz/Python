import os
from time import sleep

cont=1
while cont == 1:
    #menu
    os.system('cls')
    title= 'ASCII-STRING'
    print(title)
    print(f'Deseja Converter De:\n[1]TEXTO\n[2]ASCII\n[9]SAIR')
    res= int(input('Oque Deseja Fazer?'))
    if res==9:
        break
    #opção do user
    elif res==1:
        sleep(1)
        os.system('cls')
        A1= ('01000001')
        B1= ('01000010')
        C1= ('01000011')
        D1= ('01000100')
        E1= ('01000101')
        F1= ('01000110')
        G1= ('01000111')
        H1= ('01001000')
        I1= ('01001001')
        J1= ('01001010')
        K1= ('01001011')
        L1= ('01001100')
        M1= ('01001101')
        N1= ('01001110')
        O1= ('01001111')
        P1= ('01010000')
        Q1= ('01010001')
        R1= ('01010010')
        S1= ('01010011')
        T1= ('01010100')
        U1= ('01010101')
        V1= ('01010110')
        W1= ('01010111')
        X1= ('01011000')
        Y1= ('01011001')
        Z1= ('01011010')
        a1= ('01100001')
        b1= ('01100010')
        c1= ('01100011')
        d1= ('01100100')
        e1= ('01100101')
        f1= ('01100110')
        g1= ('01100111')
        h1= ('01101000')
        i1= ('01101001')
        j1= ('01101010')
        k1= ('01101011')
        l1= ('01101100')
        m1= ('01101101')
        n1= ('01101110')
        o1= ('01101111')
        p1= ('01110000')
        q1= ('01110001')
        r1= ('01110010')
        s1= ('01110011')
        t1= ('01110100')
        u1= ('01110101')
        v1= ('01110110')
        w1= ('01110111')
        x1= ('01111000')
        y1= ('01111001')
        z1= ('01111010')

        text= input ('Digite A Palavra Que Quer Criptografar:')
        finaltext= (text.replace('a',a1).replace('b',b1).replace('c',c1).replace('d',d1).replace('e',d1).replace('f',f1).replace('g',g1).replace('h',h1).replace('i',i1).replace('j',j1).replace('k',k1).replace('l',l1).replace('m',m1).replace('n',n1).replace('o',o1).replace('p',p1).replace('q',q1).replace('r',r1).replace('s',s1).replace('t',t1).replace('u',u1).replace('v',v1).replace('w',w1).replace('x',x1).replace('y',y1).replace('z',z1).replace('A',A1).replace('B',B1).replace('C',C1).replace('D',D1).replace('E',E1).replace('F',F1).replace('G',G1).replace('H',H1).replace('I',I1).replace('J',J1).replace('K',K1).replace('L',L1).replace('M',M1).replace('N',N1).replace('O',O1).replace('P',P1).replace('Q',Q1).replace('R',R1).replace('S',S1).replace('T',T1).replace('U',U1).replace('V',V1).replace('W',W1).replace('X',X1).replace('Y',Y1).replace('Z',Z1))
        print ("Sua Palavra Criptografada é: ",finaltext)
        sleep(5)
        os.system('cls')
        print(30*'-')
        print('[1]SIM')
        print('[2]NÃO')
        cont=int(input('Deseja Continuar? '))
        if cont==2:
            break

    elif res==2:
        sleep(1)
        os.system('cls')
        ascii_to_str= int(input('Digite A Palavra Que Quer Descriptografar:'),2);
        #Pega numero de letras de str
        num_bytes= (ascii_to_str.bit_length()+7)//8
        str_array= ascii_to_str.to_bytes(num_bytes,'big')
        #converte
        ASCII_OK= str_array.decode()
        print("Sua Palavra Descriptografada é: ",ASCII_OK)
        sleep(8)
        os.system('cls')
        print(30*'-')
        print('[1]SIM')
        print('[2]NÃO')
        cont=int(input('Deseja Continuar? '))
        if cont==2:
            break
    elif res==9:
        break
    else:
        os.system('cls')
        print('Digite Alguma Opção Válida')
        sleep(5)
        cont=1

os.system('cls')
print('ADEUS')
sleep(3)
os.system('cls')







    #01100111011101010111001101110100011000010111011001101111
    #01000111011101010111001101110100011000010111011001101111
