---
declaration: lemma
origin: cited
lean: ProbabilityTheory.posSemidef_brownianCovMatrix
statement: formalized
proof: formalized
---

# posSemidef_brownianCov

For $I = \{t_1, \ldots, t_n\}$ a finite subset of $\mathbb{R}_+$, let $C \in \mathbb{R}^{n \times n}$ be the matrix $C_{ij} = \min(t_i, t_j)$ for $1 \leq i,j \leq n$. Then $C$ is positive semidefinite.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [posSemidef_gramMatrix](lem-possemidef-grammatrix.md)

## Proof

$C$ is a Gram matrix by Lemma [C_eq_gramMatrix](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/projective_family.tex#L79). By Lemma [posSemidef_gramMatrix](lem-possemidef-grammatrix.md), it is positive semidefinite.

## Lean

Formalized as [`ProbabilityTheory.posSemidef_brownianCovMatrix`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.posSemidef_brownianCovMatrix).

## Sources

- [Brownian motion blueprint: chapters/projective_family.tex, line 98](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/projective_family.tex#L98)
