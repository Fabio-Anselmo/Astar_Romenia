# Fase 3: nó e fronteira, expandindo Arad na mão
# Cada nó é representado como uma tupla: (f, g, cidade, caminho)
# onde f = g + h (estimativa total), g = custo acumulado e caminho = rota até a cidade
from mapa import mapa_romenia, heuristica_bucareste

print('=== Fase 3: Nó e fronteira (expansão manual de Arad) ===\n')

inicio = 'Arad'
h_inicio = heuristica_bucareste[inicio]

# Cria a fronteira inicial contendo apenas o nó de origem (f = 0 + h(inicio), g = 0)
fronteira = [(h_inicio, 0, inicio, [inicio])]
print(f'Cidade inicial: {inicio} (h = {h_inicio})')
print('Fronteira inicial:', fronteira)

# Remove e retorna o primeiro elemento da fronteira (índice 0) para expandir
f, g, cidade, caminho = fronteira.pop(0)
print('\n--- Retirando nó da fronteira ---')
print('Tirei:', cidade, '| f =', f, '| g =', g, '| caminho =', caminho)
print('Fronteira após pop(0):', fronteira)

# Expande a cidade atual gerando um nó filho para cada vizinho direto
print(f'\n--- Gerando vizinhos de {cidade} ---')
for vizinho, custo in mapa_romenia[cidade]:
    h_vizinho = heuristica_bucareste[vizinho]
    novo_g = g + custo
    novo_f = novo_g + h_vizinho
    novo_caminho = caminho + [vizinho]

    # caminho + [x] cria uma nova lista; usar append() alteraria a lista compartilhada do nó pai
    fronteira.append((novo_f, novo_g, vizinho, novo_caminho))
    print(
        f'  Vizinho {vizinho:<12} | estrada = {custo:>3} km | '
        f'g = {novo_g:>3} | h = {h_vizinho:>3} | f = {novo_f:>3}'
    )

print('\nDepois de expandir Arad:')
print(f'Total de nós na fronteira: {len(fronteira)}')
for i, no in enumerate(fronteira, start=1):
    print(f'  {i}. {no}')

# Ordena os nós da fronteira do menor para o maior valor de f(n)
fronteira.sort(key=lambda no: no[0])
print('\nOrdenada por f (menor f primeiro):')
for i, no in enumerate(fronteira, start=1):
    print(f'  {i}. {no[2]:<12} -> f={no[0]}, g={no[1]}, caminho={no[3]}')

# Seleciona o próximo nó de menor f que seria expandido na próxima etapa
proximo = fronteira.pop(0)
print('\n--- Próxima escolha do A* ---')
print('Próximo:', proximo[2], 'com f =', proximo[0], '| g =', proximo[1], '| caminho =', proximo[3])
print('Nós restantes na fronteira:', len(fronteira))

print('\n=== Fim da Fase 3 ===')