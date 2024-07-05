import os.path
import pygame

# Initialize pygame.font module and load the font file.
pygame.font.init()
FONT = os.path.join("res", "Asimov.otf")

# Load different sizes of the font.
head = pygame.font.Font(FONT, 80)
large = pygame.font.Font(FONT, 50)
medium = pygame.font.Font(FONT, 38)
small = pygame.font.Font(FONT, 27)
vsmall = pygame.font.Font(FONT, 17)

# Define RGB color constants for use.
WHITE = (255, 255, 255)
GREY = (180, 180, 180)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (200, 20, 20)

# Define a few constants that contain loaded texts of numbers and chararters.
NUM = [vsmall.render(str(i), True, WHITE) for i in range(10)]
LNUM = [small.render(str(i), True, WHITE) for i in range(10)]
BLNUM = [small.render(str(i), True, BLACK) for i in range(10)]
SLASH = vsmall.render("/", True, WHITE)
COLON = vsmall.render(":", True, WHITE)

# This function displays a number in a position, very small sized text used.
def putNum(win, num, pos):
    for cnt, i in enumerate(list(str(num))):
        win.blit(NUM[int(i)], (pos[0] + (cnt * 9), pos[1]))

# This function displays a number in a position, Small sized text used.
def putLargeNum(win, num, pos, white=True):
    for cnt, i in enumerate(list(str(num))):
        if white:
            win.blit(LNUM[int(i)], (pos[0] + (cnt * 14), pos[1]))
        else:
            win.blit(BLNUM[int(i)], (pos[0] + (cnt * 14), pos[1]))

# This function displays the date and time in a position on the screen.
def putDT(win, DT, pos):
    var = DT.split()
    date = var[0].split("/")
    time = var[1].split(":")

    for cnt, num in enumerate(map(lambda x: format(int(x), "02"), date)):
        putNum(win, num, (pos[0] + 24 * cnt - 5, pos[1]))

    win.blit(SLASH, (pos[0] + 13, pos[1]))
    win.blit(SLASH, (pos[0] + 35, pos[1]))

    for cnt, num in enumerate(map(lambda x: format(int(x), "02"), time)):
        putNum(win, num, (pos[0] + 24 * cnt, pos[1] + 21))

    win.blit(COLON, (pos[0] + 20, pos[1] + 21))
    win.blit(COLON, (pos[0] + 44, pos[1] + 21))

# This splits a string at regular intervals of "index" characters
def splitstr(string, index=57):
    data = []
    while len(string) >= index:
        data.append(string[:index])
        string = string[index:]
    data.append(string)
    return data

# Defined important globals for loading background image sprites.
BGSPRITE = pygame.image.load(os.path.join("res", "img", "bgsprites.jpg"))
PSPRITE = pygame.image.load(os.path.join("res", "img", "piecesprite.png"))

# Load global image for back
BACK = pygame.image.load(os.path.join("res", "img", "back.png"))

class CHESS:
    PIECES = ({}, {})
    for i, ptype in enumerate(["k", "q", "b", "n", "r", "p"]):
        for side in range(2):
            PIECES[side][ptype] = PSPRITE.subsurface((i * 50, side * 50, 50, 50))

    CHECK = small.render("¡JAQUE!", True, BLACK)
    STALEMATE = small.render("¡TABLAS POR AHOGADO!", True, BLACK)
    CHECKMATE = small.render("¡JAQUE MATE!", True, BLACK)
    LOST = small.render("PERDIDO", True, BLACK)
    CHOOSE = small.render("ESCOGE:", True, BLACK)
    SAVE = small.render("Guardar", True, BLACK)
    UNDO = small.render("Deshacer", True, BLACK)

    MESSAGE = (
        small.render("¿Quieres salir", True, WHITE),
        small.render("de este juego?", True, WHITE),
    )
    
    MESSAGE2 = (
        small.render("Juego guardado. ¿Ahora", True, WHITE),
        small.render("quieres salir?", True, WHITE),
    )

    YES = small.render("SÍ", True, WHITE)
    NO = small.render("NO", True, WHITE)
    MSG = vsmall.render("El juego se guardará con ID", True, WHITE)
    SAVE_ERR = vsmall.render("ERROR: Límite de Guardado Excedido", True, WHITE)

    TURN = (
        small.render("Turno del otro jugador", True, BLACK),
        small.render("Tu turno", True, BLACK),
    )

    DRAW = small.render("Empate", True, BLACK)
    RESIGN = small.render("Renunciar", True, BLACK)
 

    TIMEUP = (
        vsmall.render("¡Tiempo!", True, WHITE),
        vsmall.render("Técnicamente el juego ha terminado, pero", True, WHITE),
        vsmall.render("puedes seguir si lo deseas - :)", True, WHITE),
    )

    OK = small.render("Ok", True, WHITE)
    COL = small.render(":", True, BLACK)

