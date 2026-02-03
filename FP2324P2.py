# This is the Python script for your project

# Inês Bentes, 107051 

# TAD intersecao

# Construtor
def cria_intersecao(col, lin) -> dict: 
    """
    Recebe um caracter e um inteiro.
    Retorna dicionário com a 'Coluna' e 'Linha' da interseção.
    """
    if type(col) != str or type(lin) != int:
        raise ValueError("cria_intersecao: argumentos invalidos")
    elif len(col) != 1 or ord('A') > ord(col) or ord(col) > ord('S') or lin < 1 or lin > 19:
        raise ValueError("cria_intersecao: argumentos invalidos")
    else:
        intersecao = {'Coluna': col, 'Linha': lin}
        return intersecao
# Seletores
def obtem_col(i) -> str:
    """
    Devolve a coluna da interseção recebida.
    """
    return i['Coluna']
def obtem_lin(i) -> int:
    """
    Devolve a linha da interseção recebida.
    """
    return int(i['Linha'])
# Reconhecedor
def eh_intersecao(arg) -> bool:
    """
    Recebe interseção e verifica a sua validade.
    Retorna True caso seja interseção, False caso contrário.
    """
    if type(arg) == dict and len(arg['Coluna']) == 1 and type(arg['Linha']) == int:
        return True
    return False 
# Teste
def intersecoes_iguais(i1, i2) -> bool:
    """
    Recebe duas interseções e verifica se são iguais.
    Retorna True caso seja interseção, False caso contrário.
    """
    if i1['Coluna'] == i2['Coluna'] and i1['Linha'] == i2['Linha']:
        return True 
    return False
# Transformador
def intersecao_para_str(i) -> str:
    """
    Recebe interseção e retorna-a em formato de str.
    """
    col = i['Coluna']
    lin = str(i['Linha'])
    return "".join([col, lin])
def str_para_intersecao(s) -> dict:
    """
    Recebe uma interseção em formato de str.
    Retorna a interseção em forma de dicionário.
    """
    aux = []
    if len(s) == 2:
        aux.append(s[0])
        aux.append(int(s[1]))
        return cria_intersecao(aux[0], aux[1]) 
    elif len(s) == 3:
        aux.append(s[0])
        lin1 = int(s[1])
        lin2 = int(s[2])
        lin = (lin1*10) + lin2 
        return cria_intersecao(aux[0], lin) 
# Funções de alto nível deste TAD
def obtem_intersecoes_adjacentes(i, l) -> tuple:
    """
    Recebe uma interseção i e uma interseção l do canto superior direito do tabuleiro.
    Retorna as interseções adjacentes a i em forma de tuplo.
    """
    aux = ()
    primeiro = {'Coluna': i['Coluna'], 'Linha': (i['Linha']-1)}
    if primeiro['Linha'] <= 0:
        primeiro = {}
    else: 
        aux += (primeiro, )
    segundo = {'Coluna': chr(ord(i['Coluna'])-1), 'Linha': i['Linha']}
    terceiro = {'Coluna': chr(ord(i['Coluna'])+1), 'Linha': i['Linha']}
    if segundo['Coluna'] < 'A':
        segundo = {}
    else: 
        aux += (segundo, )
    if terceiro['Coluna'] > l['Coluna']:
        terceiro = {}
    else: 
        aux += (terceiro, )
    quarto = {'Coluna': i['Coluna'], 'Linha': (i['Linha']+1)}
    if quarto['Linha'] > 19:
        quarto = {} 
    else:
        aux += (quarto, )
    return aux 
def ordena_intersecoes(t) -> tuple:
    """
    Recebe tuplo de interseções.
    Retorna tuplo ordenado de acordo com a ordem de leitura do tabuleiro Go.
    """
    t = list(t)
    n = len(t)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if (t[j]['Linha'] > t[j + 1]['Linha'] or
               (t[j]['Linha'] == t[j + 1]['Linha'] and t[j]['Coluna'] > t[j + 1]['Coluna'])):
                t[j], t[j + 1] = t[j + 1], t[j]
    return tuple(t)  
    
