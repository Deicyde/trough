---
declaration: lemma
origin: cited
lean: dlog_riemannZeta_bdd_on_vertical_lines
statement: formalized
proof: formalized
---

# dlog-riemannZeta-bdd-on-vertical-lines

For $\sigma_0 > 1$, there exists a constant $C > 0$ such that

$$
\forall t \in \mathbb{R}, \quad
\left\| \frac{\zeta'(\sigma_0 + t i)}{\zeta(\sigma_0 + t i)} \right\| \leq C.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Write as Dirichlet series and estimate trivially using Theorem [LogDerivativeDirichlet](logderivativedirichlet.md).

## Lean

Formalized as [`dlog_riemannZeta_bdd_on_vertical_lines`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/dlog_riemannZeta_bdd_on_vertical_lines).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
