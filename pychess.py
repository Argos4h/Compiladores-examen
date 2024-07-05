import sys  
import pygame

import chess  # Importa el módulo del juego de ajedrez
import menus  # Importa los módulos de los menús del juego
from tools.loader import MAIN  # Importa recursos específicos del juego desde el módulo loader
from tools import sound  # Importa el módulo de sonido del juego

# Este código no es relevante. Limpia stdout, útil en caso de que programas externos llamen a esta aplicación.
sys.stdout.flush()

# Inicialización de pygame
pygame.init()
clock = pygame.time.Clock()

# Inicializa la pantalla, establece el título y el icono. Usa SCALED si estás usando pygame 2.
if pygame.version.vernum[0] >= 2:
    win = pygame.display.set_mode((500, 500), pygame.SCALED)
else:
    win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ajedres")  # Establece el título de la ventana
pygame.display.set_icon(MAIN.ICON)  # Establece el ícono de la ventana

# Coordenadas de los botones en notación de rectángulo.
sngl = (300, 140, 220, 40)
mult = (280, 200, 200, 40)
onln = (360, 260, 120, 40)
load = (260, 320, 200, 40)
pref = (0, 450, 210, 40)
abt = (320, 450, 110, 40)
hwto = (350, 410, 90, 30)
stok = (0, 410, 240, 30)

# Función que muestra la pantalla principal.
# Recibe "prefs", una lista de todas las configuraciones del usuario.
def showMain(prefs):
    global cnt, img  # Variables globales cnt e img

    # Muestra primero la imagen de fondo (basado en la variable img)
    win.blit(MAIN.BG[img], (0, 0))

    # Verifica si el usuario ha habilitado la función de animación de fondo
    if prefs["slideshow"]:
        cnt += 1  # Incrementa el contador de fotogramas
        if cnt >= 150:
            # Si el contador alcanza 150 (5 segundos han pasado), comienza a desvanecer lentamente la imagen
            s = pygame.Surface((500, 500))
            s.set_alpha((cnt - 150) * 4)
            s.fill((0, 0, 0))
            win.blit(s, (0, 0))

        if cnt == 210:
            cnt = 0
            img = 0 if img == 3 else img + 1
    else:
        cnt = -150
        img = 0

    # Muestra todos los textos en la pantalla uno por uno
    win.blit(MAIN.HEADING, (80, 20))
    pygame.draw.line(win, (255, 255, 255), (80, 100), (130, 100), 4)
    pygame.draw.line(win, (255, 255, 255), (165, 100), (340, 100), 4)
    win.blit(MAIN.VERSION, (345, 95))

    win.blit(MAIN.SINGLE, sngl[:2])
    win.blit(MAIN.MULTI, mult[:2])
    win.blit(MAIN.ONLINE, onln[:2])
    win.blit(MAIN.LOAD, load[:2])
    win.blit(MAIN.PREF, pref[:2])
    win.blit(MAIN.HOWTO, hwto[:2])
    win.blit(MAIN.ABOUT, abt[:2])
    win.blit(MAIN.STOCK, stok[:2])

# Inicialización de algunas variables adicionales
cnt = 0
img = 0
run = True

# Carga la configuración del jugador
prefs = menus.pref.load()