# TAD pedra

# Construtor
def cria_pedra_branca() -> str:
    """
    Devolve pedra branca.
    """
    return 'Branca' 
def cria_pedra_preta() -> str:
    """
    Devolve pedra preta.
    """
    return 'Preta'
def cria_pedra_neutra() -> str:
    """
    Devolve pedra neutra.
    """
    return 'Neutra'
# Reconhecedor
def eh_pedra(arg) -> bool:
    """
    Recebe qualquer argumento arg.
    Retorna True caso seja pedra, False caso contrário.
    """
    if arg == 'Branca' or arg == 'Preta' or arg == 'Neutra':
        return True 
    return False 
def eh_pedra_branca(p) -> bool:
    """
    Recebe pedra.
    Retorna True caso seja branca, False caso não seja. 
    """
    if p == 'Branca':
        return True 
    return False 
def eh_pedra_preta(p) -> bool:
    """
    Recebe pedra.
    Retorna True caso seja preta, False caso não seja. 
    """
    if p == 'Preta':
        return True 
    return False 
# Teste
def pedras_iguais(p1, p2) -> bool:
    """
    Recebe duas pedras.
    Retorna True caso sejam iguais, False caso contrário.
    """
    if p1 == p2:
        return True 
    return False 
# Transformador
def pedra_para_str(p) -> str:
    """
    Recebe uma pedra.
    Retorna uma str que representa o jogador dono da pedra.
    'X': Preto, 'O': Branco, '.': Neutra.
    """
    if p == 'Branca':
        return 'O'
    elif p == 'Preta':
        return 'X'
    else:
        return '.'
# Funções de alto nível deste TAD
def eh_pedra_jogador(p) -> bool:
    """
    Recebe uma pedra.
    Retorna True caso pertença a um jogador, False caso contrário.
    """
    if eh_pedra_branca(p) or eh_pedra_preta(p):
        return True 
    return False  

# TAD goban 

# Construtor
def cria_goban_vazio(n) -> dict:
    """
    Cria um goban vazio de tamanho n.
    Retorna todas as interseções do goban, vazio (Neutra).
    """
    goban = ()
    if not isinstance(n, int):
        raise ValueError("cria_goban_vazio: argumento invalido")
    if n != 19:
        if n != 13:
            if n!= 9:
                raise ValueError("cria_goban_vazio: argumento invalido")
    # Limites 
    lin = n 
    col = chr(64+n)
    i = 1
    while i <= lin:
        x = 'A'
        while ord(x) <= ord(col):
            goban += ({'Coluna': x, 'Linha': i, 'Jogador': 'Neutra'}, )
            x = chr(ord(x)+1) 
        i += 1
    return goban 
def cria_goban(n, ib, ip) -> tuple:
    """
    Cria goban com as interseções de ib e ip ocupadas.
    Retorna o goban, com as interseções neutras, pretas e brancas.
    """
    # Todas as verificações de argumentos 
    if not isinstance(n, int) or not isinstance(ib, tuple) or not isinstance(ip, tuple):
        raise ValueError("cria_goban: argumentos invalidos") 
    if n != 19:
        if n != 13:
            if n!= 9:
                raise ValueError("cria_goban: argumentos invalidos")
    for a in ib:
        for b in ip:
            if a == b:
                raise ValueError("cria_goban: argumentos invalidos")
    for a in ib:
        if ib.count(a) > 1:
            raise ValueError("cria_goban: argumentos invalidos")
    for a in ip:
        if ip.count(a) > 1:
            raise ValueError("cria_goban: argumentos invalidos")
        
    goban_vazio = cria_goban_vazio(n)
    def intersecoes(intersecoes, jogador):
        for i in intersecoes:
            coluna, linha = i['Coluna'], i['Linha']
            if coluna > chr(64+n) or linha > n:
                raise ValueError("cria_goban: argumentos invalidos")
            for x in goban_vazio:
                if x['Coluna'] == coluna and x['Linha'] == linha:
                    x['Jogador'] = jogador 

    if type(ib) == tuple:
        intersecoes(ib, 'Branca')
    else:
        intersecoes([ib], 'Branca')
    if type(ip) == tuple:
        intersecoes(ip, 'Preta')
    else:
        intersecoes([ip], 'Preta')
    
    goban = goban_vazio 
    return goban
