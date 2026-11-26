# Fase 2: cálculo de custo de caminho e valores g, h, f na busca A*
from mapa import mapa_romenia, heuristica_bucareste

print('=== Fase 2: Custo de caminho e g, h, f ===\n')


def custo_da_estrada(origem, destino):
    """Retorna a distância em km entre duas cidades conectadas diretamente, ou None."""
    # Percorre todas as ligações diretas partindo de `origem`
    for vizinho, custo in mapa_romenia[origem]:
        if vizinho == destino:
            return custo
    # Caso não exista aresta direta entre `origem` e `destino`
    return None


def custo_do_caminho(caminho):
    """Soma o custo em km de cada trecho consecutivo de uma lista de cidades."""
    total = 0
    # Vai até len(caminho) - 1 porque cada passo liga caminho[i] a caminho[i + 1]
    for i in range(len(caminho) - 1):
        trecho = custo_da_estrada(caminho[i], caminho[i + 1])
        total += trecho
    return total


def mostrar_g_h_f(caminho):
    """Exibe uma tabela com g (custo acumulado), h (heurística) e f = g + h para cada cidade."""
    print(f' {"cidade":<15} {"g":>5} {"h":>5} {"f":>5}')
    print(' ' + '-' * 33)
    for i, cidade in enumerate(caminho):
        # Fatiar caminho[:i + 1] pega o prefixo do caminho do início até a cidade atual
        g = custo_do_caminho(caminho[:i + 1])
        h = heuristica_bucareste[cidade]
        f = g + h
        print(f' {cidade:<15} {g:>5} {h:>5} {f:>5}')


# Dois caminhos candidatos clássicos de Arad até Bucharest no mapa da Romênia
por_fagaras = ['Arad', 'Sibiu', 'Fagaras', 'Bucharest']
por_pitesti = ['Arad', 'Sibiu', 'Rimnicu Vilcea', 'Pitesti', 'Bucharest']

print('--- Consulta de estradas diretas ---')
print('Arad -> Sibiu:', custo_da_estrada('Arad', 'Sibiu'), 'km')
print('Arad -> Bucharest:', custo_da_estrada('Arad', 'Bucharest'), '(sem estrada direta)')

print('\n--- Custo total de cada caminho candidato ---')
print('Calculando custo total do caminho por Fagaras...')
print('Por Fagaras:', ' -> '.join(por_fagaras), '=', custo_do_caminho(por_fagaras), 'km')

print('Calculando custo total do caminho por Pitesti...')
print('Por Pitesti:', ' -> '.join(por_pitesti), '=', custo_do_caminho(por_pitesti), 'km')

print('\n--- Tabela g, h e f ao longo do caminho ---')
print('\nValores por Fagaras:')
mostrar_g_h_f(por_fagaras)

print('\nValores por Pitesti:')
mostrar_g_h_f(por_pitesti)

print('\n=== Fim da Fase 2 ===')