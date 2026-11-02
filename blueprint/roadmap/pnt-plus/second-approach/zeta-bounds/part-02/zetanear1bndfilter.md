---
declaration: lemma
origin: cited
lean: ZetaNear1BndFilter
statement: formalized
proof: formalized
---

# ZetaNear1BndFilter

As $\sigma\to1^+$,

$$
|\zeta(\sigma)| \ll 1/(\sigma-1).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Zeta has a simple pole at $s=1$. Equivalently, $\zeta(s)(s-1)$ remains bounded near $1$. Lots of ways to prove this. Probably the easiest one: use the expression for $\zeta_0 (N,s)$ with $N=1$ (the term $N^{1-s}/(1-s)$ being the only unbounded one).

## Lean

Formalized as [`ZetaNear1BndFilter`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaNear1BndFilter).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
