---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: MeasurableEquiv.continuousMapToFun
---

# MeasurableEquiv.continuousMap

The identity is a measurable equivalence between the continuous functions of $\mathbb{R}^{\mathbb{R}_+}$ with the subset sigma-algebra obtained from the product sigma-algebra, and $C(\mathbb{R}_+, \mathbb{R})$ with the Borel sigma-algebra coming from the compact-open topology.

Mathematically this says nothing more than the equality of sigma-algebras of Theorem [ContinuousMap.borel_eq_iSup_comap_eval](thm-continuousmap-borel-eq-isup-comap-eval.md) but in Lean we have two different types so we need an equivalence.

## Depends on

- [ContinuousMap.borel_eq_iSup_comap_eval](thm-continuousmap-borel-eq-isup-comap-eval.md)

## Lean

Formalized as [`MeasurableEquiv.continuousMapToFun`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasurableEquiv.continuousMapToFun).

## Sources

- [Brownian motion blueprint: chapters/brownian.tex, line 232](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/brownian.tex#L232)
