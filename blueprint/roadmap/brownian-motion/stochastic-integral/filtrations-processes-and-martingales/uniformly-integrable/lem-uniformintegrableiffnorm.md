---
declaration: lemma
origin: cited
lean: MeasureTheory.uniformIntegrable_iff_norm
statement: formalized
proof: formalized
---

# uniformIntegrableIffNorm

Let $(X_t)_{t \in T}$ be a family of uniformly integrable random variables. It is uniformly integrable if and only if $(\|X_t\|)_{t \in T}$ is.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [uniformIntegrableNorm](lem-uniformintegrablenorm.md)
- [uniformIntegrableDominated](lem-uniformintegrabledominated.md)

## Proof

The forward direction is Lemma [uniformIntegrableNorm](lem-uniformintegrablenorm.md). The converse direction follows from Lemma [uniformIntegrableDominated](lem-uniformintegrabledominated.md) with $Y := (\|X_t\|)_{t \in T}$.

## Lean

Formalized as [`MeasureTheory.uniformIntegrable_iff_norm`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.uniformIntegrable_iff_norm).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 834](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L834)
