---
declaration: module
origin: cited
lean: GlobalGaugeGroup.MatterField
statement: formalized
proof: formalized
---

# Matter fields of a global gauge group

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.Basic`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean): 2 declarations (1 instance with no name), 2 with a docstring.

> A matter field transforming under a continuous finite-dimensional representation of a global
> gauge group.

## i. Overview

> A matter field of a gauge theory with global gauge group `G` takes values in a
> finite-dimensional complex vector space `V`, on which `G` acts through a continuous
> representation `ρ : G → GL(V)` by invertible linear maps. Here `V` is a normed space, which
> fixes its topology, the unique one of a finite-dimensional complex vector space, and makes the
> linear maps `V →L[ℂ] V` a Banach algebra. Continuity is what lets `ρ` be differentiated to the
> Lie algebra, in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.DerivRep`,
> and extended to the jets of gauge transformations, in
> `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.JetRep`.
> As for any matter field, `V` also carries a representation of the Lorentz group, and the
> field has a mass weight and a declared statistics.

## ii. Key results

> - `GlobalGaugeGroup.MatterField` : a matter field transforming under a continuous
>   representation of a global gauge group.

## iv. References

> * None.

## A. Matter fields

**`GlobalGaugeGroup.MatterField`**, a structure, [line 70](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean#L70).

> A matter field transforming under a continuous representation of the global gauge group
> `G`. It has a finite-dimensional complex normed target space `V`, the continuous
> representation `rep : G → GL(V)` by invertible linear maps, the Lorentz representation on
> `V`, the mass weight of the field (in the units in which a derivative has weight `2`), and
> its declared statistics.

```lean
structure MatterField (G : GlobalGaugeGroup κ) where
  /-- The target space of the field. -/
  V : Type
  [instNormedAddCommGroup : NormedAddCommGroup V]
  [instNormedSpace : NormedSpace ℂ V]
  [instFiniteDimensional : FiniteDimensional ℂ V]
  /-- The continuous representation of the global gauge group on the target space. -/
  rep : G.group →ₜ* (V →L[ℂ] V)ˣ
  /-- The representation of the Lorentz group on the target space. -/
  repLorentz : Representation ℂ SL(2,ℂ) V
  /-- The mass weight of the field. -/
  massWeight : ℕ
  /-- The statistics the field is declared to obey, bosonic or fermionic. -/
  statistic : FieldStatistic
```

**An instance with no name**, [line 89](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean#L89).

> The target space of a matter field is complete, being finite-dimensional.

```lean
instance (G : GlobalGaugeGroup κ) (M : G.MatterField) : CompleteSpace M.V
```

## Depends on

- [Field statistics](../../../../physlib/qft/perturbationtheory/part-01/fieldstatistics-basic.md)
- [Global gauge groups](../part-02/globalgaugegroup-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Basic.lean)
