---
declaration: lemma
origin: cited
lean: ZetaLowerBnd
statement: formalized
proof: formalized
---

# ZetaLowerBnd

For any $A>0$ sufficiently small, there is a constant $C>0$ so that whenever $1- A / \log^9 |t| \le \sigma < 1$ and $3 < |t|$, we have that:

$$
|\zeta(\sigma+it)| \ge C \log^7 |t|.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaLowerBound3](zetalowerbound3.md)
- [Zeta-diff-Bnd](zeta-diff-bnd.md)

## Proof

Follow same argument.

## Lean

Formalized as [`ZetaLowerBnd`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaLowerBnd).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
