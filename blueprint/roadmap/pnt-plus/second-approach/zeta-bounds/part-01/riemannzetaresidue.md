---
declaration: theorem
origin: cited
lean: riemannZetaResidue
statement: formalized
proof: formalized
---

# riemannZetaResidue

The Riemann zeta function $\zeta(s)$ has a simple pole at $s=1$ with residue $1$. In particular, the function $\zeta(s) - \frac{1}{s-1}$ is bounded in a neighborhood of $s=1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ResidueOfTendsTo](residueoftendsto.md)

## Proof

From `riemannZeta_residue_one` (in Mathlib), we know that $(s-1)\zeta(s)$ goes to $1$ as $s\to1$. Now apply Theorem [ResidueOfTendsTo](residueoftendsto.md). (This can also be done using $\zeta_0$ below, which is expressed as $1/(s-1)$ plus things that are holomorphic for $\Re(s)>0$...)

## Lean

Formalized as [`riemannZetaResidue`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/riemannZetaResidue).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
