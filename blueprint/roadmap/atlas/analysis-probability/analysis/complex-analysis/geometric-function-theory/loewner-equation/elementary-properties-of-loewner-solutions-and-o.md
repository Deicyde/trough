---
declaration: section
origin: cited
lean: StatMech.SLE.loewnerReflection, StatMech.SLE.hasHalfPlaneCapacity_comp, StatMech.SLE.HasCapacityRate, StatMech.SLE.MonotoneHullFamily
statement: formalized
proof: formalized
---

# Elementary properties of Loewner solutions and of half-plane capacity

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/elementary-properties-of-loewner-solutions-and-o/index.html).

## Reflection across the imaginary axis

The reflection `z ↦ -z̄` across the imaginary axis.

Formalized by `StatMech.SLE.loewnerReflection`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerProps.lean, line 66](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Loewner/LoewnerProps.lean#L66). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/elementary-properties-of-loewner-solutions-and-o/index.html#loewner-reflection).

## Additivity of half-plane capacity under composition

Half-plane capacity is additive under composition: `hcap(f ∘ g) = hcap(f) + hcap(g)`.

Formalized by `StatMech.SLE.hasHalfPlaneCapacity_comp`, a theorem declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerProps.lean, line 274](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Loewner/LoewnerProps.lean#L274). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/elementary-properties-of-loewner-solutions-and-o/index.html#has-half-plane-capacity-comp).

## Half-plane capacity rate of a Loewner family

The family `g_t` has half-plane capacity `a t` for every `t ≥ 0`.

Formalized by `StatMech.SLE.HasCapacityRate`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerProps.lean, line 316](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Loewner/LoewnerProps.lean#L316). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/elementary-properties-of-loewner-solutions-and-o/index.html#has-capacity-rate).

## Increasing family of compact hulls

An increasing family `(K_t)` of compact `ℍ`-hulls.

Formalized by `StatMech.SLE.MonotoneHullFamily`, a definition declared in [MathlibExt/Analysis/Complex/Loewner/LoewnerProps.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Complex/Loewner/LoewnerProps.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/elementary-properties-of-loewner-solutions-and-o/index.html#monotone-hull-family).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Elementary properties of Loewner solutions and of half-plane capacity](https://deicyde.github.io/atlas-lean/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/elementary-properties-of-loewner-solutions-and-o/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/complex-analysis/geometric-function-theory/loewner-equation/elementary-properties-of-loewner-solutions-and-o)
