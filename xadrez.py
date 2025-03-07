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
            
        self.matriz[7][0] = "T"
        self.matriz[7][1] = "C"
        self.matriz[7][2] = "B"
        self.matriz[7][3] = "D"
        self.matriz[7][4] = "R"
        self.matriz[7][5] = "B"
        self.matriz[7][6] = "C"
        self.matriz[7][7] = "T"
        
       
        for i in range(8):
            self.matriz[1][i] = "p"

        self.matriz[0][0] = "t"
        self.matriz[0][1] = "c"
        self.matriz[0][2] = "b"
        self.matriz[0][3] = "d"
        self.matriz[0][4] = "r"
        self.matriz[0][5] = "b"
        self.matriz[0][6] = "c"
        self.matriz[0][7] = "t"
        
      
        self.tabAtual = [linha[:] for linha in self.matriz]
    
    def printarTabuleiro(self):
        linhaRef = ['A  B   C   D   E   F   G   H']
        print(linhaRef)
        print("  -----------------------------")
        colunaRef = list(range(9, 0, -1))
        k = 0
        for linha in self.tabAtual:
            for elemento in linha:
                print(f"'{elemento}'", end=" ")
            print('|', colunaRef[k])
            k += 1
            print()
    
    def verificarTurno(self, pedra):
        if (self.turno == 'brancas' and pedra.isupper()) or (self.turno == 'pretas' and pedra.islower()):
            return True
        return False
    
    def mudarTurno(self):
        self.turno = 'pretas' if self.turno == 'brancas' else 'brancas'
    
    
    def movimentoRei(self, pedra, x, y, tabuleiro=None):
        if tabuleiro is None:
            tabuleiro = self.tabAtual
        movimentos_validos = []
        possiveis_movimentos = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]
        for dx, dy in possiveis_movimentos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                destino = tabuleiro[nx][ny]
                if destino == ".":
                    movimentos_validos.append((x, y, nx, ny))
                elif (pedra.isupper() and destino.islower()) or (pedra.islower() and destino.isupper()):
                    movimentos_validos.append((x, y, nx, ny))
        return movimentos_validos

    def movimentoBispo(self, pedra, x, y, tabuleiro=None):
        if tabuleiro is None:
            tabuleiro = self.tabAtual
        possiveis_movimentos = [(-1, +1), (-1, -1), (1, +1), (1, -1)]
        movimentos_validos = []
        for dx, dy in possiveis_movimentos:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                destino = tabuleiro[nx][ny]
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

    def movimentoDama(self, pedra, x, y, tabuleiro=None):
        if tabuleiro is None:
            tabuleiro = self.tabAtual
        movimentos_validos = []
        direcoes = [
            (-1, 0), (1, 0), (0, -1), (0, 1),
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                destino = tabuleiro[nx][ny]
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

    def movimentoPeao(self, pedra, x, y, tabuleiro=None):
        if tabuleiro is None:
            tabuleiro = self.tabAtual
        
        movimentos_validos = []
        
        if pedra == 'p':
         
            if x + 1 < 8:
                destino = tabuleiro[x + 1][y]
                if destino == '.':
                    movimentos_validos.append((x, y, x + 1, y))
            
          
            if x == 1 and x + 2 < 8:
                if tabuleiro[x + 1][y] == '.' and tabuleiro[x + 2][y] == '.':
                    movimentos_validos.append((x, y, x + 2, y))
            
           
            if x + 1 < 8 and y + 1 < 8:
                captura1 = tabuleiro[x + 1][y + 1]
                if captura1 != '.' and captura1.isupper():
                    movimentos_validos.append((x, y, x + 1, y + 1))
            if x + 1 < 8 and y - 1 >= 0:
                captura2 = tabuleiro[x + 1][y - 1]
                if captura2 != '.' and captura2.isupper():
                    movimentos_validos.append((x, y, x + 1, y - 1))
            
          
            if x == 4: 
              
                if y + 1 < 8 and tabuleiro[x][y + 1].lower() == 'p' and tabuleiro[x][y + 1] == '.' and self.jogadas:
                    ultima_jogada = self.jogadas[-1]
                    origem_x, origem_y = ultima_jogada[0]
                    destino_x, destino_y = ultima_jogada[1]
                    if origem_x == 6 and destino_x == 4 and origem_y == y + 1:
                        
                        movimentos_validos.append((x, y, x + 1, y + 1))  
                        
                if y - 1 >= 0 and tabuleiro[x][y - 1].lower() == 'p' and tabuleiro[x][y - 1] == '.' and self.jogadas:
                    ultima_jogada = self.jogadas[-1]
                    origem_x, origem_y = ultima_jogada[0]
                    destino_x, destino_y = ultima_jogada[1]
                    if origem_x == 6 and destino_x == 4 and origem_y == y - 1:
                      
                        movimentos_validos.append((x, y, x + 1, y - 1))  

            return movimentos_validos

        if pedra == 'P':
            if x - 1 >= 0:
                destino = tabuleiro[x - 1][y]
                if destino == '.':
                    movimentos_validos.append((x, y, x - 1, y))
            
            if x == 6 and x - 2 >= 0:
                if tabuleiro[x - 1][y] == '.' and tabuleiro[x - 2][y] == '.':
                    movimentos_validos.append((x, y, x - 2, y))
            
           
            if x - 1 >= 0 and y + 1 < 8:
                captura1 = tabuleiro[x - 1][y + 1]
                if captura1 != '.' and captura1.islower():
                    movimentos_validos.append((x, y, x - 1, y + 1))
            if x - 1 >= 0 and y - 1 >= 0:
                captura2 = tabuleiro[x - 1][y - 1]
                if captura2 != '.' and captura2.islower():
                    movimentos_validos.append((x, y, x - 1, y - 1))
            
           
            if x == 3: 
                if y + 1 < 8 and tabuleiro[x][y + 1].lower() == 'p' and tabuleiro[x][y + 1] == '.' and self.jogadas:
                    ultima_jogada = self.jogadas[-1]
                    origem_x, origem_y = ultima_jogada[0]
                    destino_x, destino_y = ultima_jogada[1]
                    if origem_x == 1 and destino_x == 3 and origem_y == y + 1:
                      
                        movimentos_validos.append((x, y, x - 1, y + 1))  

                if y - 1 >= 0 and tabuleiro[x][y - 1].lower() == 'p' and tabuleiro[x][y - 1] == '.' and self.jogadas:
                    ultima_jogada = self.jogadas[-1]
                    origem_x, origem_y = ultima_jogada[0]
                    destino_x, destino_y = ultima_jogada[1]
                    if origem_x == 1 and destino_x == 3 and origem_y == y - 1:
                       
                        movimentos_validos.append((x, y, x - 1, y - 1))  

            return movimentos_validos


    def movimentoCavalo(self, pedra, x, y, tabuleiro=None):
        if tabuleiro is None:
            tabuleiro = self.tabAtual
        movimentos_validos = []
        possiveis_movimentos = [
            (-2, 1), (-2, -1), (2, 1), (2, -1),
            (-1, 2), (-1, -2), (1, 2), (1, -2)
        ]
        for dx, dy in possiveis_movimentos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                destino = tabuleiro[nx][ny]
                if destino == '.':
                    movimentos_validos.append((x, y, nx, ny))
                elif (pedra.isupper() and destino.islower()) or (pedra.islower() and destino.isupper()):
                    movimentos_validos.append((x, y, nx, ny))
        return movimentos_validos

    def movimentoTorre(self, pedra, x, y, tabuleiro=None):
        if tabuleiro is None:
            tabuleiro = self.tabAtual
        movimentos_validos = []
        direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                destino = tabuleiro[nx][ny]
                if destino == '.':
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
            tabuleiro = self.tabAtual
        
        # Define o rei conforme a cor
        rei = 'R' if cor == 'brancas' else 'r'
        rei_x, rei_y = -1, -1
        for i in range(8):
            for j in range(8):
                if tabuleiro[i][j] == rei:
                    rei_x, rei_y = i, j
                    break
            if rei_x != -1:
                break
        if rei_x == -1:
            return False
        
       
        for i in range(8):
            for j in range(8):
                peca = tabuleiro[i][j]
                if peca == '.':
                    continue
                if (cor == 'brancas' and peca.islower()) or (cor == 'pretas' and peca.isupper()):
                    movimentos = []
                    if peca.lower() == 'p':
                        movimentos = self.movimentoPeao(peca, i, j, tabuleiro)
                    elif peca.lower() == 't':
                        movimentos = self.movimentoTorre(peca, i, j, tabuleiro)
                    elif peca.lower() == 'c':
                        movimentos = self.movimentoCavalo(peca, i, j, tabuleiro)
                    elif peca.lower() == 'b':
                        movimentos = self.movimentoBispo(peca, i, j, tabuleiro)
                    elif peca.lower() == 'd':
                        movimentos = self.movimentoDama(peca, i, j, tabuleiro)
                    elif peca.lower() == 'r':
                        movimentos = self.movimentoRei(peca, i, j, tabuleiro)
                    
                    for mov in movimentos:
                        if mov[2] == rei_x and mov[3] == rei_y:
                            return True
        return False

    def simularMovimento(self, origem, destino):
        tabuleiro_simulado = [linha[:] for linha in self.tabAtual]
        origem_x, origem_y = origem
        destino_x, destino_y = destino
        pedra = tabuleiro_simulado[origem_x][origem_y]
        tabuleiro_simulado[destino_x][destino_y] = pedra
        tabuleiro_simulado[origem_x][origem_y] = "."
        return tabuleiro_simulado

    def buscarTodosLances(self, cor=None):
        lances_possiveis = []
        if cor is None:
            cor = self.turno
        for i in range(8):
            for j in range(8):
                peca = self.tabAtual[i][j]
                if (cor == "brancas" and peca.isupper()) or (cor == "pretas" and peca.islower()):
                    movimentos_validos = []
                    if peca.upper() == 'T':
                        movimentos_validos = self.movimentoTorre(peca, i, j)
                    elif peca.upper() == 'C':
                        movimentos_validos = self.movimentoCavalo(peca, i, j)
                    elif peca.upper() == 'P':
                        movimentos_validos = self.movimentoPeao(peca, i, j)
                    elif peca.upper() == 'B':
                        movimentos_validos = self.movimentoBispo(peca, i, j)
                    elif peca.upper() == 'R':
                        movimentos_validos = self.movimentoRei(peca, i, j)
                      
                        if cor == self.turno:
                            resultado_roque = self.pode_fazer_roque(cor)
                            if resultado_roque == 'roque pequeno':
                                movimentos_validos.append((i, j, i, j + 2))
                            elif resultado_roque == 'roque grande':
                                movimentos_validos.append((i, j, i, j - 2))
                    elif peca.upper() == 'D':
                        movimentos_validos = self.movimentoDama(peca, i, j)
                    else:
                        continue

                    for movimento in movimentos_validos:
                        destino_i, destino_j = movimento[2], movimento[3]
                      
                        if self.tabAtual[destino_i][destino_j] != '.':
                            peca_destino = self.tabAtual[destino_i][destino_j]
                            if (cor == "brancas" and peca_destino.isupper()) or (cor == "pretas" and peca_destino.islower()):
                                continue
                     
                        tabuleiro_simulado = self.simularMovimento((i, j), (destino_i, destino_j))
                        if self.emXeque(cor, tabuleiro_simulado):
                            continue
                        lances_possiveis.append(((i, j), (destino_i, destino_j)))
        return lances_possiveis

    def pode_fazer_roque(self, cor):
        if self.emXeque(cor):
            return False
        if cor == 'brancas':
            rei_pos = (7, 4)
            torre_esq_pos = (7, 0)
            torre_dir_pos = (7, 7)
            adversaria = 'pretas'
        else:
            rei_pos = (0, 4)
            torre_esq_pos = (0, 0)
            torre_dir_pos = (0, 7)
            adversaria = 'brancas'
        
        for jogada in self.jogadas:
            if jogada[0] == rei_pos or jogada[0] == torre_esq_pos or jogada[0] == torre_dir_pos:
                return False
        
        lances_adversarios = self.buscarTodosLances(cor=adversaria)
        casas_proibidas = {lance[1] for lance in lances_adversarios}
        if rei_pos in casas_proibidas:
            return False
    
        if (self.tabAtual[rei_pos[0]][1] == '.' and
            self.tabAtual[rei_pos[0]][2] == '.' and
            self.tabAtual[rei_pos[0]][3] == '.'):
            if ((rei_pos[0], 2) not in casas_proibidas and
                (rei_pos[0], 3) not in casas_proibidas):
                return 'roque grande'
       
        if self.tabAtual[rei_pos[0]][5] == '.' and self.tabAtual[rei_pos[0]][6] == '.':
            if ((rei_pos[0], 5) not in casas_proibidas and
                (rei_pos[0], 6) not in casas_proibidas):
                return 'roque pequeno'
        return False
    
    def verificarFimDeJogo(self):
       
        lances = self.buscarTodosLances(self.turno)
        if not lances:
           
            if self.emXeque(self.turno):
                vencedor = "pretas" if self.turno == "brancas" else "brancas"
                print(f"Xeque mate! Vitória das {vencedor}.")
                return "xeque mate", vencedor
            else:
                
                print("Empate por afogamento!")
                return "empate", None
        return None, None

    def validarLance(self, pedra, origem, destino, checkTurn=True):
        origem_x, origem_y = origem
        destino_x, destino_y = destino

        if (origem_x > 7 or origem_y > 7 or destino_x > 7 or destino_y > 7 or
            origem_x < 0 or origem_y < 0 or destino_x < 0 or destino_y < 0):
            print("Lance inválido: Posições fora do tabuleiro")
            return None

        if checkTurn and not self.verificarTurno(pedra):
            print("Lance inválido: Não é a vez dessa cor")
            return None

        if pedra.upper() == 'T':
            movimentos_validos = self.movimentoTorre(pedra, origem_x, origem_y)
        elif pedra.upper() == 'C':
            movimentos_validos = self.movimentoCavalo(pedra, origem_x, origem_y)
        elif pedra.upper() == 'P':
            movimentos_validos = self.movimentoPeao(pedra, origem_x, origem_y)
        elif pedra.upper() == 'B':
            movimentos_validos = self.movimentoBispo(pedra, origem_x, origem_y)
        elif pedra.upper() == 'R':
            movimentos_validos = self.movimentoRei(pedra, origem_x, origem_y)
            resultado_roque = self.pode_fazer_roque(self.turno)
            if resultado_roque == 'roque pequeno':
                movimentos_validos.append((origem_x, origem_y, origem_x, origem_y + 2))
            elif resultado_roque == 'roque grande':
                movimentos_validos.append((origem_x, origem_y, origem_x, origem_y - 2))
        elif pedra.upper() == 'D':
            movimentos_validos = self.movimentoDama(pedra, origem_x, origem_y)
        else:
            return None

        if (origem_x, origem_y, destino_x, destino_y) not in movimentos_validos:
            return None

        tabuleiro_simulado = self.simularMovimento((origem_x, origem_y), (destino_x, destino_y))
        if self.emXeque(self.turno, tabuleiro_simulado):
            print("Lance inválido: o rei ficará em xeque após o movimento")
            return None

        return movimentos_validos
            


    def moverPedra(self, origem, destino):
        origem_x, origem_y = origem
        destino_x, destino_y = destino
        pedra = self.tabAtual[origem_x][origem_y]

        if not self.verificarTurno(pedra):
            print("Lance inválido: Não é a vez dessa cor")
            return

       
        if (destino_x, destino_y) == (origem_x, origem_y + 2) or (destino_x, destino_y) == (origem_x, origem_y - 2):
            resultado_roque = self.pode_fazer_roque(self.turno)
            if resultado_roque:
                if resultado_roque == "roque grande":
                    self.tabAtual[origem_x][origem_y] = "."
                    self.tabAtual[origem_x][origem_y - 2] = "R" if self.turno == 'brancas' else "r"
                    self.tabAtual[origem_x][0] = "."
                    self.tabAtual[origem_x][3] = "T" if self.turno == 'brancas' else "t"
                    print("Roque grande realizado!")
                elif resultado_roque == "roque pequeno":
                    self.tabAtual[origem_x][origem_y] = "."
                    self.tabAtual[origem_x][origem_y + 2] = "R" if self.turno == 'brancas' else "r"
                    self.tabAtual[origem_x][7] = "."
                    self.tabAtual[origem_x][5] = "T" if self.turno == 'brancas' else "t"
                    print("Roque pequeno realizado!")
                self.jogadas.append((origem, destino))
                self.mudarTurno()
                return
            else:
                print("Roque inválido!")
                return

        if self.validarLance(pedra, origem, destino) is None:
            print("Lance inválido: Movimento não permitido para essa peça")
            return

      
        if pedra.upper() == 'P' and origem_y != destino_y and self.tabAtual[destino_x][destino_y] == '.':
            self.tabAtual[origem_x][destino_y] = "."

        self.tabAtual[destino_x][destino_y] = pedra
        self.tabAtual[origem_x][origem_y] = "."
        self.jogadas.append((origem, destino))
        self.mudarTurno()

        
        fim, vencedor = self.verificarFimDeJogo()
        if fim == "xeque mate":
            print(f"Fim de jogo: Xeque mate! Vitória das {vencedor}.")
        elif fim == "empate":
            print("Fim de jogo: Empate por afogamento.")


    
        


xadrez = Xadrez()
xadrez.criarTabuleiro()

print("Tabuleiro inicial:")
xadrez.printarTabuleiro()

print("\nMovimento 1: Peão branco de (6,4) para (4,4)")
xadrez.moverPedra((6, 4), (4, 4))
xadrez.printarTabuleiro()

print("\nMovimento 2: Peão preto de (1,4) para (3,4)")
xadrez.moverPedra((1, 4), (3, 4))
xadrez.printarTabuleiro()

print("\nMovimento 3: Rainha branca de (7,3) para (3,7)")
xadrez.moverPedra((7, 3), (3, 7))
xadrez.printarTabuleiro()

xadrez.moverPedra((1, 5), (2, 5))
xadrez.printarTabuleiro()
xadrez.buscarTodosLances()

if xadrez.emXeque('pretas'):
    print('esta em xeque')

else:  
    print('nao esta em xeque')