def cria_copia_goban(t) -> tuple:
    """
    Recebe um goban.
    Retorna uma cópia dele. 
    """
    copia_goban = [dict(intersecoes) for intersecoes in t]
    return copia_goban
# Seletores
def obtem_ultima_intersecao(g) -> dict:
    """
    Recebe um goban g.
    Retorna a sua última interseção. 
    """
    aux = g[-1]
    ultima = {'Coluna': aux['Coluna'], 'Linha': aux['Linha']}
    return ultima 
def obtem_pedra(g, i) -> str:
    """
    Recebe um goban g e uma interseção i.
    Retorna a pedra nessa interseção, 'Neutra' caso esteja vazia. 
    """
    for x in g:
        if x['Coluna'] == i['Coluna'] and x['Linha'] == i['Linha']:
            return x['Jogador']
        
# Função auxiliar para obtem_cadeia
def obtem_adjacentes_iguais(g, i) -> tuple:
    """
    Recebe um goban g e uma interseção i.
    Retorna um tuplo com as interseções adjacentes a i com pedras que pertencem
    ao mesmo jogador ou que estão livres.
    """
    jogador = obtem_pedra(g, i)
    adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
    adj = (i, )
    for x in adjacentes:
        if obtem_pedra(g, x) == jogador:
            adj += (x, )
    return adj 
def obtem_cadeia(g, i) -> tuple:
    """
    Recebe um goban g e uma interseção i.
    Retorna um tuplo com a cadeia que passa por i. Caso não esteja ocupada,
    devolve a cadeia de posições livres. 
    """
    adj = obtem_adjacentes_iguais(g, i)
    aux = adj 
    for x in adj:
        if x != i:
            aux1 = obtem_adjacentes_iguais(g, x) 
            for y in aux1:
                if y not in aux:
                    aux += (y, )
            index = len(aux) - 1
            check = obtem_adjacentes_iguais(g, i)
            while index < len(aux):
                check = obtem_adjacentes_iguais(g, aux[index])
                for z in check:
                    if z not in aux:
                        aux += (z, )
                index += 1
    cadeia = ordena_intersecoes(aux)        
    return cadeia  
# Modificadores 
def coloca_pedra(g, i, p) -> tuple:
    """
    Recebe um goban g, uma interseção i e um jogador p.
    Retorna goban modificado destrutivamente, colocando a pedra do jogador 
    na interseção recebida.
    """
    for x in g:
        if x['Coluna'] == i['Coluna'] and x['Linha'] == i['Linha']:
            if p == 'Preta': 
                x['Jogador'] = 'Preta'
            elif p == 'Branca':
                x['Jogador'] = 'Branca'
            else:
                x['Jogador'] = 'Neutra'
    return g
def remove_pedra(g, i) -> tuple:
    """
    Recebe um goban g, uma interseção i e um jogador p.
    Retorna goban modificado destrutivamente, remove pedra na interseção i.
    """
    for x in g:
        if x['Coluna'] == i['Coluna'] and x['Linha'] == i['Linha']:
            x['Jogador'] = 'Neutra'
    return g
def remove_cadeia(g, t) -> tuple:
    """
    Recebe um goban g e um tuplo t de uma cadeia.
    Retorna goban modificado destrutivamente, remove pedras em todas as
    interseções em t, ou seja, remove a cadeia.
    """
    for x in g:
        for y in t:
            if x['Coluna'] == y['Coluna'] and x['Linha'] == y['Linha']:
                x['Jogador'] = 'Neutra' 
    return g
