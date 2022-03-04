import os
import pyautogui
import time
import random
import PySimpleGUI as sg



class InstagramBot:
    def __init__(self):
        #self.drive = os.startfile("C:\ProgramData\BlueStacks\Client\Bluestacks.exe")
         self.drive = os.startfile("C:\Program Files\BlueStacks_msi2\HD-RunApp.exe")

    '''def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('COLOQUE A BIOS QUE DESEJAR, NÃO COLOQUE EMOJIS E ACENTOS!', size=(58, 1))],
            [sg.Text('LINHA 1 \U0001F388'),
             sg.Input(key='linha1', size=(40, 1))],
            [sg.Text('LINHA 2 \U0001F4CC'),
             sg.Input(key='linha2', size=(40, 1))],
            [sg.Text('LINHA 3 \U0001F4BC'),
             sg.Input(key='linha3', size=(40, 1))],
            [sg.Text('LINHA 4 \U0001F4DA'),
             sg.Input(key='linha4', size=(40, 1))],
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

    def CreatingBios(self):
        pyautogui.click(938, 351)  # clica em editar perfil
        time.sleep(random.randint(1, 2))
        pyautogui.click(766, 641)  ##clica na bios
        time.sleep(random.randint(1, 2))
        pyautogui.click(722, 167)
        line1 = open('BIOSline1.txt').read()
        line2 = open('BIOSline2.txt').read()
        line3 = open('BIOSline3.txt').read()
        line4 = open('BIOSline4.txt').read()
        a = pyperclip.copy(line1)
        pyperclip.paste()
        time.sleep(2)
        pyautogui.keyDown('return')
        time.sleep(2)
        pyautogui.write(line2)
        time.sleep(2)
        pyautogui.keyDown('return')
        time.sleep(2)
        pyautogui.write(line3)
        time.sleep(2)
        pyautogui.keyDown('return')
        time.sleep(2)
        pyautogui.write(line4)
        time.sleep(2)
        pyautogui.click(1193, 106)
        pyautogui.click(1193, 106)
        time.sleep(10)'''

    def OffSavePhotos(self):
        time.sleep(3)
        pyautogui.click(1171, 107)
        time.sleep(1)
        pyautogui.click(770, 632)
        time.sleep(1)
        pyautogui.click(733, 560)
        time.sleep(1)
        pyautogui.click(752, 788)
        time.sleep(1)
        pyautogui.click(1162, 186)
        time.sleep(0.5)
        pyautogui.click(1162, 307)
        time.sleep(0.5)
        pyautogui.click(1162, 363)
        time.sleep(0.5)
        pyautogui.click(676, 110)
        time.sleep(1)
        pyautogui.click(1151, 1008)

    def PerfilPhoto(self):
        time.sleep(3)
        pyautogui.click(756, 214) #CLICA NO PERFIL
        time.sleep(random.randint(1, 2))
        pyautogui.click(928, 526) #Add foto de perfil/opção
        time.sleep(random.randint(1, 2))
        pyautogui.click(789, 928) #abre galeria
        time.sleep(2)
        pyautogui.click(1021, 627)
        time.sleep(2)
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(987, 901)  # clica na primeira foto da primeira coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1159, 105)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(1159, 105)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        time.sleep(8)

    def PhotosFeed(self):
        time.sleep(2)
        pyautogui.click(1134, 96)  #clica no +
        time.sleep(3)
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735) #clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(1021, 627) #clica pra permitir, caso precisar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1021, 627) #clica pra permitir, caso precisar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1021, 627) #clica pra permitir, caso precisar
        pyautogui.click(750, 1020) #clica na galery
        time.sleep(random.randint(1, 2))
        pyautogui.moveTo(765, 764) #se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(858, 909) #clica na primeira foto da segunda coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90) #clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90) #clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(1)
        pyautogui.click(745, 185)
        time.sleep(2)
        pyautogui.write('sudke')
        time.sleep(2.5)
        pyautogui.click(730, 257)
        time.sleep(2)
        pyautogui.click(806, 152) #clica pra escrever legenda
        pyautogui.write('Happy')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('#home')
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185, 93) #clica pra publicar
        time.sleep(random.randint(7, 10))
        #AGAIN, NEXT PHOTO 2
        #AGAIN, NEXT PHOTO 2
        #AGAIN, NEXT PHOTO 2
        pyautogui.click(1134, 96)  # clica no +
        time.sleep(random.randint(1, 2))
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735)  # clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(750, 1020)  # clica na galery
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(715, 911) #clica na primeira foto da segunda coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(random.randint(1, 2))
        pyautogui.click(745, 185)
        time.sleep(1.3)
        pyautogui.write('sudke')
        time.sleep(2.5)
        pyautogui.click(742, 325)
        time.sleep(2)
        pyautogui.click(806, 152)  # clica pra escrever legenda
        legend_2 = 'Party\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '#party\n'
        pyautogui.write(legend_2)
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185, 93) #clica pra publicar
        time.sleep(random.randint(7, 10))
        # AGAIN, NEXT PHOTO 3
        # AGAIN, NEXT PHOTO 3
        # AGAIN, NEXT PHOTO 3
        pyautogui.click(1134, 96)  # clica no +
        time.sleep(random.randint(1, 2))
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735)  # clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(750, 1020)  # clica na galery
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(1108, 766)  # clica na primeira foto da segunda coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(random.randint(1, 2))
        pyautogui.click(745, 185)
        time.sleep(1.3)
        pyautogui.write('sudke')
        time.sleep(2.5)
        pyautogui.click(714, 408)
        time.sleep(2)
        pyautogui.click(806, 152)  # clica pra escrever legenda
        legend_3 = 'Just It\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '#wave\n'
        pyautogui.write(legend_3)
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185,93) #clica pra publicar
        time.sleep(random.randint(7, 10))
        # AGAIN, NEXT PHOTO 4
        # AGAIN, NEXT PHOTO 4
        # AGAIN, NEXT PHOTO 4
        pyautogui.click(1134, 96)  # clica no +
        time.sleep(random.randint(1, 2))
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735)  # clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(750, 1020)  # clica na galery
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(1003, 776)  # clica na primeira foto da segunda coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(random.randint(1, 2))
        pyautogui.click(745, 185)
        time.sleep(1.3)
        pyautogui.write('sudke')
        time.sleep(2.5)
        pyautogui.click(717, 478)
        time.sleep(2)
        pyautogui.click(806, 152)  # clica pra escrever legenda
        legend_4 = 'Feelings\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '#feeling\n'
        pyautogui.write(legend_4)
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185, 93)  # clica pra publicar
        time.sleep(random.randint(7, 10))
        # AGAIN, NEXT PHOTO 5
        # AGAIN, NEXT PHOTO 5
        # AGAIN, NEXT PHOTO 5
        pyautogui.click(1134, 96)  # clica no +
        time.sleep(random.randint(1, 2))
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735)  # clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(750, 1020)  # clica na galery
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(855, 759)  # clica na primeira foto da terceira coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(random.randint(1, 2))
        pyautogui.click(745, 185)
        time.sleep(1.3)
        pyautogui.write('sudke')
        time.sleep(2.5)
        pyautogui.click(710, 548)
        time.sleep(2)
        pyautogui.click(806, 152)  # clica pra escrever legenda
        legend_5 = 'Nice Day\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '#hairstyles\n'
        pyautogui.write(legend_5)
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185, 93)  # clica pra publicar
        time.sleep(random.randint(7, 10))
        # AGAIN, NEXT PHOTO 6
        # AGAIN, NEXT PHOTO 6
        # AGAIN, NEXT PHOTO 6
        pyautogui.click(1134, 96)  # clica no +
        time.sleep(random.randint(1, 2))
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735)  # clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(750, 1020)  # clica na galery
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(721, 769)  # clica na primeira foto da terceira coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(random.randint(1, 2))
        pyautogui.click(745, 185)
        time.sleep(1.3)
        pyautogui.write('sudke')
        time.sleep(2.5)
        pyautogui.click(710, 618)
        time.sleep(2)
        pyautogui.click(806, 152)  # clica pra escrever legenda
        legend_6 = 'Amo\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '#blackandwhite\n'
        pyautogui.write(legend_6)
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185, 93)  # clica pra publicar
        time.sleep(random.randint(7, 10))
        # AGAIN, NEXT PHOTO 7
        # AGAIN, NEXT PHOTO 7
        # AGAIN, NEXT PHOTO 7
        pyautogui.click(1134, 96)  # clica no +
        time.sleep(random.randint(1, 2))
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735)  # clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(750, 1020)  # clica na galery
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(1137, 629)  # clica na primeira foto da terceira coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(random.randint(1, 2))
        pyautogui.click(745, 185)
        time.sleep(1.3)
        pyautogui.write('sadkw')
        time.sleep(2.5)
        pyautogui.click(730, 257)
        time.sleep(2)
        pyautogui.click(806, 152)  # clica pra escrever legenda
        legend_7 = 'Life\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '#life\n'
        pyautogui.write(legend_7)
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185, 93)  # clica pra publicar
        time.sleep(random.randint(7, 10))
        # AGAIN, NEXT PHOTO 8
        # AGAIN, NEXT PHOTO 8
        # AGAIN, NEXT PHOTO 8
        pyautogui.click(1134, 96)  # clica no +
        time.sleep(random.randint(1, 2))
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735)  # clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(750, 1020)  # clica na galery
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(1008, 630)  # clica na primeira foto da terceira coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(random.randint(1, 2))
        pyautogui.click(745, 185)
        time.sleep(1.3)
        pyautogui.write('sadkw')
        time.sleep(2.5)
        pyautogui.click(742, 325)
        time.sleep(2)
        pyautogui.click(806, 152)  # clica pra escrever legenda
        pyautogui.write('Loved')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('#love')
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185, 93)  # clica pra publicar
        time.sleep(random.randint(7, 10))
        # AGAIN, NEXT PHOTO 9
        # AGAIN, NEXT PHOTO 9
        # AGAIN, NEXT PHOTO 9
        pyautogui.click(1134, 96)  # clica no +
        time.sleep(random.randint(1, 2))
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735)  # clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(750, 1020)  # clica na galery
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(856, 625)  # clica na primeira foto da quarta coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(random.randint(1, 2))
        pyautogui.click(745, 185)
        time.sleep(1.3)
        pyautogui.write('sadkw')
        time.sleep(2.5)
        pyautogui.click(714, 408)
        time.sleep(2)
        pyautogui.click(806, 152)  # clica pra escrever legenda
        legend_9 = 'Style\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '.\n' \
                   '#casualstyle\n'
        pyautogui.write(legend_9)
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185, 93)  # clica pra publicar
        time.sleep(random.randint(7, 10))
        # AGAIN, NEXT PHOTO 10
        # AGAIN, NEXT PHOTO 10
        # AGAIN, NEXT PHOTO 10
        pyautogui.click(1134, 96)  # clica no +
        time.sleep(random.randint(1, 2))
        pyautogui.click(774, 668)  # clica pra add feed,MSI
        pyautogui.click(721, 735)  # clica pra add feed, BLUESTACKS
        time.sleep(random.randint(1, 2))
        pyautogui.click(750, 1020)  # clica na galery
        pyautogui.moveTo(765, 764)  # se move
        time.sleep(random.randint(1, 2))
        pyautogui.scroll(-100)
        time.sleep(random.randint(1, 2))
        pyautogui.click(711, 626)  # clica na primeira foto da quarta coluna/direita
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(random.randint(1, 2))
        pyautogui.click(1184, 90)  # clica pra avançar
        time.sleep(2)
        pyautogui.click(741, 324) #clica pra add localização
        time.sleep(random.randint(1, 2))
        pyautogui.click(745, 185)
        time.sleep(1.3)
        pyautogui.write('sadkw')
        time.sleep(2.5)
        pyautogui.click(717, 478)
        time.sleep(2)
        pyautogui.click(806, 152)  # clica pra escrever legenda
        pyautogui.write('Peaceful')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('.')
        pyautogui.press('return')
        pyautogui.write('#peace')
        time.sleep(random.randint(2, 4))
        pyautogui.click(1185, 93)  # clica pra publicar 


    def PostarStory(self):
        time.sleep(3)
        pyautogui.click(1134, 96)  # CLICA NO PERFIL
        time.sleep(random.randint(1, 2))
        pyautogui.click(739, 802)
        time.sleep(1.5)
        pyautogui.click(1029, 623)
        time.sleep(1)
        pyautogui.click(1029, 623)
        time.sleep(1)
        pyautogui.click(1029, 623)
        time.sleep(1)
        pyautogui.click(1029, 623)
        time.sleep(1)
        pyautogui.click(690, 996)
        time.sleep(1)
        #pyautogui.click(735, 685)
        pyautogui.click(1040, 288)
        time.sleep(2)
        pyautogui.click(696, 974)
        time.sleep(4)
        #STORY 2
        #STORY 2
        pyautogui.click(1134, 96)  # CLICA NO PERFIL
        time.sleep(random.randint(1, 2))
        pyautogui.click(739, 802)
        time.sleep(1.5)
        pyautogui.click(690, 996)
        time.sleep(1)
        #pyautogui.click(1123, 373)
        pyautogui.click(920, 288)
        time.sleep(2)
        pyautogui.click(696, 974)
        time.sleep(4)
        #STORY 3
        #STORY 3
        pyautogui.click(1134, 96)  # CLICA NO PERFIL
        time.sleep(random.randint(1, 2))
        pyautogui.click(739, 802)
        time.sleep(1.5)
        pyautogui.click(690, 996)
        time.sleep(1)
        #pyautogui.click(930, 384)
        pyautogui.click(813, 295)
        time.sleep(3)
        pyautogui.click(696, 974)
        time.sleep(4)
        #STORY 4
        #STORY 4
        pyautogui.click(1134, 96)  # CLICA NO +
        time.sleep(random.randint(1, 2))
        pyautogui.click(739, 802)
        time.sleep(1.5)
        pyautogui.click(690, 996)
        time.sleep(1)
        pyautogui.click(739, 353)
        time.sleep(3)
        pyautogui.click(696, 974)
        time.sleep(4)

    def Destaques(self):
        pyautogui.click(756, 214)  # CLICA NO PERFIL
        time.sleep(2)
        pyautogui.click(1090, 953)
        time.sleep(2)
        pyautogui.write('Me')
        time.sleep(1.7)
        pyautogui.click(925, 600)
        time.sleep(2)
        pyautogui.click(921, 750)
        time.sleep(1)
        pyautogui.click(1169, 575)
        time.sleep(1)
        #DESTAQUE 2
        #DESTAQUE 2
        pyautogui.click(1090, 953)
        time.sleep(1.5)
        pyautogui.click(811, 896)
        time.sleep(1.5)
        pyautogui.write('Feelings')
        time.sleep(1.7)
        pyautogui.click(925, 600)
        time.sleep(2)
        pyautogui.click(921, 750)
        time.sleep(1)
        #DESTAQUE 3
        #DESTAQUE 3
        pyautogui.click(1090, 953)
        time.sleep(1.5)
        pyautogui.click(917, 898)
        time.sleep(1.5)
        pyautogui.write('Look')
        time.sleep(1.7)
        pyautogui.click(925, 600)
        time.sleep(2)
        pyautogui.click(921, 750)
        time.sleep(1)
        #DESTAQUE 4
        #DESTAQUE 4
        pyautogui.click(1090, 953)
        time.sleep(1.5)
        pyautogui.click(1033, 894)
        time.sleep(1.5)
        pyautogui.write('Love')
        time.sleep(1.7)
        pyautogui.click(925, 600)
        time.sleep(2)
        pyautogui.click(921, 750)
        time.sleep(1)








#1123, 373
#930, 384
#739, 353




#StartBot1 = InstagramBot().ScreenBios()
#StartBot2 = InstagramBot().CreatingBios()

StartBoFeelingst3 = InstagramBot().OffSavePhotos()
StartBot4 = InstagramBot().PerfilPhoto()
StartBot5 = InstagramBot().PhotosFeed()
StartBot6 = InstagramBot().PostarStory()
StartBot7 = InstagramBot().Destaques()






