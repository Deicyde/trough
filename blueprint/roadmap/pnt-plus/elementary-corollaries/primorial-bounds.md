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

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/Consequences.lean)