# Reconhecedor 
def eh_goban(g) -> bool:
    """
    Recebe um argumento g.
    Retorna True caso seja goban, False caso contrário.
    """
    if len(g) != 81:
        if len(g) != 169:
            if len(g) != 361:
                return False 
    return True
def eh_intersecao_valida(g, i) -> bool:
    """
    Recebe um goban g e uma interseção i.
    Retorna True caso seja uma interseção válida no goban recebido, False
    caso contrário.
    """
    sup_dir = obtem_ultima_intersecao(g)
    if i['Coluna'] > sup_dir['Coluna'] or i['Linha'] > sup_dir['Linha']:
        return False 
    return True 
# Teste 
def gobans_iguais(g1, g2) -> bool:
    """
    Recebe dois gobans.
    Retorna True caso sejam iguais, False caso contrário.
    """
    for i in g2:
        if i not in g1:
            return False 
    return True 
# Transformador 
def goban_para_str(g) -> str:
    """
    Recebe um goban e retorna a cadeia de caracteres que o representa.
    """
    supd = obtem_ultima_intersecao(g) 
    tamanho = supd['Linha'] + 2
    pt_final = []
    pt = []
    x = 0
    while x < supd['Linha']:
        if (x+1) > 9:
            pt.append('{}'.format(x+1))
        else:
            pt.append(' {}'.format(x+1))
        for i in g:
            if i['Linha'] == x+1: 
                if i['Jogador'] == 'Branca':
                    pt.append('O')
                elif i['Jogador'] == 'Preta':
                    pt.append('X')
                else:
                    pt.append('.')
        if (x+1) > 9:
            pt.append('{}'.format(x+1))
        else:
            pt.append(' {}'.format(x+1))
        x += 1
    
    for i in range(0, len(pt), tamanho):
        aux = pt[i:i+tamanho]
        pt_final.append(aux)
    pt_final.reverse()
    letras = [chr(i) for i in range(65, (ord(supd['Coluna'])+1))]

    letras = '   ' + ' '.join(letras)
    meio = ''
    for i in pt_final:
        meio += ' '.join(i) + '\n'
    final = letras + '\n' + meio + letras 
    return final 
# Funções de alto nível deste TAD 
def obtem_adjacentes_diferentes(g, t) -> tuple:
    """
    Recebe um goban e um tuplo formado por interseções.
    Retorna tuplo das interseções:
    a) livres, caso as interseções de t estejam ocupadas.
    b) ocupadas, caso as interseções de t estejam livres.
    """
    adj_final = ()
    for i in t:
        jogador_i = obtem_pedra(g, i)
        adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        for y in adjacentes:
            if obtem_pedra(g, y) != jogador_i:
                if jogador_i == 'Neutra': 
                    if y not in adj_final:
                        adj_final += (y, )
                elif eh_pedra_branca(jogador_i) or eh_pedra_preta(jogador_i):
                    if obtem_pedra(g, y) == 'Neutra':
                        if y not in adj_final:
                            adj_final += (y, )
    return ordena_intersecoes(adj_final)
def obtem_territorios(g) -> tuple:
    """
    Recebe um goban.
    Retorna o tuplo formado pelos territórios de t.
    """
    cadeias_livres = ()
    territorios = ()
    # Forma um tuplo em cadeias_livres constituído por outro tuplos de cadeias de interseções livres.
    for i in g:
        if eh_pedra_jogador(obtem_pedra(g, i)) == False:
            cadeia = obtem_cadeia(g, i)
            if len(cadeia) > 1:
                if cadeia[0]['Coluna'] == cadeia[1]['Coluna'] and cadeia[0]['Linha'] == cadeia[1]['Linha']:
                    cadeia = cadeia[1:]
            if cadeia not in cadeias_livres:
                cadeias_livres += (cadeia, )
    # Tendo em conta o tamanho de cada cadeia livre, procura saber se tem fronteira, ou seja, se é território
    for i in cadeias_livres:
        tamanho = len(i)
        adjacentes_dif = obtem_adjacentes_diferentes(g, i)
        x = len(adjacentes_dif) 
        if len(adjacentes_dif) == x:
            jogador = obtem_pedra(g, adjacentes_dif[0])
            cnt = 0
            for y in adjacentes_dif:
                # Break caso o território não seja formado por pedras do mesmo jogador 
                if obtem_pedra(g, y) != jogador:
                    break
                else: 
                # Contagem para verificar se a fronteira do território está completa
                    cnt += 1
        if cnt == x:
            territorios += (i, )
        territorios_final = ()
        for i in territorios:
            # Ordena as interseções de cada um dos territórios 
            territorios_final += (ordena_intersecoes(i), )
        return territorios_final
    