class LOADGAME:
    HEAD = large.render("Cargar Juegos", True, WHITE)
    LIST = medium.render("Lista de Juegos", True, WHITE)
    EMPTY = small.render("No hay juegos guardados aún.....", True, WHITE)
    GAME = small.render("Juego", True, WHITE)
    TYPHEAD = vsmall.render("Tipo:", True, WHITE)
    TYP = {
        "single": vsmall.render("Un Jugador", True, WHITE),
        "mysingle": vsmall.render("Un Jugador", True, WHITE),
        "multi": vsmall.render("Multijugador", True, WHITE),
    }
    DATE = vsmall.render("Fecha-", True, WHITE)
    TIME = vsmall.render("Hora-", True, WHITE)

    DEL = pygame.image.load(os.path.join("res", "img", "delete.jpg"))
    LOAD = small.render("CARGAR", True, WHITE)

    MESSAGE = (
        small.render("¿Estás seguro de que", True, WHITE),
        small.render("quieres eliminar el juego?", True, WHITE),
    )
    YES = small.render("SÍ", True, WHITE)
    NO = small.render("NO", True, WHITE)

    LEFT = medium.render("<", True, WHITE)
    RIGHT = medium.render(">", True, WHITE)
    PAGE = [medium.render("Página " + str(i), True, WHITE) for i in range(1, 5)]

class MAIN:
    HEADING = head.render("Ajedres", True, WHITE)
    VERSION = vsmall.render( "0.4", True, WHITE)
    ICON = pygame.image.load(os.path.join("res", "img", "icon.gif"))
    BG = [BGSPRITE.subsurface((i * 500, 0, 500, 500)) for i in range(4)]

    
    SINGLE = medium.render("Un jugador", True, WHITE)
    MULTI = medium.render("Multijugador", True, WHITE)
    ONLINE = medium.render("En línea", True, WHITE)
    LOAD = medium.render("Cargar Juego", True, WHITE)
    HOWTO = small.render("Cómo jugar", True, WHITE)
    ABOUT = medium.render("Acerca de", True, WHITE)
    PREF = medium.render("Ajustes", True, WHITE)
    STOCK = small.render("Configurar Stockfish", True, WHITE)

    SINGLE_H = medium.render("Un jugador", True, GREY)
    MULTI_H = medium.render("Multijugador", True, GREY)
    ONLINE_H = medium.render("En línea", True, GREY)
    LOAD_H = medium.render("Cargar Juego", True, GREY)
    HOWTO_H = small.render("Cómo jugar", True, GREY)
    ABOUT_H = medium.render("Acerca de", True, GREY)
    PREF_H = medium.render("Ajuster", True, GREY)
    STOCK_H = small.render("Configurar Stockfish", True, GREY)


class PREF:
    HEAD = large.render("Ajustes", True, WHITE)

    SOUNDS = medium.render("Sonidos", True, WHITE)
    FLIP = medium.render("Rotacion", True, WHITE)
    CLOCK = medium.render("Mostrar Reloj", True, WHITE)
    SLIDESHOW = medium.render("Presentación", True, WHITE)
    MOVE = medium.render("Movimientos", True, WHITE)
    UNDO = medium.render("Permitir deshacer", True, WHITE)

    COLON = medium.render(":", True, WHITE)

    TRUE = medium.render("On", True, WHITE)
    FALSE = medium.render("Off", True, WHITE)

    SOUNDS_H = (
        vsmall.render("Reproducir diferentes sonidos", True, WHITE),
        vsmall.render("y música", True, WHITE),
    )
    FLIP_H = (
        vsmall.render("Esto voltea la pantalla", True, WHITE),
        vsmall.render("después de cada movimiento", True, WHITE),
    )
    CLOCK_H = (
        vsmall.render("Mostrar un reloj en el ajedrez", True, WHITE),
        vsmall.render("cuando el temporizador está desactivado", True, WHITE),
    )
    SLIDESHOW_H = (
        vsmall.render("Esto muestra una serie de", True, WHITE),
        vsmall.render("fondos en la pantalla", True, WHITE),
    )
    MOVE_H = (
        vsmall.render("Esto muestra todos los movimientos", True, WHITE),
        vsmall.render("legales de una pieza seleccionada", True, WHITE),
    )
    UNDO_H = (
        vsmall.render("Esto permite deshacer si", True, WHITE),
        vsmall.render("se establece en verdadero", True, WHITE),
    )

    BSAVE = medium.render("Guardar", True, WHITE)
    TIP = vsmall.render("CONSEJO: Pase el mouse sobre la característica", True, WHITE)
    TIP2 = vsmall.render("para saber más al respecto.", True, WHITE)

    PROMPT = (
        vsmall.render("¿Estás seguro de que quieres salir?", True, WHITE),
        vsmall.render("Los cambios no se guardarán.", True, WHITE),
    )

    YES = small.render("SÍ", True, WHITE)
    NO = small.render("NO", True, WHITE)


