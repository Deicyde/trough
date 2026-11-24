---
declaration: lemma
origin: cited
lean: LogDerivZetaBndUnif99
statement: formalized
proof: formalized
---

# LogDerivZetaBndUnif99

There exist $A, C > 0$ such that

$$
|\frac{\zeta'}{\zeta}(\sigma + it)|\leq C \log |t|^9
$$

whenever $|t|>3$ and $\sigma > 1 - A/\log |t|^9$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [riemannZetaLogDerivResidue](../part-01/riemannzetalogderivresidue.md)
- [LogDerivZetaBnd](../part-02/logderivzetabnd.md)

## Proof

For $\sigma$ close to $1$ use Lemma [LogDerivZetaBnd](../part-02/logderivzetabnd.md), otherwise estimate trivially.

## Lean

Formalized as [`LogDerivZetaBndUnif99`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/LogDerivZetaBndUnif99).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/ZetaBounds.lean)
