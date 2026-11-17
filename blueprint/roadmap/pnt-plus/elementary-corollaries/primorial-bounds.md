---
declaration: corollary
origin: cited
lean: primorial_bounds
statement: formalized
proof: formalized
---

# primorial-bounds

We have

$$
\prod_{p \leq x} p = \exp( x + o(x) )
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [chebyshev-asymptotic](chebyshev-asymptotic.md)

## Proof

Exponentiate Theorem chebyshev_asymptotic.

## Lean

Formalized as [`primorial_bounds`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/primorial_bounds).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/Consequences.lean)
