---
declaration: lemma
origin: cited
lean: ZetaBnd_aux2
statement: formalized
proof: formalized
---

# ZetaBnd-aux2

Given $n ≤ t$ and $\sigma$ with $1-A/\log t \le \sigma$, we have that

$$
|n^{-s}| \le n^{-1} e^A.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Use $|n^{-s}| = n^{-\sigma} = e^{-\sigma \log n} \le \exp(-\left(1-\frac{A}{\log t}\right)\log n) \le n^{-1} e^A$, since $n\le t$.

## Lean

Formalized as [`ZetaBnd_aux2`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaBnd_aux2).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/ZetaBounds.lean)
