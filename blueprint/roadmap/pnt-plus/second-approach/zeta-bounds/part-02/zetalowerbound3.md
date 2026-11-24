---
declaration: lemma
origin: cited
lean: ZetaLowerBound3
statement: formalized
proof: formalized
---

# ZetaLowerBound3

There exists a $c>0$ such that for all $1 < \sigma <= 2$ and $3 < |t|$,

$$
c \frac{(\sigma-1)^{3/4}}{(\log |t|)^{1/4}} \le |\zeta(\sigma + tI)|.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaUpperBnd](zetaupperbnd.md)
- [ZetaNear1BndExact](zetanear1bndexact.md)

## Proof

Combine Lemma ZetaLowerBound2 with upper bounds for $|\zeta(\sigma)|$ (from Lemma [ZetaNear1BndExact](zetanear1bndexact.md)) and $|\zeta(\sigma+2it)|$ (from Lemma [ZetaUpperBnd](zetaupperbnd.md)).

## Lean

Formalized as [`ZetaLowerBound3`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaLowerBound3).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/ZetaBounds.lean)