# Função Auxiliar
def obtem_adjacentes_dif(g, i) -> tuple:
    """
    Recebe um goban g e uma interseção i.
    Retorna um tuplo com as interseções adjacentes a i com pedras que pertencem
    ao outro jogador.
    """
    jogador = obtem_pedra(g, i)
    if eh_pedra_preta(jogador):
        jogador = 'Branca'
    else:
        jogador = 'Preta'
    adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
    adj = ()
    for x in adjacentes:
        if obtem_pedra(g, x) == jogador:
            adj += (x, )
    return adj 

def jogada(g, i, p) -> tuple:
    """
    Recebe um goban g, uma interseção i e um jogador p.
    Retorna o goban após a jogada do jogador p na interseção i.
    """
    coloca_pedra(g, i, p)
    jogador = p 
    adj = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
    dif = ()
    for x in adj:
        if obtem_pedra(g, x) != jogador and obtem_pedra(g, x) != 'Neutra':
            dif += (x, )
    if len(dif) == len(adj):
        for y in dif:
            adj_aux = obtem_intersecoes_adjacentes(y, obtem_ultima_intersecao(g))
            adj_dif = obtem_adjacentes_dif(g, y)
            if len(adj_aux) == len(adj_dif): 
                return g 
    for y in dif:
        if obtem_pedra(g, y) != 'Neutra':
            cad = obtem_cadeia(g, y)
            remove_cadeia(g, cad)
    return g
def obtem_pedras_jogadores(g) -> tuple:
    """
    Recebe um goban.
    Retorna um tuplo do número de pedras ocupadas por jogador branco e preto, respetivamente.
    """
    b = 0
    p = 0
    for i in g:
        pedra = obtem_pedra(g, i)
        if eh_pedra_branca(pedra):
            b += 1
        elif eh_pedra_preta(pedra):
            p += 1
    return (b, p)

# Funções Adicionais 

def calcula_pontos(g) -> tuple:
    """
    Recebe um goban.
    Retorna um tuplo com os pontos dos jogadores branco e preto, respetivamente.
    """
    cnt_p, cnt_b = 0, 0
    for x in g:
        if eh_pedra_preta(x['Jogador']) or eh_pedra_branca(x['Jogador']):
            if eh_pedra_preta(x['Jogador']):
                cnt_p += 1
            else:
                cnt_b += 1 
    if cnt_p == 0 and cnt_b == 1:
        return (len(g), 0)
    elif cnt_p == 1 and cnt_b == 0:
        return (0, len(g))
    pontos_ocupados = list(obtem_pedras_jogadores(g))
    territorios = obtem_territorios(g)
    for i in territorios:
        jogador = obtem_adjacentes_diferentes(g, i)
        jogador = obtem_pedra(g, jogador[0])
        if eh_pedra_branca(jogador):
            pontos_ocupados[0] += len(i)
        elif eh_pedra_preta(jogador):
            pontos_ocupados[1] += len(i)
    return tuple(pontos_ocupados)

# Função auxiliar a eh_jogada_legal
def obtem_adj_vazias(g, i) -> tuple:
    """
    Recebe um goban g e uma interseção i.
    Retorna um tuplo com as interseções adjacentes a i vazias.
    """
    jogador = 'Neutra'
    adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
    adj = ()
    for x in adjacentes:
        if obtem_pedra(g, x) == jogador:
            adj += (x, )
    return adj 
