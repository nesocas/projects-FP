# This is the Python script for your project
# Inês Bentes, 107501
def eh_territorio(arg) -> bool:
    """
    Verifica se um território é válido.
    Retorna True caso seja território, False se falhar em alguma das verificações.
    """
    if type(arg) != tuple or len(arg) < 1 or len(arg) > 26:  
        return False
    if type(arg[0]) != tuple:
        return False 
    tamanho = len(arg[0]) 
    for i in arg:
        if type(i) != tuple:
            return False
        if len(i) > 99 or len(i) < 1 or len(i) != tamanho: 
            return False                    
        for x in i:
            if type(x) != int:
                return False 
            if x > 1 or x < 0: 
                return False 
    return True 

def obtem_ultima_intersecao(arg) -> tuple:
    """
    Recebe um território e transforma em interseção.
    Retorna a interseção em forma de tuplo.
    """
    intersecao = ()
    vertical = chr((len(arg)-1) + 65) 
    intersecao += (vertical, ) + (len(arg[0]), ) 
    return intersecao

def eh_intersecao(arg) -> bool:
    """
    Recebe um argumento de qualquer tipo.
    Retorna True caso seja interseção, False se falhar em alguma das verificações.
    """
    if type(arg) != tuple or len(arg) != 2 or type(arg[0]) != str:
        return False
    if len(arg[0]) != 1:
        return False
    if type(arg[1]) != int: 
        return False 
    if ord('A') > ord(arg[0]) or ord(arg[0]) > ord('Z') or 99 < arg[1] or arg[1] < 1:
        return False 
    return True

def eh_intersecao_valida(t, arg) -> bool: 
    """
    Recebe um território e uma interseção.
    Retorna True caso seja interseção válida, False se falhar em alguma das verificações.
    """
    if eh_intersecao(arg) == False:
        return False 
    vertical_pri = ord('A')
    vertical_ult = len(t) + 65
    tamanho_h = len(t[0])
    if vertical_pri <= ord(arg[0]) < vertical_ult and 1 <= arg[1] <= tamanho_h:
        return True 
    return False

def eh_intersecao_livre(t, arg) -> bool:
    """
    Recebe um território e uma interseção do território.
    Retorna True caso a interseção seja 0, False se fôr 1.
    """
    linha_v = ord(arg[0]) - 65 
    linha_h = arg[1] - 1
    if t[linha_v][linha_h] == 0:
        return True 
    return False 

def obtem_intersecoes_adjacentes(t, arg) -> tuple:
    """
    Recebe um território e uma interseção do território.
    Pela ordem correta, procura as interseções adjacentes, retornando apenas as interseções que se
    enquadram no território inicialmente recebido.
    """
    final = ()
    max_t = len(t) + 65 
    primeiro = (arg[0], arg[1]-1)
    segundo = (chr(ord(arg[0])-1), arg[1])
    terceiro = (chr(ord(arg[0])+1), arg[1])
    quarto = (arg[0], arg[1]+1)
    if primeiro[1] > 0:
        final += (primeiro, )
    if 65 <= ord(segundo[0]) <= 90:
        final += (segundo, )
    if 65 <= ord(terceiro[0]) <= 90 and ord(terceiro[0]) < max_t:
        final += (terceiro, )
    if quarto[1] <= len(t[0]):
        final += (quarto, )
    return final

def obtem_intersecoes_adj_ocupadas(t, arg) -> tuple:
    """
    Recebe um território e uma interseção.
    Função auxiliar de procura de interseções adjacentes à interseção recebida.
    Retorna apenas as ocupadas (com valor igual a 1).
    """
    ocupadas = ()
    adjacentes = obtem_intersecoes_adjacentes(t, arg)
    for i in adjacentes:
        if eh_intersecao_livre(t, i) == False:
            ocupadas += (i, )
    return ocupadas

def obtem_intersecoes_adj_livres(t, arg) -> tuple:
    """
    Recebe um território e uma interseção.
    Função auxiliar de procura de interseções adjacentes à interseção recebida.
    Retorna apenas as livres (com valor igual a 0).
    """
    livres = ()
    adjacentes = obtem_intersecoes_adjacentes(t, arg)
    for i in adjacentes:
        if eh_intersecao_livre(t, i) == True:
            livres += (i, )
    return livres 

