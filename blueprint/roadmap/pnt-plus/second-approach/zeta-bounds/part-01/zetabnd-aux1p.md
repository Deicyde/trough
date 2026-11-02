---
declaration: lemma
origin: cited
lean: ZetaBnd_aux1p
statement: formalized
proof: formalized
---

# ZetaBnd-aux1p

For any $N\ge1$ and $s = \sigma + tI \in \mathbb{C}$, $\sigma=\in(0,2], 2 < |t|$,

$$
\left| s\int_N^\infty \frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx \right|
\ll |t| \frac{N^{-\sigma}}{\sigma}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaBnd-aux1b](zetabnd-aux1b.md)

## Proof

Apply Lemma [ZetaBnd-aux1b](zetabnd-aux1b.md) and estimate $|s|\ll |t|$.

## Lean

Formalized as [`ZetaBnd_aux1p`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaBnd_aux1p).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
