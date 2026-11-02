---
declaration: lemma
origin: cited
lean: ZetaZeroFree9
statement: formalized
proof: formalized
---

# ZetaZeroFree9

There is an $A>0$ so that for $1-A/\log^9 |t| \le \sigma < 1$ and $3 < |t|$,

$$
\zeta(\sigma+it) \ne 0.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaLowerBnd](zetalowerbnd.md)

## Proof

Apply Lemma [ZetaLowerBnd](zetalowerbnd.md).

## Lean

Formalized as [`ZetaZeroFree9`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaZeroFree9).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
