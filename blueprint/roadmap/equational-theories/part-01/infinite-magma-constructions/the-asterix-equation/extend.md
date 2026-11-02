---
declaration: corollary
origin: cited
---

# extend

Every partial solution $(E_0,E_1,E_2,f)$ to [(1)](README.md) can be extended to a full solution $\tilde f: \mathbb{Z} \to \mathbb{Z}$.

## Depends on

- [partial-solution](partial-solution.md)

## Proof depends on

- [Enlarging a partial solution](iteration.md)

## Proof

If we arbitrarily well-order the integers, and iterate [Enlarging a partial solution](iteration.md) to add the least element of $\mathbb{Z} \backslash E_0$ in this well-ordering to $E_0$, we obtain an increasing sequence $(E^{(n)}_0, E^{(n)}_1, E^{(n)}_2, f^{(n)})$ of partial solutions to [(1)](README.md), where the $E^{(n)}_0$ exhaust $\mathbb{Z}$: $\bigcup_{n=1}^\infty E^{(n)}_0 = \mathbb{Z}$. Taking limits, we obtain a full solution $\tilde f$.

## Sources

- [Equational Theories blueprint: chapter/infinite_magma_constructions.tex, line 147](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/infinite_magma_constructions.tex#L147)
