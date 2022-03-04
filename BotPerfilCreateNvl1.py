import os
import pyautogui
import time
import random
import keyboard



os.startfile("C:\Program Files\BlueStacks_msi2\HD-RunApp.exe")

while keyboard.is_pressed('p')== False:
time.sleep(3)
pyautogui.click(1171, 107)
time.sleep(1)
pyautogui.click(955, 1013)
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


time.sleep(3)
pyautogui.click(756, 214) #CLICA NO PERFIL
time.sleep(random.randint(1, 2))
pyautogui.click(928, 526) #Add foto de perfil/opção
time.sleep(random.randint(1, 2))
pyautogui.click(789, 928) #abre galeria
time.sleep(2)
pyautogui.click(1021, 627)
time.sleep(1)
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
legend_1 = 'Happy\n' \
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
           '.\n ' \
           ' #home\n'
pyautogui.write(legend_1)
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
legend_6 = 'sz\n' \
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
           '.\n'  \
           ' #blackandwhite\n'
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
legend_8 = 'Loved\n' \
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
           '#love\n'
pyautogui.write(legend_8)
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
legend_9 = 'style\n' \
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
legend_10 = 'Peaceful\n' \
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
           '#peace\n'
pyautogui.write(legend_10)
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
pyautogui.click(735, 685)
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
pyautogui.click(1123, 373)
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
pyautogui.click(930, 384)
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
pyautogui.click(1169, 575)

StartBot1 = InstagramBot().OffSavePhotos()
if keyboard.is_pressed('p'):
    breakpoint(StartBot1)
StartBot2 = InstagramBot().PerfilPhoto()
StartBot3 = InstagramBot().PhotosFeed()
StartBot4 = InstagramBot().PostarStory()
StartBot5 = InstagramBot().Destaques()






