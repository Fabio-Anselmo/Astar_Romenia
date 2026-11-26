# Fase 1: inspeção inicial dos dados do mapa e da heurística antes da busca
from mapa import mapa_romenia, heuristica_bucareste

print('=== Fase 1: Inspeção dos dados ===\n')

# Verifica quantas cidades existem no grafo e quantos valores heurísticos estão cadastrados
print('Cidades no mapa:', len(mapa_romenia))
print('Valores de h:', len(heuristica_bucareste))
print('Iniciando inspeção detalhada a partir de Arad...\n')

# Acessa a lista de conexões diretas a partir de Arad
vizinhos_arad = mapa_romenia['Arad']
print('--- Vizinhos de Arad ---')
print('Vizinhos de Arad:', vizinhos_arad)
print('Tipo:', type(vizinhos_arad))

# Inspeciona o primeiro elemento da lista (normalmente uma tupla (cidade_vizinha, custo_km))
primeira = vizinhos_arad[0]
print('\n--- Primeira aresta de Arad ---')
print('Primeira estrada de Arad:', primeira)
print(' vizinho:', primeira[0])
print(' custo  :', primeira[1])

# Percorre todas as conexões diretas saindo de Arad e exibe o custo em km
print('\nEstradas que saem de Arad:')
for vizinho, custo in mapa_romenia['Arad']:
    print(' Arad ->', vizinho, '=', custo, 'km')
print('Total de estradas saindo de Arad:', len(mapa_romenia['Arad']))

# Lista cada cidade do mapa e a quantidade de ligações diretas que ela possui
print('\nEstradas por cidade:')
for cidade in mapa_romenia:
    print(f' {cidade:<15} {len(mapa_romenia[cidade])}')
print('Contagem de estradas por cidade concluída.')

# Compara a distância em linha reta até Bucareste (h) com o custo da estrada (g local) para os vizinhos de Arad
print('\n--- Heurística (h) vs. Custo da estrada ---')
print('h(Arad) =', heuristica_bucareste['Arad'])
print('Comparando vizinhos de Arad (custo da aresta vs. heurística até Bucharest):')
for vizinho, custo in mapa_romenia['Arad']:
    h = heuristica_bucareste[vizinho]
    print(f' {vizinho:<10} estrada = {custo:>3}   h = {h:>3}')

print('\n=== Fim da Fase 1 ===')