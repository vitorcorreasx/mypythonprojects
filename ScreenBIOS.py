import PySimpleGUI as sg

class SCREENBIOS:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('COLOQUE A BIOS QUE DESEJAR, NÃO COLOQUE EMOJIS E ACENTOS!', size=(58, 1))],
            [sg.Text('LINHA 1'),
             sg.Input(key='linha1', size=(40, 1))],
            [sg.Text('LINHA 2'),
             sg.Input(key='linha2', size=(40, 1))],
            [sg.Text('LINHA 3'),
             sg.Input(key='linha3', size=(40, 1))],
            [sg.Text('LINHA 4'),
             sg.Input(key='linha4', size=(40, 1))],
            [sg.Text('U0001F388 = \U0001F388 // U0001F4CC = \U0001F4CC // U0001F4BC = \U0001F4BC // U0001F4DA = \U0001F4DA ')],
            [sg.Button('CONTINUE')]
        ]
        self.screen = sg.Window('COLOQUE A BIOS', layout)


    def ScreenBios(self):
        while True:
            BIOS, bios_info = self.screen.read()
            if BIOS == sg.WINDOW_CLOSED:
                break
            if BIOS == 'CONTINUE':
                with open('BIOSline1.txt', 'w') as arquivo:
                    arquivo.write(f"{bios_info['linha1']}")
            if BIOS == 'CONTINUE':
                with open('BIOSline2.txt', 'w') as arquivo:
                    arquivo.write(f"{bios_info['linha2']}")
            if BIOS == 'CONTINUE':
                with open('BIOSline3.txt', 'w') as arquivo:
                    arquivo.write(f"{bios_info['linha3']}")
            if BIOS == 'CONTINUE':
                with open('BIOSline4.txt', 'w') as arquivo:
                    arquivo.write(f"{bios_info['linha4']}")
            if BIOS == 'CONTINUE':
                break



STARTBIOS = SCREENBIOS()
STARTBIOS.ScreenBios()

