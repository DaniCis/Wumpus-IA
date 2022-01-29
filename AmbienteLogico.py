import random

class tablero(object):
    def __init__(self):
        self.tablero_observado = [] #Conocimiento
        #self.tablero = [['vacio', 'vacio', 'vacio', 'vacio'], ['vacio', 'oro ', 'brisa', 'brisa'], ['vacio', 'b y h', 'pozo', 'pozo'], ['hedor', 'wumpus', 'pozo', 'brisa']]
        self.tablero = []
        self.pos_actual_x = 0
        self.pos_actual_y = 0
        self.posiciones_seguras = []
        self.puntos_visitados=[]

    def llenar_tablero(self, cantidad):
        # Se llena con espacios vacios
        for i in range(cantidad):
            fila = []
            for j in range(cantidad):
                fila.append("vacio")
            self.tablero.append(fila)

        # Generar pozos
        for i in range(cantidad):
            for j in range(cantidad):
                num_random = random.randint(1, 5)
                if num_random == 5 and (i != 0 and j != 0):
                    self.tablero[i][j] = "pozo"
                    if i == cantidad - 1 and j == cantidad - 1:
                        if self.tablero[i - 1][j] != "pozo":
                            self.tablero[i - 1][j] = "brisa"
                        if self.tablero[i][j - 1] != "pozo":
                            self.tablero[i][j - 1] = "brisa"
                    elif i == cantidad - 1 and j == 0:
                        if self.tablero[i - 1][j] != "pozo":
                            self.tablero[i - 1][j] = "brisa"
                        if self.tablero[i][j + 1] != "pozo":
                            self.tablero[i][j + 1] = "brisa"
                    elif i == 0 and j == cantidad - 1:
                        if self.tablero[i + 1][j] != "pozo":
                            self.tablero[i + 1][j] = "brisa"
                        if self.tablero[i][j - 1] != "pozo":
                            self.tablero[i][j - 1] = "brisa"
                    elif i == 0:
                        if self.tablero[i + 1][j] != "pozo":
                            self.tablero[i + 1][j] = "brisa"
                        if self.tablero[i][j + 1] != "pozo":
                            self.tablero[i][j + 1] = "brisa"
                        if self.tablero[i][j - 1] != "pozo":
                            self.tablero[i][j - 1] = "brisa"
                    elif j == 0:
                        if self.tablero[i][j + 1] != "pozo":
                            self.tablero[i][j + 1] = "brisa"
                        if self.tablero[i + 1][j] != "pozo":
                            self.tablero[i + 1][j] = "brisa"
                        if self.tablero[i - 1][j] != "pozo":
                            self.tablero[i - 1][j] = "brisa"
                    elif i == cantidad - 1:
                        if self.tablero[i - 1][j] != "pozo":
                            self.tablero[i - 1][j] = "brisa"
                        if self.tablero[i][j + 1] != "pozo":
                            self.tablero[i][j + 1] = "brisa"
                        if self.tablero[i][j - 1] != "pozo":
                            self.tablero[i][j - 1] = "brisa"
                    elif j == cantidad - 1:
                        if self.tablero[i][j - 1] != "pozo":
                            self.tablero[i][j - 1] = "brisa"
                        if self.tablero[i + 1][j] != "pozo":
                            self.tablero[i + 1][j] = "brisa"
                        if self.tablero[i - 1][j] != "pozo":
                            self.tablero[i - 1][j] = "brisa"
                    else:
                        if self.tablero[i + 1][j] != "pozo":
                            self.tablero[i + 1][j] = "brisa"
                        if self.tablero[i - 1][j] != "pozo":
                            self.tablero[i - 1][j] = "brisa"
                        if self.tablero[i][j + 1] != "pozo":
                            self.tablero[i][j + 1] = "brisa"
                        if self.tablero[i][j - 1] != "pozo":
                            self.tablero[i][j - 1] = "brisa"

        # Generar Wumpus
        wumpus = True
        while wumpus:
            wumpus_x = random.randint(0, cantidad - 1)
            wumpus_y = random.randint(0, cantidad - 1)
            if (wumpus_y == 0 and wumpus_x == 0) or self.tablero[wumpus_x][wumpus_y] == "pozo":
                wumpus = True
            else:
                self.tablero[wumpus_x][wumpus_y] = "wumpus"
                wumpus = False
                if wumpus_x == cantidad - 1 and wumpus_y == cantidad - 1:
                    if self.tablero[wumpus_x - 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x - 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x - 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x - 1][wumpus_y] = "hedor"
                    if self.tablero[wumpus_x][wumpus_y - 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y - 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y - 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y - 1] = "hedor"
                elif wumpus_x == cantidad - 1 and wumpus_y == 0:
                    if self.tablero[wumpus_x - 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x - 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x - 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x - 1][wumpus_y] = "hedor"
                    if self.tablero[wumpus_x][wumpus_y + 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y + 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y + 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y + 1] = "hedor"
                elif wumpus_x == 0 and wumpus_y == cantidad - 1:
                    if self.tablero[wumpus_x + 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x + 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x + 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x + 1][wumpus_y] = "hedor"
                    if self.tablero[wumpus_x][wumpus_y - 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y - 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y - 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y - 1] = "hedor"
                elif wumpus_x == 0:
                    if self.tablero[wumpus_x + 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x + 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x + 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x + 1][wumpus_y] = "hedor"
                    if self.tablero[wumpus_x][wumpus_y + 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y + 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y + 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y + 1] = "hedor"
                    if self.tablero[wumpus_x][wumpus_y - 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y - 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y - 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y - 1] = "hedor"
                elif wumpus_y == 0:
                    if self.tablero[wumpus_x][wumpus_y + 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y + 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y + 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y + 1] = "hedor"
                    if self.tablero[wumpus_x + 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x + 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x + 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x + 1][wumpus_y] = "hedor"
                    if self.tablero[wumpus_x - 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x - 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x - 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x - 1][wumpus_y] = "hedor"
                elif wumpus_x == cantidad - 1:
                    if self.tablero[wumpus_x - 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x - 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x - 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x - 1][wumpus_y] = "hedor"
                    if self.tablero[wumpus_x][wumpus_y + 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y + 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y + 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y + 1] = "hedor"
                    if self.tablero[wumpus_x][wumpus_y - 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y - 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y - 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y - 1] = "hedor"
                elif wumpus_y == cantidad - 1:
                    if self.tablero[wumpus_x][wumpus_y - 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y - 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y - 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y - 1] = "hedor"
                    if self.tablero[wumpus_x + 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x + 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x + 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x + 1][wumpus_y] = "hedor"
                    if self.tablero[wumpus_x - 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x - 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x - 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x - 1][wumpus_y] = "hedor"
                else:
                    if self.tablero[wumpus_x + 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x + 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x + 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x + 1][wumpus_y] = "hedor"
                    if self.tablero[wumpus_x - 1][wumpus_y] == "brisa":
                        self.tablero[wumpus_x - 1][wumpus_y] = "b y h"
                    elif self.tablero[wumpus_x - 1][wumpus_y] == "vacio":
                        self.tablero[wumpus_x - 1][wumpus_y] = "hedor"
                    if self.tablero[wumpus_x][wumpus_y + 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y + 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y + 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y + 1] = "hedor"
                    if self.tablero[wumpus_x][wumpus_y - 1] == "brisa":
                        self.tablero[wumpus_x][wumpus_y - 1] = "b y h"
                    elif self.tablero[wumpus_x][wumpus_y - 1] == "vacio":
                        self.tablero[wumpus_x][wumpus_y - 1] = "hedor"

        # Generar Oro
        Oro = True
        while Oro:
            oro_x = random.randint(0, cantidad-1)
            oro_y = random.randint(0, cantidad-1)
            if (self.tablero[oro_x][oro_y] == "vacio" or self.tablero[oro_x][oro_y] == "hedor" or self.tablero[oro_x][oro_y] == "brisa") and (oro_x != 0 and oro_y != 0):
                if self.tablero[oro_x][oro_y] == "wumpus":
                    self.tablero[oro_x][oro_y] = "o y w"
                else:
                    self.tablero[oro_x][oro_y] = "oro "
                Oro = False

    #LLenamos el arreglo de sensores con el siguiente orden
    # 0 Seguro 1 Brisa, 2 Hedor, 3 Resplandor, 4 Grito, 5 Golpe

    def llenar_tablero_observado(self, cantidad):
        for i in range(cantidad):
            fila = []
            for j in range(cantidad):
                sensores = []
                aux = []
                for l in range(2):
                    aux.append("vacio")
                sensores.append(aux)
                for k in range(5): #Sensores del mundo conocido
                    sensores.append(False)
                fila.append(sensores)
            self.tablero_observado.append(fila)

    def actualizar_sensor(self):
        if self.tablero[self.pos_actual_x][self.pos_actual_y] == "oro ":
            self.puntos_visitados.append([str(self.pos_actual_x), str(self.pos_actual_y)])
            print("Oro encontrado")
            return True
        elif self.tablero[self.pos_actual_x][self.pos_actual_y] == "pozo" or self.tablero[self.pos_actual_x][self.pos_actual_y] == "wumpus":
            return True
        elif self.tablero[self.pos_actual_x][self.pos_actual_y] == "brisa":
            self.tablero_observado[self.pos_actual_x][self.pos_actual_y][1] = True
        elif self.tablero[self.pos_actual_x][self.pos_actual_y] == "hedor":
            self.tablero_observado[self.pos_actual_x][self.pos_actual_y][2] = True
        elif self.tablero[self.pos_actual_x][self.pos_actual_y] == "b y h":
            self.tablero_observado[self.pos_actual_x][self.pos_actual_y][1] = True
            self.tablero_observado[self.pos_actual_x][self.pos_actual_y][2] = True
        if self.pos_actual_x == 0 or self.pos_actual_x == len(self.tablero[1])-1 or self.pos_actual_y == 0 or self.pos_actual_y == len(self.tablero[0])-1:
            self.tablero_observado[self.pos_actual_x][self.pos_actual_y][5] = True
        return False

    def establecer_inferencias(self, muerte, peligro, cantidad):
        inferencias = []
        for i in range(cantidad):
            fila = []
            for j in range(cantidad):
                clausula = []
                if (i == 0 and j == 0) or (i == cantidad - 1 and j == cantidad - 1) or (i == cantidad - 1 and j == 0) or (i == 0 and j == cantidad - 1):
                    for k in range(2):
                        termino = []
                        termino.append("vacio")
                        termino.append("vacio")
                        clausula.append(termino)
                elif (i == 0) or (j == 0) or (i == cantidad - 1) or (j == cantidad - 1):
                    for k in range(3):
                        termino = []
                        termino.append("vacio")
                        termino.append("vacio")
                        clausula.append(termino)
                else:
                    for k in range(4):
                        termino = []
                        termino.append("vacio")
                        termino.append("vacio")
                        clausula.append(termino)
                fila.append(clausula)
            inferencias.append(fila)

        for i in range(cantidad):
            for j in range(cantidad):
                if i == 0 and j == 0:
                    # Esquina superior izquierda
                    inferencias[i][j][0][0] = "!" + muerte + str(i + 1) + str(j) #!wumpus10
                    inferencias[i][j][0][1] = peligro + str(i) + str(j)
                    inferencias[i][j][1][0] = "!" + muerte + str(i) + str(j + 1)
                    inferencias[i][j][1][1] = peligro + str(i) + str(j)
                elif i == cantidad - 1 and j == cantidad - 1:
                    # Esquina inferior derecha
                    inferencias[i][j][0][0] = "!" + muerte + str(i - 1) + str(j)
                    inferencias[i][j][0][1] = peligro + str(i) + str(j)
                    inferencias[i][j][1][0] = "!" + muerte + str(i) + str(j - 1)
                    inferencias[i][j][1][1] = peligro + str(i) + str(j)
                elif i == cantidad - 1 and j == 0:
                    # Esquina derecha superior
                    inferencias[i][j][0][0] = "!" + muerte + str(i - 1) + str(j)
                    inferencias[i][j][0][1] = peligro + str(i) + str(j)
                    inferencias[i][j][1][0] = "!" + muerte + str(i) + str(j + 1)
                    inferencias[i][j][1][1] = peligro + str(i) + str(j)
                elif i == 0 and j == cantidad - 1:
                    # Esquina inferior izquierda
                    inferencias[i][j][0][0] = "!" + muerte + str(i + 1) + str(j)
                    inferencias[i][j][0][1] = peligro + str(i) + str(j)
                    inferencias[i][j][1][0] = "!" + muerte + str(i) + str(j - 1)
                    inferencias[i][j][1][1] = peligro + str(i) + str(j)
                elif i == 0:
                    inferencias[i][j][0][0] = "!" + muerte + str(i + 1) + str(j)
                    inferencias[i][j][0][1] = peligro + str(i) + str(j)
                    inferencias[i][j][1][0] = "!" + muerte + str(i) + str(j + 1)
                    inferencias[i][j][1][1] = peligro + str(i) + str(j)
                    inferencias[i][j][2][0] = "!" + muerte + str(i) + str(j - 1)
                    inferencias[i][j][2][1] = peligro + str(i) + str(j)
                elif j == 0:
                    inferencias[i][j][0][0] = "!" + muerte + str(i + 1) + str(j)
                    inferencias[i][j][0][1] = peligro + str(i) + str(j)
                    inferencias[i][j][1][0] = "!" + muerte + str(i - 1) + str(j)
                    inferencias[i][j][1][1] = peligro + str(i) + str(j)
                    inferencias[i][j][2][0] = "!" + muerte + str(i) + str(j + 1)
                    inferencias[i][j][2][1] = peligro + str(i) + str(j)
                elif i == cantidad - 1:
                    inferencias[i][j][0][0] = "!" + muerte + str(i - 1) + str(j)
                    inferencias[i][j][0][1] = peligro + str(i) + str(j)
                    inferencias[i][j][1][0] = "!" + muerte + str(i) + str(j + 1)
                    inferencias[i][j][1][1] = peligro + str(i) + str(j)
                    inferencias[i][j][2][0] = "!" + muerte + str(i) + str(j - 1)
                    inferencias[i][j][2][1] = peligro + str(i) + str(j)
                elif j == cantidad - 1:
                    inferencias[i][j][0][0] = "!" + muerte + str(i) + str(j - 1)
                    inferencias[i][j][0][1] = peligro + str(i) + str(j)
                    inferencias[i][j][1][0] = "!" + muerte + str(i + 1) + str(j)
                    inferencias[i][j][1][1] = peligro + str(i) + str(j)
                    inferencias[i][j][2][0] = "!" + muerte + str(i - 1) + str(j)
                    inferencias[i][j][2][1] = peligro + str(i) + str(j)
                else:
                    inferencias[i][j][0][0] = "!" + muerte + str(i + 1) + str(j)
                    inferencias[i][j][0][1] = peligro + str(i) + str(j)
                    inferencias[i][j][1][0] = "!" + muerte + str(i - 1) + str(j)
                    inferencias[i][j][1][1] = peligro + str(i) + str(j)
                    inferencias[i][j][2][0] = "!" + muerte + str(i) + str(j + 1)
                    inferencias[i][j][2][1] = peligro + str(i) + str(j)
                    inferencias[i][j][3][0] = "!" + muerte + str(i) + str(j - 1)
                    inferencias[i][j][3][1] = peligro + str(i) + str(j)
        return inferencias

    def verificar(self, hedor_inferencia, brisa_inferencia):
        flag = True
        self.tablero_observado[self.pos_actual_x][self.pos_actual_y][0] = []
        #Llenar la base de conocimiento provenientes de los sensores
        if self.tablero_observado[self.pos_actual_x][self.pos_actual_y][1]:
            self.tablero_observado[self.pos_actual_x][self.pos_actual_y][0].append("brisa" + str(self.pos_actual_x) + str(self.pos_actual_y))
        else:
            self.tablero_observado[self.pos_actual_x][self.pos_actual_y][0].append("!brisa" + str(self.pos_actual_x) + str(self.pos_actual_y))
        if self.tablero_observado[self.pos_actual_x][self.pos_actual_y][2]:
            self.tablero_observado[self.pos_actual_x][self.pos_actual_y][0].append("hedor" + str(self.pos_actual_x) + str(self.pos_actual_y))
        else:
            self.tablero_observado[self.pos_actual_x][self.pos_actual_y][0].append("!hedor" + str(self.pos_actual_x) + str(self.pos_actual_y))
        posiciones = []
        for aux in range(2):
            for i in range(len(hedor_inferencia[self.pos_actual_x][self.pos_actual_y])):# compara las inferencias con las clausulas de la posicion actual
                if aux == 0:
                    alfa = str(brisa_inferencia[self.pos_actual_x][self.pos_actual_y][i][0])
                    alfa = alfa.replace("!", "")
                    if not [str(alfa[4]), str(alfa[5])] in self.posiciones_seguras:
                        posiciones.append([alfa[4], alfa[5]])
                        posiciones.append([str(self.pos_actual_x), str(self.pos_actual_y)])
                    if self.tablero_observado[self.pos_actual_x][self.pos_actual_y][0][aux] != brisa_inferencia[self.pos_actual_x][self.pos_actual_y][i][1]:
                        if brisa_inferencia[self.pos_actual_x][self.pos_actual_y][i][0] != alfa and flag != False:
                            self.tablero_observado[int(alfa[4])][int(alfa[5])][0] = "segura"
                    else:
                        self.tablero_observado[int(alfa[4])][int(alfa[5])][0] = "no"
                        flag = False
                else:
                    alfa = str(hedor_inferencia[self.pos_actual_x][self.pos_actual_y][i][0])
                    alfa = alfa.replace("!", "")
                    if self.tablero_observado[self.pos_actual_x][self.pos_actual_y][0][aux] != \
                            hedor_inferencia[self.pos_actual_x][self.pos_actual_y][i][1]:
                        if hedor_inferencia[self.pos_actual_x][self.pos_actual_y][i][0] != alfa and flag != False:
                            self.tablero_observado[int(alfa[6])][int(alfa[7])][0] = "segura"
                    else:
                        self.tablero_observado[int(alfa[6])][int(alfa[7])][0] = "no"
                        flag = False

        if self.tablero_observado[int(posiciones[0][0])][int(posiciones[0][1])][0] == "segura":
            if len(self.posiciones_seguras) != 0:
                self.posiciones_seguras.remove(self.posiciones_seguras[0])
            self.posiciones_seguras = posiciones + self.posiciones_seguras
            #print(self.posiciones_seguras)
        return flag

    def imprimir_tablero(self):
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero)):
                print(self.tablero[i][j], end="\t")
            print("")
