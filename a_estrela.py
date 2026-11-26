# Busca A* de Arad até Bucareste (Russell & Norvig, cap. 3)
# f(n) = g(n) + h(n):
#   g(n) = custo real acumulado do início até o nó n (km percorridos)
#   h(n) = heurística admissível até o objetivo (distância em linha reta até Bucareste)
#   f(n) = estimativa do custo total do caminho passando por n
from mapa import mapa_romenia, heuristica_bucareste


def resumo_fronteira(fronteira):
    """Formata a fronteira como 'Cidade(f=..., g=..., h=...)' para facilitar a leitura."""
    return ', '.join(
        f'{c}(f={f}, g={g}, h={h})'
        for f, g, h, c, caminho in fronteira
    )


def busca_a_estrela(inicio, objetivo, grafo, heuristica, mostrar=True):
    """Executa a busca A* (grafo com conjunto de explorados) e devolve (caminho, custo).

    Retorna (None, inf) caso não exista caminho de `inicio` até `objetivo`.
    Cada nó na fronteira é uma tupla: (f, g, h, cidade, caminho).
    """
    # h(inicio) é o custo estimado inicial já que g(inicio) = 0
    h_inicial = heuristica[inicio]
    fronteira = [(h_inicial, 0, h_inicial, inicio, [inicio])]

    # Conjunto de cidades já expandidas para evitar reprocessamento em grafos com ciclos
    explorados = set()
    iteracao = 0

    if mostrar:
        print(f'=== A* de {inicio} para {objetivo} ===')
        print(f'Nó inicial: {inicio} | g=0, h={h_inicial}, f={h_inicial}')
        print(f'Fronteira inicial: {resumo_fronteira(fronteira)}\n')

    while fronteira:
        iteracao += 1

        # Ordena a fronteira pelo menor valor de f(n) para simular uma fila de prioridade
        fronteira.sort(key=lambda no: no[0])
        f, g, h, cidade, caminho = fronteira.pop(0)

        if mostrar:
            print(f'[Iteração {iteracao}] Retirado da fronteira: {cidade} (f={f}, g={g}, h={h})')
            print(f'   Caminho até aqui: {" -> ".join(caminho)}')

        # Se a cidade já foi explorada antes, ignora esta cópia (provavelmente com f maior ou igual)
        if cidade in explorados:
            if mostrar:
                print(f'   -> {cidade} já está em explorados; ignorando nó duplicado.\n')
            continue

        # Teste de objetivo: em A* com heurística consistente, o primeiro pop do objetivo é ótimo
        if cidade == objetivo:
            if mostrar:
                print(f'   -> OBJETIVO {objetivo} alcançado! Custo total g={g}.')
                print(f'   -> Total de cidades expandidas: {len(explorados)}\n')
            return caminho, g

        # Marca a cidade atual como explorada antes de expandir seus vizinhos
        explorados.add(cidade)
        if mostrar:
            print(f'   -> Marcado {cidade} como explorado. Explorados: {sorted(explorados)}')

        # Expande todos os vizinhos conectados diretamente à cidade atual
        vizinhos = grafo.get(cidade, [])
        if mostrar:
            print(f'   -> Avaliando {len(vizinhos)} vizinho(s) de {cidade}:')

        for vizinho, custo in vizinhos:
            h_vizinho = heuristica[vizinho]
            if vizinho in explorados:
                # Com heurística consistente, um vizinho já explorado já tem o menor g possível
                if mostrar:
                    print(f'      - {vizinho} (aresta={custo} km): já explorado, pulando.')
                continue

            novo_g = g + custo
            novo_f = novo_g + h_vizinho
            novo_caminho = caminho + [vizinho]
            fronteira.append((novo_f, novo_g, h_vizinho, vizinho, novo_caminho))

            if mostrar:
                print(
                    f'      + {vizinho} (aresta={custo} km): '
                    f'g={novo_g}, h={h_vizinho} -> f={novo_f}'
                )

        if mostrar:
            # Reordena apenas para exibir a fronteira na ordem de prioridade atual
            fronteira_ordenada = sorted(fronteira, key=lambda no: no[0])
            print(f'   Fronteira ao fim da iteração {iteracao} ({len(fronteira_ordenada)} nó(s)):')
            print(f'      {resumo_fronteira(fronteira_ordenada) or "(vazia)"}\n')

    # Se a fronteira esvaziou sem encontrar o objetivo, não há rota possível
    if mostrar:
        print(f'Fronteira esvaziou após {iteracao} iterações sem encontrar {objetivo}.')
    return None, float('inf')


def main():
    print('Iniciando simulação de busca A*...\n')
    caminho, custo = busca_a_estrela(
        'Arad', 'Bucharest', mapa_romenia, heuristica_bucareste, mostrar=True
    )

    print('--- Resultado Principal (Arad -> Bucharest) ---')
    if not caminho:
        print('Sem caminho.')
        return

    print('Caminho encontrado:', ' -> '.join(caminho))
    print(f'Custo total: {custo} km em {len(caminho) - 1} passo(s)')

    # Verificação de referência do capítulo 3 de Russell & Norvig
    if custo == 418 and len(caminho) - 1 == 4:
        print('Status: Confere com o livro (418 km, 4 passos).')
    else:
        print('Status: ATENÇÃO — diferente do livro (418 km, 4 passos).')

    print('\n--- Outras origens até Bucharest (modo resumido) ---')
    for origem in ['Timisoara', 'Oradea', 'Craiova', 'Iasi']:
        print(f'Calculando rota de {origem} até Bucharest...')
        caminho_alt, custo_alt = busca_a_estrela(
            origem, 'Bucharest', mapa_romenia, heuristica_bucareste, mostrar=False
        )
        if caminho_alt:
            print(
                f'  {origem:<10} | {custo_alt:>4} km | '
                f'{len(caminho_alt) - 1} passos | {" -> ".join(caminho_alt)}'
            )
        else:
            print(f'  {origem:<10} | Sem caminho encontrado')

    print('\nExecução concluída.')


if __name__ == '__main__':
    main()