music = sound.Music()
music.play(prefs)
while run:
    clock.tick(30)  # Limita la velocidad de fotogramas a 30 por segundo
    showMain(prefs)  # Llama a la función para mostrar la pantalla principal

    x, y = pygame.mouse.get_pos()  # Obtiene la posición del mouse

    # Verifica si el mouse está sobre algún botón y muestra la versión resaltada del botón
    if sngl[0] < x < sum(sngl[::2]) and sngl[1] < y < sum(sngl[1::2]):
        win.blit(MAIN.SINGLE_H, sngl[:2])

    if mult[0] < x < sum(mult[::2]) and mult[1] < y < sum(mult[1::2]):
        win.blit(MAIN.MULTI_H, mult[:2])

    if onln[0] < x < sum(onln[::2]) and onln[1] < y < sum(onln[1::2]):
        win.blit(MAIN.ONLINE_H, onln[:2])

    if load[0] < x < sum(load[::2]) and load[1] < y < sum(load[1::2]):
        win.blit(MAIN.LOAD_H, load[:2])

    if pref[0] < x < sum(pref[::2]) and pref[1] < y < sum(pref[1::2]):
        win.blit(MAIN.PREF_H, pref[:2])
        
    if hwto[0] < x < sum(hwto[::2]) and hwto[1] < y < sum(hwto[1::2]):
        win.blit(MAIN.HOWTO_H, hwto[:2])

    if abt[0] < x < sum(abt[::2]) and abt[1] < y < sum(abt[1::2]):
        win.blit(MAIN.ABOUT_H, abt[:2])

    if stok[0] < x < sum(stok[::2]) and stok[1] < y < sum(stok[1::2]):
        win.blit(MAIN.STOCK_H, stok[:2])

    # Bucle de eventos de pygame para manejar todos los eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            # El usuario ha hecho clic en algún lugar, determina qué botón y
            # llama a una función para manejar el juego en una ventana diferente.
            x, y = event.pos

            if sngl[0] < x < sum(sngl[::2]) and sngl[1] < y < sum(sngl[1::2]):
                sound.play_click(prefs)
                ret = menus.splayermenu(win)
                if ret == 0:
                    run = False
                elif ret != 1:
                    if ret[0]:
                        run = chess.mysingleplayer(win, ret[1], prefs)
                    else:
                        run = chess.singleplayer(win, ret[1], ret[2], prefs)

            elif mult[0] < x < sum(mult[::2]) and mult[1] < y < sum(mult[1::2]):
                sound.play_click(prefs)
                ret = menus.timermenu(win, prefs)
                if ret == 0:
                    run = False
                elif ret != 1:
                    run = chess.multiplayer(win, ret[0], ret[1], prefs)

            elif onln[0] < x < sum(onln[::2]) and onln[1] < y < sum(onln[1::2]):
                sound.play_click(prefs)
                ret = menus.onlinemenu(win)
                if ret == 0:
                    run = False
                elif ret != 1:
                    run = chess.online(win, ret[0], prefs, ret[1])

            elif load[0] < x < sum(load[::2]) and load[1] < y < sum(load[1::2]):
                sound.play_click(prefs)
                ret = menus.loadgamemenu(win)
                if ret == 0:
                    run = False

                elif ret != 1:
                    if ret[0] == "multi":
                        run = chess.multiplayer(win, *ret[1:3], prefs, ret[3])
                    elif ret[0] == "single":
                        run = chess.singleplayer(win, *ret[1:3], prefs, ret[3])
                    elif ret[0] == "mysingle":
                        run = chess.mysingleplayer(win, ret[1], prefs, ret[2])

            elif pref[0] < x < sum(pref[::2]) and pref[1] < y < sum(pref[1::2]):
                sound.play_click(prefs)
                run = menus.prefmenu(win)
                
                prefs = menus.pref.load()
                if music.is_playing():
                    if not prefs["sounds"]:
                        music.stop()
                else:
                    music.play(prefs)
                    
            elif hwto[0] < x < sum(hwto[::2]) and hwto[1] < y < sum(hwto[1::2]):
                sound.play_click(prefs)
                run = menus.howtomenu(win)

            elif abt[0] < x < sum(abt[::2]) and abt[1] < y < sum(abt[1::2]):
                sound.play_click(prefs)
                run = menus.aboutmenu(win)

            elif stok[0] < x < sum(stok[::2]) and stok[1] < y < sum(stok[1::2]):
                sound.play_click(prefs)
                run = menus.sfmenu(win)

    # Actualiza la pantalla en cada fotograma
    pygame.display.flip()

# Detén la música y cierra pygame después de salir del bucle principal
music.stop()
pygame.quit()
