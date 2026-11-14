---
declaration: module
origin: cited
lean: MeasureTheory.Measure.pi_mono
statement: formalized
proof: formalized
---

# Monotonicity of finite product measures

The module `PhyslibAlpha.Mathematics.MeasureTheory.Pi`, [PhyslibAlpha/Mathematics/MeasureTheory/Pi.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/Pi.lean): 1 declaration, 1 with a docstring.

> Finite product measures `MeasureTheory.Measure.pi` are monotone in each of their factors.

## i. Overview

> Mathlib constructs the finite product `Measure.pi μ` of a family of measures `μ i`, but does
> not (yet) record that it is monotone in the family. This file proves that if `μ i ≤ ν i` for
> every `i`, then `Measure.pi μ ≤ Measure.pi ν`. No `SigmaFinite` assumption is needed, since the
> proof goes through the outer measure `MeasureTheory.OuterMeasure.pi` from which `Measure.pi` is
> built.

## ii. Key results

> - `MeasureTheory.Measure.pi_mono` : the finite product of measures is monotone in the family.

## iv. References

> * None.

## A. Monotonicity of the product measure

**`MeasureTheory.Measure.pi_mono`**, a lemma, [line 50](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/Pi.lean#L50).

> The finite product measure `Measure.pi μ` is monotone in the family of measures `μ`:
> if `μ i ≤ ν i` for every `i`, then `Measure.pi μ ≤ Measure.pi ν`.

```lean
lemma pi_mono {ι : Type*} [Fintype ι] {α : ι → Type*} [∀ i, MeasurableSpace (α i)]
    {μ ν : (i : ι) → Measure (α i)} (h : ∀ i, μ i ≤ ν i) : Measure.pi μ ≤ Measure.pi ν
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/MeasureTheory/Pi.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Mathematics/MeasureTheory/Pi.lean)
