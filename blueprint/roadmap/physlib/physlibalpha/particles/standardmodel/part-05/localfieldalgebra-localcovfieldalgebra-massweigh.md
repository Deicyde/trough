---
declaration: module
origin: cited
lean: StandardModel.LocalCovFieldAlgebra.isMassWeightPoly, StandardModel.LocalCovFieldAlgebra.hasPositiveMassWeights, StandardModel.LocalCovFieldAlgebra.hasMassWeightParity, StandardModel.LocalCovFieldAlgebra.massWeightSubmodule, StandardModel.LocalCovFieldAlgebra.massWeightSubmoduleLE, StandardModel.LocalCovFieldAlgebra.massWeightSubmodule_zero, StandardModel.LocalCovFieldAlgebra.massWeightSubmoduleLE_eq_iSup, StandardModel.LocalCovFieldAlgebra.massWeightSubmodule_eq_iSup_sectorMassWeight
statement: formalized
proof: formalized
---

# The mass-weight grading of the covariant field algebra of the Standard Model

The module `PhyslibAlpha.Particles.StandardModel.LocalFieldAlgebra.LocalCovFieldAlgebra.MassWeight`, [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean): 12 declarations, 12 with a docstring.

> The generic mass-weight grading of a covariant field algebra, at the mass-weight polynomial of
> the Standard Model.

## i. Overview

> The mass-weight polynomial `LocalCovFieldAlgebra.massWeightPoly` of the Standard Model gives the
> field-strength tower `∇_l F_μν` weight `4 + 2 |l|`, the Higgs towers weight `2 + 2 n` and the
> fermion towers weight `3 + 2 n`. The Higgs has mass weight two and every fermion mass weight
> three. So the polynomial is a mass-weight polynomial in the sense of
> `GaugeFieldData.LocalCovFieldAlgebra.IsMassWeightPoly`, every species has positive mass weight,
> and the mass weights have the parity of the statistics. The generic grading, its weight
> components, its filtration and the generic sectors therefore apply to the covariant field
> algebra of the Standard Model. This file records the three facts and names the weight pieces and
> the filtration at this polynomial.

## ii. Key results

> - `StandardModel.LocalCovFieldAlgebra.isMassWeightPoly` : the mass-weight polynomial of the
>   Standard Model gives every covariant generator its mass weight.
> - `StandardModel.LocalCovFieldAlgebra.hasPositiveMassWeights`,
>   `StandardModel.LocalCovFieldAlgebra.hasMassWeightParity` : the species weights are positive,
>   odd for the fermions and even for the Higgs.
> - `StandardModel.LocalCovFieldAlgebra.massWeightSubmodule`,
>   `StandardModel.LocalCovFieldAlgebra.massWeightSubmoduleLE` : the weight pieces and the
>   filtration of the covariant field algebra of the Standard Model.

## iv. References

> * None.

## A. The mass-weight polynomial of the Standard Model

**`StandardModel.LocalCovFieldAlgebra.isMassWeightPoly`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L68).

> The mass-weight polynomial of the Standard Model gives every covariant generator its mass
> weight, `4 + 2 |l|` for the field-strength tower, `2 + 2 n` for the Higgs towers and
> `3 + 2 n` for the fermion towers.

```lean
lemma isMassWeightPoly : GaugeFieldData.LocalCovFieldAlgebra.IsMassWeightPoly massWeightPoly
```

**`StandardModel.LocalCovFieldAlgebra.hasPositiveMassWeights`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L99).

> Every species of the Standard Model has positive mass weight.

```lean
lemma hasPositiveMassWeights : fieldData.HasPositiveMassWeights
```

**`StandardModel.LocalCovFieldAlgebra.hasMassWeightParity`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L104).

> The fermions of the Standard Model have odd mass weight and the Higgs even mass weight.

```lean
lemma hasMassWeightParity : fieldData.HasMassWeightParity
```

## B. The weight pieces and the filtration

**`StandardModel.LocalCovFieldAlgebra.massWeightSubmodule`**, an abbrev, [line 116](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L116).

> The elements of the covariant field algebra of the Standard Model of mass weight exactly
> `n`.

