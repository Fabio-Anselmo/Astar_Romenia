# Fase 5: busca A* completa com laço while
# Cada nó na fronteira é uma tupla (f, g, cidade, caminho), onde f = g + h
from mapa import mapa_romenia, heuristica_bucareste

print('=== Fase 5: Busca A* com while ===\n')


def busca_a_estrela(inicio, objetivo):
    """Executa a busca A* de `inicio` até `objetivo` e retorna (caminho, custo)."""
    h_inicio = heuristica_bucareste[inicio]
    # Inicia a fronteira com o nó de partida (custo g=0 e f=h(inicio))
    fronteira = [(h_inicio, 0, inicio, [inicio])]
    # Mantém as cidades já expandidas para evitar ciclos e reexpansões
    explorados = set()
    iteracao = 0

    print(f'Iniciando busca de {inicio} para {objetivo} (h inicial = {h_inicio})')
    print(f'Fronteira inicial: {fronteira}\n')

    while fronteira:
        iteracao += 1

        # Ordena pelo menor valor de f(n) e retira o nó mais promissor
        fronteira.sort(key=lambda no: no[0])
        f, g, cidade, caminho = fronteira.pop(0)
        print(f'[Iteração {iteracao}] Retirado: {cidade} | f={f}, g={g}, h={heuristica_bucareste[cidade]}')
        print(f'   Caminho atual: {" -> ".join(caminho)}')

        # Testa o objetivo ao tirar da fronteira, não ao gerar o nó
        if cidade == objetivo:
            print(f'   -> Objetivo {objetivo} alcançado na iteração {iteracao} com custo {g} km!\n')
            return caminho, g

        # Se a cidade já foi explorada antes, ignora esta entrada duplicada
        if cidade in explorados:
            print(f'   -> {cidade} já está em explorados; ignorando.\n')
            continue

        # Registra a cidade atual como explorada antes de gerar seus sucessores
        explorados.add(cidade)
        print(f'   -> {cidade} adicionado a explorados. Total explorados: {len(explorados)}')

        # Expande os vizinhos diretos que ainda não foram explorados
        for vizinho, custo in mapa_romenia[cidade]:
            if vizinho not in explorados:
                novo_g = g + custo
                novo_f = novo_g + heuristica_bucareste[vizinho]
                fronteira.append((novo_f, novo_g, vizinho, caminho + [vizinho]))
                print(
                    f'      + Vizinho {vizinho:<14} | estrada={custo:>3} km | '
                    f'g={novo_g:>3}, h={heuristica_bucareste[vizinho]:>3} -> f={novo_f:>3}'
                )
            else:
                print(f'      - Vizinho {vizinho:<14} | já explorado, ignorado.')

        # Exibe um resumo da fronteira ao final da iteração
        fronteira_ordenada = sorted(fronteira, key=lambda no: no[0])
        resumo = ', '.join(f'{c}(f={nf})' for nf, ng, c, _ in fronteira_ordenada)
        print(f'   Fronteira ({len(fronteira_ordenada)} nós): {resumo}\n')

    # Se a fronteira esvaziar sem achar o objetivo, não há caminho possível
    print(f'Fronteira esvaziou após {iteracao} iterações sem encontrar {objetivo}.')
    return None, float('inf')


print('Executando busca principal (Arad -> Bucharest)...\n')
caminho, custo = busca_a_estrela('Arad', 'Bucharest')

print('--- Resultado final ---')
if caminho:
    print('Caminho:', ' -> '.join(caminho))
    print('Custo :', custo, 'km')
    print('Passos:', len(caminho) - 1)
else:
    print('Caminho: Nenhum encontrado')
    print('Custo :', custo)
    print('Passos: 0')
print('\n=== Fim da Fase 5 ===')