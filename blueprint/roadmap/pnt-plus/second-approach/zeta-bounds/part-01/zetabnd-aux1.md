---
declaration: lemma
origin: cited
lean: ZetaBnd_aux1
statement: formalized
proof: formalized
---

# ZetaBnd-aux1

For any $N\ge1$ and $s = \sigma + tI \in \mathbb{C}$, $\sigma=\in(0,2], 2 < |t|$,

$$
\left| s\int_N^\infty \frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx \right|
\le 2 |t| \frac{N^{-\sigma}}{\sigma}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaBnd-aux1b](zetabnd-aux1b.md)

## Proof

Apply Lemma [ZetaBnd-aux1b](zetabnd-aux1b.md) and estimate $|s|\ll |t|$.

## Lean

Formalized as [`ZetaBnd_aux1`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaBnd_aux1).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/ZetaBounds.lean)