class ONLINE:
    ERR = (
        vsmall.render("Intentando conectar al servidor..", True, WHITE),
        vsmall.render("[ERR 1] No se pudo encontrar el servidor..", True, WHITE),
        vsmall.render("[ERR 2] Las versiones son incompatibles..", True, WHITE),
        vsmall.render("[ERR 3] El servidor está lleno (máx = 10)..", True, WHITE),
        vsmall.render("[ERR 4] El servidor está bloqueado...", True, WHITE),
        vsmall.render("[ERR 5] Ocurrió un error desconocido...", True, WHITE),
        vsmall.render("Te desconectaste del servidor..", True, WHITE),
    )
    GOBACK = vsmall.render("Volver", True, WHITE)
        
    EMPTY = small.render("No hay nadie conectado, estás solo.", True, WHITE)

    LOBBY = large.render("Lobby Online", True, WHITE)
    LIST = medium.render("Lista de Jugadores", True, WHITE)
    PLAYER = small.render("Jugador", True, WHITE)
    DOT = small.render(".", True, WHITE)

    ACTIVE = small.render("ACTIVO", True, GREEN)
    BUSY = small.render("OCUPADO", True, RED)
    REQ = small.render("Enviar Solicitud", True, WHITE)
    YOUARE = medium.render("Tú Eres", True, WHITE)
    
    ERRCONN = vsmall.render("No se pudo conectar con ese jugador..", True, WHITE)

    REFRESH = pygame.image.load(os.path.join("res", "img", "refresh.png"))

    REQUEST1 = (
        vsmall.render("Por favor espera a que el otro jugador", True, WHITE),
        vsmall.render("acepte tu solicitud. El juego comenzará", True, WHITE),
        vsmall.render("pronto. Jugarás como blancas", True, WHITE),
    )
    REQUEST2 = (
        vsmall.render("El jugador", True, WHITE),
        vsmall.render("quiere jugar contigo.", True, WHITE),
        vsmall.render("Acepta para jugar. Jugarás como negras", True, WHITE),
    )

    DRAW1 = (
        vsmall.render("Enviaste una solicitud a tu oponente para", True, WHITE),
        vsmall.render("empatar, espera la respuesta.", True, WHITE),
    )

    DRAW2 = (
        vsmall.render("Tu oponente está solicitando un", True, WHITE),
        vsmall.render("empate, por favor responde.", True, WHITE),
    )
    
    POPUP = {
        "quit": vsmall.render("El oponente se desconectó", True, WHITE),
        "resign": vsmall.render("El oponente ha renunciado", True, WHITE),
        "draw": vsmall.render("Se ha acordado un empate", True, WHITE),
        "end": vsmall.render("El juego ha terminado, el oponente se fue", True, WHITE),
        "abandon": vsmall.render("El oponente abandonó la partida", True, WHITE),
    }

    NO = small.render("NO", True, WHITE)
    OK = small.render("OK", True, WHITE)

class ONLINEMENU:
    HEAD = large.render("En línea", True, WHITE)
    with open(os.path.join("res", "texts", "online.txt"), encoding="utf-8") as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    CONNECT = small.render("Conectar", True, WHITE)

class SINGLE:
    HEAD = large.render("Un jugador", True, WHITE)
    SELECT = pygame.image.load(os.path.join("res", "img", "select.jpg"))
    CHOOSE = small.render("Elige:", True, WHITE)
    START = small.render("Iniciar", True, WHITE)
    OR = medium.render("O", True, WHITE)
    
    with open(os.path.join("res", "texts", "single1.txt"), encoding="utf-8") as f:
        PARA1 = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    with open(os.path.join("res", "texts", "single2.txt"), encoding="utf-8") as f:
        PARA2 = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]
        
    LEVEL = small.render("Nivel:", True, WHITE)

    BACK = vsmall.render("Volver", True, WHITE)
    _CONFIG = (
        "Parece que no has configurado",
        "Stockfish. Para jugar, necesitas",
        "hacerlo.",
    )
    CONFIG = [vsmall.render(i, True, WHITE) for i in _CONFIG]
    OK = vsmall.render("Ok", True, WHITE)
    NOTNOW = vsmall.render("Ahora No", True, WHITE)


