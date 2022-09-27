import PySimpleGUI as sg

sg.theme('DarkAmber')
layout = [
    [sg.Text('Coins Multiplier')],
    [sg.Text('Nome:')],
    [sg.InputText()],
    [sg.Text('Coins:')],
    [sg.InputText()],
    [sg.Text('Numero Da Sorte:')],
    [sg.InputText()],
    [sg.Text('Valor Da Aposta:')],
    [sg.InputText()],
    [sg.Button("Começar"),sg.Button("Sair")],
    [sg.Text("", key="Numero_Sorteado")],
]


janela = sg.Window ('Coins Multiplier', layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == "Sair":
        break
    if evento == "Começar":
        print("Loading")

janela.close()