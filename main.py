import time
import AmbienteLogico
import pygame

a = AmbienteLogico.tablero()

def comenzar_juego():
    a.llenar_tablero(cantidad)
    a.llenar_tablero_observado(cantidad)
    a.imprimir_tablero()

# dibujar escenario
def escenario():
    # Dibuja el escenario visitado
    for k in range(len(a.puntos_visitados)):
        if a.tablero[int(a.puntos_visitados[k][0])][int(a.puntos_visitados[k][1])] == "brisa":
            screen.blit(brisa_icono, (int(a.puntos_visitados[k][1]) * 100, int(a.puntos_visitados[k][0]) * 100))
        elif a.tablero[int(a.puntos_visitados[k][0])][int(a.puntos_visitados[k][1])] == "hedor":
            screen.blit(hedor_icono, (int(a.puntos_visitados[k][1]) * 100, int(a.puntos_visitados[k][0]) * 100))
        elif a.tablero[int(a.puntos_visitados[k][0])][int(a.puntos_visitados[k][1])] == "vacio":
            screen.blit(vacio_icono, (int(a.puntos_visitados[k][1]) * 100, int(a.puntos_visitados[k][0]) * 100))
        elif a.tablero[int(a.puntos_visitados[k][0])][int(a.puntos_visitados[k][1])] == "b y h":
            screen.blit(byh_icono, (int(a.puntos_visitados[k][1]) * 100, int(a.puntos_visitados[k][0]) * 100))
        elif a.tablero[int(a.puntos_visitados[k][0])][int(a.puntos_visitados[k][1])] == "oro ":
            screen.blit(oro_icono, (int(a.puntos_visitados[k][1]) * 100, int(a.puntos_visitados[k][0]) * 100))
    # Dibuja el escenario no visitado
    for i in range(4):
        for j in range(4):
            if not [str(i), str(j)] in a.puntos_visitados:
                screen.blit(oculto_icono, (j * 100, i * 100))
    screen.blit(puntaje, (10, 420))
    screen.blit(estado, (200, 420))

def personaje():
    if contador != 0:
        if a.pos_actual_x - pos_anterior_x == 1:
            screen.blit(player_frontal_icono, (pos_anterior_y * 100, pos_anterior_x * 100))
        elif a.pos_actual_x - pos_anterior_x == -1:
            screen.blit(player_posterior_icono, (pos_anterior_y * 100, pos_anterior_x * 100))
        elif a.pos_actual_y - pos_anterior_y == 1:
            screen.blit(player_derecha_icono, (pos_anterior_y * 100, pos_anterior_x * 100))
        elif a.pos_actual_y - pos_anterior_y == -1:
            screen.blit(player_izquierda_icono, (pos_anterior_y * 100, pos_anterior_x * 100))
        else:
            screen.blit(player_ganador_icono, (pos_anterior_y * 100, pos_anterior_x * 100))
    else:
        screen.blit(player_frontal_icono, (pos_anterior_y * 100, pos_anterior_x * 100))

pygame.init()
screen = pygame.display.set_mode((400, 450))
pygame.display.set_caption("Mundo de Wumpus")

# Cargar iconos
brisa_icono = pygame.image.load('Graficas/brisa.png')
hedor_icono = pygame.image.load('Graficas/hedor.png')
pozo_icono = pygame.image.load('Graficas/pozo.png')
wumpus_icono = pygame.image.load('Graficas/wumpus.png')
vacio_icono = pygame.image.load('Graficas/vacio.png')
oculto_icono = pygame.image.load('oculto.png')
byh_icono = pygame.image.load('Graficas/b y h.png')
player_frontal_icono = pygame.image.load('Graficas/Bomberman/Frontal.png')
player_posterior_icono = pygame.image.load('Graficas/Bomberman/Posterior.png')
player_derecha_icono = pygame.image.load('Graficas/Bomberman/Derecha.png')
player_izquierda_icono = pygame.image.load('Graficas/Bomberman/Izquierda.png')
player_ganador_icono = pygame.image.load('Graficas/Bomberman/Ganador.png')
oro_icono = pygame.image.load('Graficas/oro.png')

