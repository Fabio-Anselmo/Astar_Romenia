# Fase 4: função expandir e controle do conjunto de nós explorados no A*
from mapa import mapa_romenia, heuristica_bucareste

print('=== Fase 4: Função expandir e conjunto de explorados ===\n')


def mostrar_fronteira(fronteira):
    """Exibe os nós atualmente na fronteira no formato 'Cidade(f=...)'."""
    print('   fronteira:', ', '.join(f'{c}(f={f})' for f, g, c, caminho in fronteira))


def expandir(no, explorados):
    """Gera os nós filhos válidos de `no`, ignorando vizinhos já em `explorados`."""
    f, g, cidade, caminho = no
    filhos = []
    print(f'   [expandir] Avaliando vizinhos de {cidade} (g={g}, f={f})...')

    # Percorre todas as conexões diretas a partir da cidade do nó atual
    for vizinho, custo in mapa_romenia[cidade]:
        # Evita reprocessar cidades já adicionadas ao conjunto de explorados
        if vizinho in explorados:
            print(f'      - {vizinho} (aresta={custo} km): já está em explorados, ignorado.')
            continue

        novo_g = g + custo
        novo_f = novo_g + heuristica_bucareste[vizinho]
        filhos.append((novo_f, novo_g, vizinho, caminho + [vizinho]))
        print(
            f'      + {vizinho} (aresta={custo} km): novo g={novo_g}, '
            f'h={heuristica_bucareste[vizinho]} -> novo f={novo_f}'
        )

    print(f'   [expandir] Total de filhos gerados a partir de {cidade}: {len(filhos)}')
    return filhos


inicio = 'Arad'
h_inicio = heuristica_bucareste[inicio]

# Fronteira começa com o nó inicial (custo acumulado g=0, f=h(inicio))
fronteira = [(h_inicio, 0, inicio, [inicio])]

# Conjunto de cidades já expandidas para evitar ciclos e reexpansões desnecessárias
explorados = set()

print(f'Cidade inicial: {inicio} (h={h_inicio})')
mostrar_fronteira(fronteira)
print('   explorados:', sorted(explorados), '\n')

# Executa 3 rodadas de seleção e expansão de nós
for rodada in range(1, 4):
    print(f'--- Rodada {rodada} ---')

    # Ordena a fronteira pelo menor valor de f(n) antes de escolher o próximo nó
    fronteira.sort(key=lambda no: no[0])
    no = fronteira.pop(0)
    cidade_atual = no[2]

    # Marca a cidade retirada da fronteira como explorada
    explorados.add(cidade_atual)
    print(f'Rodada {rodada}: expandindo {cidade_atual} (f={no[0]}, g={no[1]})')
    print(f'   Caminho até {cidade_atual}: {" -> ".join(no[3])}')

    # Adiciona os novos nós filhos à fronteira e exibe o estado atualizado
    novos_filhos = expandir(no, explorados)
    fronteira += novos_filhos

    # Exibe a fronteira ordenada para facilitar a visualização da próxima escolha
    fronteira_exibicao = sorted(fronteira, key=lambda item: item[0])
    mostrar_fronteira(fronteira_exibicao)
    print('   explorados:', sorted(explorados), '\n')

print('=== Fim da Fase 4 ===')