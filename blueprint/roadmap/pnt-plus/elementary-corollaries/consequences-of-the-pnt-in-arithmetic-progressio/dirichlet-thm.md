---
declaration: corollary
origin: cited
lean: dirichlet_thm
statement: formalized
proof: formalized
---

# Dirichlet's theorem

Any primitive residue class contains an infinite number of primes.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Prime number theorem in AP](chebyshev-asymptotic-pnt.md)

## Proof

If this were not the case, then the sum $\sum_{p \leq x: p = a\ (q)} \log p$ would be bounded in $x$, contradicting Theorem [Prime number theorem in AP](chebyshev-asymptotic-pnt.md).

## Lean

Formalized as [`dirichlet_thm`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/dirichlet_thm).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Consequences.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Consequences.lean)
