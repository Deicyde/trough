---
declaration: lemma
origin: cited
lean: MeasureTheory.UniformIntegrable.add
statement: formalized
proof: formalized
---

# uniformIntegrableAdd

Let $(X_t)_{t \in T}$ and $(Y_t)_{t \in T}$ be two families of uniformly integrable random variables. Then the family $(X_t + Y_t)_{t \in T}$ is uniformly integrable.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The families $X$ and $Y$ are uniformly integrable in the measure-theoretic sense and almost-everywhere strongly measurable, so $X + Y$ is too (see [MeasureTheory.UnifIntegrable.add](https://leanprover-community.github.io/mathlib4_docs/Mathlib/MeasureTheory/Function/UniformIntegrable.html#MeasureTheory.UnifIntegrable.add)). Moreover, $X$ and $Y$ are bounded in $L^p$, so $X + Y$ is too. So $X + Y$ is uniformly integrable.

## Lean

Formalized as [`MeasureTheory.UniformIntegrable.add`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.UniformIntegrable.add).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 787](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L787)
