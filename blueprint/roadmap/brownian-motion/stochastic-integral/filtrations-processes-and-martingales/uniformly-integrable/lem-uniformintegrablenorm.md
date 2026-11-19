---
declaration: lemma
origin: cited
lean: MeasureTheory.UniformIntegrable.norm
statement: formalized
proof: formalized
---

# uniformIntegrableNorm

If $(X_t)_{t \in T}$ is a family of uniformly integrable random variables, then so is $(\|X_t\|)_{t \in T}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [uniformIntegrableDominated](lem-uniformintegrabledominated.md)

## Proof

Apply Lemma [uniformIntegrableDominated](lem-uniformintegrabledominated.md) with $Y := X$.

## Lean

Formalized as [`MeasureTheory.UniformIntegrable.norm`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.UniformIntegrable.norm).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 822](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L822)