def eh_jogada_legal(g, i, p, l) -> bool:
    """
    Recebe um goban g, uma interseção i, um jogador p e um goban g.
    Retorna True caso seja jogada legal, False caso contrário.
    """
    g_aux = cria_copia_goban(g)
    jogadas = coloca_pedra(g_aux, i, p)
    if g_aux == l:
        return False 
    adjacentes = obtem_adjacentes_iguais(jogadas, i)
    if len(adjacentes) == 1:
        adj_dif = obtem_adj_vazias(jogadas, i)
        adj_aux = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        if len(adj_aux) == len(adj_dif):
                return True
        else:
            adjacentes = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
            for x in adjacentes:
                adj_dif = obtem_adjacentes_dif(jogadas, x)
                adj_aux = obtem_intersecoes_adjacentes(x, obtem_ultima_intersecao(g))
                if len(adj_aux) == len(adj_dif):
                    return True
                elif (len(adj_aux) - 1) == len(adj_dif):
                    return True 
            return False 
    else:
        cadeia = obtem_cadeia(jogadas, i)
        adjacentes = obtem_adjacentes_diferentes(jogadas, cadeia)
        if len(adjacentes) < 1:
            return False
        else:
            return True
def turno_jogador(g, p, l) -> bool:
    """
    Recebe um goban g, um jogador p e um goban l.
    Retorna False caso o jogador passe, True caso a jogada seja válida e realizada.
    """
    i1 = input("Escreva uma intersecao ou 'P' para passar {}:". format([['X'] if eh_pedra_preta(p) else ['O']]))
    while i1 != 'P':
        i1 = str_para_intersecao(i1)
        if  eh_intersecao_valida(g, i1):
            if eh_jogada_legal(g, i1, p, l):
                g = jogada(g, i1, p)
                if g != l:
                    return True 
        i1 = input("Escreva uma intersecao ou 'P' para passar {}:". format([['X'] if eh_pedra_preta(p) else ['O']]))
    if i1 == 'P':
        return False 
  
# Função Final

def go(n, tb, tn):
    """
    Função principal que permite jogar um jogo de Go com dois jogadores.
    O jogo termina quando os dois jogadores passarem a vez consecutivamente. 
    Retorna True caso o jogador branco ganhe, False caso o jogador preto ganhe. 
    """
    p, b = 'Preta', 'Branca'
    aux = 0
    if n != 19:
        if n != 13:
            if n!= 9:
                raise ValueError("go: argumentos invalidos")
    if not isinstance(tb, tuple) or not isinstance(tn, tuple):
        raise ValueError("go: argumentos invalidos")
    if len(tb) == 0 and len(tn) == 0:
        goban = cria_goban_vazio(n)
    else:
        goban = cria_goban(n, tb, tn)
    pontos = calcula_pontos(goban)
    print("Branco (O) tem {} pontos\nPreto (X) tem {} pontos".format(pontos[0], pontos[1]))
    print(goban_para_str(goban))
    
    goban_aux = cria_copia_goban(goban)
    turno = turno_jogador(goban, p, goban_aux)
    cnt_p, cnt_b = 1, 0
    while aux != 2:
        pontos = calcula_pontos(goban)
        print("Branco (O) tem {} pontos\nPreto (X) tem {} pontos".format(pontos[0], pontos[1]))
        print(goban_para_str(goban))
        goban_aux = cria_copia_goban(goban)
        if cnt_b < cnt_p: 
            turno = turno_jogador(goban, b, goban_aux)
            if not turno:
                aux += 1
            else:
                aux = 0 
            cnt_b += 1 
        else:
            turno = turno_jogador(goban, p, goban_aux)
            if not turno:
                aux += 1
            else: 
                aux = 0
            cnt_p += 1
        if aux == 2:
            pontos = calcula_pontos(goban)
            print("Branco (O) tem {} pontos\nPreto (X) tem {} pontos".format(pontos[0], pontos[1]))
            print(goban_para_str(goban))
            if pontos[0] > pontos[1]:
                return True
            return False 