def ordena_intersecoes(t) -> tuple:
    """
    Recebe um tuplo de interseções (potencialmente vazio).
    Retorna um tuplo com essas mesmas interseções, ordenadas de acordo com a
    ordem de leitura do território.
    """
    linhas_h = []
    ind = 0
    for i in t: 
    # ordena o tuplo recebido numa lista de acordo com a numeração das linhas horizontais
        linhas_h += (i, ) 
        if len(linhas_h) > 1:
            ind += 1
        index = ind
        while index > 0:
            if linhas_h[index][1] < linhas_h[index-1][1]:
                linhas_h[index-1], linhas_h[index] = linhas_h[index], linhas_h[index-1]
            index -= 1
    index = 0
    max = len(linhas_h)
    while index < max:
    # ordena as linhas verticias tendo em conta as linhas horizontais já organizadas no loop anterior
        ind = index 
        while ind+1 < max and linhas_h[ind][1] == linhas_h[ind+1][1]:
            if ord(linhas_h[ind][0]) > ord(linhas_h[ind+1][0]):
                linhas_h[ind], linhas_h[ind+1] = linhas_h[ind+1], linhas_h[ind]
            ind += 1
        index += 1
    index = 0
    while index+1 < len(linhas_h):
        if ord(linhas_h[index][0]) > ord(linhas_h[index+1][0]) and linhas_h[index][1] == linhas_h[index+1][1]: 
        # verifica uma última vez todos os elementos
            linhas_h[index], linhas_h[index+1] = linhas_h[index+1], linhas_h[index]
        index += 1
    linhas_h = tuple(linhas_h)
    return linhas_h 

def territorio_para_str(t) -> str:
    """
    Recebe um território e devolve uma string que o representa.
    """
    pt = []
    pt_final = []
    tamanho = len(t) + 2
    x = 0
    if eh_territorio(t) == False:
        raise ValueError("territorio_para_str: argumento invalido")
    while x < len(t[0]): 
    # adiciona à lista pt todos os argumentos necessários para criar a parte do meio do território
        i = 0
        if (x+1) > 9: 
        # normaliza caso o número da lista horizontal tenha dois digitos
            pt.append('{}'.format(x+1))
        else:
            pt.append(' {}'.format(x+1))
        while i < len(t):
            if t[i][x] == 0:
                pt.append('.')
            else: 
                pt.append('X')
            i += 1
        if (x+1) > 9:
            pt.append('{}'.format(x+1))
        else:
            pt.append(' {}'.format(x+1))
        x += 1

    for i in range(0, len(pt), tamanho): 
    # separa os elementos da lista pt por linhas, criando a lista pt_final
        aux = pt[i:i+tamanho]
        pt_final.append(aux)
    pt_final.reverse()
    # inverte-a de modo a ler as linhas horizontais de baixo para cima
    letras = [chr(i) for i in range(65, len(t)+65)]

    letras = '   ' + ' '.join(letras)
    meio = ''
    for i in pt_final:
        meio += ' '.join(i) + '\n'

    final = letras + '\n' + meio + letras 
    # cria a string final 
    return final

