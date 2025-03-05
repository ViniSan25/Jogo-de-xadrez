class Xadrez:

    def __init__(self):
        self.matriz = []
        for i in range(8):
            linha = [] 
            for j in range(8):
                linha.append(".")
            self.matriz.append(linha)
        

        self.tabAtual = []
        self.turno = "brancas"
        self.jogadas = []

    def criarTabuleiro(self):
        for i in range(8):
            self.matriz[6][i] = "P"
        
        for i in range(8):
            self.matriz[1][i] = "p"

        self.matriz[7][0] = "T"
        self.matriz[7][1] = "C"
        self.matriz[7][2] = "B"
        self.matriz[7][3] = "D"
        self.matriz[7][4] = "R"
        self.matriz[7][5] = "B"
        self.matriz[7][6] = "C"
        self.matriz[7][7] = "T"

        self.matriz[0][0] = "t"
        self.matriz[0][1] = "c"
        self.matriz[0][2] = "b"
        self.matriz[0][3] = "d"
        self.matriz[0][4] = "r"
        self.matriz[0][5] = "b"
        self.matriz[0][6] = "c"
        self.matriz[0][7] = "t"

        self.tabAtual = []
        for linha in self.matriz:
            nova_linha = []
            for elemento in linha:
                nova_linha.append(elemento)
            self.tabAtual.append(nova_linha)

    


    def printarTabuleiro(self):
        linhaRef = ['A  B   C   D   E   F   G   H']
        print(linhaRef)
        print("  -----------------------------")
        colunaRef = []
        for i in range(9, 0, -1):
            colunaRef.append(i)
        k = 1

        for linha in self.tabAtual:
            for elemento in linha:
                print(f"'{elemento}'", end=" ")
            
            print('|', colunaRef[k])
            k+=1
            print()

    
            
  
    
    def verificarTurno(self, pedra):
            if (self.turno == 'brancas' and pedra.isupper()) or (self.turno == 'pretas' and pedra.islower()):
                return True
            return False
    
    def mudarTurno(self):
        if self.turno == 'brancas':
            self.turno = 'pretas'
        else:
            self.turno = 'brancas'

    def movimentoRei(self, pedra, x, y):
        movimentos_validos = []
        possiveis_movimentos = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),         (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for dx, dy in possiveis_movimentos:
            nx, ny = x + dx, y + dy

            if 0 <= nx < 8 and 0 <= ny < 8:
                destino = self.tabAtual[nx][ny]

                if destino == ".":  # Movimento livre
                    movimentos_validos.append((x, y, nx, ny))
                elif (pedra.isupper() and destino.islower()) or (pedra.islower() and destino.isupper()):
                    # Captura de peça adversária
                    movimentos_validos.append((x, y, nx, ny))

        return movimentos_validos

    def movimentoBispo(self, pedra, x, y):
        possiveis_movimentos = [
            (-1, +1), (-1, -1), (1, +1), (1, -1)
        ]
        movimentos_validos = []

        for dx, dy in possiveis_movimentos:
            nx, ny = x + dx, y + dy

            while 0 <= nx < 8 and 0 <= ny < 8:
                destino = self.tabAtual[nx][ny]

                if destino == ".":
                    movimentos_validos.append((x, y, nx, ny))
                elif (pedra.isupper() and destino.islower()) or (pedra.islower() and destino.isupper()):
                    movimentos_validos.append((x, y, nx, ny))
                    break  
                else:
                    break  

                nx += dx
                ny += dy

        return movimentos_validos

    def movimentoDama(self, pedra, x, y):
        movimentos_validos = []

        # Movimentos possíveis da Dama: combina os movimentos de Torre e Bispo
        direcoes = [
            (-1, 0), (1, 0), (0, -1), (0, 1),  # Movimentos verticais e horizontais (Torre)
            (-1, -1), (-1, 1), (1, -1), (1, 1)  # Movimentos diagonais (Bispo)
        ]
        
        # Itera por todas as direções possíveis
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            
            while 0 <= nx < 8 and 0 <= ny < 8:
                destino = self.tabAtual[nx][ny]

                if destino == ".":  # Casa vazia, movimento válido
                    movimentos_validos.append((x, y, nx, ny))
                elif (pedra.isupper() and destino.islower()) or (pedra.islower() and destino.isupper()):
                    # Peça adversária, captura válida
                    movimentos_validos.append((x, y, nx, ny))
                    break  # Depois de capturar, a Dama não pode continuar indo nessa direção
                else:
                    break  # Se encontrar uma peça da mesma cor, não pode continuar movendo nessa direção

                # Continua o movimento na direção atual
                nx += dx
                ny += dy

        return movimentos_validos


    def movimentoPeao(self, pedra, x, y):
        movimentos_validos = []

        if pedra == 'p':
            if x + 1 < 8: 
                destino = self.tabAtual[x+1][y]
                if destino == '.':
                    movimentos_validos.append((x, y, x+1, y))

            if x == 1 and x + 2 < 8:  
                destino = self.tabAtual[x+2][y]
                if destino == '.':
                    movimentos_validos.append((x, y, x+2, y))

            if x + 1 < 8 and y + 1 < 8:  
                captura1 = self.tabAtual[x+1][y+1]
                if captura1 != '.' and captura1.isupper():
                    movimentos_validos.append((x, y, x+1, y+1))

            if x + 1 < 8 and y - 1 >= 0:  
                captura2 = self.tabAtual[x+1][y-1]
                if captura2 != '.' and captura2.isupper():
                    movimentos_validos.append((x, y, x+1, y-1))

            return movimentos_validos

        if pedra == 'P':
            if x - 1 >= 0: 
                destino = self.tabAtual[x-1][y]
                if destino == '.':
                    movimentos_validos.append((x, y, x-1, y))

            if x == 6 and x - 2 >= 0:  
                destino = self.tabAtual[x-2][y]
                if destino == '.':
                    movimentos_validos.append((x, y, x-2, y))

            if x - 1 >= 0 and y + 1 < 8: 
                captura1 = self.tabAtual[x-1][y+1]
                if captura1 != '.' and captura1.islower():
                    movimentos_validos.append((x, y, x-1, y+1))

            if x - 1 >= 0 and y - 1 >= 0: 
                captura2 = self.tabAtual[x-1][y-1]
                if captura2 != '.' and captura2.islower():
                    movimentos_validos.append((x, y, x-1, y-1))

            return movimentos_validos

            



    def movimentoCavalo(self, pedra, x, y):
        movimentos_validos = []
        possiveis_movimentos = [
            (-2, 1), (-2, -1), (2, 1), (2, -1),
            (-1, 2), (-1, -2), (1, 2), (1, -2)
        ]
        for dx, dy in possiveis_movimentos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                destino = self.tabAtual[nx][ny]
                if destino == ".":
                    movimentos_validos.append((x, y, nx, ny))
                else:
                    if pedra.isupper() and destino.islower():
                        movimentos_validos.append((x, y, nx, ny))
                    elif pedra.islower() and destino.isupper():
                        movimentos_validos.append((x, y, nx, ny))
        return movimentos_validos


    def movimentoTorre(self, pedra, x, y):
        movimentos_validos = []
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy

            while 0 <= nx < 8 and 0 <= ny < 8:
                destino = self.tabAtual[nx][ny]

                if destino == ".":
                    movimentos_validos.append((x, y, nx, ny))
                elif (pedra.isupper() and destino.islower()) or (pedra.islower() and destino.isupper()):
                    movimentos_validos.append((x, y, nx, ny))
                    break  
                else:
                    break  

                nx += dx
                ny += dy

        return movimentos_validos
    
    def emXeque(self, cor, tabuleiro=None):
        if tabuleiro is None:
            tabuleiro = self.tabAtual  # Usar o tabuleiro atual se não for fornecido um

        if cor == 'brancas':
            rei = 'R'
        else:
            rei = 'r'

        # Encontrar a posição do rei
        rei_x, rei_y = -1, -1
        for i in range(8):
            for j in range(8):
                if tabuleiro[i][j] == rei:
                    rei_x, rei_y = i, j
                    break  # Sai do loop interno
            if rei_x != -1:  # Se já encontrou o rei, sai do loop externo também
                break  

        for i in range(8):
            for j in range(8):
                pedra = tabuleiro[i][j]
                if pedra == ".":
                    continue  # Ignora as casas vazias

                # Se for peça do oponente, verificar se pode atacar o rei
                if (cor == 'brancas' and pedra.islower()) or (cor == 'pretas' and pedra.isupper()):
                    if self.validarLance(pedra, (i, j), (rei_x, rei_y), checkTurn=False):
                        return True  # Retorna True se a peça pode atacar o rei
        return False
    
    def buscarTodosLances(self):
        lances_possiveis = []
        cor_atual = self.turno  # "brancas" ou "pretas"

        # Percorre todas as casas do tabuleiro
        for i in range(8):
            for j in range(8):
                peca = self.tabAtual[i][j]

                # Verifica se a peça pertence à cor que está no turno
                if (cor_atual == "brancas" and peca.isupper()) or (cor_atual == "pretas" and peca.islower()):
                    
                    # Testa todos os possíveis movimentos dentro do tabuleiro (8x8)
                    if peca.upper() == 'T':  # Torre
                        movimentos_validos = self.movimentoTorre(peca, i, j)
                    elif peca.upper() == 'C':  # Cavalo
                        movimentos_validos = self.movimentoCavalo(peca, i, j)
                    elif peca.upper() == 'P':  # Peão
                        movimentos_validos = self.movimentoPeao(peca, i, j)
                    elif peca.upper() == 'B':  # Bispo
                        movimentos_validos = self.movimentoBispo(peca, i, j)

                    elif peca.upper() == 'R':  # Rei
                        movimentos_validos = self.movimentoRei(peca, i, j)
                        resultado_roque = self.pode_fazer_roque(cor_atual)
                        if resultado_roque == 'roque pequeno':
                            lances_possiveis.append(((i, j), (i, j + 2)))
                        elif resultado_roque == 'roque grande':
                            lances_possiveis.append(((i, j), (i, j - 2)))

                    elif peca.upper() == 'D':  # Dama
                        movimentos_validos = self.movimentoDama(peca, i, j)
                    
                    else:
                        continue  # Se a peça ainda não foi implementada, ignora

                    # Valida cada movimento antes de adicionar
                    for movimento in movimentos_validos:
                        destino_i, destino_j = movimento[2], movimento[3]
                        
                        # Validação do lance 
                        if self.tabAtual[destino_i][destino_j] != '.':  # Se a casa de destino não estiver vazia
                            peca_destino = self.tabAtual[destino_i][destino_j]
                            if (cor_atual == "brancas" and peca_destino.isupper()) or (cor_atual == "pretas" and peca_destino.islower()):
                                continue  # Se a casa de destino tem uma peça da mesma cor, ignora o movimento

                        # Se o movimento é válido, adiciona
                        lances_possiveis.append(((i, j), (destino_i, destino_j)))

        return lances_possiveis

    def simularMovimento(self, origem, destino):
        """Retorna uma cópia do tabuleiro após um movimento."""
        tabuleiro_simulado = [linha[:] for linha in self.tabAtual]  # Copia o tabuleiro
        origem_x, origem_y = origem
        destino_x, destino_y = destino
        pedra = tabuleiro_simulado[origem_x][origem_y]

        tabuleiro_simulado[destino_x][destino_y] = pedra
        tabuleiro_simulado[origem_x][origem_y] = "."

        return tabuleiro_simulado

    def pode_fazer_roque(self, cor):
        # Define as posições iniciais do rei e das torres com base na cor
        if self.emXeque(cor):
            return False

        if cor == 'brancas':
            rei_pos = (7, 4)
            torre_esq_pos = (7, 0)
            torre_dir_pos = (7, 7)
        else:  # cor == 'pretas'
            rei_pos = (0, 4)
            torre_esq_pos = (0, 0)
            torre_dir_pos = (0, 7)
        
        # Verifica se o rei ou as torres já se moveram
        for jogada in self.jogadas:
            if jogada[0] == rei_pos:
                return False
            if jogada[0] == torre_esq_pos:
                return False
            if jogada[0] == torre_dir_pos:
                return False
        
        # Verifica se o rei está em xeque ou passará por casas atacadas
        lances_adversarios = self.buscarTodosLances()
        casas_proibidas = {lance[1] for lance in lances_adversarios}
        
        if rei_pos in casas_proibidas:
            return False
        
        # Verifica se há peças entre o rei e as torres e se as casas por onde o rei passará não estão sob ataque
        # Roque grande (movimento para a esquerda)
        if self.tabAtual[rei_pos[0]][1] == '.' and self.tabAtual[rei_pos[0]][2] == '.' and self.tabAtual[rei_pos[0]][3] == '.':
            if (rei_pos[0], 2) not in casas_proibidas and (rei_pos[0], 3) not in casas_proibidas:
                return 'roque grande'
        
        # Roque pequeno (movimento para a direita)
        if self.tabAtual[rei_pos[0]][5] == '.' and self.tabAtual[rei_pos[0]][6] == '.':
            if (rei_pos[0], 5) not in casas_proibidas and (rei_pos[0], 6) not in casas_proibidas:
                return 'roque pequeno'
        
        return False




    def validarLance(self, pedra, origem, destino, checkTurn=True):

        
        origem_x, origem_y = origem
        destino_x, destino_y = destino

        if (origem_x > 7 or origem_y > 7 or destino_x > 7 or destino_y > 7 or
            origem_x < 0 or origem_y < 0 or destino_x < 0 or destino_y < 0):
            print("Lance inválido: Posições fora do tabuleiro")
            return

        # Verifica o turno apenas se checkTurn for True
        if checkTurn and not self.verificarTurno(pedra):
            return "Lance inválido: Não é a vez dessa cor"

        # Valida o movimento da peça
        if pedra.upper() == 'T':  # Torre
            movimentos_validos = self.movimentoTorre(pedra, origem_x, origem_y)
        elif pedra.upper() == 'C':  # Cavalo
            movimentos_validos = self.movimentoCavalo(pedra, origem_x, origem_y)
        elif pedra.upper() == 'P':  # Peão
            movimentos_validos = self.movimentoPeao(pedra, origem_x, origem_y)
        elif pedra.upper() == 'B':  # Bispo
            movimentos_validos = self.movimentoBispo(pedra, origem_x, origem_y)

        elif pedra.upper() == 'R':  # Rei
            movimentos_validos = self.movimentoRei(pedra, origem_x, origem_y)
            resultado_roque = self.pode_fazer_roque(self.turno)
            if resultado_roque == 'roque pequeno':
                movimentos_validos.append(((origem_x), (origem_y + 2)))
            elif resultado_roque == 'roque grande':
                movimentos_validos.append(((origem_x), (origem_y - 2)))

        elif pedra.upper() == 'D':  # Dama
            movimentos_validos = self.movimentoDama(pedra, origem_x, origem_y)
        else:
            return "Movimentação para essa peça ainda não foi implementada."

        if (origem_x, origem_y, destino_x, destino_y) not in movimentos_validos:
            return "Lance inválido para a peça!"

        # Simula o movimento e verifica se o rei ficará em xeque
        tabuleiro_simulado = self.simularMovimento(origem, destino)
        if self.emXeque(self.turno, tabuleiro_simulado):
            return "Movimento inválido: Rei ainda em xeque!"

        return None  # Retorna None se o lance for válido
            


    def moverPedra(self, origem, destino):
        origem_x, origem_y = origem
        destino_x, destino_y = destino
        pedra = self.tabAtual[origem_x][origem_y]

        # Verifica se o turno está correto
        if not self.verificarTurno(pedra):
            print("Lance inválido: Não é a vez dessa cor")
            return

        # Verifica se o movimento é um roque (movimento de 2 casas para os lados)
        if (destino_x, destino_y) == (origem_x, origem_y + 2) or (destino_x, destino_y) == (origem_x, origem_y - 2):
            resultado_roque = self.pode_fazer_roque(self.tabAtual, self.turno)
            if resultado_roque:
                if resultado_roque == "roque grande":
                    # Roque grande: rei vai de (x,4) para (x,2) e torre de (x,0) para (x,3)
                    self.tabAtual[origem_x][origem_y] = "."  # Remove o rei da posição original
                    self.tabAtual[origem_x][origem_y - 2] = "R" if self.turno == 'brancas' else "r"
                    self.tabAtual[origem_x][0] = "."  # Remove a torre da posição original
                    self.tabAtual[origem_x][3] = "T" if self.turno == 'brancas' else "t"
                    print("Roque grande realizado!")
                elif resultado_roque == "roque pequeno":
                    # Roque pequeno: rei vai de (x,4) para (x,6) e torre de (x,7) para (x,5)
                    self.tabAtual[origem_x][origem_y] = "."
                    self.tabAtual[origem_x][origem_y + 2] = "R" if self.turno == 'brancas' else "r"
                    self.tabAtual[origem_x][7] = "."
                    self.tabAtual[origem_x][5] = "T" if self.turno == 'brancas' else "t"
                    print("Roque pequeno realizado!")
                self.mudarTurno()  # Troca de turno após o roque
                self.jogadas.append((origem, destino))
                return
            else:
                print("Roque inválido!")
                return

        # Se não for roque, valida o lance normalmente
        if not self.validarLance(pedra, origem, destino):
            print("Lance inválido: Movimento não permitido para essa peça")
            return

        # Movimento normal da peça
        self.tabAtual[destino_x][destino_y] = pedra
        self.tabAtual[origem_x][origem_y] = "."

        # Registra a jogada e muda o turno
        self.jogadas.append((origem, destino))
        self.mudarTurno()

    
        

xadrez = Xadrez()
xadrez.criarTabuleiro()
xadrez.moverPedra((6, 4),(4, 4))
xadrez.buscarTodosLances()
xadrez.printarTabuleiro()


