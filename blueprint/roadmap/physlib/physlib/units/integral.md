---
declaration: module
origin: cited
lean: scaleUnit_measure, integral_isDimensionallyCorrect
statement: formalized
proof: formalized
---

# Dimensional invariance of the integral

The module `Physlib.Units.Integral`, [Physlib/Units/Integral.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Integral.lean): 3 declarations (1 instance with no name), 1 with a docstring.

> In this module we prove that the dimensional properties of the integral.

**An instance with no name**, [line 26](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Integral.lean#L26).

```lean
noncomputable instance (M : Type)
    [NormedAddCommGroup M] [NormedSpace ℝ M] [HasDim M]
    [MeasurableSpace M] [self : MeasurableConstSMul ℝ M] :
      MulUnitDependent (MeasureTheory.Measure M)
```

**`scaleUnit_measure`**, a lemma, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Integral.lean#L57).

```lean
lemma scaleUnit_measure (u1 u2 : LTMCTUnitChoices) (μ : MeasureTheory.Measure M) :
    scaleUnit u1 u2 μ = μ.map (fun m => scaleUnit u1 u2 m)
```

**`integral_isDimensionallyCorrect`**, a lemma, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Integral.lean#L72).

> The statement that for a measure `μ` of dimension `d`, and a function
>   `f : M → G` of dimension `(CarriesDimension.d G * d⁻¹)` (where `CarriesDimension.d G`
>   is the dimension associated with terms of type `G`), then
>   `∫ x, f x ∂μ `
>   has the correct dimension, namely `CarriesDimension.d G`.
>
>   In other words, the function:
> ```
> fun (μ : DimSet (MeasureTheory.Measure M) d)
>     (f : DimSet (M → G) (CarriesDimension.d G * d⁻¹)) ↦ ∫ x, f.1 x ∂μ.1
> ```
>   is dimensionally correct.

```lean
lemma integral_isDimensionallyCorrect (d : Dimension LTMCTDimensionBase) :
    IsDimensionallyCorrect (fun (μ : DimSet (MeasureTheory.Measure M) d)
      (f : DimSet (M → G) (dim G * d⁻¹)) ↦ ∫ x, f.1 x ∂μ.1)
```

## Depends on

- [Physlib.Units.UnitDependent](unitdependent.md)

## Sources

- [Physlib/Units/Integral.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Units/Integral.lean)
