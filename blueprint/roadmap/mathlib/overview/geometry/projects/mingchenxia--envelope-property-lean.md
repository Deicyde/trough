---
declaration: theorem
origin: cited
lean: EnvelopeProperty.ProjSubvariety.isPSH_of_isPSH_comp_proj, EnvelopeProperty.ProjSubvariety.isPSH_of_isPSH_comp_proj_of_convexPLApproximation, EnvelopeProperty.Berkovich.RelativeSpectrum.exists_centeredGaussAway_ne_in_nhds, EnvelopeProperty.Berkovich.RelativeSpectrum.not_isOpen_singleton_centeredGaussAway_zero, EnvelopeProperty.Berkovich.RelativeSpectrum.centeredGaussAway_val_ne_zero, EnvelopeProperty.Berkovich.RelativeSpectrum.centeredGaussAway_support_eq_bot, EnvelopeProperty.Berkovich.RelativeSpectrum.centeredGaussAway_zero_mem_closure_generic, EnvelopeProperty.Berkovich.RelativeSpectrum.isCompact_preimage_comap_of_isIntegral
statement: formalized
---

# envelope-property-lean

*The envelope property for unibranch projective varieties*

[MingchenXia/envelope-property-lean](https://github.com/MingchenXia/envelope-property-lean) at commit [bb713041](https://github.com/MingchenXia/envelope-property-lean/tree/bb7130411c5594e951c5923f8b82c021ce3d6c8d), 2026-10-30.

> A Lean 4 / Mathlib formalization of the main results of Yanbo Fang, Jiyuan Han and Mingchen Xia, *The envelope property for unibranch projective varieties* ([paper and bibliography](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/paper)).

*Quoted from [README.md](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/README.md), Apache-2.0.*

## Depends on

- [Extended real number](../../general-algebra/numbers/extended-real-number.md)
- [Field](../../general-algebra/field-theory/field.md)
- [Algebraically closed field](../../general-algebra/field-theory/algebraically-closed-field.md)
- [Set](../../data-structures/sets/set.md)
- [Closure](../../topology/general-topology/part-01/closure.md)
- [Compactness in terms of filters](../../topology/general-topology/part-01/compactness-in-terms-of-filters.md)

## Proof depends on

- [M. Riesz extension theorem](../../../thousand-plus/analysis/46-functional-analysis/m-riesz-extension-theorem.md)
- [Rank–nullity theorem](../../../thousand-plus/algebra/15-linear-and-multilinear-algebra-matrix-theory/rank-nullity-theorem.md)
- [Compactness in terms of open covers (Borel-Lebesgue)](../../topology/general-topology/part-01/compactness-in-terms-of-open-covers-borel-lebesg.md)
- [Sum of kth powers](../../../hundred-theorems/part-03/sum-of-kth-powers.md)
- [Positive cone](../convex-geometry/positive-cone.md)
- [Hilbert basis theorem](../../general-algebra/polynomials-and-power-series/hilbert-basis-theorem.md)
- [Prime spectrum](../algebraic-geometry/prime-spectrum.md)
- [Separable polynomial](../../general-algebra/polynomials-and-power-series/separable-polynomial.md)

## Main results

Its Lean names are 8 of the 857 Lean names of the blueprint nodes that no other node uses, marked \leanok:

- [`EnvelopeProperty.ProjSubvariety.isPSH_of_isPSH_comp_proj`](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/EnvelopeProperty/Projective/BlowupDescent.lean#L207) (theorem)
- [`EnvelopeProperty.ProjSubvariety.isPSH_of_isPSH_comp_proj_of_convexPLApproximation`](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/EnvelopeProperty/Projective/BlowupDescent.lean#L118) (theorem)
- [`EnvelopeProperty.Berkovich.RelativeSpectrum.exists_centeredGaussAway_ne_in_nhds`](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/EnvelopeProperty/Berkovich/LineGaussPaths.lean#L178) (theorem)
- [`EnvelopeProperty.Berkovich.RelativeSpectrum.not_isOpen_singleton_centeredGaussAway_zero`](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/EnvelopeProperty/Berkovich/LineGaussPaths.lean#L192) (theorem)
- [`EnvelopeProperty.Berkovich.RelativeSpectrum.centeredGaussAway_val_ne_zero`](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/EnvelopeProperty/Berkovich/LineGaussPaths.lean#L209) (theorem)
- [`EnvelopeProperty.Berkovich.RelativeSpectrum.centeredGaussAway_support_eq_bot`](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/EnvelopeProperty/Berkovich/LineGaussPaths.lean#L221) (theorem)
- [`EnvelopeProperty.Berkovich.RelativeSpectrum.centeredGaussAway_zero_mem_closure_generic`](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/EnvelopeProperty/Berkovich/LineGaussPaths.lean#L231) (theorem)
- [`EnvelopeProperty.Berkovich.RelativeSpectrum.isCompact_preimage_comap_of_isIntegral`](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/EnvelopeProperty/Berkovich/SpectrumIntegral.lean#L80) (theorem)

## Project

- Lean v4.33.1, Mathlib at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- 6,161 .lean files; its Lean libraries `EnvelopeProperty` hold 5,000 (the first read), declaring 50,558 names, with `sorry` in 0 files and 0 axioms, read without Lean.
- License: Apache-2.0 ([LICENSE](https://github.com/MingchenXia/envelope-property-lean/blob/bb7130411c5594e951c5923f8b82c021ce3d6c8d/LICENSE)).

## Builds on

- Mathlib, at [0df444a3](https://github.com/leanprover-community/mathlib4/tree/0df444a360eaa60ab8c11dca51a86af692955474).
- `aintlib`.
- `hironaka`.
- `tauceti`.

## Placement

Of its imports of Mathlib modules in an overview area, 598 of 2968 are in Geometry, 8.5 times the average project's share, the most of the areas holding a tenth of its imports.

## Mathlib use

Areas of its Mathlib imports by lift over the average project: Geometry (598 of 2968 imports, 8.5×), Linear algebra (308 of 2968 imports, 1.8×), General algebra (1538 of 2968 imports, 1.5×). *Proof depends on* lists 8 of the 199 Mathlib overview articles whose Lean names its files write, those written most often relative to the other projects; a name match, not an import.

## Sources

- [MingchenXia/envelope-property-lean at bb713041](https://github.com/MingchenXia/envelope-property-lean/tree/bb7130411c5594e951c5923f8b82c021ce3d6c8d)
