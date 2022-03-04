import PySimpleGUI as sg


class HaLogin:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Username:', size=(10, 1)),
             sg.Input(key='username', size=(20, 1))],
            [sg.Text('Password:', size=(10, 1)),
             sg.Input(key='password', size=(20, 1))],
            [sg.Button('LOGIN')],

        ]
        self.screen = sg.Window('Tela de Login', layout)

    def starts(self):
        while True:
            event, users = self.screen.read()
            if event == sg.WINDOW_CLOSED:
                break
            if event == 'LOGIN':
                with open('usuario.txt', 'w') as arquivo:
                    arquivo.write(f"{users['username']}")
            if event == 'LOGIN':
                with open('senha.txt', 'w') as arquivo:
                    arquivo.write(f"{users['password']}")
                    import botOpenSC
                    botOpenSC








btc = HaLogin()
btc.starts()










