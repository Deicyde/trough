---
declaration: proposition
origin: cited
mathlib: true
mathlib_declaration: CategoryTheory.Over.postAdjunctionRight
---

# Sliced adjoint functors

If $a : F \vdash G$ is an adjunction between $F : C \to D$ and $G : D \to C$ and $X : C$, then there is an adjunction between $F / X : C / X \to D / F(X)$ and $G / X : D / F(X) \to C / X$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

See https://ncatlab.org/nlab/show/sliced+adjoint+functors+–+section.

## Lean

Formalized as [`CategoryTheory.Over.postAdjunctionRight`](https://yaeldillies.github.io/toric/docs/find/#doc/CategoryTheory.Over.postAdjunctionRight).

## Sources

- [Toric varieties blueprint: chapters/1-1-over-cat.tex, line 4](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/1-1-over-cat.tex#L4)
