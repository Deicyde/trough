---
declaration: lemma
origin: cited
lean: ZetaBnd_aux1b
statement: formalized
proof: formalized
---

# ZetaBnd-aux1b

For any $N\ge1$ and $s = \sigma + tI \in \mathbb{C}$, $\sigma > 0$,

$$
\left| \int_N^\infty \frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx \right|
\le \frac{N^{-\sigma}}{\sigma}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaBnd-aux1a](zetabnd-aux1a.md)

## Proof

Apply Lemma [ZetaBnd-aux1a](zetabnd-aux1a.md) with $a=N$ and $b\to \infty$.

## Lean

Formalized as [`ZetaBnd_aux1b`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaBnd_aux1b).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