class STOCKFISH:
    HEAD = large.render("Motor Stockfish", True, WHITE)
    CONFIG = small.render("Configurar Stockfish", True, WHITE)
    with open(os.path.join("res", "texts", "stockfish", "stockfish.txt"), "r", encoding="utf-8") as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    with open(os.path.join("res", "texts", "stockfish", "configd.txt"), "r", encoding="utf-8") as f:
        CONFIGURED = [vsmall.render(i, True, GREEN) for i in f.read().splitlines()]

    with open(os.path.join("res", "texts", "stockfish", "nonconfigd.txt"), "r", encoding="utf-8") as f:
        NONCONFIGURED = [vsmall.render(i, True, RED) for i in f.read().splitlines()]

    CLICK = vsmall.render("Haz clic aquí", True, WHITE)
    BACK = vsmall.render("Volver", True, WHITE)
    INSTALL = small.render("Instalar", True, WHITE)
    TEST = vsmall.render(
        "Después de completar todos los pasos, presiona el botón de abajo.", True, WHITE
    )

    WIN_HEAD = small.render("Guía de Instalación para Windows", True, WHITE)
    LIN_HEAD = small.render("Guía de Instalación para Linux -", True, WHITE)
    MAC_HEAD = small.render("Guía de Instalación para Mac", True, WHITE)
    OTH_HEAD = small.render("Guía de Instalación para Otros Sistemas Operativos", True, WHITE)

    with open(os.path.join("res", "texts", "stockfish", "win.txt"), "r", encoding="utf-8") as f:
        WIN_TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    with open(os.path.join("res", "texts", "stockfish", "linux.txt"), "r", encoding="utf-8") as f:
        LIN_TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    with open(os.path.join("res", "texts", "stockfish", "linux2.txt"), "r", encoding="utf-8") as f:
        LIN_TEXT2 = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    with open(os.path.join("res", "texts", "stockfish", "mac.txt"), "r", encoding="utf-8") as f:
        MAC_TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    with open(os.path.join("res", "texts", "stockfish", "other.txt"), "r", encoding="utf-8") as f:
        OTH_TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

    for line in splitstr(os.path.abspath("res/stockfish/build/stockfish.exe")):
        WIN_TEXT.append(vsmall.render(line, True, WHITE))

    for line in splitstr(os.path.abspath("res/stockfish/build/stockfish")):
        LIN_TEXT2.append(vsmall.render(line, True, WHITE))
        OTH_TEXT.append(vsmall.render(line, True, WHITE))

    LOADING = head.render("Cargando", True, WHITE)
    _SUCCESS = ("Configuración exitosa, ahora puedes", "volver y jugar ajedrez.")
    _NOSUCCESS = (
        "Configuración no exitosa, intenta re-",
        "configurar. Sigue las instrucciones",
        "cuidadosamente e intenta de nuevo.",
    )

    SUCCESS = [vsmall.render(i, True, GREEN) for i in _SUCCESS]
    NOSUCCESS = [vsmall.render(i, True, RED) for i in _NOSUCCESS]
    
    PROMPT = (
        small.render("¿Deseas salir?", True, WHITE),
        vsmall.render("Stockfish aún no está configurado.", True, WHITE)
    )
    YES = small.render("Sí", True, WHITE)
    NO = small.render("No", True, WHITE)

class ABOUT:
    HEAD = large.render("Acerca de:", True, WHITE)

    with open(os.path.join("res", "texts", "about.txt"), "r", encoding="utf-8") as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

class HOWTO:
    HEAD = large.render("Cómo Jugar:", True, WHITE)

    with open(os.path.join("res", "texts", "howto.txt"), "r", encoding="utf-8") as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

class TIMER:
    HEAD = large.render("Temporizador", True, WHITE)
    
    YES = small.render("Sí", True, WHITE)
    NO = small.render("No", True, WHITE)
    
    PROMPT = vsmall.render("¿Establecer un temporizador?", True, WHITE)

    with open(os.path.join("res", "texts", "timer.txt"), "r", encoding="utf-8") as f:
        TEXT = [vsmall.render(i, True, WHITE) for i in f.read().splitlines()]

pygame.font.quit()
