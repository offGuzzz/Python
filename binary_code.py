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

asciid= {
    '01000001': 'A',
    '01000010': 'B',
    '01000011': 'C',
    '01000100': 'D',
    '01000101': 'E',
    '01000110': 'F',
    '01000111': 'G',
    '01001000': 'H',
    '01001001': 'I',
    '01001010': 'J',
    '01001011': 'K',
    '01001100': 'L',
    '01001101': 'M',
    '01001110': 'N',
    '01001111': 'O',
    '01010000': 'P',
    '01010001': 'Q',
    '01010010': 'R',
    '01010011': 'S',
    '01010100': 'T',
    '01010101': 'U',
    '01010110': 'V',
    '01010111': 'W',
    '01011000': 'X',
    '01011001': 'Y',
    '01011010': 'Z',
    '01100001': 'a',
    '01100010': 'b',
    '01100011': 'c',
    '01100100': 'd',
    '01100101': 'e',
    '01100110': 'f',
    '01100111': 'g',
    '01101000': 'h',
    '01101001': 'i',
    '01101010': 'j',
    '01101011': 'k',
    '01101100': 'l',
    '01101101': 'm',
    '01101110': 'n',
    '01101111': 'o',
    '01110000': 'p',
    '01110001': 'q',
    '01110010': 'r',
    '01110011': 's',
    '01110100': 't',
    '01110101': 'u',
    '01110110': 'v',
    '01110111': 'w',
    '01111000': 'x',
    '01111001': 'y',
    '01111010': 'z'
}
ascii= 1
text=9

print('1 = ASCII > TEXTO')
print('9 = TEXTO > ASCII')

res= float(input('OQUE DESEJA FAZER? '))

if res > 5:
    text= input ('Digite A Palavra Que Quer Criptografar:'.upper())
    finaltext= (text.replace('a',a1).replace('b',b1).replace('c',c1).replace('d',d1).replace('e',d1).replace('f',f1).replace('g',g1).replace('h',h1).replace('i',i1).replace('j',j1).replace('k',k1).replace('l',l1).replace('m',m1).replace('n',n1).replace('o',o1).replace('p',p1).replace('q',q1).replace('r',r1).replace('s',s1).replace('t',t1).replace('u',u1).replace('v',v1).replace('w',w1).replace('x',x1).replace('y',y1).replace('z',z1).replace('A',A1).replace('B',B1).replace('C',C1).replace('D',D1).replace('E',E1).replace('F',F1).replace('G',G1).replace('H',H1).replace('I',I1).replace('J',J1).replace('K',K1).replace('L',L1).replace('M',M1).replace('N',N1).replace('O',O1).replace('P',P1).replace('Q',Q1).replace('R',R1).replace('S',S1).replace('T',T1).replace('U',U1).replace('V',V1).replace('W',W1).replace('X',X1).replace('Y',Y1).replace('Z',Z1))
    print ("Sua Palavra Criptografada é:",finaltext)

else:
    textt= input ('Digite A Palavra Que Quer Descriptografar:')
    finaltextt= (textt.replace('01100001','a').replace('01100010','b').replace('01100011','c').replace('01100100','d').replace('01100101','e').replace('01100110','f').replace('01100111','g').replace('01101000','h').replace('01101001','i').replace('01101010','j').replace('01101011','k').replace('01101100','l').replace('01101101','m').replace('01101110','n').replace('01101111','o').replace('01110000','p').replace('01110001','q').replace('01110010','r').replace('01110011','s').replace('01110100','t').replace('01110101','u').replace('01110110','v').replace('01110111','w').replace('01111000','x').replace('01111001','y').replace('01111010','z').replace('01000001','A').replace('01000010','B').replace('01000011','C').replace('01000100','D').replace('01000101','E').replace('01000110','F').replace('01000111','G').replace('01001000','H').replace('01001001','I').replace('01001010','J').replace('01001011','K').replace('01001100','L').replace('01001101','M').replace('01001110','N').replace('01001111','O').replace('01010000','P').replace('01010001','Q').replace('01010010','R').replace('01010011','S').replace('01010100','T').replace('01010101','U').replace('01010110','V').replace('01010111','W').replace('01011000','X').replace('01011001','Y').replace('01011010','Z'))
    print (asciid[textt])