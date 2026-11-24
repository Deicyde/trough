---
declaration: definition
origin: cited
mathlib: true
mathlib_declaration: Rep.quotientToInvariantsFunctor, Rep.res
---

# inflation restriction functors

The map $M \mapsto M \downarrow S$ defines a functor $\mathbf{res} : \mathbf{Rep}(R,G) \to \mathbf{Rep}(R,S)$. If $S$ is a normal subgroup of $G$ then then map $M \mapsto M^S$ defines a functor $\mathbf{invar} : \mathbf{Rep}(R,G) \to \mathbf{Rep}(R, G/S)$. These functors are called *restriction* and *inflation* respectively. These are defined in Mathlib as `Rep.res` and `Rep.quotientToInvariantsFunctor`.

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`Rep.quotientToInvariantsFunctor`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.quotientToInvariantsFunctor), [`Rep.res`](https://kbuzzard.github.io/ClassFieldTheory/docs/find/#doc/Rep.res).

## Sources

- [Class field theory blueprint: _2_cohomology.tex, line 71](https://github.com/kbuzzard/ClassFieldTheory/blob/1e7f5dbe38358bd37a0643bb0db2dd3a436e6cb7/blueprint/src/_2_cohomology.tex#L71)
