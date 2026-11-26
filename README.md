# astar-romenia

Implementação do algoritmo de busca A* para encontrar a menor rota entre Arad e Bucareste, baseada no capítulo 3 do livro *Artificial Intelligence: A Modern Approach* (Russell & Norvig).

Projeto desenvolvido para a disciplina **Inteligência Artificial I (IIA-008)**.

**Autor:** Fabio Anselmo

## Visão geral do algoritmo

A busca A* avalia os nós usando a função:

$$f(n) = g(n) + h(n)$$

- **$g(n)$**: custo real acumulado (em km) desde a cidade inicial até o nó $n$.
- **$h(n)$**: heurística admissível (distância em linha reta em km) de $n$ até o objetivo (`Bucharest`).
- **$f(n)$**: estimativa do custo total do caminho passando por $n$, orientando a expansão sempre pelo menor valor de $f$.

## Execução

Para rodar o programa principal no terminal:

```bash
python a_estrela.py