contador = 0
juego = "Jugando..."
# Cargar Letra
font = pygame.font.Font(None, 20)
puntaje = font.render("Puntaje: " + str(0 - contador), True, (255, 255, 255))
estado = font.render("Estado : "+str(juego), True, (255, 255, 255))

cantidad = 4
comenzar_juego()

flag = True
Gameover = False
pos_anterior_x = 0
pos_anterior_y = 0
hedor = a.establecer_inferencias("wumpus", "hedor", cantidad)
brisa = a.establecer_inferencias("pozo", "brisa", cantidad)
# Loop del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not Gameover:
        while not a.actualizar_sensor():
            puntaje = font.render("Puntaje: " + str(0- contador), True, (255, 255, 255))
            time.sleep(1)
            if flag:  # Nos controla si el jugador se regresa o continua por el mismo camino
                a.puntos_visitados.append([str(a.pos_actual_x), str(a.pos_actual_y)])
                flag = a.verificar(hedor, brisa)
                if len(a.posiciones_seguras) != 0:
                    for aux in range(1, len(a.posiciones_seguras), 1):
                        if ([str(a.pos_actual_x), str(a.pos_actual_y)]) == a.posiciones_seguras[aux] and \
                                a.posiciones_seguras[0] in a.puntos_visitados:
                            a.posiciones_seguras = a.posiciones_seguras[aux + 1:]
                            break
                    pos_anterior_x = a.pos_actual_x
                    pos_anterior_y = a.pos_actual_y
                    a.pos_actual_x = int(a.posiciones_seguras[0][0])
                    a.pos_actual_y = int(a.posiciones_seguras[0][1])
                    # a.posiciones_seguras.remove([str(pos_anterior_x), str(pos_anterior_y)])
                    contador += 1
                    screen.fill((0, 0, 0))
                    escenario()
                    personaje()
                    pygame.display.flip()
                    time.sleep(1)
            elif len(a.posiciones_seguras) == 0:
                juego = "No estamos seguros"
                estado = font.render("Estado : " + str(juego), True, (255, 0, 0))
                print("No estamos seguros")
                screen.fill((0, 0, 0))
                escenario()
                personaje()
                pygame.display.flip()
                Gameover = True
                break
            elif a.posiciones_seguras[0] in a.puntos_visitados:
                pos_anterior_x = a.pos_actual_x
                pos_anterior_y = a.pos_actual_y
                a.pos_actual_x = int(a.posiciones_seguras[0][0])
                a.pos_actual_y = int(a.posiciones_seguras[0][1])
                a.posiciones_seguras.remove(a.posiciones_seguras[0])
                screen.fill((0, 0, 0))
                escenario()
                personaje()
                pygame.display.flip()
                time.sleep(1)
            else:
                flag = True
                contador+=1
                pos_anterior_x = a.pos_actual_x
                pos_anterior_y = a.pos_actual_y
                a.pos_actual_x = int(a.posiciones_seguras[0][0])
                a.pos_actual_y = int(a.posiciones_seguras[0][1])
                a.posiciones_seguras.remove(a.posiciones_seguras[0])
                screen.fill((0, 0, 0))
                escenario()
                personaje()
                pygame.display.flip()
                time.sleep(1)
        # Comprueba si ya se termino el juego
        if a.actualizar_sensor():
            juego = "Oro encontrado"
            estado = font.render("Estado : " + str(juego), True, (255, 255, 0))
            puntaje = font.render("Puntaje: " + str(1000 - contador), True, (255, 255, 255))
            pos_anterior_x = a.pos_actual_x
            pos_anterior_y = a.pos_actual_y
            contador += 1
            screen.fill((0, 0, 0))
            escenario()
            personaje()
            pygame.display.flip()
            Gameover = True