def obtem_cadeia(t, arg) -> tuple:
    """
    Recebe um território e uma interseção dele (ocupada ou livre).
    Retorna o tuplo formado por todas as interseções conectadas à interseção recebida,
    incluindo ela própria.
    """
    x = 0
    if eh_territorio(t) == False or eh_intersecao(arg) == False or eh_intersecao_valida(t, arg) == False:
        raise ValueError("obtem_cadeia: argumentos invalidos")
    montanhas = (arg, )
    livres = (arg, )
    if (eh_intersecao_livre(t, arg) == False): 
    # criação de um tuplo cadeia ao qual é adicionado todas as montanhas pertencentes a ela
        montanhas += obtem_intersecoes_adj_ocupadas(t, arg)
        cadeia = montanhas
        for i in montanhas:
            if i != arg:
                aux = obtem_intersecoes_adj_ocupadas(t, i)
                for x in aux:
                    if x not in cadeia:
                    # adiciona apenas se ainda não estiver na cadeia 
                        cadeia += (x, )
                index = len(cadeia) - 1
                check = obtem_intersecoes_adj_ocupadas(t, i)
                while index < len(cadeia):
                    check = obtem_intersecoes_adj_ocupadas(t, cadeia[index])
                    for y in check:
                        if y not in cadeia: 
                        # adiciona apenas se ainda não estiver na cadeia 
                            cadeia += (y, )
                    index += 1
        if len(cadeia) > 1:
            cadeia = ordena_intersecoes(cadeia)
        return cadeia       
    else: # faz o mesmo que o loop anterior mas para o caso de cadeias de interseções livres 
        livres += obtem_intersecoes_adj_livres(t, arg)
        cadeia = livres 
        for i in livres:
            if i != arg:
                aux = obtem_intersecoes_adj_livres(t, i)
                for x in aux:
                    if x not in cadeia:
                        cadeia += (x, )
                index = len(cadeia) - 1
                check = obtem_intersecoes_adj_livres(t, i)
                while index < len(cadeia):
                    check = obtem_intersecoes_adj_livres(t, cadeia[index])
                    for y in check:
                        if y not in cadeia:
                            cadeia += (y, )
                    index += 1
        if len(cadeia) > 1: 
            cadeia = ordena_intersecoes(cadeia)
        return cadeia 

def obtem_vale(t, arg) -> tuple:
    """
    Recebe um território e uma interseção ocupada por uma montanha.
    Retorna o tuplo (potencialmente vazio) formado por todas as interseções consideradas
    vales da montanha ou da cadeia de montanhas.
    """
    if eh_territorio(t) == False or eh_intersecao_valida(t, arg) == False or eh_intersecao_livre(t, arg) == True:
        raise ValueError("obtem_vale: argumentos invalidos")
    if len(obtem_cadeia(t, arg)) == 1:
        return obtem_intersecoes_adj_livres(t, arg)
    vales = ()
    cadeia = obtem_cadeia(t, arg)
    for i in cadeia:
        aux = obtem_intersecoes_adj_livres(t, i)
        for x in aux:
            if x not in vales:
                vales += (x, )
    return ordena_intersecoes(vales)

def verifica_conexao(t, i1, i2) -> bool:
    """
    Recebe um território e duas interseções do território.
    Retorna True se duas interseções estão conectadas, False caso contrário.
    """
    if eh_territorio(t) == False or eh_intersecao_valida(t, i1) == False or eh_intersecao_valida(t, i2) == False:
        raise ValueError("verifica_conexao: argumentos invalidos")
    cadeia = obtem_cadeia(t, i1)
    if i2 in cadeia:
        return True
    return False 

def calcula_numero_montanhas(t) -> int:
    """
    Recebe um território.
    Devolve o número de interseções ocupadas por montanhas nesse mesmo
    território.
    """
    if eh_territorio(t) == False:
        raise ValueError("calcula_numero_montanhas: argumento invalido")
    cnt = 0
    for i in t:
        for x in i:
            if x == 1:
                cnt += 1
    return cnt 

def calcula_numero_cadeias_montanhas(t) -> int:
    """
    Recebe um território.
    Devolve o número de cadeias de montanhas nesse mesmo território.
    """
    if eh_territorio(t) == False:
        raise ValueError("calcula_numero_cadeias_montanhas: argumento invalido")
    cadeias_aux = ()
    cnt = 0
    for x, i in enumerate(t):
        letra = chr(x+65)
        numero = 1
        for y in i:
            if y == 1:
                aux = obtem_cadeia(t, (letra, numero))
                if len(aux) == (len(i)*len(t))-1:
                    return 1 
                if aux not in cadeias_aux:
                    cadeias_aux += (aux, )
                    cnt += 1
            numero += 1
    return cnt 

def calcula_tamanho_vales(t) -> int:
    """
    Recebe um território.
    Devolve número total de interseções diferentes que formam todos os vales
    do território.
    """
    if eh_territorio(t) == False:
        raise ValueError("calcula_tamanho_vales: argumento invalido")
    vales = ()
    for x, i in enumerate(t):
        letra = chr(x+65)
        numero = 1
        for y in i:
            if y == 1:
                aux = obtem_intersecoes_adj_livres(t, (letra, numero))
                for z in aux:
                    if z not in vales:
                        vales += (z, ) 
            numero += 1
    return len(vales)