```lean
noncomputable abbrev massWeightSubmodule (n : ℕ) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.massWeightSubmoduleLE`**, an abbrev, [line 121](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L121).

> The elements of the covariant field algebra of the Standard Model of mass weight at most
> `w`. A Lagrangian of mass dimension at most `w / 2` lies here.

```lean
noncomputable abbrev massWeightSubmoduleLE (w : ℕ) : Submodule ℂ fieldData.LocalCovFieldAlgebra
```

**`StandardModel.LocalCovFieldAlgebra.massWeightSubmodule_zero`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L126).

> The weight-zero part of the covariant field algebra is the scalars, the constant term of mass
> dimension zero.

```lean
lemma massWeightSubmodule_zero : massWeightSubmodule 0 = 1
```

**`StandardModel.LocalCovFieldAlgebra.massWeightSubmoduleLE_eq_iSup`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L131).

> The filtration as a join over a finite index type.

```lean
lemma massWeightSubmoduleLE_eq_iSup (w : ℕ) :
    massWeightSubmoduleLE w = ⨆ k : Fin (w + 1), massWeightSubmodule (k : ℕ)
```

**`StandardModel.LocalCovFieldAlgebra.massWeightSubmodule_eq_iSup_sectorMassWeight`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L136).

> The weight-`w` piece is the join of the weight-`w` pieces of the sectors.

```lean
lemma massWeightSubmodule_eq_iSup_sectorMassWeight (w : ℕ) :
    massWeightSubmodule w = ⨆ A, fieldData.sectorMassWeight A w
```

## C. Stability under the gauge and Lorentz groups

**`StandardModel.LocalCovFieldAlgebra.repGauge_mem_massWeightSubmodule`**, a lemma, [line 147](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L147).

> The global gauge group preserves the weight pieces.

```lean
lemma repGauge_mem_massWeightSubmodule {w : ℕ} {x : fieldData.LocalCovFieldAlgebra}
    (g : GaugeGroupI)
    (hx : x ∈ massWeightSubmodule w) : repGaugeGroupI g x ∈ massWeightSubmodule w
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_mem_massWeightSubmodule`**, a lemma, [line 154](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L154).

> The Lorentz group preserves the weight pieces.

```lean
lemma repLorentz_mem_massWeightSubmodule {w : ℕ} {x : fieldData.LocalCovFieldAlgebra} (Λ : SL(2,ℂ))
    (hx : x ∈ massWeightSubmodule w) : repLorentzGroup Λ x ∈ massWeightSubmodule w
```

**`StandardModel.LocalCovFieldAlgebra.repGauge_mem_sectorMassWeight`**, a lemma, [line 160](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L160).

> The global gauge group preserves the weight pieces of every sector.

```lean
lemma repGauge_mem_sectorMassWeight {A : Finset GaugeFieldData.FieldKind} {w : ℕ}
    {x : fieldData.LocalCovFieldAlgebra} (g : GaugeGroupI)
    (hx : x ∈ fieldData.sectorMassWeight A w) :
    repGaugeGroupI g x ∈ fieldData.sectorMassWeight A w
```

**`StandardModel.LocalCovFieldAlgebra.repLorentz_mem_sectorMassWeight`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean#L167).

> The Lorentz group preserves the weight pieces of every sector.

```lean
lemma repLorentz_mem_sectorMassWeight {A : Finset GaugeFieldData.FieldKind} {w : ℕ}
    {x : fieldData.LocalCovFieldAlgebra} (Λ : SL(2,ℂ)) (hx : x ∈ fieldData.sectorMassWeight A w) :
    repLorentzGroup Λ x ∈ fieldData.sectorMassWeight A w
```

## Depends on

- [The sectors of a gauge field theory](../../../classicalfieldtheory/gaugetheory/part-05/localfieldalgebra-localcovfieldalgebra-sector.md)
- [The covariant field algebra of the Standard Model](localfieldalgebra-localcovfieldalgebra-basic.md)

## Sources

- [PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Particles/StandardModel/LocalFieldAlgebra/LocalCovFieldAlgebra/MassWeight.lean)
