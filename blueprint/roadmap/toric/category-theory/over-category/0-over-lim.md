---
declaration: proposition
origin: cited
lean: CategoryTheory.Limits.PreservesLimitsOfShape.overPost, CategoryTheory.Limits.PreservesLimitsOfSize.overPost
statement: formalized
proof: formalized
---

# Limit-preserving functors lift to over categories

Let $J$ be a shape (i.e. a category). Let $\widetilde J$ denote the category which is the same as $J$, but has an extra object $*$ which is terminal. If $F : C \to D$ is a functor preserving limits of shape $\widetilde J$, then the obvious functor $C / X \to D / F(X)$ preserves limits of shape $J$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Extend a functor $K\colon J \to C / X$ to a functor $\widetilde K\colon \widetilde J \to C$, by letting $\widetilde K (*) = X$.

## Lean

Formalized as [`CategoryTheory.Limits.PreservesLimitsOfShape.overPost`](https://yaeldillies.github.io/toric/docs/find/#doc/CategoryTheory.Limits.PreservesLimitsOfShape.overPost), [`CategoryTheory.Limits.PreservesLimitsOfSize.overPost`](https://yaeldillies.github.io/toric/docs/find/#doc/CategoryTheory.Limits.PreservesLimitsOfSize.overPost).

## Sources

- [Toric varieties blueprint: chapters/1-1-over-cat.tex, line 21](https://github.com/YaelDillies/toric/blob/5956b80249ec5416a266f68b5142606b060d7628/blueprint/src/chapters/1-1-over-cat.tex#L21)
