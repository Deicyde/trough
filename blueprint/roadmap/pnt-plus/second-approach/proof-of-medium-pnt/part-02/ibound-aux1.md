---
declaration: lemma
origin: cited
lean: IBound_aux1
statement: formalized
proof: formalized
---

# IBound-aux1

Given a natural number $k$ and a real number $X_0 > 0$, there exists $C \geq 1$ so that for all $X \geq X_0$,

$$
\log^k X \le C \cdot X.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We use the fact that $\log^k X / X$ goes to $0$ as $X \to \infty$. Then we use the extreme value theorem to find a constant $C$ that works for all $X \geq X_0$.

## Lean

Formalized as [`IBound_aux1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/IBound_aux1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
