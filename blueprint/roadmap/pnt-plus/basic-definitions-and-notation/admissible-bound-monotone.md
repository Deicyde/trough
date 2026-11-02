---
declaration: lemma
origin: cited
lean: admissible_bound.mono
statement: formalized
proof: formalized
discussion: https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/issues/900
---

# Admissible bound decreasing for large x

If $A,B,C,R > 0$ then the classical bound is monotone decreasing for $x \geq \exp( R (2B/C)^2 )$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Differentiate the bound and check the sign.

## Lean

Formalized as [`admissible_bound.mono`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/admissible_bound.mono).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Defs.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Defs.lean)
